import sys
import time
import datetime
import logging
import rtde as rtde
import rtde_config as rtde_config
import socket
import numpy as np
from itertools import combinations
def io_signals():
    datarate=10 # Time interval for data logging in Hz


    #######################################################

    ROBOT_HOST = '169.254.37.99'#'192.168.1.103'
    ROBOT_PORT = 30004
    config_filename = 'control_loop_configuration.xml'

    #Initialize RTDE Connection
    logging.getLogger().setLevel(logging.INFO)
    conf = rtde_config.ConfigFile(config_filename)
    state_names, state_types = conf.get_recipe('state')
    watchdog_names, watchdog_types = conf.get_recipe('watchdog')
    con = rtde.RTDE(ROBOT_HOST, ROBOT_PORT)
    con.connect()
    connected = con.is_connected()
    if connected == True:
        print('Connected')

    # get controller version
    con.get_controller_version()

    # setup recipes
    con.send_output_setup(state_names, state_types)
    watchdog = con.send_input_setup(watchdog_names, watchdog_types)

    sensor_data = []
    # The function "rtde_set_watchdog" in the "rtde_control_loop.urp" creates a 1 Hz watchdog
    watchdog.input_int_register_0 = 0
    ##########################################################################
    #FUNCTIONS
    def read_data(sensor_data):
        num=state.actual_digital_input_bits#return 2th power and add them in case of multiple
        k=[]
        if (num==0):
            sensor_data.append('None')
        else:
            for i in range(1,11):
                comb= combinations([0,1,2,3,4,5,6,7,16,17], i)
                for j in list(comb):
                    l=len(j)
                    num1=0
                    for x in range(l):
                        num1=num1+pow(2,j[x])
                    if num1==num:
                        j=list(j)
                        sensor_data.append(j)
                        #print(j)
                        break
        #sensor_data.append(state.tool_digital_output0_mode)#returns 2th 16
        #sensor_data.append(state.tool_digital_output1_mode)#returns 2th 17
        return sensor_data

    ##########################################################################
    #start data synchronization
    if not con.send_start():
        sys.exit()

    ##########################################################################
    t0=time.process_time() #time stamp
    t0_temp=time.process_time() #temporary time stamp

    print('Reading from robot')

    try:
        while True:
            # receive the current state
            # the data that will be received is configured in the
            # control_loop_configuration.xml
            state = con.receive()
            t1=time.process_time()
            if t1-t0_temp>=1./datarate:
                sensor_data = read_data(sensor_data) #put data from state in a dictionary
                #print(sensor_data)
                # or do something else with the dictionary...

                t0_temp=time.process_time()
                break
            con.send(watchdog) # kick watchdog
    except KeyboardInterrupt:

        con.send_pause() #RTDE
        con.disconnect() #RTDE
    return sensor_data