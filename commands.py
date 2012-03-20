# Here you can create play commands that are specific to the module, and extend existing commands

import os, os.path
import sys
import shutil
import subprocess

MODULE = 'wsimport'

# Commands that are specific to your module

COMMANDS = ['wsimport:gen']

def execute(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "wsimport:gen":
        if os.path.exists("tmp/jaxws/"):
            shutil.rmtree("tmp/jaxws")

        os.makedirs("tmp/jaxws/")

        for x in args:
            wsimport_args = ["-d ", "tmp/jaxws/ ", x]
            java_cmd = app.java_cmd(['-Xmx64m'], className='com.sun.tools.ws.WsImport', args=[wsimport_args])
            #print java_cmd
            #print os.environ
            subprocess.call(java_cmd, env=os.environ)

        jar_args = [" -cvf", " lib/jaxws.jar", " -C"," tmp/jaxws/", " ."]
        java_cmd = app.java_cmd(['-Xmx64m'], className='sun.tools.jar.Main', args=[jar_args])
        #print java_cmd
        subprocess.call(java_cmd, env=os.environ)

# This will be executed before any command (new, run...)
def before(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")


# This will be executed after any command (new, run...)
def after(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "new":
        pass
