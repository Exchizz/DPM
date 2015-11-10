#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

distance_old = 0
pub = None
def callback(data):
        global distance_old
        a = 0.1
        distance = data.data
        distance_old = a*distance + (1-a)*distance_old

        print "Distance above MESL: ", distance_old


        pub.publish(distance_old)

def listener():
    global pub
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    sensor_num = rospy.get_param('~num','num')

    rospy.Subscriber("sensor_" + str(sensor_num), Float32, callback)
    pub = rospy.Publisher('sensor_' + str(sensor_num) + 'out', Float32, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

