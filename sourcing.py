from flask import Flask, render_template, request
#from werkzeug import secure_filename
import os



class ConfigData :
    def __init__(self,file,m):
        self.f =file
        self.m = m

    def get_avi_video (self):
        file_avi =[]
        cwd =os.getcwd()
        for l in os.listdir(cwd):
            if l.endswith(".avi"):
                file_avi.append(l)

        return file_avi
