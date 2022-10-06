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
