#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
#plotするためのモジュール
import matplotlib.pyplot as plt

def callback(message):
    print(message.data)
 # bicubicのデータ
    frame = message.data
    sensordata = frame.reshape(24,32)
    fig = plt.imshow(data, cmap="inferno", interpolation="bicubic")
    plt.colorbar()

if __name__ == "__main__":
    rospy.init_node('vis_therm_sub')
    sub = rospy.Subscriber('Thermal', Float64 , callback)
    rospy.spin()
