#!/usr/bin/env python3
#Pythonでrosを扱う時に使う
import rospy
#std_msgsのFloat32MultiArrayという型のメッセージをインポート
from std_msgs.msg import Float32MultiArray
#処理時間を計測
import time
#i2cを使うためのモジュール
import busio
#GPIOを使うためのモジュール
import board
#amg8833を使うためのモジュール
import adafruit_amg88xx




#vis_thermというノードを定義
rospy.init_node('vis_therm_pub')

#Thermalというトピックmsgの型、queue_sizeが1のパブリッシャを定義
pub = rospy.Publisher('Thermal', Float32MultiArray , queue_size=1)

# I2Cバスの初期化
i2c_bus = busio.I2C(board.SCL, board.SDA)

# センサーの初期化
sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)

#配列の初期化
sensordata[8][8] = [[0]*8]*8

# センサーの初期化待ち
time.sleep(.1)

#10Hz周期でwhileを回す
rate = rospy.Rate(10)

#shutdownされるまで実行
while not rospy.is_shutdown():
		# データ取得
    sensordata = sensor.pixels
    pub.publish(sensordata)
    rate.sleep()
