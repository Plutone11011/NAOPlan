import rospy
import random
from naoqi import ALProxy
import threading
from params import *

# animations
from animations import backRubs_pose, excited_pose, excited2_pose, exhausted_pose, exhausted2_pose, lookHand_pose, nod_pose, stretch3_pose 
from animations import pensive_pose, relaxation_pose, rest_pose, scratchBottom_pose, scratchHead_pose, scratchHand_pose,sneeze_pose
from animations import sneeze_pose, stretch1_pose, stretch2_pose, stretch3_pose, yum_pose, stretch1_pose, stretch2_pose, yum_pose
from animations import happy_pose, happy2_pose, happy3_pose, proud_pose, showMuscles1_pose, showMuscles2_pose, winner_pose, winner2_pose
from animations import crying_pose, desperate_pose, desperate2_pose, desperate3_pose, disappointed_pose, embarassed_pose, crying_pose


class RobotManager:
	def __init__(self):

		self.connected = False
		self.adaptorOn = ADAPTOR_ON
		self.breathOn = BREATH_ON
		self.animationStates = {
		"adaptor": [exhausted_pose, exhausted2_pose, lookHand_pose, pensive_pose, relaxation_pose, rest_pose, showMuscles1_pose,
		scratchBottom_pose, scratchHead_pose, scratchHand_pose, stretch1_pose, yum_pose, proud_pose, desperate_pose, desperate2_pose, desperate3_pose], 
		"happy": [happy2_pose, happy3_pose, excited2_pose, showMuscles2_pose, winner_pose, winner2_pose],
		"sad": [crying_pose, embarassed_pose, crying_pose]
		}

	def connect(self, ip, port):

		try:
			self.textSpeakProxy = ALProxy("ALTextToSpeech", ip, port)
			self.motionProxy  = ALProxy("ALMotion", ip, port)
			self.postureProxy = ALProxy("ALRobotPosture", ip, port)
			self.connected = True

			# launch adaptor movements
			if self.adaptorOn and self.connected == True:
				# start adaptor movements
				threading.Timer(ADAPTOR_ANIMATION_PERIOD, self.launchAnimation).start()
		except:
			pass

		return self.connected

	def initRobot(self, robotName):

		if self.connected:
			# Wake up robot
			self.motionProxy.wakeUp()

			# Send robot to Stand Init
			self.postureProxy.goToPosture("Stand", 0.5)

			if self.breathOn and self.connected:
				# enable breath
				self.enableBreath(True)

			# introduce yourself
			self.say("Hello " + robotName + ",my name is " + ROBOT_NAME )

	def openHand(self):

		if self.connected:
			self.motionProxy.openHand("RHand")

	def drawTrace(self, listActuator, referenceFrame, path, axis, time):

		# post path to draw
		self.motionProxy.post.positionInterpolations(listActuator, referenceFrame, path, axis, time)
		# go back to position
		self.postureProxy.post.goToPosture("Stand", 0.5)

	def isMoving(self):

		for task in self.motionProxy.getTaskList():
			if task[0] == 'angleInterpolationBezier':
				return True

		return False

	def launchAnimation(self, animationType="adaptor"):

		# choose another animation
		animation = None
		if animationType == "adaptor":
			animation = random.choice(self.animationStates["adaptor"])
		elif animationType == "happy":
			animation = random.choice(self.animationStates["happy"])
		elif animationType == "sad":
			animation = random.choice(self.animationStates["sad"])

		if not self.isMoving() and self.adaptorOn:
			self.runMotion(animation)

		# relaunch threading
		if self.connected == True:
			threading.Timer(ADAPTOR_ANIMATION_PERIOD, self.launchAnimation).start()

	def runMotion(self, pose, post = True):

		# launch animation
		if post == True:
			self.motionProxy.post.angleInterpolationBezier(pose.names, pose.times, pose.keys)
		else:
			self.motionProxy.angleInterpolationBezier(pose.names, pose.times, pose.keys)

	def lookAtTablet(self):

		self.motionProxy.setAngles(["HeadYaw", "HeadPitch"], [-0.01538, 0.512], 0.2)

	def freezeAliveMode(self, freeze = True):

		if freeze == False:
			# enable breath
			self.enableBreath(True)
			self.adaptorOn = True

		else:
			# disable adaptor movements	
			self.adaptorOn = False

			# disable breath
			self.enableBreath(False)

			# wait that no adaptor movements are in to start the game
			while(self.isMoving()):
				rospy.sleep(0.1)

	def enableBreath(self, enable = True):

		if enable == True:
			# start breathing
			print("robot Manager -> start breathing mode")
			self.motionProxy.setBreathConfig([['Bpm', 10.0], ['Amplitude', 1.0]])
			if self.motionProxy.getBreathEnabled("Body") == False:
				self.motionProxy.setBreathEnabled("Body", True)
		else:
			# stop breathing
			print("robot Manager -> stop breathing mode")
			self.motionProxy.setBreathEnabled("Body", False)

	def say(self, sentence, post = True):

		if post:
			self.textSpeakProxy.post.say(sentence)
		else:
			self.textSpeakProxy.say(sentence)

	def killTasks(self):
		# kill all task
		self.motionProxy.killAll()
		# and go back to position
		self.postureProxy.post.goToPosture("Stand", 0.5)

	### degub part ###
	def testMovement(self, animation):
		self.runMotion(animation)


