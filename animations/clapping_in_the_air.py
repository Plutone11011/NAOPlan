# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.28, 0.8, 1.28, 1.8, 2.28, 2.8])
keys.append([-0.0782759, -0.50166, -0.0782759, -0.50166, -0.0782759, -0.50166])

names.append("HeadYaw")
times.append([0.28, 0.8, 1.28, 1.8, 2.28, 2.8])
keys.append([-0.0859459, -0.0706059, -0.0859459, -0.0706059, -0.0859459, -0.0706059])

names.append("LAnklePitch")
times.append([0.32, 1.36, 2.88])
keys.append([-0.0910584, -0.298148, -0.298148])

names.append("LAnkleRoll")
times.append([0.32, 1.36, 2.88])
keys.append([-0.0329368, 0.0192192, 0.0192192])

names.append("LElbowRoll")
times.append([0.32, 0.84, 1.32, 1.84, 2.32, 2.84])
keys.append([0, -0.612024, 0, -0.612024, 0, -0.612024])

names.append("LElbowYaw")
times.append([0.32, 0.84, 1.32, 1.84, 2.32, 2.84])
keys.append([-0.420357, -0.374338, -0.420357, -0.374338, -0.420357, -0.374338])

names.append("LHand")
times.append([0.76, 2.76])
keys.append([0.796751, 0.796751])

names.append("LHipPitch")
times.append([0.32, 1.36, 2.88])
keys.append([0.340577, 0.25774, 0.25774])

names.append("LHipRoll")
times.append([0.32, 1.36, 2.88])
keys.append([0.090152, 0.0671419, 0.0671419])

names.append("LHipYawPitch")
times.append([0.32, 1.36, 2.88])
keys.append([-0.360449, -0.384992, -0.384992])

names.append("LKneePitch")
times.append([0.32, 1.36, 2.88])
keys.append([0.0714636, 0.405876, 0.405876])

names.append("LShoulderPitch")
times.append([0.32, 0.84, 1.32, 1.84, 2.32, 2.84])
keys.append([-1.05237, -0.823801, -1.05237, -0.823801, -1.05237, -0.823801])

names.append("LShoulderRoll")
times.append([0.32, 0.84, 1.32, 1.84, 2.32, 2.84])
keys.append([0.432547, 0.0352401, 0.432547, 0.0352401, 0.432547, 0.0352401])

names.append("LWristYaw")
times.append([0.76, 2.76])
keys.append([-1.30394, -1.30394])

names.append("RAnklePitch")
times.append([0.32, 1.36, 2.88])
keys.append([-0.0787807, -0.292008, -0.292008])

names.append("RAnkleRoll")
times.append([0.32, 1.36, 2.88])
keys.append([0.165806, 0.0680678, 0.0558505])

names.append("RElbowRoll")
times.append([0.32, 0.84, 1.32, 1.84, 2.32, 2.84])
keys.append([4.19617e-05, 0.656595, 4.19617e-05, 0.656595, 4.19617e-05, 0.656595])

names.append("RElbowYaw")
times.append([0.32, 0.84, 1.32, 1.84, 2.32, 2.84])
keys.append([0.233125, 0.170232, 0.233125, 0.170232, 0.233125, 0.170232])

names.append("RHand")
times.append([0.76, 2.76])
keys.append([0.849115, 0.849115])

names.append("RHipPitch")
times.append([0.32, 1.36, 2.88])
keys.append([0.355635, 0.26973, 0.26973])

names.append("RHipRoll")
times.append([0.32, 1.36, 2.88])
keys.append([-0.119116, -0.0853684, -0.0853684])

names.append("RKneePitch")
times.append([0.32, 1.36, 2.88])
keys.append([0.0476684, 0.388217, 0.388217])

names.append("RShoulderPitch")
times.append([0.32, 0.84, 1.32, 1.84, 2.32, 2.84])
keys.append([-1.11978, -0.926494, -1.11978, -0.926494, -1.11978, -0.926494])

names.append("RShoulderRoll")
times.append([0.32, 0.84, 1.32, 1.84, 2.32, 2.84])
keys.append([-0.454107, -0.0245859, -0.454107, -0.0245859, -0.454107, -0.0245859])

names.append("RWristYaw")
times.append([0.76, 2.76])
keys.append([1.31153, 1.31153])
