import sys
import rospy
import moveit_commander
import math
import tf
import geometry_msgs.msg

rospy.init_node('test_ur3')
moveit_commander.roscpp_initialize(sys.argv)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

group_name = robot.get_group_names()
cur_pose = geometry_msgs.msg.Pose()
move_group = moveit_commander.MoveGroupCommander(group_name[1])


def move_joints(move_group, goal):
  move_group.go(goal, wait=True)
  move_group.stop()

def get_joint_state(move_group):
  
  joint_state = move_group.get_current_joint_values()
  print " --> current joint state as follow (rad) :"
  print joint_state
  print " --> current joint state as follows (degree) : "
  print [joint*180./math.pi for joint in joint_state] 
  
def get_goal_pose(move_group):
  cur_pose = move_group.get_current_pose()
  print "-----cur_pose: ", cur_pose

  position_list = [cur_pose.pose.position.x, cur_pose.pose.position.y, cur_pose.pose.position.z]
  orientation_list = tf.transformations.euler_from_quaternion([cur_pose.pose.orientation.x,
  cur_pose.pose.orientation.y, 
  cur_pose.pose.orientation.z,
  cur_pose.pose.orientation.w])

  
  print "======= pos(meter): ", position_list
  print "======= rot(rad): ", orientation_list,
  print ""

  
def start():
  #MoveJ P1 (start point)
  p1 = [n*math.pi/180. for n in [-194., -96.7, 118.29, 7.29, 73.61, 176.08]]
  move_joints(move_group, p1)
  print "get ready"
  print "--------moveJ P1 state:"
  #get_joint_state(move_group)
  goal_pose = get_goal_pose(move_group)

  #move start
  print  " >>>>>> press enter to start <<<<<<< "
  raw_input()

  #MoveJ P2
  p2 = [n*math.pi/180. for n in [-190.50, -56.32, 124.74, -66.84, 78.29, -66.84]]
  move_joints(move_group, p2)
  print "--------moveJ P2 state:"
  #get_joint_state(move_group)
  goal_pose = get_goal_pose(move_group)  

  rospy.sleep(0.7)

  #MoveJ P3
  p3 = [n*math.pi/180. for n in [-190.63, -42.10, 123.94, -80.28, 78.01, 270.99]]
  move_joints(move_group, p3)
  print "--------moveJ P3 state:"
  #get_joint_state(move_group)
  goal_pose = get_goal_pose(move_group)  

  rospy.sleep(0.7)

  #MoveJ sponge_disk
  sp = [n*math.pi/180. for n in [-178.87, -19.59, 111.80, -99.36, 88.15, 183.35]]
  move_joints(move_group, sp)
  print "--------moveJ sponge_disk state:"
  #get_joint_state(move_group)
  goal_pose = get_goal_pose(move_group)  

  rospy.sleep(2)

  #MoveJ P3
  p3 = [n*math.pi/180. for n in [-190.63, -42.10, 123.94, -80.28, 78.01, 270.99]]
  move_joints(move_group, p3)
  print "--------moveJ P3 state:"
  #get_joint_state(move_group)
  goal_pose = get_goal_pose(move_group)  

  rospy.sleep(0.7)

  #MoveJ P2
  p2 = [n*math.pi/180. for n in [-190.50, -56.32, 124.74, -66.84, 78.29, -66.84]]
  move_joints(move_group, p2)
  print "--------moveJ P2 state:"
  #get_joint_state(move_group)
  goal_pose = get_goal_pose(move_group)  

  rospy.sleep(0.7)

  #Drop
  drop = [n*math.pi/180. for n in [-240.56, -46.38, 106.69, -70.05, 24.05, 222.69]]
  move_joints(move_group, drop)
  print "--------moveJ drop state:"
  #get_joint_state(move_group)
  goal_pose = get_goal_pose(move_group)  

  rospy.sleep(0.7)

  #Drop2
  drop2 = [n*math.pi/180. for n in [-235.76, -40.69, 87.02, -35.37, 35.56, 204.23]]
  move_joints(move_group, drop2)
  print "--------moveJ drop2 state:"
  #get_joint_state(move_group)
  goal_pose = get_goal_pose(move_group)  

  rospy.sleep(2)

  #waypoint
  wp = [n*math.pi/180. for n in [-194.90, -91.24, 126.27, -6.12, 73.35, 175.96]]
  move_joints(move_group, wp)
  print "--------moveJ drop state:"
  get_joint_state(move_group)

  goal_pose = get_goal_pose(move_group)  
  print "<<<<<< way point >>>>>>>"
  rospy.sleep(3)
  

if __name__ == '__main__': 
  
  start()
  
