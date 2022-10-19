from django.urls import path
from .views import views
from .views import article

# appごとのルーティングを定義する
urlpatterns = [
  path('', views.index, name='index'), # nameは名前つきルート?
  path('test/', views.test, name='test'),
  path('dtl/', views.djangoTemplateLanguage, name='dtl'),
  path('create/', article.create, name='create'),
]
