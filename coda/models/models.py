from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user, get_user_model

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
# User.id -> has many -> Article.user_id ユーザーは複数の記事を持つ
# User.id -> has many -> Code.user_id ユーザーは複数のコードを持つ
# Article.id -> has many -> Code.article_id 記事は複数のコードを持つ
# Language.id -> has many -> Article.language_id, Code.language_id 言語は複数の記事とコードを持つ

# article
# id, title, body, is_public, user, created_at, updated_at

# article_module_dependencyテーブル
# ※一つのarticleに対し、3つのモジュールまで
# ※記事は書いたユーザーのものだが、モジュールは作成した人のもの
# id, article_id, module_id, created_at, updated_at
# 1, 1, 1 \
# 2, 1, 2  | これは絶対に同じユーザーのモジュールにならなくてはいけない→そんなことはない
# 3, 1, 3 /

# moduleテーブル（複数のファイルをパッケージ化したもの）
# id, name, is_public, is_importable, is_executable, user, created_at, updated_at

# fileテーブル（ファイル命名規則: 作成日時_userid_fileid.lang）
# ※publicはファイルを他ユーザーに公開するかを規定
# ※importableは他ユーザーのファイルimportを許可するかを規定
# ※executableは実行可能環境がないけど共有したいコードかどうかを規定（bashコードとか送られても実行できない）
# id, language, file_tag_name, module, code, file_name, file_path, is_public, is_importable, is_executable, user, article, created_at, updated_at

# file_dependency中間テーブル（多ファイル対多ファイルを表現）
# dependency_pair_id, file_id, dependency_file_id, created_at, updated_at
# dependency_pair_id, file_id, dependency_file_id...

# language
# id, name
# 1 python
# 2 php
# 3 css
# 4 html
# 5 js
# 6 scss
# 7 bash

# デザイン
# ＋モジュール
# ＋モジュール
# ＋モジュール
# 記事タイトル
# 記事本文

# ＋モジュール（開）
# |エディタ
# |
# |
# ...
# |
# stdout stdin（タブ別）

class Article(models.Model):
  title = models.CharField(max_length=50) # 記事タイトル
  body = models.TextField() # 記事本文
  is_public = models.BooleanField(default=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Module(models.Model):
  name = models.CharField(max_length=255)
  is_public = models.BooleanField(default=True)
  is_importable = models.BooleanField(default=True)
  is_executable = models.BooleanField(default=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Language(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class File(models.Model):
  language = models.ForeignKey(Language, on_delete=models.CASCADE)
  file_tag_name = models.CharField(max_length=255) # SayHello
  code = models.TextField() # print("Hello")
  file_name = models.CharField(max_length=255)
  file_path = models.CharField(max_length=1023) # path/to/file
  is_public = models.BooleanField(default=True)
  is_importable = models.BooleanField(default=True)
  is_executable = models.BooleanField(default=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Article_Module_Dependencies(models.Model):
  """ArticleとModuleのN対N中間テーブル"""
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  module = models.ForeignKey(Module, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Module_File_Dependencies(models.Model):
  """
  ModuleとFileの中間テーブル
  原則1モジュール対3ファイルだが、
  別のモジュールとのリレーションがあってもいいはず
  なのでN対Nになり中間テーブルが必要になる
  """
  module = models.ForeignKey(Module, on_delete=models.CASCADE)
  file = models.ForeignKey(File, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class File_File_Dependencies(models.Model):
  """FileとFileの中間テーブル"""
  file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='origin_file')
  dependency_file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='reference_file')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# ・python3 manage.py makemigrations coda
# モデルに記述したDBスキーマを元にマイグレーションファイルを作成する

# ・python3 manage.py sqlmigrate coda <migration id>
# python3 manage.py sqlmigrate coda 0001 みたいな
# （テーブル作成したときの）sql文を出力しながらmigrateしてくれる

# ・python3 manage.py migrate
# こちらもmigrate実行
