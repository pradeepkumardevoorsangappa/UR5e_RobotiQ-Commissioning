# Import necessary libraries
import rtde_control
import time
ip = "  " (Give the ip)

# initialize RTDE interface to control the robot
rtde_c = rtde_control.RTDEControlInterface(ip)

# Moving the robot with predefined position 
rtde_c.moveL([-0.36783,-0.68956,0.11500,2.232,2.201,-0.005], 0.5, 0.3)

rtde_c.moveL([-0.36783,-0.68956,0.00500,2.232,2.201,-0.005], 0.5, 0.3)

rtde_c.disconnect()