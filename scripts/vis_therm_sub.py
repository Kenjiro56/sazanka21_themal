#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray
#plotするためのモジュール
import matplotlib.pyplot as plt

def callback(message):
    print(message.data)
 # bicubicのデータ
    fig = plt.imshow(data, cmap="inferno", interpolation="bicubic")
    plt.colorbar()

if __name__ == "__main__":
    rospy.init_node('vis_therm_sub')
    sub = rospy.Subscriber('Thermal', Float32MultiArray , callback)
    rospy.spin()
