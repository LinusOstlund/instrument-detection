import librosa

def get_audio(f):
    y, _ = librosa.load(f)
    return y

def process_frame(f):
    # changed your logic here as I couldn't repro it
    return f, get_audio
