from django.shortcuts import render
from django.http import HttpResponse

# ここでviewを作成できる
# Create your views here.
def index(request):
  return HttpResponse('hello world')

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
