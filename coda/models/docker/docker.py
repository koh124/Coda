from coda.models.docker.dockerinterface import DockerInterface
import os
import subprocess
import time

"""
【Docker】
dockerの機能を持つ
codeを受け取り、webかserverか処理したい希望を聞いて、docker runコマンドを組み立てて実行する。
コンテナとアプリのinterfaceと言える。
"""

class Docker(DockerInterface):
  name = ''
  # WORKING_DIR = '/usr/src/myapp'
  WORKING_DIR = '/usr/app'

  def __init__(self, file) -> None: # オブジェクト生成時にcodeを受け取る
    self.file = file
    self.name = 'running-script' + '_' + file.getFullFileName() + '_' + str(file.id)

  def run(self):
    cmd =  f"docker run -it --name {self.name} -v ./coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} {self.file.language.name} {self.file.language.name} ./codes/user1/{self.file.getFullFileName()}"
    cmd =  f"docker run -it --rm --name {self.name} -v ./coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} {self.file.language.name} {self.file.language.name} ./codes/user1/{self.file.getFullFileName()}"
    cmd =  f"docker run -it --rm --name {self.name} -v ~/devs/Coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} {self.file.language.name} {self.file.language.name} ./codes/user1/{self.file.getFullFileName()}"
    cmd =  f"docker run -it --rm --name {self.name} -v ${{PWD}}/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} {self.file.language.name} {self.file.language.name} ./codes/user1/{self.file.getFullFileName()}"
    print(self.name)
    if self.file.language.name == 'js':
      cmd =  f"docker run -it sample-image:latest sh"
      cmd =  f"docker run -it sample-image:latest"

      self.build()

    # cmd =  f"docker run -it --rm --name node-docker -v ~/desktop/coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} node:alpine node ./codes/user1/{self.file.getFullFileName()}"
    # cmd =  f"docker run -it --rm --name node-docker -v ~/desktop/coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} node:alpine node 20221123-024047_0001_00000368.js"
    # cmd =  f"docker run -it --name node-docker -v ~/desktop/coda_project/coda/models:{self.WORKING_DIR} -w {self.WORKING_DIR} -u node node ./codes/user1/20221021-060946_0001_00000094.js"
    print(self.file.getFullFileName())
    print(cmd)

    # return os.system(cmd)

    return subprocess.check_output(cmd, shell=True).decode()

    return subprocess.run(
      cmd, timeout=15, shell=True,
      stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).stdout.decode()

  def build(self):
    # file_name =  f'../codes/user1/{self.file.getFullFileName()}'
    # file_name = '20221123-024047_0001_00000368.js'
    file_name = self.file.getFullFileName()

    with open('./coda/models/codes/Dockerfile', mode='w', encoding='utf-8') as f:
      f.write('FROM node:alpine\n')
      f.write('WORKDIR /usr/app\n')
      f.write('COPY ./package.json ./\n')
      f.write('RUN npm install\n')
      # f.write('COPY ./ ./\n')
      f.write('COPY ./user1/ ./\n')
      f.write(f'CMD ["node", "{file_name}"]')
      f.close()

    cmd = 'docker build -t sample-image:latest ./coda/models/codes/'
    print(os.path)
    return os.system(cmd)

  def tag():
    pass

  def volume():
    pass
