#very smooth recording

import rclpy
import pyaudio
from rclpy.node import Node
from std_msgs.msg import ByteMultiArray
from std_msgs.msg import MultiArrayLayout, MultiArrayDimension

class RealtimeAudio(Node):
    def __init__(self):
        super().__init__('realtime_audio')
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 22050 
        self.p = pyaudio.PyAudio()

        self.publisher = self.create_publisher(ByteMultiArray, '/audio_for_PC', 10)
        self.subscriber = self.create_subscription(ByteMultiArray, '/audio_for_Orin', 10)
        # self.subscriber
        self.timer = self.create_timer(0.01, self.pub_audio)

        # 스트림 변수 초기화
        self.input_stream = None
        self.output_stream = None

    def open_set(self):
        self.input_stream = self.p.open(format=self.FORMAT,
                      channels=self.CHANNELS,
                      rate=self.RATE,
                      input=True,
                      frames_per_buffer=self.CHUNK)
        
        self.output_stream = self.p.open(format=self.FORMAT,
                       channels=self.CHANNELS,
                       rate=self.RATE,
                       output=True)
        
        print('start recording and streaming')

    def pub_audio(self):
        if self.input_stream is None and self.output_stream is None:
            self.open_set()
            print("open port")
        else :
            print("can't port")

        # 데이터 읽기 및 전송
        data = self.CHUNK
        byte_array = ByteMultiArray()
        byte_array.layout = MultiArrayLayout(
            dim=[MultiArrayDimension(label='audio_data', size=len(data), stride=1)],
            data_offset=0
        )
        byte_array.data = list(data)

        # 퍼블리시
        self.publisher.publish(byte_array)
        self.output_stream.write(data)

        print('recording and streaming stopped')

        def audio_callback(self, msg):
            # 수신한 오디오 데이터를 출력
            data = bytes(msg.data)
            self.output_stream.write(data)
    

    def main(args=None):
        rclpy.init(args=args)
        audio_node = RealtimeAudio()
        rclpy.spin(audio_node)

        # # 스트림 및 PyAudio 종료
        # audio_node.input_stream.stop_stream()
        # audio_node.input_stream.close()
        # audio_node.output_stream.stop_stream()
        # audio_node.output_stream.close()
        # audio_node.p.terminate()
        

    if __name__ == '__main':
        main()
