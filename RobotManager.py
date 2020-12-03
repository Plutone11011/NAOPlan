from naoqi import ALProxy
import time
from qi import Session
from robot.constants import JOINT_NAMES, NAO_PORT, NAO_IP
from robot.search import NaoNode, NaoState, NaoProblem, StandZero
# animations
from animations import backRubs_pose, excited_pose, excited2_pose, exhausted_pose, exhausted2_pose, lookHand_pose, nod_pose, stretch3_pose
from animations import pensive_pose, relaxation_pose, rest_pose, scratchBottom_pose, scratchHead_pose, scratchHand_pose,sneeze_pose
from animations import sneeze_pose, stretch1_pose, stretch2_pose, stretch3_pose, yum_pose, stretch1_pose, stretch2_pose, yum_pose
from animations import happy_pose, happy2_pose, happy3_pose, proud_pose, showMuscles1_pose, showMuscles2_pose, winner_pose, winner2_pose
from animations import crying_pose, desperate_pose, desperate2_pose, desperate3_pose, disappointed_pose, embarassed_pose, crying_pose

class RobotManager:

	def __init__(self):
		self.connected = False
		self.session = Session()

	def robotConnect(self):
		print("robot trying to connect")
		try:
			self.textSpeakProxy = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
			self.postureProxy = ALProxy("ALRobotPosture", NAO_IP, NAO_PORT)
			self.motionProxy = ALProxy("ALMotion", NAO_IP, NAO_PORT)
			self.session.connect("tcp://" + NAO_IP + ":" + str(NAO_PORT))
			self.connected = True
			print("robot connected")

		except RuntimeError:
			print ("Can't connect to Naoqi at ip \"" + NAO_IP + "\" on port " + str(NAO_PORT) + ".\n")


	def initRobot(self):
		if self.connected:
			self.postureProxy.goToPosture("StandInit", 1.0)
			self.motionProxy.setAngles(["HeadYaw", "HeadPitch"], [-0.01538, 0.512], 0.2)
			#self.second_state = NaoState(self.motionProxy)
			self.textSpeakProxy.post.say("Hello")
			self.motionProxy.setFallManagerEnabled(True)

	def planning(self):
		print(self.postureProxy.getPostureList())
		listOfMoves = ["Stand", "StandZero", "Sit", "SitRelax"]
		for move in listOfMoves:
			time.sleep(1)
			self.postureProxy.goToPosture(move, 0.7)
		self.textSpeakProxy.post.say("Tired")
		self.runMotion(exhausted_pose)
		self.runMotion(exhausted2_pose)

	def onFinish(self):
		self.textSpeakProxy.post.say("Bye!")
		self.postureProxy.goToPosture("Crouch", 0.5)

	def runMotion(self, pose, post = True):
		# launch animation
		# if post == True:
		# 	self.motionProxy.post.angleInterpolationBezier(pose.names, pose.times, pose.keys)
		# else:
		self.motionProxy.angleInterpolationBezier(pose.names, pose.times, pose.keys)
