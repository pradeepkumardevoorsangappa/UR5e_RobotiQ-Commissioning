import socket
import time

# function defined for Actuating the gripper
def Activate():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_activate = open ("file_path_for Gripper.script", "rb")
    l_activate = f_activate.read(1024)
    while (l_activate):
        s.send(l_activate)
        l_activate = f_activate.read(1024)
    s.close()

# function defined for Opening the gripper
def Open():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_open = open ("file_path_for Gripper.script", "rb")
    l_open = f_open.read(1024)
    while (l_open):
        s.send(l_open)
        l_open = f_open.read(1024)
    s.close()

# function defined for Closing the gripper
def Close():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_close = open ("file_path_for Gripper.script", "rb")
    l_close = f_close.read(1024)
    while (l_close):
        s.send(l_close)
        l_close = f_close.read(1024)
    s.close()
    
# function defined for Resetting the gripper
def reset():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_reset = open ("file_path_for Gripper.script", "rb")
    l_reset = f_reset.read(1024)
    while (l_reset):
        s.send(l_reset)
        l_reset = f_reset.read(1024)
    s.close()


def cw():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_cw = open ("file_path_for Gripper.script", "rb")
    print(f_cw)
    l_cw = f_cw.read(1024)
    print(l_cw)
    while (l_cw):
        s.send(l_cw)
        l_cw = f_cw.read(1024)
    s.close()
    return f_cw,l_cw