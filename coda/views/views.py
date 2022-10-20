from django.shortcuts import render
from django.http import HttpResponse
from numpy import array
from ..models.models import *
from ..models.docker.docker import Docker
from ..models.languages import LANGUAGES
from datetime import datetime
import os
import re

# ここでviewを作成できる
# Create your views here.
def index(request):
  # print(File.objects.get(id=33).getLang())
  # print(File.objects.get(id=33).writeFile())
  # File(
  #   file_tag_name = 'sayHello',
  #   code = 'print("hello", "this is completely done")',
  #   file_name = 'sample_file_name',
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

  # output = Docker(File.objects.last()).run()
  # print(output)

  tree = createParamTree(request.POST)
  print(tree)

  # 継承したテンプレートを返す
  return render(request, 'index.html')

  # 文字列だけページに表示する
  return HttpResponse('Hello world!!')

def test(request):
  return render(request, 'index.html')

def djangoTemplateLanguage(request):
  param = {
    'key': 'value',
    'film': 'ワンピースFILM RED',
    'food': '寿司',
    'array': ['coffee', 'orange juice', 'vegetables']
  }
  return render(request, 'dtl.html', param) # viewに変数を渡す

# 草案
def createParamTree(params):
  result = {}
  for key in dict(params):
    separated = re.split('(?!\[|\])(.*?[0-9])', key) # module4, [][], file1, [][]に分割できる
    separated = [i for i in separated if not i is ''] # ''をリスト内から削除

    if len(separated) == 1:
      result[separated[0]] = {}
      result[separated[0]]['value'] = params.getlist(key)
    elif len(separated) == 2:
      if separated[1].startswith('file'):
        result[separated[0]]['files'] = params.getlist(key)

    print(separated, 'this is separated')
  print(result, 'これで完成?')

def Toy1(separated):
  # ["module4", "[][]"] これを ["module4[][]"] にする
  array = []
  for i in separated:
    if not i.startswith('[]'):
      array.append(i)
    else:
      array[-1] += i
  print(array)

def Toy2(params):
  """
  # 仕様
  # <input name='data[]' value='a'>
  # <input name='data[]' value='b'>
  # <input name='data[][]' value='c'>
  # <input name='data[][]' value='d'>
  # ↓こうする
  # dict[key_name][depth][index]
  # {
  #   key_name: {
  #     (depth)0: [],
  #     (depth)1: []
  #   }
  # }
  """
  result = {}
  for key in dict(params):
    separated = re.split('(\[\])', key) # module4, [], file1を区切れるが、module4file1を分割できない
    print(separated)
    key_name = separated[0]
    array_depth = separated.count('[]')
    if key_name not in result:
      result[key_name] = {}
    result[key_name][array_depth] = params.getlist(key)
  return result

def testPost():
  # post項目
  # ・user_id...auth_userから取得
  # ・article...{title, body, is_public}
  # ・module...
  # name=module, 同じdepth0のインデックスで1〜3個を表現
  # 各モジュール {name, is_public, is_importable, is_executable}
  # ・File...
  # name=file, 同じdepth0のインデックスで複数ファイルを表現
  # {language, file_tag_name, code, is_public, is_importable, is_executable, user_id, article_id
  #

  return
