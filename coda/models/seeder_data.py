from .models import *
from django.contrib.auth.models import User
from datetime import datetime
import random
from .languages import LANGUAGES
# from .docker.docker import Docker
# from .docker.dockerinterface import DockerInterface
# import os

Article(
  title = 'DjangoのORMについて',
  body = '記事の本文です',
  is_public = True,
  user = User(id=1),
  created_at = datetime.now(),
  updated_at = datetime.now()
).save()

Module(
  name = 'ORM_ver0.1',
  is_public = True,
  is_importable = True,
  is_executable = True,
  user = User(id=1),
  created_at = datetime.now(),
  updated_at = datetime.now()
).save()

File(
  file_tag_name = 'ファイルA',
  code = 'print("hello, world!!")',
  file_name = 'sample_file',
  file_path = 'path/to/file',
  is_public = True,
  is_importable = True,
  is_executable = True,
  created_at = datetime.now(),
  updated_at = datetime.now(),
  article = Article.objects.all().first(),
  language = Language.objects.all().first(),
  user = User(id=1),
).save()
File.objects.last().writeFile()

File(
  file_tag_name = 'ファイルB',
  code = 'print("hello, coda!!")',
  file_name = 'sample_file',
  file_path = 'path/to/file',
  is_public = True,
  is_importable = True,
  is_executable = True,
  created_at = datetime.now(),
  updated_at = datetime.now(),
  article = Article.objects.all().first(),
  language = Language.objects.all().first(),
  user = User(id=1),
).save()
File.objects.last().writeFile()

File(
  file_tag_name = 'ファイルC',
  code = 'print("hello, CodaProject!!")',
  file_name = 'sample_file',
  file_path = 'path/to/file',
  is_public = True,
  is_importable = True,
  is_executable = True,
  created_at = datetime.now(),
  updated_at = datetime.now(),
  article = Article.objects.all().first(),
  language = Language.objects.all().first(),
  user = User(id=1),
).save()
File.objects.last().writeFile()

Article_Module_Dependencies(
  article = Article.objects.all().first(),
  module = Module.objects.all().first(),
  created_at = datetime.now(),
  updated_at = datetime.now()
).save()

for file in File.objects.all():
  Module_File_Dependencies(
    module = Module.objects.all().first(),
    file = file,
    created_at = datetime.now(),
    updated_at = datetime.now()
  ).save()

File_File_Dependencies(
  file = File.objects.all().first(),
  dependency_file = File.objects.all().first(),
  created_at = datetime.now(),
  updated_at = datetime.now()
).save()

User_Follow_Follower(
  follow_user = User(id=1),
  follower_user = User(id=1),
  created_at = datetime.now(),
  updated_at = datetime.now()
).save()

Import_Log(
  import_user = User(id=1),
  content_type = random.randint(22,23),
  content = File.objects.all().first().id,
  created_at = datetime.now(),
  updated_at = datetime.now()
).save()

Favorite(
  favorite_user = User(id=1),
  content_type =  random.randint(22,23),
  content = File.objects.all().first().id,
  created_at = datetime.now(),
  updated_at = datetime.now()
).save()

# variable = ''
