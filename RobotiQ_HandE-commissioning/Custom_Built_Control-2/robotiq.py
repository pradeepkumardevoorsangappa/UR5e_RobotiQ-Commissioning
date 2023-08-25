import socket
import time

file=" path_to Gripper.script" #Destination to the .script file

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

# function defined for Actuating the gripper
def Activate():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    command='   rq_activate_and_wait()\n'
    replace_line(file,2374,command)
    f_activate = open ("path_to Gripper.script", "rb")
    l_activate = f_activate.read(1024)
    while (l_activate):
        s.send(l_activate)
        l_activate = f_activate.read(1024)
    s.close()

# function defined for Openning the gripper    
def Open():
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    command='   rq_open()\n'
    replace_line(file,2374,command)
    f_open = open ("path_to Gripper.script", "rb")
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
    command='   rq_close()\n'
    replace_line(file,2374,command)
    f_close = open ("path_to Gripper.script", "rb")
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
    command='   rq_reset()\n'
    replace_line(file,2374,command)
    f_reset = open ("path_to Gripper.script", "rb")
    l_reset = f_reset.read(1024)
    while (l_reset):
        s.send(l_reset)
        l_reset = f_reset.read(1024)
    s.close()

# function defined for Closing the gripper
def move(n):
    HOST = " ip " # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    i=int(int(n)*255/100)
    pos=f'rq_move({i},gripper_socket="1")'
    command=f'   {pos}\n'
    replace_line(file,2374,command)
    f_cw = open ("path_to Gripper.script", "rb")
    l_cw = f_cw.read(1024)
    while (l_cw):
        s.send(l_cw)
        l_cw = f_cw.read(1024)
    s.close()