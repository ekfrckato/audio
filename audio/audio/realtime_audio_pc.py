#very smooth recording

import rclpy
import pyaudio
from rclpy.node import Node
from std_msgs.msg import UInt8MultiArray
from std_msgs.msg import MultiArrayLayout, MultiArrayDimension
import sys, os

class RealtimeAudio(Node):
    def __init__(self):
        super().__init__('realtime_audio_pc')
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 22050 
        self.p = pyaudio.PyAudio()

        self.publisher = self.create_publisher(UInt8MultiArray, '/voicePC', 10)
        self.subscription = self.create_subscription(UInt8MultiArray, '/voice_Orin',self.sub_audio, 10)
        self.subscription
        self.timer = self.create_timer(0.01, self.pub_audio)

        # 스트림 변수 초기화
        self.input_stream = None
        self.output_stream = None
        self.input_stream = self.p.open(format=self.FORMAT,
                      channels=self.CHANNELS,
                      rate=self.RATE,
                      input=True,
                      frames_per_buffer=self.CHUNK)
        
        self.output_stream = self.p.open(format=self.FORMAT,
                       channels=self.CHANNELS,
                       rate=self.RATE,
                       output=True)
        
        os.environ["ROS_DOMAIN_ID"] = "10"
        
        print('start recording and streaming')

    def pub_audio(self):
        # 데이터 읽기 및 전송
        data = self.input_stream.read(self.CHUNK)
        print(type(data), data)
        pub_msg = UInt8MultiArray()
        pub_msg.data = list(data)
        
        # 퍼블리시
        self.publisher.publish(pub_msg)
        
    def sub_audio(self, sub_msg):
        sub_msg_ = bytes(sub_msg.data)
        self.output_stream.write(sub_msg_)

def main(args=None):
    rclpy.init(args=args)
    audio_node = RealtimeAudio()
    rclpy.spin(audio_node)    

if __name__ == '__main__':
    main()
