from scipy.io.wavfile import write
import sounddevice as REC

# Recording properties
SAMPLE_RATE = 44100
SECONDS = 10

# Channels
MONO    = 1
STEREO  = 2

# Command to get all devices listed: py -m sounddevice 
# Device you want to record
REC.default.device = 'arsh (2- High Definition Audio Device',' Windows DirectSound (0 in, 2 out)'
print(f'Recording for {SECONDS} seconds')

# Starts recording
recording = REC.rec(int(SECONDS * SAMPLE_RATE), samplerate = SAMPLE_RATE, channels = MONO)
REC.wait()  # Waits for recording to finish

# Writes recorded data in to the wave file
write('recording11.wav', SAMPLE_RATE, recording)
