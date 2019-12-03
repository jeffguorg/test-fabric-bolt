from fabric.api import run, local, sudo

def ping():
    print("pong")

def sleep(dur):
    local("sleep " + str(dur))
