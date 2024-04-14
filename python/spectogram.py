# -*- coding: utf-8 -*-
"""
Plot a spectrogram
"""

__author__ = "Brendan Harmon"
__copyright__ = 'Copyright 2022, Algorithmic Landscapes'
__email__ =  "brendan.harmon@gmail.com"
__license__ = "GPLv3"
__version__ = "0.0.1"

# import libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import seaborn as sns
sns.set_theme()

# conda install -c conda-forge librosa
# conda install -c conda-forge pysoundfile

audio = os.path.join(os.getcwd(), 'audio.mp3')

Fs = 11025
x, Fs = librosa.load(os.path.join('..', 'data', 'B', audio), sr=Fs)
t = np.arange(x.shape[0]) / Fs


## waveform

# plt.figure(figsize=(6, 1.8))
# plt.plot(t, x, color='gray')
# librosa.display.waveshow(x, sr=Fs, color='gray')

# spectogram

N, H = 2048, 1024
X = librosa.stft(x, n_fft=N, hop_length=H, win_length=N, window='hanning')
Y = np.abs(X)
print('Shape of spectrogram:', Y.shape)
plt.figure(figsize=(8, 3))
librosa.display.specshow(
    librosa.amplitude_to_db(Y, ref=np.max),
    y_axis='linear',
    x_axis='time',
    sr=Fs,
    hop_length=H,
    cmap='viridis'
    )
plt.colorbar(format='%+2.0f dB')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency (Hz)')
plt.tight_layout()





## references
# https://www.audiolabs-erlangen.de/resources/MIR/FMP/B/B_PythonVisualization.html