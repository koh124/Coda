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


# File(
#   file_tag_name = 'ファイルD',
#   code = '<?php echo "Hello, Seader, and php!!"',
#   file_name = 'sample_file',
#   file_path = 'path/to/file',
#   is_public = True,
#   is_importable = True,
#   is_executable = True,
#   created_at = datetime.now(),
#   updated_at = datetime.now(),
#   article = Article.objects.all().first(),
#   language = Language.objects.all().get(id=40),
#   user = User(id=1),
# ).save()
# File.objects.last().writeFile()

# File(
#   file_tag_name = 'ファイルE',
#   code = 'print("hello, Seader, and Python!!")',
#   file_name = 'sample_file',
#   file_path = 'path/to/file',
#   is_public = True,
#   is_importable = True,
#   is_executable = True,
#   created_at = datetime.now(),
#   updated_at = datetime.now(),
#   article = Article.objects.all().first(),
#   language = Language.objects.all().first(),
#   user = User(id=1),
# ).save()
# File.objects.last().writeFile()

# File(
#   file_tag_name = 'ファイルF',
#   code = 'echo "Hello, Seader, and Ruby"',
#   file_name = 'sample_file',
#   file_path = 'path/to/file',
#   is_public = True,
#   is_importable = True,
#   is_executable = True,
#   created_at = datetime.now(),
#   updated_at = datetime.now(),
#   article = Article.objects.all().first(),
#   language = Language.objects.get(id=41),
#   user = User(id=1),
# ).save()
# File.objects.last().writeFile()

# Article_Module_Dependencies(
#   article = Article.objects.all().first(),
#   module = Module.objects.all().last(),
#   created_at = datetime.now(),
#   updated_at = datetime.now()
# ).save()


def create(request):
  post = request.POST
  # for i in post:
  #   print(i)
  # print(post)

  # print(post)
  # print('ここからcreateParamTree')
  # print(ArticleEditPagePostParam(post).data)

  # return

  if 'csrfmiddlewaretoken' in post:
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

  return render(request, 'article/create_base.html')
  return render(request, 'article/create_base.html', getArticlePageByArticleId())

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

  """
  サンプルコード
  for i in range(0, 10):
  print(i *for i in range(0, 10):
  print(i * 2)

class myClass():
  num1 = 0
  num2 = 0

  def __init__(self, arg1, arg2):
    self.num1 = arg1
    self.num2 = arg2

  def call(self):
    self.addition(self.num1, self.num2)

  def addition(self, arg1, arg2):
    print(arg1 + arg2)

myClass(100, 150).call()
  """

  """
  class MyClass():
  num1 = 0
  num2 = 0

  def python():
    print('my message')

  def __init__(self):
    self.num1 = 100
    self.num2 = 100
    self.add(self.num1, self.num2)

  def add(self, num1, num2):
    print(num1 + num2)

MyClass()
  """
