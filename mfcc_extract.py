import math
import librosa

default_sample_rate = 44100
n_mfcc = 2
window_length = int(math.pow(2, 16))
n_fft = window_length
hop_length = int(window_length / 4)
n_mels = 23

melkwargs = {
    "n_fft": n_fft,
    "win_length": window_length,
    "hop_length": hop_length,
    "n_mels": n_mels,
    "center": False,
}



def extract_mfcc(filename):
    print(filename)

    y, sr = librosa.load(filename, sr=default_sample_rate)
    print(sr)

    fft_size = int(math.pow(2, 16))
    hop_size = int(fft_size / 4)

    audio_mfcc = librosa.feature.mfcc(y=y, sr=sr, n_fft=fft_size, hop_length=hop_size, n_mfcc=2)

    return  audio_mfcc.T.tolist()
