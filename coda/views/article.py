from django.shortcuts import render
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

"""SQL
select coda_module.id as module_id, coda_article.id as article_id, coda_file.id as file_id  from coda_module inner join coda_article_module_dependencies on coda_module.id = coda_article_module_dependencies.module_id inner join coda_article on coda_article.id = coda_article_module_dependencies.article_id inner join coda_module_file_dependencies on coda_module_file_dependencies.module_id = coda_module.id inner join coda_file on coda_file.id = coda_module_file_dependencies.file_id;
"""

def create(request):
  post = request.POST
  print(post, '生のpost')

  # 実行するボタンでコード実行したときのみ
  # パラメータにはexecuteを含ませている
  if 'execute' in post:
    print(post)
    File(
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
      language = Language.objects.filter(name=post['language']).first(),
      user = User(id=1),
    ).save()
    File.objects.last().writeFile()

    output = Docker(File.objects.last()).run()
    print(output)

    json_str = json.dumps({
      'result': output
    }, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)

  # post通信があったときだけ
  if len(post):
    param_tree = ArticleEditPagePostParam(post).data
    SaveParamTree(param_tree)

  return render(request, 'article/create_base.html')

# ParamTreeを解析してDBに保存する
def SaveParamTree(param_tree):
  created_at = datetime.now()
  updated_at = datetime.now()

  # まずArticleを最初に保存する
  article = param_tree['article']
  title = article['title']
  body = article['body']

  Article(
    title = title,
    body = body,
    is_public = True,
    user = User.objects.get(id=1),
    created_at = created_at,
    updated_at = updated_at,
  ).save()

  # articleを削除すると、param_treeはmoduleだけになる
  param_tree.pop('article')

  print(param_tree) # moduleだけになっている

  zip_key = []
  zip_files = []

  for key in param_tree:
    # moduleの取得とこの2モデルをDBへ保存
    module = param_tree[key]
    name = module['name']
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
      article = Article.objects.all().last(),
      module = Module.objects.all().last(),
      created_at = created_at,
      updated_at = updated_at,
    ).save()

    # moduleからnameを削除するとfilesだけになる
    module.pop('name')

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

    files = collection[key]
    for file_id, file_values in files.items():
      file_tag_name = file_values['name']
      code = file_values['code']
      language = file_values['language']
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
        article = Article.objects.all().last(),
        language = Language.objects.filter(name=language).first(),
        user = User.objects.get(id=1),
      ).save()
      Module_File_Dependencies(
        module = Module.objects.all().last(),
        file = File.objects.all().last(),
        created_at = created_at,
        updated_at = updated_at,
      ).save()

  return


def getArticlePageByArticleId():
  user_id = 1
  article_id = 11

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
    'modules': {}
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


  # post = request.POST
  # for i in post:
  #   print(i)
  # print(post)

  # # print(post)
  # print('ここからcreateParamTree')
  # print(ArticleEditPagePostParam(post).data)

  # return



  # return render(request, 'article/create_base.html', getArticlePageByArticleId())
