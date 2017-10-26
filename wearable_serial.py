import serial
import time
from json import *
# windows 7

class myserial():
    pass

def serial_read_data(if_return_data = True):
    ser = serial.Serial('COM21', 115200, timeout=None)
    data_file = open("serial.text", "w")
    dict_data = {}

    count = 0

    return_data = ""
     
    while 1:
        try:
            data = ser.readline()
            #data = ser.read(256)
            

                    
            #time.sleep(0.01)
        except ser.SerialTimeoutException:
            print('Data could not be read')


        if(len(data) > 0):
            count = count + 1
            print "Read-Index"+":"+str(count) + "\t" +  "Read-Length"+":"+str(len(data)) +  "\t" + "Total-Length"+":"+str(len(return_data)+ len(data))
            #dict_data.append(data)
            return_data = return_data + data
            #print data

        if count == 128:
        #if len(return_data) >= (128*256):
            if if_return_data == False:
                count = 0
                dict_data['data'] = return_data
                dump(dict_data, data_file)
                return_data = ""
            else:
                ser.close()
                return return_data



if __name__ == "__main__":

    serial_read_data(False)
