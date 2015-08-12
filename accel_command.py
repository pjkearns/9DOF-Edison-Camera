from SF_9DOF import IMU
import time
import sys, os, re, socket
from settings import camaddr
from settings import camport
count = 0

# Create IMU object
imu = IMU() # To select a specific I2C port, use IMU(n). Default is 1. 

# Initialize IMU
imu.initialize()

# Enable accel, mag, gyro, and temperature
imu.enable_accel()
imu.enable_mag()
imu.enable_gyro()
imu.enable_temp()

# Set range on accel, mag, and gyro

# Specify Options: "2G", "4G", "6G", "8G", "16G"
imu.accel_range("4G")       # leave blank for default of "2G" 

# Specify Options: "2GAUSS", "4GAUSS", "8GAUSS", "12GAUSS"
imu.mag_range("2GAUSS")     # leave blank for default of "2GAUSS"

# Specify Options: "245DPS", "500DPS", "2000DPS" 
imu.gyro_range("2000DPS")    # leave blank for default of "245DPS"

def photo():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.connect((camaddr, camport))
    srv.send('{"msg_id":257,"token":0}')
    data = srv.recv(512)
    if "rval" in data:
        token = re.findall('"param": (.+) }',data)[0]
    else:
        data = srv.recv(512)
        if "rval" in data:
            token = re.findall('"param": (.+) }',data)[0]
    tosend = '{"msg_id":769,"token":%s}' %token
    srv.send(tosend)
    srv.recv(512)

def record_start():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.connect((camaddr, camport))
    srv.send('{"msg_id":257,"token":0}')
    data = srv.recv(512)
    if "rval" in data:
	    token = re.findall('"param": (.+) }',data)[0]
    else:
	    data = srv.recv(512)
	    if "rval" in data:
		    token = re.findall('"param": (.+) }',data)[0]
    tosend = '{"msg_id":513,"token":%s}' %token
    srv.send(tosend)
    srv.recv(512)

def record_stop():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.connect((camaddr, camport))
    srv.send('{"msg_id":257,"token":0}')
    data = srv.recv(512)
    if "rval" in data:
	    token = re.findall('"param": (.+) }',data)[0]
    else:
	    data = srv.recv(512)
	    if "rval" in data:
		    token = re.findall('"param": (.+) }',data)[0]
    tosend = '{"msg_id":514,"token":%s}' %token
    srv.send(tosend)
    srv.recv(512)

# Loop and read accel, mag, and gyro
while(1):
    imu.read_accel()
    imu.read_mag()
    imu.read_gyro()
    imu.readTemp()

    if imu.gx >= 800:
        print "Photo Taken"
        photo()
        time.sleep(1.0)

    if abs(imu.gz) >= 250:
	count += 1
	if count == 3:
	    print "Camera started"    
	    record_start()
	    time.sleep(1.0)
	elif count == 6:
	    print "Camera stopped"
	    record_stop()
	    time.sleep(1.0)
	    count = 0






    # Print the results
    #print "Accel: " + str(imu.ax) + ", " + str(imu.ay) + ", " + str(imu.az) 
    #Rprint "Mag: " + str(imu.mx) + ", " + str(imu.my) + ", " + str(imu.mz) 
    #print "Gyro: " + str(imu.gx) + ", " + str(imu.gy) + ", " + str(imu.gz) 
    #print "Temperature: " + str(imu.temp) 
    
    time.sleep(.03)

 
