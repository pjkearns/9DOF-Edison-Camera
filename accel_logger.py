from SF_9DOF import IMU
import time

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

log_file = open("data_9DOF.csv", "w")
log_file.write("Ax,Ay,Az,,Mx,My,Mz,,Gx,Gy,Gz,,Temp\n") 

# Loop and read accel, mag, and gyro
while(1):
    imu.read_accel()
    imu.read_mag()
    imu.read_gyro()
    imu.readTemp()

    # Print the results
    #print "Accel: " + str(imu.ax) + ", " + str(imu.ay) + ", " + str(imu.az) 
    #print "Mag: " + str(imu.mx) + ", " + str(imu.my) + ", " + str(imu.mz) 
    #print "Gyro: " + str(imu.gx) + ", " + str(imu.gy) + ", " + str(imu.gz) 
    #print "Temperature: " + str(imu.temp) 

    # Log the results
    log_file.write(str(imu.ax) + "," + str(imu.ay) + "," + str(imu.az) + "," + "" + ",")
    log_file.write(str(imu.mx) + "," + str(imu.my) + "," + str(imu.mz) + "," + "" + ",")
    log_file.write(str(imu.gx) + "," + str(imu.gy) + "," + str(imu.gz) + "," + "" + ",")
    log_file.write(str(imu.temp) + "\n")


    # Sleep for 1/20th of a second
    time.sleep(0.05)
