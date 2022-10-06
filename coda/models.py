from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# クラスはテーブルの定義
class Film(models.Model):
  name = models.CharField(max_length=100)
  publication_date = models.DateTimeField('date published')

class Theater(models.Model):
  # filmsに対してリレーションを作る
  film = models.ForeignKey(Film, on_delete=models.CASCADE) # 外部キー
  name = models.CharField(max_length=100)
  area = models.CharField(max_length=100)

# ・python3 manage.py makemigrations coda
# モデルに記述したDBスキーマを元にマイグレーションファイルを作成する

# ・python3 manage.py sqlmigrate coda <migration id>
# python3 manage.py sqlmigrate coda 0001 みたいな
# （テーブル作成したときの）sql文を出力しながらmigrateしてくれる

# ・python3 manage.py migrate
# こちらもmigrate実行
