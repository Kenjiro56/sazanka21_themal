#!/usr/bin/env python3
#Pythonでrosを扱う時に使う
import rospy
#std_msgsのFloat64という型のメッセージをインポート
from std_msgs.msg import Float64
#処理時間を計測
import time
#i2cを使うためのモジュール
import busio
#GPIOを使うためのモジュール
import board
#amg8833を使うためのモジュール
import adafruit_mlx90640

#vis_thermというノードを定義
rospy.init_node('vis_therm_pub')

#Thermalというトピック名、Float64というmsgの型、queue_sizeが1のパブリッシャを定義
pub = rospy.Publisher('Thermal', Float64 , queue_size=1)

# I2Cバスの初期化
i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

# センサーの初期化
mlx = adafruit_mlx90640.MLX90640(i2c)

mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
frame = [0] * 768
# センサーの初期化待ち
time.sleep(.1)

#10Hz周期でwhileを回す
rate = rospy.Rate(10)

#shutdownされるまで実行
while not rospy.is_shutdown():
		# データ取得
    try:
        mlx.getFrame(frame)
    except ValueError:
        # these happen, no biggie - retry
        continue
    pub.publish(frame)
    rate.sleep()
