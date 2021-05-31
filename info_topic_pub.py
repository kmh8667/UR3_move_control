#!/usr/bin/env python
import sys
import rospy
import moveit_commander
import math
import tf
import geometry_msgs.msg
from std_msgs.msg import String

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = robot.get_group_names()
cur_pose = geometry_msgs.msg.Pose()
move_group = moveit_commander.MoveGroupCommander(group_name[1])
p_x = open("p_x.txt",'w')
p_y = open("p_y.txt",'w')
p_z = open("p_z.txt",'w')
o_x = open("o_x.txt",'w')
o_y = open("o_y.txt",'w')
o_z = open("o_z.txt",'w')


def test_info():
      pub = rospy.Publisher('info_test',String,queue_size=10)
      rospy.init_node('info_test_n', anonymous = True)
      rate = rospy.Rate(10) #10hz
    
      while not rospy.is_shutdown():
            cur_pose = move_group.get_current_pose()
            pose_x = "pose x: %s\n" %cur_pose.pose.position.x
            pose_y = "pose y: %s\n" %cur_pose.pose.position.y
            pose_z = "pose z: %s\n" %cur_pose.pose.position.z
            
            orientation_list = tf.transformations.euler_from_quaternion([cur_pose.pose.orientation.x,
                                cur_pose.pose.orientation.y, 
                                cur_pose.pose.orientation.z,
                                cur_pose.pose.orientation.w])
            orientation_x = orientation_list[0]
            orientation_y = orientation_list[1]
            orientation_z = orientation_list[2]
            
            ori_x = "ori x: %s\n" %orientation_x
            ori_y = "ori y: %s\n" %orientation_y
            ori_z = "ori z: %s\n" %orientation_z
            rospy.loginfo(pose_x)
            rospy.loginfo(pose_y)
            rospy.loginfo(pose_z)
            rospy.loginfo(ori_x)
            rospy.loginfo(ori_y)
            rospy.loginfo(ori_z)
            p_x.write(pose_x)
            p_y.write(pose_y)
            p_z.write(pose_z)
            o_x.write(ori_x)
            o_y.write(ori_y)
            o_z.write(ori_z)

            pub.publish(pose_x)
            pub.publish(pose_y)
            pub.publish(pose_z)
            pub.publish(ori_x)
            pub.publish(ori_y)
            pub.publish(ori_z)
            rate.sleep()

if __name__=='__main__':
    try:
        test_info()
    except rospy.ROSInterruptException:
        pass
        p_x.close()
        p_y.close()
        p_z.close()
        o_x.close()
        o_y.close()
        o_z.close()