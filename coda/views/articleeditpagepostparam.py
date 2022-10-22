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
    self.article = []
    self.modules = []
    self.files = []
    for model_name in self.data:
      if model_name.startswith('article'):
        self.article = self.data[model_name]
      elif model_name.startswith('module'):
        self.modules.append(self.data[model_name])
        self.files = ([i for i in self.data[model_name]])
    print('ここからコンストラクタ')
    print(self.data)
    print(self.article)
    print(self.modules)
    print(self.files)

  def createParamTree(self, post):
    result = {}
    for key in dict(post):
      if key == 'csrfmiddlewaretoken':
        continue

      value = post[key]
      splitted = key.split('-')
      model_name = splitted[0]
      value_name = splitted[1]
      separated = re.split('(.*?[0-9])', model_name)
      separated = [i for i in separated if not i is ''] # ''をリスト内から削除

      print(model_name, value_name, value, separated)

      if not separated[0] in result:
        result[separated[0]] = {}

      if len(separated) == 1:
        result[separated[0]][value_name] = value
      elif len(separated) == 2:
        result[separated[0]][separated[1]] = {}
        result[separated[0]][separated[1]][value_name] = value

    print(result)
    # print(result['module1'])
    # print(result['module1']['file1'])
    # print(result['module1']['file1']['name'])

    return result

  # 草案
  def Toy(params):
    result = {}
    for key in dict(params):
      separated = re.split('(?!\[|\])(.*?[0-9])', key) # module4, [][], file1, [][]に分割できる
      separated = [i for i in separated if not i is ''] # ''をリスト内から削除

      if len(separated) == 1:
        result[separated[0]] = {}
        result[separated[0]]['value'] = params.getlist(key)
      elif len(separated) == 2:
        if separated[1].startswith('file'):
          result[separated[0]]['files'] = params.getlist(key)

      print(separated, 'this is separated')
    print(result, 'これで完成?')

  def Toy1(separated):
    # ["module4", "[][]"] これを ["module4[][]"] にする
    array = []
    for i in separated:
      if not i.startswith('[]'):
        array.append(i)
      else:
        array[-1] += i
    print(array)

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
