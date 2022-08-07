import sounddevice as sd
from scipy.io.wavfile import write

# Recording properties
SAMPLE_RATE = 44100
SECONDS = 10

# Channels
MONO    = 1
STEREO  = 2
sd.default.samplerate = 44100
sd.default.device = 'arsh (2- High Definition Audio'
print(f'Recording for {SECONDS} seconds')

# Starts recording
recording = sd.rec(int(SECONDS * SAMPLE_RATE), samplerate = SAMPLE_RATE, channels = MONO)
sd.wait()  # Waits for recording to finish

# Writes recorded data in to the wave file
write('recording11.wav', SAMPLE_RATE, recording)
