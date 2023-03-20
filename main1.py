
#import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

#sampling frequency
freq = 44100
#Recording Duration
duration = 5

#Start Recoder With The Given Values of duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate = freq, channels = 2)

#Recode audio for the given number of seconds
sd.wait()

#this will convert the Numpy array to an Audio
#File with The Given Sampling Frequency
write("recording0.wav", freq, recording)

#Convert the Numpy Array To Audio File
wv.write("recording1.wav", recording, freq, sampwidth = 2)