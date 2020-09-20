# Usage example: $ python captions-download.py Txvud7wPbv4

from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/youtube.force-ssl'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
YOUTUBE = discovery.build('youtube', 'v3', http=creds.authorize(Http()))

def process(vid):
    caption_info = YOUTUBE.captions().list(
            part='id', videoId=vid).execute().get('items', [])
    caption_str = YOUTUBE.captions().download(
            id=caption_info[0]['id'], tfmt='srt').execute()
    caption_data = caption_str.split('\n\n')
    for line in caption_data:
        if line.count('\n') > 1:
            i, cap_time, caption = line.split('\n', 2)
            print('%02d) [%s] %s' % (
                    int(i), cap_time, ' '.join(caption.split())))

if __name__ == '__main__':
    #import sys
    #if len(sys.argv) == 2:
    #    VID = sys.argv[1]
    process("Txvud7wPbv4")