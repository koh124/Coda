import re

"""
POSTパラメータ命名規則
①articleは常にひとつ
②moduleは連番
module1, module2, module3
③モデル自身のパラメータは-で表現
article-title, article-body, module1-name, module1-is_public
④has関係は所有モデル名のあとに付け加える
複合キー的にどこに依存してるモデルのvalueか分かる
module1file1, module2file1, module2file-code
"""

# 目的: POSTパラメータを整形したり管理する
class ArticleEditPagePostParam():

  def __init__(self, param):
    self.data = self.createParamTree(param)

  def createParamTree(self, post):
    result = {}
    for key in dict(post):
      if key == 'csrfmiddlewaretoken':
        continue

      value = post[key]
      splitted = key.split('-')
      model_name = splitted[0]
      value_name = splitted[1]
      separated = re.split('_', model_name) # module0file0の繋がりをsplitする
      # separated = re.split('(.*?[0-9])', model_name) # module0file0の繋がりをsplitする
      separated = [i for i in separated if i != ''] # ''をリスト内から削除
      print(separated, 'separatedはこれです')

      print(model_name, value_name, value, separated)

      # パターン
      # module.article.title
      # module.file_new0.language, name, code
      # module.file_new1.language, name, code
      # 初期化作業
      # module = {}
      # module.file_new0 = {}
      # module.file_new1 = {}
      # つまりモジュールに1回、fileごとに1回初期化が必要

      # separatedが['article'], ['module_new0', 'file_new0'], ['module_new0', 'file_new1']のどちらでも
      # result = {'module_new0': {}} となる初期化は必要になる（モジュールの初期化）
      if not(separated[0] in result):
        result[separated[0]] = {}

      # separatedの要素数が1、つまりarticle
      # ↓これを作る
      # result = {
      #   'article': {
      #     'title': value,
      #     'body': value
      #   }
      # }
      if len(separated) == 1:
        result[separated[0]][value_name] = value # すでにキーがあるならそのままvalueを突っ込む

      # separatedの要素数が2、つまりmodule0file0の場合
      # ↓これをつくる
      # result = {
      #   'module_new0': {
      #     'file_new0': {
      #       'name': 'ファイル名',
      #       'code': 'print()'
      #     }
      #   }
      # }
      # 課題 result.module_new.file_new1, result.module_new.file_new2 のケースがある
      elif len(separated) == 2:
        if not(separated[1] in result[separated[0]]):
          result[separated[0]][separated[1]] = {}
        result[separated[0]][separated[1]][value_name] = value

    print(result, 'これがParamTree')

    return result

  # 草案
  def Toy(params):
      separated = re.split('(?!\[|\])(.*?[0-9])', params) # module4, [][], file1, [][]に分割できる

  def Toy2(params):
    """
    # 仕様
    # <input name='data[]' value='a'>
    # <input name='data[]' value='b'>
    # <input name='data[][]' value='c'>
    # <input name='data[][]' value='d'>
    # ↓こうする
    # dict[key_name][depth][index]
    # {
    #   key_name: {
    #     (depth)0: [],
    #     (depth)1: []
    #   }
    # }
    """
    result = {}
    for key in dict(params):
      separated = re.split('(\[\])', key) # module4, [], file1を区切れるが、module4file1を分割できない
      print(separated)
      key_name = separated[0]
      array_depth = separated.count('[]')
      if key_name not in result:
        result[key_name] = {}
      result[key_name][array_depth] = params.getlist(key)
    return result
