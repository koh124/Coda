# Coda

# 概要
codaは主にスクリプト言語のオンライン実行環境＋記事投稿形式でのコード共有サービスを提供することを目指して、開発されています。

現在、オンライン実行環境はpython、php、ruby、javascriptの4つの言語に対応しています。

実装済み機能

・python, php, ruby, javascriptコード(node.js, 非モジュール)の実行

・コードの記事新規作成

・作成した記事の読み込み

・記事の編集

・記事の削除

# 使い方
コードのオンライン実行環境はDockerで動作しているので、Dockerをインストールしてログインしておく必要があります。

```
git clone https://github.com/koh124/Coda.git 
```
.envファイルに必要な環境変数のサンプルがあります。ファイル名を.env.devに書き換えると、settings.pyで読み込んでくれます。

・開発環境でのデフォルトのDBはMySQLです。

・ビルド
```
bash ./build.sh
```

・アプリケーションスタート
```
python3 manage.py runserver
```

# 開発環境
vscode
python/Django
javascript/jquery
html
css

デプロイ環境...render.com（進行中）
