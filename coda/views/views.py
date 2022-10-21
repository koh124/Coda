from django.shortcuts import render
from django.http import HttpResponse
from ..models.models import *
from ..models.docker.docker import Docker
from .articleeditpagepostparam import ArticleEditPagePostParam
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

  print(request.POST)
  ArticleEditPagePostParam(request.POST)

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
