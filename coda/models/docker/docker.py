# from coda.models.code.codeinterface import CodeInterface
from coda.models.docker.dockerinterface import DockerInterface
import os
import subprocess

"""
【Docker】
dockerの機能を持つ
codeを受け取り、webかserverか処理したい希望を聞いて、docker runコマンドを組み立てて実行する。
コンテナとアプリのinterfaceと言える。
"""

class Docker(DockerInterface):
  name = 'running-script' + 'a'
  WORKING_DIR = '/usr/src/myapp'
  code = ''

  def __init__(self, code) -> None: # オブジェクト生成時にcodeを受け取る
    self.code = code

  def run(self):
    # cmd =  f"docker run -it --rm --name {self.name} -v ~/desktop/coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} {self.lang} {self.lang} ./codes/user1/{self.FILE_NAME}"
    # cmd =  f"docker run -it --name {self.name} -v ~/desktop/coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} {self.lang} {self.lang} ./codes/user1/{self.FILE_NAME}"
    cmd =  f"docker run -it --rm --name {self.name} -v ~/desktop/coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} {self.code.language} {self.code.language} ./codes/user1/{self.code.file_name}"
    print(cmd)

    ret = subprocess.run(
      cmd, timeout=15, shell=True,
      stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )

    return ret.stdout.decode()

  def build():
    pass

  def tag():
    pass

  def volume():
    pass
