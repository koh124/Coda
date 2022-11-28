FROM python:3.7

RUN mkdir /app
WORKDIR /app

COPY ./ ./

# 環境変数の設定
# APP_ENVをprodにするとsettings.pyで.env.prodを自動読み込み
ENV APP_ENV=dev

# ビルド開始
# RUN bash ./build.sh
RUN python3 -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt
RUN pip install mysqlclient
# RUN python3 manage.py collectstatic --no-input
# RUN python3 manage.py migrate
# RUN python3 manage.py setdefaultsuperuser
# RUN python3 manage.py seedlanguages

EXPOSE 8000

# アプリケーションスタート
# RUN gunicorn Coda_project.wsgi:application
