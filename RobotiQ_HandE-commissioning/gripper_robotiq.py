import socket
import time

def Activate():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_activate = open ("path_to /Gripperactivate.script", "rb")
    l_activate = f_activate.read(1024)
    while (l_activate):
        s.send(l_activate)
        l_activate = f_activate.read(1024)
    s.close()
    
def Open():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_open = open ("path_to /Gripperopen.script", "rb")
    l_open = f_open.read(1024)
    while (l_open):
        s.send(l_open)
        l_open = f_open.read(1024)
    s.close()

def Close():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_close = open ("path_to /Gripperclose.script", "rb")
    l_close = f_close.read(1024)
    while (l_close):
        s.send(l_close)
        l_close = f_close.read(1024)
    s.close()
def reset():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_reset = open ("path_to /Gripperreset.script", "rb")
    l_reset = f_reset.read(1024)
    while (l_reset):
        s.send(l_reset)
        l_reset = f_reset.read(1024)
    s.close()
def Control():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_cw = open ("path_to /Gripper.script", "rb")
    l_cw = f_cw.read(1024)
    while (l_cw):
        s.send(l_cw)
        l_cw = f_cw.read(1024)
    s.close()