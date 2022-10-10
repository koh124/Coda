from django.shortcuts import render
from django.http import HttpResponse
from .models.code.code import Code
from .models.docker.docker import Docker

import debugpy
port = 5678
debugpy.listen(port)
debugpy.wait_for_client()

# ここでviewを作成できる
# Create your views here.
def index(request):
  post = ['python', 'print("hello!! this is from a view")']
  post = ['php', '<?php \necho("hi!! Im come from view!");']
  post = ['python', "import math\nprint(math.sqrt(81))"] # モジュールはインストールしないと使えない

  code = Code(lang=post[0], code=post[1])
  code.writeFile()

  docker = Docker(code)
  output = docker.run()

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
