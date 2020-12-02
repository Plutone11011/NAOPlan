from naoqi import ALProxy
from qi import Session
from robot.constants import JOINT_NAMES, NAO_PORT, NAO_IP
from robot.search import NaoNode, NaoState, NaoProblem, StandZero

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
			self.second_state = NaoState(self.motionProxy)
			self.textSpeakProxy.post.say("Hello")
			#problem = NaoProblem(first_state, second_state)
			#print problem.h(first_state)
			# for name in JOINT_NAMES:
			#    print second_state.get_joint_coordinate(name)
	# except RuntimeError:
	# return self.connected
		#first_state = NaoState(motion_proxy)
		# for name in JOINT_NAMES:
		#    print first_state.get_joint_coordinate(name)
