#very smooth recording

import pyaudio

# 기본 설정
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 22050

# PyAudio 초기화
p = pyaudio.PyAudio()

# 입력 스트림 열기
input_stream = p.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      input=True,
                      frames_per_buffer=CHUNK)

# 출력 스트림 열기
output_stream = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       output=True)

print('start recording and streaming')

seconds = 3
for _ in range(0, int(RATE / CHUNK * seconds)):
    data = input_stream.read(CHUNK)
    output_stream.write(data)  # 읽은 데이터를 바로 스피커로 출력

print('recording and streaming stopped')

# 스트림 및 PyAudio 종료
input_stream.stop_stream()
input_stream.close()
output_stream.stop_stream()
output_stream.close()
p.terminate()
