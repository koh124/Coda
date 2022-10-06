from django.urls import path
from . import views

# urlとviewの対応を定義する（紐付けただけで、登録は別で行う）
urlpatterns = [
  path('', views.index, name='index'), # nameは名前つきルート?
  path('test', views.test, name='test'),
]
