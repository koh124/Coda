from .models import *
from datetime import datetime
# from ..models.docker.docker import Docker
# from ..models.docker.dockerinterface import DockerInterface
# from ..models.languages import LANGUAGES
# import random
# import os

# Language
array = ['python', 'php', 'ruby', 'html', 'css', 'js']
for i in array:
  Language(
    name = i,
    created_at = datetime.now(),
    updated_at = datetime.now()
  ).save()

# Content_type
contents = ['file', 'module', 'article']
for i in contents:
  Content_Type(
    name = i,
    created_at = datetime.now(),
    updated_at = datetime.now()
  ).save()
