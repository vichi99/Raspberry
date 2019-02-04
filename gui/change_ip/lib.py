import subprocess, os
# subprocess.call("echo 'a'", shell=True)

class ChangeConf():

    def __init__(self, file_path = "", password = ""):
        self.file_path = file_path
        self.text = ""
        self.password = password

    def load_data(self, data):
        self.data = data

    def check_file(self):
        if os.path.isfile(self.file_path):
            print("file ok")
            return True
        else:
            print("file Nok")
            return False

    def load_file(self):
        if self.check_file():
            self.file = open(self.file_path, "r")
            line = self.file.readline().rstrip()  # strip()
            while line:
                if line == "\n":            # if empty line, continue
                    line = " "
                    # continue
                else:
                    line = line.strip()     #if not empty, strip

                if line.find("#", 0, 5):    # check if commented
                    for key, value in self.data.items():
                        if key in line:
                            line = value

                self.text += line + "\n"
                line = self.file.readline()

            self.file.close()

    def save_file(self):
        self.file = open(self.file_path, "w")
        self.file.write(self.text)
        self.file.close()

    def bash(self, commands):
        for i in commands:
            # subprocess.call(i + " | sudo -S {}".format(self.password), shell=True)
            pass
