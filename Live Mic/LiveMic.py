
import pyaudio
import numpy as np
import pylab
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
from scipy.io import wavfile
import time
import sys
import os
import wave, struct, math, random
import threading 


global keep_going
keep_going = True


FORMAT = pyaudio.paInt16 # We use 16bit format per sample
CHANNELS = 1 # 1:mono , 2:stereo
RATE = 44100
CHUNK = 4096 # 4096 1024 bytes of data red from a buffer

WAVE_OUTPUT_FILENAME = "file.wav"
audio_frame_counts = 0
audio_frames = []
global DATA_
DATA_ = None

audio_in = pyaudio.PyAudio()
audio_out = pyaudio.PyAudio()

# start Recording
input_audio_stream = audio_in.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
output_audio_stream = audio_out.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

Wave_write = wave.open(WAVE_OUTPUT_FILENAME,'wb')
Wave_write.setnchannels(CHANNELS) 
Wave_write.setsampwidth(audio_in.get_sample_size(FORMAT)) 
Wave_write.setframerate(RATE)



def plotter(in_data):

	fig = plt.figure(figsize=(8,3))
	#fig.set_size_inches(8, 3, , forward=True)
	ax = plt.axes(xlim=(0, CHUNK-1), ylim=(-9999, 9999))
	line, = ax.plot([], [], lw=1)
	x = np.linspace(0, CHUNK-1, CHUNK)

	def init():
	    line.set_data([], [])
	    return line,
	def animate(i):
		if keep_going:
		    #y = np.frombuffer(input_audio_stream.read(CHUNK), dtype=np.int16)
		    if(DATA_ != None):
		    	y = np.frombuffer(DATA_, dtype=np.int16) # random.randint(-9999, 9999)
		    else:
		    	y = 0
		    line.set_data(x, y)
		    return line,
		else:
			plt.close()
			return None

	anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
	plt.style.use('bmh')
	plt.tight_layout(pad=0)
	#plt.subplots_adjust(left=0.1, right=0.1, top=0.1, bottom=0.1)
	plt.show() # (block=False)

	"""
	anim.save('continuousSineWave.mp4', writer = 'ffmpeg', fps = 30) # avconv
	anim.save('sine_wave.gif', writer='imagemagick')
	"""


thread_anime = threading.Thread(target=plotter, args=(DATA_,))
thread_anime.start()

input_audio_stream.start_stream()
output_audio_stream.start_stream()

while keep_going:
    try:
    	DATA_ = input_audio_stream.read(CHUNK)
    	audio_frame_counts += 1
    	#audio_frames.append(DATA_)
    	Wave_write.writeframesraw(DATA_)
    	output_audio_stream.write(DATA_)
    	print(np.frombuffer(DATA_, dtype=np.int16))
    except KeyboardInterrupt:
        keep_going=False
    except:
        pass

input_audio_stream.stop_stream()
input_audio_stream.close()
audio_in.terminate()

output_audio_stream.stop_stream()
output_audio_stream.close()
audio_out.terminate()

thread_anime.join()

print("recorded audio frames : ",audio_frame_counts)
#Wave_write.setnframes(audio_frame_counts)
#Wave_write.writeframes(b''.join(audio_frames))
#Wave_write.writeframes('')
Wave_write.close()






os.system("pause")