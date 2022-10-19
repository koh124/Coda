from django.shortcuts import render
from django.http import HttpResponse
from ..models.models import *
from ..models.docker.docker import Docker
from ..models.docker.dockerinterface import DockerInterface
from ..models.languages import LANGUAGES
from datetime import datetime
import os
# from ..models.seeder_data import variable # seeder

def create(request):
  post = request.POST
  for i in post:
    print(i)
  print(post)
  return render(request, 'article/create_base.html')
