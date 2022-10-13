from django.db import models

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
  language = models.ForeignKey(Language, on_delete=models.CASCADE)

class Code(models.Model):
  module_name = models.CharField(max_length=50) # SayHello
  language = models.CharField(max_length=50) # python
  code = models.TextField() # print("Hello")
  file_name = models.CharField(max_length=50) # 20221212_something_11.py
  file_path = models.URLField() # path/to/file
  web_client_lang = models.BooleanField(default=False) # False
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Code_Conf(models.Model):
  public = models.BooleanField(default=False)
  executable = models.BooleanField(default=False)
  code = models.ForeignKey(Code, on_delete=models.CASCADE)

# ・python3 manage.py makemigrations coda
# モデルに記述したDBスキーマを元にマイグレーションファイルを作成する

# ・python3 manage.py sqlmigrate coda <migration id>
# python3 manage.py sqlmigrate coda 0001 みたいな
# （テーブル作成したときの）sql文を出力しながらmigrateしてくれる

# ・python3 manage.py migrate
# こちらもmigrate実行
