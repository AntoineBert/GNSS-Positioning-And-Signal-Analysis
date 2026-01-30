import serial

port = 'COM7'
baud_rate = 4800
filename = "gps_data_nmea.txt"

with serial.Serial(port, baud_rate, timeout=1) as ser, open(filename, 'w') as file:
    while True:
        line = ser.readline().decode('ascii', errors='replace')
        if line.startswith('$'):
            print(line.strip())
            file.write(line.strip('\n'))
