'''
Test loading of sound file
'''
import os
import sys
from bin.soundSample import soundSample

'''
filename = '../../samples/New_Recording_5.m4a'
wav_name = '../../samples/New_Recording_5.wav'

sound = AudioSegment.from_file(filename, format='m4a')
file_handle = sound.export(wav_name, format='wav')
print(file_handle)
'''

s = soundSample('/Users/carleen/Documents/misc_code/encore/samples/', 'New_Recording_4.wav')
s.plotAllFrequencies()

