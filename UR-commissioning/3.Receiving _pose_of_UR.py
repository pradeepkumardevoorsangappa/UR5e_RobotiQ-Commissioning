# Import necessary libraries
import rtde_receive
import math
import io_signals

# initialize RTDE interface to receive the commands from the robot
rtde_r = rtde_receive.RTDEReceiveInterface("ip")

# Getting the current pose of the robot
actual_q = rtde_r.getActualQ() 
print(actual_q)

# Converting the radians into Degree
joints=math.degrees(actual_q[0]),math.degrees(actual_q[1]),math.degrees(actual_q[2]),math.degrees(actual_q[3]),math.degrees(actual_q[4]),math.degrees(actual_q[5])]
print(joints)

# Reading the Digital Inputs from Robot PLC
num=io_signals.io_signals()
num=num[0]
print(num)