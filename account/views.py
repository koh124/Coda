from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from . import forms

class TopView(TemplateView):
  template_name = "account/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
  template_name = "account/home.html"

  # django.contrib.auth.mixins の AccessMixinクラス の持つメソッド、
  # get_redirect_field_name()をオーバーライド
  # ここでreturnする文字列が未認証でhomeにきたときの
  # リダイレクト後のgetパラメータのnameに紐付けられる
  def get_redirect_field_name(self) -> str:
    return ''

class LoginView(LoginView):
  """ログインページ"""
  form_class = forms.LoginForm
  template_name = "account/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
  """ログアウトページ"""
  template_name = "account/login.html"
