"""PyAudio Example: Play a wave file."""

import wave
import sys
import os

import pyaudio

CHUNK = 1024

# 파일 경로 설정
file_path = "/home/cae/ros2_ws/output.wav"
# 경로 확장
expanded_path = os.path.expanduser(file_path)

if len(sys.argv) < 2:
    print(f'Plays a wave file. Usage: {sys.argv[0]} filename.wav')
    sys.exit(-1)

with wave.open(expanded_path, 'rb') as wf:
    # Instantiate PyAudio and initialize PortAudio system resources (1)
    p = pyaudio.PyAudio()

    # Open stream (2)
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=22050, output=True,
                    output_device_index=6)
    

    # Play samples from the wave file (3)
    while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
        stream.write(data)

    # Close stream (4)
    stream.close()

    # Release PortAudio system resources (5)
    p.terminate()