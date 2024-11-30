'''
Read/load signal and perform filtering
'''

import scipy.io.wavfile as wavfile
from scipy import signal
from pydub import AudioSegment
from scipy.fftpack import fft
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

class soundSample:

    def __init__(self, filepath, filename):
        # Instance attributes
        self.filepath = filepath
        self.filename = filename # Needs to be in .wav format
        self.path_to_wav = os.path.join(self.filepath, self.filename)

        self.samplerate, self.data = self.getWavData()
        self.frequency, self.time, self.spec = self.getSpectrogram()

    def getWavData(self):

        samplerate, data = wavfile.read(self.path_to_wav)
        sample_length = data.shape[0] / samplerate
        time_arr = np.linspace(0., sample_length, data.shape[0])
        return samplerate, data

    def plotAllFrequencies(self):
        data_length = self.data.shape[0] / self.samplerate
        time = np.linspace(0., data_length, self.data.shape[0])
        normsig = np.array([(ele/2**8.)*2-1 for ele in self.data])
        fft_sig = fft(normsig)
        length_fft = int(len(fft_sig) / 2)
        cwd = os.getcwd()
        figure_name = 'freq_plot.png'
        figures_path = os.path.join(cwd, '../../figures')
        figure_full_path = os.path.join(figures_path, figure_name)
        plt.plot(abs(fft_sig[0:(length_fft-1)]), 'r')
        plt.xlim([0, 25e3])
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Intensity')
        plt.savefig(figure_full_path)



    def getSpectrogram(self):
        frequency, time, spec = signal.spectrogram(self.data, self.samplerate)
        return frequency, time, spec


    def convertToWav(self, m4a_name, wav_name):
        sound = AudioSegment.from_file(m4a_name, format='m4a')
        file_handle = sound.export(wav_name, format='wav')
        print('Success')
