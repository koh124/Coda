from django.urls import path
from . import views

# appごとのルーティングを定義する
urlpatterns = [
  path('', views.index, name='index'), # nameは名前つきルート?
  path('test', views.test, name='test'),
  path('dtl', views.djangoTemplateLanguage, name='dtl'),
]
