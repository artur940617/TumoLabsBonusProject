import datetime
import time




p = 0
st = input('Insert time to count down (h:m:s) ')
date_time_obj = datetime.datetime.strptime(st, '%H:%M:%S')
m = datetime.datetime.strptime('0:0:0', '%H:%M:%S')

while True:

        s = datetime.datetime.strptime('0:0:{}'.format(p), '%H:%M:%S')
        if date_time_obj >= s:
                p += 1
                x = date_time_obj - s
                z = time.strftime("%H:%M:%S")
                print(x)
                time.sleep(1)
        else:
                print('Time is over !')
                break







