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
  name = ''
  WORKING_DIR = '/usr/src/myapp'

  def __init__(self, file) -> None: # オブジェクト生成時にcodeを受け取る
    self.file = file
    self.name = 'running-script' + '_' + file.getFullFileName() + '_' + str(file.id)

  def run(self):
    cmd =  f"docker run -it --name {self.name} -v ~/desktop/coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} {self.file.language.name} {self.file.language.name} ./codes/user1/{self.file.getFullFileName()}"
    cmd =  f"docker run -it --rm --name {self.name} -v ~/desktop/coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} {self.file.language.name} {self.file.language.name} ./codes/user1/{self.file.getFullFileName()}"
    # cmd =  f"docker run -it --rm --name node-docker -v ~/desktop/coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} -u node node ./codes/user1/{self.file.getFullFileName()}"
    # cmd =  f"docker run -it --name node-docker -v ~/desktop/coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} -u node node ./codes/user1/20221021-060946_0001_00000094.js"
    print(self.file.getFullFileName())
    print(cmd)

    return subprocess.run(
      cmd, timeout=15, shell=True,
      stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).stdout.decode()

  def build():
    pass

  def tag():
    pass

  def volume():
    pass
