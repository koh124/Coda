from .codeinterface import CodeInterface
from coda.models.docker.docker import DockerInterface
from .languages import LANGUAGES
from datetime import datetime
import os

"""
【Code】
このApiを使えば、コードの実行環境をつくり、入力→処理→出力を行ってもらえることが保証される

【対応言語（＝サーバーサイド言語）】
python、php、Ruby、node.js...
などをサポート
"""

example = {
  'lang': 'python',
  'code': 'print("hello coda!!")'
}

class Code(CodeInterface):
  user_id = ''
  lang = ''
  code = ''
  created_at = ''
  file_name = ''
  file_path = ''

  def __init__(self, lang=example['lang'], code=example['code']) -> None:
    self.lang = lang
    self.code = code

  def getLang(self):
    return self.lang

  def writeFile(self):
    # ファイル名: フォーマット
    # YYYYMMDDHHmmSS_userid_1111.lang
    date = datetime.now()
    self.created_at = date

    file_name = str(date.year) + str(date.month) + str(date.day) + str(date.hour) + str(date.minute) + str(date.second) + '_' + '1' + '_' + '1111' + '.' + LANGUAGES[self.lang]
    self.file_name = file_name

    file_path = os.path.join('coda/models/codes/user1', file_name)
    self.file_path = file_path

    with open(file_path, 'w', encoding='utf-8') as file: # 一時的にファイルオブジェクトを作り、書き込みを行う
      file.write(self.code)

    return self

  def exec(self, docker:DockerInterface): # 依存注入できるようにした（スタブを入れてテストできる）
    docker.run()

  def getStdOut(self):
    pass
