from django.shortcuts import render
from django.shortcuts import redirect
import json
from django.http import HttpResponse, JsonResponse
from ..models.models import *
from ..models.docker.docker import Docker
from ..models.docker.dockerinterface import DockerInterface
from ..models.languages import LANGUAGES
from .articleeditpagepostparam import ArticleEditPagePostParam
from datetime import datetime
import os
# from ..models.seeder_data import * # seeder
import time

"""SQL
select coda_module.id as module_id, coda_article.id as article_id, coda_file.id as file_id  from coda_module inner join coda_article_module_dependencies on coda_module.id = coda_article_module_dependencies.module_id inner join coda_article on coda_article.id = coda_article_module_dependencies.article_id inner join coda_module_file_dependencies on coda_module_file_dependencies.module_id = coda_module.id inner join coda_file on coda_file.id = coda_module_file_dependencies.file_id;
"""

def read(request):
  # editページに飛ばす
  if len(request.GET):
    print(request.GET, 'いいいいい')
    a_id = request.GET['a_id']
    return render(request, 'article/create_base.html', getArticlePageByArticleId(a_id))
  elif request.path == '/edit/':
    # パラメータなしURLがeditのアクセスはcreateに飛ばす
    return redirect('/create')
  elif request.path == '/':
    return redirect('/create')

  post = request.POST
  print(post, '生のpost')

  # 実行するボタンでコード実行したときのみ
  # パラメータにはexecuteを含ませている
  if 'execute' in post:

    if post['language'] == 'javascript':
      language = 'js'
    else:
      language = post['language']

    file = File(
      file_tag_name = 'MyPostCode',
      code = post[[i for i in post if i.startswith('module')][0]],
      file_name = 'mypostcode',
      file_path = 'path/to/file',
      is_public = True,
      is_importable = True,
      is_executable = True,
      created_at = datetime.now(),
      updated_at = datetime.now(),
      article = Article.objects.all().first(),
      language = Language.objects.filter(name=language).first(),
      user = User(id=1),
    )

    file.writeFile()

    output = Docker(file).run()
    print(output)

    json_str = json.dumps({
      'result': output
    }, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

  # post通信があったときだけ
  if len(post):
    param_tree = ArticleEditPagePostParam(post).data
    SaveParamTree(param_tree)
    print(param_tree, 'こああああああ')
    if 'id' in param_tree['article']:
      article_id = param_tree['article']['id']
      print('これ？')
    else:
      article_id = Article.objects.all().last().id
      print('それともこれ？')

    return redirect(f'{request.scheme}://{request.get_host()}/edit/?a_id={article_id}')
    # return redirect(f'http://localhost:8000/edit/?a_id={article_id}')

  print(request.scheme, request.get_host())
  return render(request, 'article/create_base.html')

def delete(request):
  print('削除')
  article_id = request.POST['article-id']
  Article.objects.get(id=article_id).delete()
  return redirect('/create')

# ParamTreeを解析してDBに保存する
def SaveParamTree(param_tree):
  created_at = datetime.now()
  updated_at = datetime.now()

  # まずArticleを最初に保存する
  article = param_tree['article']
  title = article['title']
  body = article['body']
  a_id = article['id']

  # article_idがpostで送られてきたら、updateとみなす
  if a_id != '':
    article = Article.objects.get(id=a_id)
    article.title = title
    article.body = body
    article.is_public = True
    article.user = User.objects.get(id=1)
    article.created_at = created_at
    article.updated_at = updated_at
    article.save()
  else:
    Article(
      title = title,
      body = body,
      is_public = True,
      user = User.objects.get(id=1),
      created_at = created_at,
      updated_at = updated_at,
    ).save()
    a_id = Article.objects.all().last().id
    article['id'] = a_id # popしてからarticleを入れ直してるけど、ここが空文字列だとエラー...

  # articleを削除すると、param_treeはmoduleだけになる
  queue = param_tree.pop('article')

  print(param_tree, 'Paramつりー') # moduleだけになっている

  # モジュールやファイルの削除の実装方法の案
  # 最初にpostで送られた新規モジュールと既存モジュールのidを保持しておく
  # 一連の保存処理が完了したあと、同じarticleの他のモジュールをすべて削除
  # ファイルはモジュールさえ削除すればかんたんに紐付けられるので容易い

  moduleid_list = []
  fileid_list = []
  for key in param_tree:

    module = param_tree[key]
    name = module['name']

    print(key, 'いまみるのはこれ')
    if 'new' in key:
      module_id = None
    else:
      module_id = module['id']

    print(module)
    # moduleの取得とこの2モデルをDBへ保存

    if module_id != None:
      module_instance = Module.objects.get(id=module_id)
      module_instance.name = name
      module_instance.is_public = True
      module_instance.is_importable = True
      module_instance.is_executable = True
      module_instance.user = User.objects.get(id=1)
      module_instance.created_at = created_at
      module_instance.updated_at = updated_at
      module_instance.save()
      moduleid_list.append(module_id)
    else:
      Module(
        name = name,
        is_public = True,
        is_importable = True,
        is_executable = True,
        user = User.objects.get(id=1),
        created_at = created_at,
        updated_at = updated_at,
      ).save()
      Article_Module_Dependencies(
        article = Article.objects.get(id=a_id),
        module = Module.objects.all().last(),
        created_at = created_at,
        updated_at = updated_at,
      ).save()
      moduleid_list.append(Module.objects.last().id)
      module_id = Module.objects.last().id

    # moduleからnameとidを削除するとfilesだけになる
    module.pop('name')
    module.pop('id')

    print(module, 'モジュールです')

    zip_key = []
    zip_files = []

    # これを作る
    # collection = {
    #   module: { {'file_name': file },{ 'file_name': file} },
    #   module: { {'file_name': file },{ 'file_name': file} },
    # }
    zip_key.append(key)
    tmp = {}
    for k, v in module.items():
      tmp[k] = v
    zip_files.append(tmp)

    collection = dict(zip(zip_key, zip_files))
    print(collection, 'コレクション')

    files = collection[key]
    # fileid_list = []
    for file_id, file_values in files.items():
      print(file_id)
      if 'new' in file_id:
        f_id = None
      else:
        f_id = file_values['id']
      file_tag_name = file_values['name']
      code = file_values['code']
      language = file_values['language']

      if f_id != None:
        file = File.objects.get(id=f_id)
        file.file_tag_name = file_tag_name
        file.code = code
        file.file_name = '考え中'
        file.file_path = 'path/to/file'
        file.is_public = True
        file.is_importable = True
        file.is_executable = True
        file.updated_at = updated_at
        file.language = Language.objects.get(name=language)
        file.save()
        fileid_list.append(f_id)
      else:
        File(
          file_tag_name = file_tag_name,
          code = code,
          file_name = '考え中',
          file_path = 'path/to/file',
          is_public = True,
          is_importable = True,
          is_executable = True,
          created_at = created_at,
          updated_at = updated_at,
          article = Article.objects.get(id=a_id),
          language = Language.objects.filter(name=language).first(),
          user = User.objects.get(id=1),
        ).save()
        f_id = File.objects.last().id
        Module_File_Dependencies(
          module = Module.objects.get(id=module_id),
          file = File.objects.get(id=f_id),
          created_at = created_at,
          updated_at = updated_at,
        ).save()
        fileid_list.append(f_id)

  # ここでモジュールのforeachループ終了
  # 以降すべてのモジュールに対して繰り返し処理が終わったあとの処理

  # postで送られてこなかったモジュールの削除処理
  article_dependency_modules = Article_Module_Dependencies.objects.filter(article=Article.objects.get(id=a_id))
  res = article_dependency_modules
  # postで送られてきたモジュールを弾く
  for i in moduleid_list:
    res = res.exclude(module=Module.objects.get(id=i))

  # # 削除実行
  for i in res:
    i.module.delete()

  # ファイルも同様に削除を行う
  # moduleid_listは残すモジュール
  for m_id in moduleid_list:
    module = Module.objects.get(id=m_id)
    module_dependency_files = Module_File_Dependencies.objects.filter(module=Module.objects.get(id=module.id))
    res = module_dependency_files

    # postで送られてきたファイルを残すために弾く
    for i in fileid_list:
      res = res.exclude(file=File.objects.get(id=i))
    for i in res:
      i.file.delete()

    print(res, 'これ')

  print(moduleid_list)

  param_tree['article'] = queue
  return


def getArticlePageByArticleId(article_id):
  user_id = 1

  # ※article_idからすべてのデータを取得する
  # フォーマット
  # result = {
  #   'modules': {
  #     0: {
  #       'module': module,
  #       'files': {
  #         0: file,
  #         1: file,
  #         2: file,
  #       }
  #     }
  #   }
  # }
  # テンプレートではmodules[0].module.name, modules[0].files[0] などでアクセス
  result = {
    'modules': {},
    'article': Article.objects.get(id=article_id),
  }
  # articleに対してhas manyであるモジュールすべて
  article_dependency_modules = Article_Module_Dependencies.objects.filter(article=article_id).all()
  # そのモジュール一つひとつをイテレータに
  for i, dependency_module in enumerate(article_dependency_modules):
    module = dependency_module.module
    # print(module)
    result['modules'][i] = {
      'module': module,
      'files': {}
    }
    # モジュールに対してhas manyであるファイルすべて
    module_dependency_files = Module_File_Dependencies.objects.filter(module=module.id).all()
    # そのファイル一つ一つをイテレータとして取得する
    for j, dependency_file in enumerate(module_dependency_files):
      file = dependency_file.file
      result['modules'][i]['files'][j] = file
      # print(file, 'これが依存ファイル')
  print(result)

  return result
