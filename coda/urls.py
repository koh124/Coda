from django.urls import path
from .views import views
from .views import article

# appごとのルーティングを定義する
urlpatterns = [
  path('dtl/', views.djangoTemplateLanguage, name='dtl'),
  # path('', views.index, name='index'),
  path('', article.read, name='index'), # nameは名前つきルート?
  path('create/', article.read, name='create'),
  path('edit/', article.read, name='edit'),
  path('delete/', article.delete, name='delete')
]
