from django.shortcuts import render
from django.http import HttpResponse
# from .models.models import Article, Code, Language, User
from ..models.docker.docker import Docker
from ..models.docker.dockerinterface import DockerInterface
from ..models.languages import LANGUAGES
from datetime import datetime
import os

# ここでviewを作成できる
# Create your views here.
def index(request):
  post = ['python', 'print("hello!! this is from a view")']
  post = ['php', '<?php \necho("hi!! Im come from view!");']
  post = ['python', "import math\nprint(math.sqrt(81))"] # モジュールはインストールしないと使えない

  # User(name='koh').save()
  # Language(name='python').save()
  # Article(title='pythonで標準出力する方法', body='pythonで標準出力する方法を紹介します', language=Language(id=1)).save()

  # code = CodeController(lang=post[0], code=post[1])
  # code.writeFile()

  # output = Docker(code).run()
  # print(output)

  # パラメータ受け取り
  print(request.POST) # postパラメータ受け取り
  print(request.GET) # getパラメータ受け取り

  # 継承したテンプレートを返す
  return render(request, 'child.html')

  # 文字列だけページに表示する
  return HttpResponse('Hello world!!')

# settings.pyで必要なこと
# INSTALLED_APPSにcoda（アプリケーション名）を追加する
# これがないとtemplatesのレンダリングができない
def test(request):
  # return HttpResponse('test routing')
  return render(request, 'index.html')

def djangoTemplateLanguage(request):
  param = {
    'key': 'value',
    'film': 'ワンピースFILM RED',
    'food': '寿司',
    'array': ['coffee', 'orange juice', 'vegetables']
  }
  return render(request, 'dtl.html', param) # viewに変数を渡す

example = {
  'lang': 'python',
  'code': 'print("hello coda!!")'
}

# Codeモデルを継承 Code
class CodeController():
  module_name = "SayHello"
  language = "python"
  code = 'print("Hello")'
  file_name = "20221212_something_11.py"
  file_path = ""
  web_client_lang = False
  user = 1
  article = 1
  created_at = datetime.now()
  updated_at = datetime.now()

  # オブジェクト生成した瞬間にレコードが1件追加されるのか？
  # case: 下書き、オンラインエディタとして実行
  # →ファイル生成やpath設定を行っていい
  # →実行したいだけなら？
  # →レコードはいらない
  def __init__(self, lang=example['lang'], code=example['code']) -> None:
    self.language = lang
    self.code = code
    self.created_at = datetime.now()

  def getLang(self):
    return self.language

  def writeFile(self):
    # ファイル名: フォーマット
    # YYYYMMDDHHmmSS_userid_1111.lang
    date = self.created_at
    self.file_name = str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second) + '_' + '1' + '_' + '1111' + '.' + LANGUAGES[self.language]
    self.file_path = os.path.join('coda/models/codes/user1', self.file_name)

    with open(self.file_path, 'w', encoding='utf-8') as file: # 一時的にファイルオブジェクトを作り、書き込みを行う
      file.write(self.code)

    return self

  def exec(self, docker:DockerInterface): # 依存注入できるようにした（スタブを入れてテストできる）
    docker.run()
