from time import sleep
import sys
import os
import io
from colorama import init, Fore
# initialize colorama
init()

"""
    file_size = path.getsize(data_path)
    pbar = tqdm(total=file_size, unit='B', unit_scale=True)

    def callback(monitor):
        progress = monitor.bytes_read - callback.last_bytes_read
        pbar.update(progress)
        callback.last_bytes_read = monitor.bytes_read
    callback.last_bytes_read = 0
"""


from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
import requests
import json



import PIL.ImageGrab
im = PIL.ImageGrab.grab()
#im.save("sc.jpg")

file2 = io.BytesIO()
im.save(file2, "JPEG")
file2.seek(0)
file2.name = "sc.jpg"

print("\n\n")	


def my_callback(monitor):
	prcnt = int(monitor.bytes_read*100/monitor.len)
	prcnt_p = int(prcnt/2)
	sys.stdout.write("\r"+" |"+'█'*prcnt_p+" "*(int(100/2)-prcnt_p)+"| "+str(prcnt)+"%")

#file1 = open('sc.jpg', 'rb')
e = MultipartEncoder(fields={'ScreenShoot': (file2.name, file2)}) #'application/octet-stream'
m = MultipartEncoderMonitor(e, my_callback)

r = requests.post('http://localhost:5000/upload', data=m,headers={'Content-Type': m.content_type})
print("\n\n")
#fn = file2.name
file2.close()
#os.remove(file1.name)

print(r.text)

print("\n\n")
