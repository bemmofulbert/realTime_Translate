import pyaudio
import numpy as np
import os

os.system("pactl set-default-sink VirtualMic")

# Audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Mono
RATE = 44100
CHUNK = 1024

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open output stream (simulating the virtual microphone)
stream_out = p.open(format=FORMAT, channels=CHANNELS,
                     rate=RATE, output=True)



# Open input stream (simulating the microphone)
stream_in = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)



print("Virtual microphone is running. Press Ctrl+C to stop.")



try:
    while True:
        # Read data from the input stream
        data = stream_in.read(CHUNK)
        # Optionally process the data here (e.g., apply effects)
        # Write data to the output stream
        stream_out.write(data)
        pass
except KeyboardInterrupt:
    print("Stopping virtual microphone.")

# Close streams
stream_in.stop_stream()
stream_in.close()
stream_out.stop_stream()
stream_out.close()

p.terminate()