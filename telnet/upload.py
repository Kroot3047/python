# load requests-module, a streamlined http-client lib
import requests
 
# load posters encode-function
from poster.encode import multipart_encode
 
 
 
# an adapter which makes the multipart-generator issued by poster accessable to requests
# based upon code from http://stackoverflow.com/a/13911048/1659732
class IterableToFileAdapter(object):
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.length = iterable.total
 
    def read(self, size=-1):
        return next(self.iterator, b'')
 
    def __len__(self):
        return self.length
 
# define a helper function simulating the interface of posters multipart_encode()-function
# but wrapping its generator with the file-like adapter
def multipart_encode_for_requests(params, boundary=None, cb=None):
    datagen, headers = multipart_encode(params, boundary, cb)
    return IterableToFileAdapter(datagen), headers
 
 
 
# this is your progress callback
def progress(param, current, total):
    if not param:
        return
 
    # check out http://tcd.netinf.eu/doc/classnilib_1_1encode_1_1MultipartParam.html
    # for a complete list of the properties param provides to you
    print ("{0} ({1}) - {2:d}/{3:d} - {4:.2f}%".format(param.name, param.filename, current, total, float(current)/float(total)*100))
 
# generate headers and gata-generator an a requests-compatible format
# and provide our progress-callback
datagen, headers = multipart_encode_for_requests(
 {'file1': open('1.png', 'rb'),}, 
 cb=progress
 )
 
# use the requests-lib to issue a post-request with out data attached
r = requests.post(
    'http://localhost:5000/upload',
    #auth=('user', 'password'),
    data=datagen,
    headers=headers
)
 
# show response-code and -body
print (r, r.text)