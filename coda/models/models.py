from django.db import models
from .code.codeinterface import CodeInterface
from .docker.docker import DockerInterface
from .languages import LANGUAGES
from datetime import datetime
import os

# Create your models here.

# モデルのルール
# ・1つのモデルは1つのテーブルと対応
# ・モデル名は大文字で始める
# ・モデルはdjango.db.models.Modelのサブクラス
# ・Primary keyを定義しなければ、idフィールドは自動で定義される
# ・オプションで指定しなければ自動的にNOT NULLになる
# ・テンプレートで {{ 小文字モデル名.メソッド名 }} とすることで戻り値を得られる

# 各フィールドの対応
# charField → varchar
# TextField → 大量の文字列を保存するのに使う（textarea）
# IntegerField → integer
# PositiveIntegerField → 正の整数
# DateField → 日付
# DateTimeField → datetime.datetimeと同じ
# FileField → ファイルアップロード

# フィールドのオプション
# ・DateTimeField
# auto_now オブジェクトが変更される度に自動的に現在の日付を保存する
# auto_now_add オブジェクトが最初に作成されたときに自動的に現在の日付を保存する

# リレーション
# User -> has many -> Article -> has many -> Code
# Code → has one → Language
# Language → has many → Article
# Language → has many → Code

# クラスはテーブルの定義
class User(models.Model):
  name = models.CharField(max_length=32)

class Language(models.Model):
  name = models.CharField(max_length=50)

class Article(models.Model):
  title = models.CharField(max_length=50) # 記事タイトル
  body = models.TextField() # 記事本文
  lang_id = models.ForeignKey(Language, on_delete=models.CASCADE)

example = {
  'lang': 'python',
  'code': 'print("hello coda!!")'
}

class Code(models.Model):
  module_name = models.CharField(max_length=50) # SayHello
  language = models.CharField(max_length=50) # python
  code = models.TextField() # print("Hello")
  file_name = models.CharField() # 20221212_something_11.py
  file_path = models.URLField() # path/to/file
  web_client_lang = models.BooleanField(default=False) # False
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

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

class Code_Conf(models.Model):
  public = models.BooleanField(default=False)
  executable = models.BooleanField(default=False)
  code_id = models.ForeignKey(Code, on_delete=models.CASCADE)

class Film(models.Model):
  name = models.CharField(max_length=100)
  publication_date = models.DateTimeField('date published')

class Theater(models.Model):
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
