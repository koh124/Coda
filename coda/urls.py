from django.urls import path
from .views import views
from .views import article

# appごとのルーティングを定義する
urlpatterns = [
  path('', views.index, name='index'), # nameは名前つきルート?
  path('dtl/', views.djangoTemplateLanguage, name='dtl'),
  path('create/', article.read, name='create'),
  path('edit/', article.read, name='edit'),
]
