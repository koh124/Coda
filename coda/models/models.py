from django.db import models
from django.contrib.auth.models import User
from .docker.docker import DockerInterface
from django.contrib.auth import get_user, get_user_model
from .languages import LANGUAGES
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

# ※リレーション再定義
# 追加の機能
# ・ユーザーのフォロー/フォロワー
# ・ユーザーのモジュール別import実績数
# ・ユーザーのファイル別import実績数
# ・記事別いいね数
# ・モジュール別いいね数
# ・ファイル別いいね数
# ・他ユーザーにモジュールがimportされると、モジュールとファイルはすべていいね＋1
# ・他ユーザーにファイルがimportされると、そのファイルはいいね＋1
# ・モジュール名やモジュールの各種設定が不要でNull able、だがシステム上はファイルとのリレーションはある

# 実装
# User_Follow_Followerテーブル
# id, follow_user, follower_user
# 1, Aさん, Bさん
# 2, Cさん, Aさん

# モジュールのimport記録
# imported_moduleテーブル
# id, import_user, imported_module
# 1, Aさん, Math pack
# ユーザーのモジュール別import実績数を取得する場合
# select count(*) from imported_module
# join imported_module_id on module.id
# where imported_module.user_id == user.id

# ファイルのimport記録
# imported_fileテーブル
# id, import_user, imported_file
# 1, Aさん, sayHello.py

# ※別のスキーマ案
# メリット: importする何か（他のユーザーから参照する何か）が増える度に改修に強い
# content_typeテーブル（これを主キーとして、fileやmoduleは外部キーで従属）
# id, name
# 1, file
# 2, module
# 3, article

# importテーブル
# content_type＋content_idの複合キーで決まる
# id, import_user, content_type, content_id
# 1, Aさん, 1, 1

# いいね機能
# favoriteテーブル
# id, favorite_user, content_type, content_id
# 1, Aさん, 3, 1
# リレーション
# いいね → one to one → article
# いいね → one to one → module
# いいね → one to one → file
# 複合して、
# いいね → has one → 複合キー(content_type + id)

# moduleテーブル
# name → null able
# module.nameが空白だったら、ユーザーはファイルだけを投稿すればいい
# module.nameが空白のまま編集中/投稿されたファイルは、ユーザーの画面ではファイルだけが見える
# module.nameを空白のまま記事を投稿することは可能である

class Article(models.Model):
  title = models.CharField(max_length=50) # 記事タイトル
  body = models.TextField() # 記事本文
  is_public = models.BooleanField(default=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Module(models.Model):
  name = models.CharField(max_length=255, blank=True, null=True)
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
  file_name = models.CharField(max_length=255) # sample_file_name # データベースに保存する名前
  file_path = models.CharField(max_length=1023) # path/to/file
  is_public = models.BooleanField(default=True)
  is_importable = models.BooleanField(default=True)
  is_executable = models.BooleanField(default=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def getLang(self):
    return self.language.name

  # fileのフルネームは保存しない
  def getFullFileName(self):
    language_extension = LANGUAGES[self.language.name]
    return f"{self.created_at.strftime('%Y%m%d-%H%M%S')}_{str(self.user.id).zfill(4)}_{str(self.id).zfill(8)}.{language_extension}"

  def writeFile(self):
    file_name = self.getFullFileName()
    file_path = os.path.join('coda/models/codes/user1', file_name)

    with open(file_path, 'w', encoding='utf-8') as file: # 一時的にファイルオブジェクトを作り、書き込みを行う
      file.write(self.code)

    return self

  def exec(self, docker:DockerInterface): # 依存注入できるようにした（スタブを入れてテストできる）
    docker.run()

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

class User_Follow_Follower(models.Model):
  """フォロー/フォロワーの組を記録する"""
  follow_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_user')
  follower_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_user')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Content_Type(models.Model):
  """file, module, article、コンテンツの種類のidを記録する"""
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Import_Log(models.Model):
  """
  file, moduleのimport履歴を記録する
  content_type, contentはimport対象を指定する複合キーになっている
  content_type=articleが不要な入力値になっているのが気になるところ
  """
  import_user = models.ForeignKey(User, on_delete=models.CASCADE)
  content_type = models.PositiveBigIntegerField()
  content = models.PositiveBigIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # 複合ユニーク制約
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['content_type', 'content'],
        name='import_log_unique'
      )
    ]

class Favorite(models.Model):
  """file, module, articleのいいねを記録する"""
  favorite_user = models.ForeignKey(User, on_delete=models.CASCADE)
  content_type = models.PositiveBigIntegerField()
  content = models.PositiveBigIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['content_type', 'content'],
        name='favorite_unique'
      )
    ]

# ・python3 manage.py makemigrations coda
# モデルに記述したDBスキーマを元にマイグレーションファイルを作成する

# ・python3 manage.py sqlmigrate coda <migration id>
# python3 manage.py sqlmigrate coda 0001 みたいな
# （テーブル作成したときの）sql文を出力しながらmigrateしてくれる

# ・python3 manage.py migrate
# こちらもmigrate実行
