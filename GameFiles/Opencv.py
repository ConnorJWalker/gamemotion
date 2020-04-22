import os
import subprocess

class OpenCV:
    def __init__(self, wd):
        self.OpenCvBuildLocation = "Debug/" if os.name == "nt" else "cmake-build-debug/" 
        self.OpenCvDirectory = wd + '../TSE-Vision/' + self.OpenCvBuildLocation#location of .exe file
        self.OpenCvFileName = 'vision'#name of your .exe file

    def start(self):
        print("Started vision code")
        self.app = subprocess.Popen([self.OpenCvFileName, "-o", "output.txt", "--render"])

    def __del__(self):
        print("Closing vision application")
        self.app.kill()