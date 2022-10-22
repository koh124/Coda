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
# from ..models.seeder_data import variable # seeder

def create(request):
  post = request.POST
  # for i in post:
  #   print(i)
  # print(post)

  print(post)
  print('ここからcreateParamTree')
  print(ArticleEditPagePostParam(post).data)

  # if 'csrfmiddlewaretoken' in post:
  #   File(
  #     file_tag_name = 'MyPostCode',
  #     code = post['module1file1-code'],
  #     file_name = 'mypostcode',
  #     file_path = 'path/to/file',
  #     is_public = True,
  #     is_importable = True,
  #     is_executable = True,
  #     created_at = datetime.now(),
  #     updated_at = datetime.now(),
  #     article = Article.objects.all().first(),
  #     language = Language.objects.all().filter(id=39).first(),
  #     user = User(id=1),
  #   ).save()
  #   File.objects.last().writeFile()

  #   output = Docker(File.objects.last()).run()
  #   print(output)

  #   json_str = json.dumps({
  #     'result': output
  #   }, ensure_ascii=False, indent=2)
  #   return HttpResponse(json_str)

  return render(request, 'article/create_base.html')

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
