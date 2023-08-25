# Import necessary libraries
import socket
import time
import numpy as np
import time

### Set up the connectivities
HOST = "  " # The remote host (Give the ip)
PORT = 30002 # The same port as used by the server

### VARIABLES IF REQUIRED
print ("Starting Program")
count = 0

while (count < 1):
    ### CONNECT 2ND CLIENT INTERFACE
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    robot_pose = -0.1215,-0.6237,0.27708,0.079,-3.120,0.041
    ###MOVE TO CAPTURE POSITION
    print("Robot goes to the capturing position")
    s.send (("movej(p[robot_pose], a=1.0, v=0.5)" + "\n").encode('utf-8'))
    time.sleep(3)
    
    count = count + 1
s.close()