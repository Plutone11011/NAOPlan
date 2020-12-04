# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.16, 0.72, 1.4, 1.96, 2.68, 3.2, 3.76])
keys.append([-0.214801, 0.217786, -0.312978, 0.205514, -0.309909, 0.185572, -0.185656])

names.append("HeadYaw")
times.append([0.16, 0.72, 1.4, 1.96, 2.68, 3.2, 3.76])
keys.append([-0.0859459, -0.0798099, -0.067538, -0.0966839, -0.055266, -0.030722, -0.021518])

names.append("LAnklePitch")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([0.138018, 0.0475121, 0.041376, 0.12728])

names.append("LAnkleRoll")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([-0.0966, -0.148756, -0.15029, -0.13495])

names.append("LElbowRoll")
times.append([0.08, 0.64, 1.36, 1.92, 2.6, 3.12, 3.68])
keys.append([-0.731675, -0.521518, -0.519984, -0.631966, -0.547595, -0.555266, -0.993989])

names.append("LElbowYaw")
times.append([0.08, 0.64, 1.36, 1.92, 2.6, 3.12, 3.68])
keys.append([-1.07691, -1.54171, -1.71505, -1.79329, -1.81937, -1.66443, -1.76875])

names.append("LHand")
times.append([0.64, 1.36, 2.6, 3.68])
keys.append([0.230571, 0.230935, 0.230935, 0.224389])

names.append("LHipPitch")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([0.0261199, 0.205598, 0.204064, 0.0982179])

names.append("LHipRoll")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([0.073674, 0.154976, 0.153442, 0.124296])

names.append("LHipYawPitch")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([-0.214717, -0.223922, -0.233125, -0.256136])

names.append("LKneePitch")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([-0.0923279, -0.0874799, -0.090548, -0.0923279])

names.append("LShoulderPitch")
times.append([0.08, 0.64, 1.36, 1.92, 2.6, 3.12, 3.68])
keys.append([1.54776, 1.6981, 1.69043, 1.57998, 1.67509, 1.60759, 1.84382])

names.append("LShoulderRoll")
times.append([0.08, 0.64, 1.36, 1.92, 2.6, 3.12, 3.68])
keys.append([0.116542, 0.171766, 0.174835, 0.11961, 0.122678, 0.11194, 0.128814])

names.append("LWristYaw")
times.append([0.64, 1.36, 2.6, 3.68])
keys.append([0.095066, 0.0966, 0.095066, 0.0889301])

names.append("RAnklePitch")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([0.145772, 0.0568, 0.055266, 0.14117])

names.append("RAnkleRoll")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([0.06447, 0.073674, 0.0782759, 0.0874799])

names.append("RElbowRoll")
times.append([0, 0.56, 1.28, 1.8, 2.52, 3.04, 3.6])
keys.append([1.55245, 0.994073, 1.51103, 0.879025, 1.56207, 1.04009, 1.56207])

names.append("RElbowYaw")
times.append([0, 0.56, 1.28, 1.8, 2.52, 3.04, 3.6])
keys.append([1.4005, 0.179436, 0.547595, 0.187106, 0.5568, 0.323633, 0.546063])

names.append("RHand")
times.append([0.56, 1.28, 2.52, 3.6])
keys.append([0.745455, 0.514873, 0.514873, 0.781818])

names.append("RHipPitch")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([0.00456004, 0.213183, 0.213183, 0.0797261])

names.append("RHipRoll")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([-0.05058, -0.0643861, -0.0643861, -0.076658])

names.append("RKneePitch")
times.append([0.6, 1.32, 2.56, 3.64])
keys.append([-0.0923279, -0.0923279, -0.0923279, -0.0923279])

names.append("RShoulderPitch")
times.append([0, 0.56, 1.28, 1.8, 2.52, 3.04, 3.6])
keys.append([0.744032, -0.808375, -1.13052, -0.777696, -0.780764, -0.84826, -0.858999])

names.append("RShoulderRoll")
times.append([0, 0.56, 1.28, 1.8, 2.52, 3.04, 3.6])
keys.append([-0.0614019, -0.602903, -1.28553, -0.546147, -1.30548, -0.527739, -1.40365])

names.append("RWristYaw")
times.append([0.56, 1.28, 2.52, 3.6])
keys.append([-0.122173, -0.119694, -0.119694, -0.130432])
