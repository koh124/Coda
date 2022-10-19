"""Coda_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from coda.views.views import test, djangoTemplateLanguage # 直接importしてルーティングを定義することもできる

# import debugpy
# port = 5678
# debugpy.listen(port)
# debugpy.wait_for_client()

# ルーティングを定義する
urlpatterns = [
    path('', include('coda.urls')),
    # path('coda/', include('coda.urls')), # "coda/url.py"のurlpatternsは、urlが'/coda'から続く形でルーティングされるようになる
    path('account/', include('account.urls')), # app名 = account のurl.pyを参照する
    # path('test/', test), # ルーティング関数を直接指定
    # path('test/', include('coda.urls')), # これらはappのurlで記述しているので、不要
    # path('dtl/', djangoTemplateLanguage),
    path('admin/', admin.site.urls),
]
