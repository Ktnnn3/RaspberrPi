# Write your code here :-)
#!/usr/bin/python

# Write your code here :-)
#!/usr/bin/python
class AdventureDone(Exception): pass
import spidev
import time
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import psutil
import time
import pandas as pd
import pandas_datareader as pdr
import math
from scipy.integrate import simps
import RPi.GPIO as GPIO
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000
# spi.max_speed_hz=50
plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

relay1 = 17
relay2 = 27
relay3 = 24

GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7


def ReadChannel(channel):
    adc = spi.xfer2([4 | 2 | (channel >> 2), (channel & 3) << 6, 0])
    data = ((adc[1] & 15) << 8) + adc[2]
    return data


def ConvertVolts(data, places):
    volts = (data * 5.0) / float(4096)
    volts = round(volts, places)
    return volts

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    if type(n) == float:
        return math.floor(n * multiplier) / multiplier
    
def round_four(num):
    xnum = num*10.0
    xnum = int(xnum)
    if xnum %10 > 4:
        return (xnum+1)/10.0
    else:
        return xnum/10.0



def calSensor(a,b,Max):
    print (a[len(a)-1])
    if a[len(a)-1] > (maxSlope[Max]) and a[len(a)-1] > cutoff[Max]:
        check[Max] = -1
        print('in condition')
        b.append(a[len(a)-1])
        maxSlope[Max] =  a[len(a)-1]
    elif (a[len(a)-1]+0.05) < (maxSlope[Max]) :
        print('maxslope',maxSlope[Max])
        print('+0.05 =',a[len(a)-1]+0.05)
        print('else')
        checkNegativeSlope()


# def calSensor(a,b,Max):
#     if np.invert(math.isnan(a[len(a)-2])) or np.invert(math.isnan(a[len(a)-2])):
#         if len(a) >= 0 :
#             a01 = a[len(a)-2]
#             a02 = a[len(a)-1]
#             a1 = math.floor(a01*100)/100
#             a2 = math.floor(a02*100)/100
#             
#             slope = (float(a2) - float(a1))/5.0
# #             slope = round_nine(slope)
#             print('a1 = ',a1)
#             print('a2 = ',a2)
#             print("slope {} : {}".format(Max,slope))
#             if slope > maxSlope[Max]:
#                 maxSlope[Max] = slope
#                 if slope > 0.00:
#                     b.append(slope)
#             elif slope < 0.00:
#                 check[Max] = slope
#                 print(check)
# #                 raise AdventureDone
#                 checkNegativeSlope()

def checkNegativeSlope():
    print('sumcheck = ',sum(check))
    if sum(lastcheck) != 7:
        for i in range(len(check)):
            if sum(check) <= -3:
                if check[i] == 0:
                    if len(y[i]) == 0:
                        y[i].append(win[i][2])
                        lastcheck[i] = 1
                    else:
                        y[i][0] = win[i][2]
                else:
                    if win[i][len(win[i])-1] < maxSlope[i]:
                        lastcheck[i] = 1
    else:  
        raise AdventureDone
    
def area(a):
    if len(a)!= 1:
        return simps(a)/10.0
    else:
        return a[0]

# def flowfunc(x):
#     return (1000*(x-1.04))/4.0

def prediction(a):
    g0 = a[0]*(1.29086995124816)
    g1 = a[1]*(-0.475657880306244)
    g2 = a[2]*(-0.100802682340145)
    g3 = a[3]*(-0.173830837011337)
    g4 = a[4]*(0.33036082983017)
    g5 = a[5]*(0.58828580379486)
    g6 = a[6]*(0.303013116121292)
    ans = g0+g1+g2+g3+g4+g5+g6
    return ans
        

# Define sensor channels
gas_channel = [0,1,2,3,4,5,6]
graphsensor0 = []
graphsensor1 = []
graphsensor2 = []
graphsensor3 = []
graphsensor4 = []
graphsensor5 = []
graphsensor6 = []
flow = []

win =[[]for i in range(7)]



y =[[]for i in range(7)]
initValue=0
maxSlope=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
check=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
cutoff=[2.7,1.4,4.50,2.40,2.30,3.30,0.31]
lastcheck=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]

timeout = 1
timeout_start = time.time()
x=1
cutvar=0

# Define delay between readings
# while time.time() < timeout_start + timeout and x < timeout*100:

try:
    while True:
    
#     while time.time() < timeout_start + timeout and x <= timeout*100:
    
#     test = 0
#     if test == 5:
#         break
#     test -= 1
    # Read the temperature sensor data
    
#         GPIO.output(relay1, GPIO.HIGH) # Turn LED on
#         time.sleep(1)                   # Delay for 1 second
#         GPIO.output(relay1, GPIO.LOW)  # Turn LED off
#         time.sleep(1)                   # Delay for 1 second
#         GPIO.output(relay2, GPIO.HIGH) # Turn LED on
#         time.sleep(1)                   # Delay for 1 second
#         GPIO.output(relay2, GPIO.LOW)  # Turn LED off
#         time.sleep(1)
#         GPIO.output(relay3, GPIO.HIGH) # Turn LED on
#         time.sleep(1)                   # Delay for 1 second
#         GPIO.output(relay3, GPIO.LOW)  # Turn LED off
#         time.sleep(1) 
        
        
        gas0_level = ReadChannel(gas_channel[0])
        gas0_volts = ConvertVolts(gas0_level, 2)

        gas1_level = ReadChannel(gas_channel[1])
        gas1_volts = ConvertVolts(gas1_level, 2)

        gas2_level = ReadChannel(gas_channel[2])
        gas2_volts = ConvertVolts(gas2_level, 2)

        gas3_level = ReadChannel(gas_channel[3])
        gas3_volts = ConvertVolts(gas3_level, 2)

        gas4_level = ReadChannel(gas_channel[4])
        gas4_volts = ConvertVolts(gas4_level, 2)

        gas5_level = ReadChannel(gas_channel[5])
        gas5_volts = ConvertVolts(gas5_level, 2)

        gas6_level = ReadChannel(gas_channel[6])
        gas6_volts = ConvertVolts(gas6_level, 2)
        
#         flow_level = ReadChannel(7)
#         flow_volts = ConvertVolts(flow_level, 2)
#         flowxx = flowfunc(flow_volts)
        

    # Print out results
#         print("--------------------------------------------")
#         print("delta V gas0 : {}V".format(gas1_volts))
#         print("Time : {} V".format(time.time()))

        graphsensor0.append(gas0_volts)
        graphsensor1.append(gas1_volts)
        graphsensor2.append(gas2_volts)
        graphsensor3.append(gas3_volts)
        graphsensor4.append(gas4_volts)
        graphsensor5.append(gas5_volts)
        graphsensor6.append(gas6_volts)
#         flow.append(flowxx)
        
    

#     without_nans = moving_averages_list[windowsdow_size - 1:]
    
   
    
        if(x%100 == 0):
            graphsensor0_s = pd.Series(graphsensor0)
            graphsensor1_s = pd.Series(graphsensor1)
            graphsensor2_s = pd.Series(graphsensor2)
            graphsensor3_s = pd.Series(graphsensor3)
            graphsensor4_s = pd.Series(graphsensor4)
            graphsensor5_s = pd.Series(graphsensor5)
            graphsensor6_s = pd.Series(graphsensor6)
            
            windows0 = graphsensor0_s.rolling(100).mean().tolist()
            windows1 = graphsensor1_s.rolling(100).mean().tolist()
            windows2 = graphsensor2_s.rolling(100).mean().tolist()
            windows3 = graphsensor3_s.rolling(100).mean().tolist()
            windows4 = graphsensor4_s.rolling(100).mean().tolist()
            windows5 = graphsensor5_s.rolling(100).mean().tolist()
            windows6 = graphsensor6_s.rolling(100).mean().tolist()
            
            ax.plot(windows0, color='b')
            ax.plot(windows1, color='r')
            ax.plot(windows2, color='g')
            ax.plot(windows3, color='c')
            ax.plot(windows4, color='m')
            ax.plot(windows5,color='y')
            ax.plot(windows6,color='k')
            fig.canvas.draw()
            
            win[0].append(windows0[x-1])
            win[1].append(windows1[x-1])
            win[2].append(windows2[x-1])
            win[3].append(windows3[x-1])
            win[4].append(windows4[x-1])
            win[5].append(windows5[x-1])
            win[6].append(windows6[x-1])
            
            if(cutvar == 0):
#                 cutoff[0] = (win[0][0])+0.1
#                 cutoff[1] = (win[1][0])+0.1
#                 cutoff[2] = (win[2][0])+0.1
#                 cutoff[3] = (win[3][0])+0.1
#                 cutoff[4] = (win[4][0])+0.1
#                 cutoff[5] = (win[5][0])+0.1
#                 cutoff[6] = (win[6][0])+0.1
                for i in range(len(cutoff)):
                    cutoff[i] = win[i][0]
                    cutoff[i] = cutoff[i]+0.1
                cutvar = 1
                for i in range (len(cutoff)):
                    print ('cutoff{} : {}'.format(i,cutoff[i]))
            
            print("delta V win0 : {}V".format(win[0]))
            print("delta V win1 : {}V".format(win[1]))
            print("delta V win2 : {}V".format(win[2]))
            print("delta V win3 : {}V".format(win[3]))
            print("delta V win4 : {}V".format(win[4]))
            print("delta V win5 : {}V".format(win[5]))
            print("delta V win6 : {}V".format(win[6]))
            print('------------------------------------')
#             print('flow', flow)
#             print('flowV', flow_volts)
            for i in range(7):
                calSensor(win[i],y[i],i)

        #time.sleep(0.005)
        x += 1
except AdventureDone:
        pass
# plt.close()
cutvar = 0
print('len graphsensor0 = ',len(graphsensor0))
print('graphsensor0 = ',graphsensor0)
for i in range(len(y)):
    print("y{} : {}".format(i,y[i]))
print('check =',check)
finalarea= [0,1,2,3,4,5,6]
for i in range(len(y)):
    print(area(y[i]))
finalarea[0] = area(y[0])
finalarea[1] = area(y[1])
finalarea[2] = area(y[2])
finalarea[3] = area(y[3])
finalarea[4] = area(y[4])
finalarea[5] = area(y[5])
finalarea[6] = area(y[6])
print(finalarea)
print(prediction(finalarea))




#print(graphsensor0)
#df['graphsensor0'].rolling(windowsdow =20).mean().plot()


