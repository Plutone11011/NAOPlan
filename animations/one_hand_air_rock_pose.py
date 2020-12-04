# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0, 0.52, 1, 1.52, 2, 2.52, 3, 3.52, 4, 4.52])
keys.append([0.406468, -0.306841, 0.406468, -0.306841, 0.406468, -0.306841, 0.406468, -0.306841, 0.406468, -0.297638])

names.append("HeadYaw")
times.append([0, 0.52, 1, 1.52, 2, 2.52, 3, 3.52, 4, 4.52])
keys.append([-0.046062, -0.0506639, -0.046062, -0.0506639, -0.046062, -0.0506639, -0.046062, -0.0506639, -0.046062, -0.055266])

names.append("LAnklePitch")
times.append([0.52, 4.52])
keys.append([0.00916204, 0.00916204])

names.append("LAnkleRoll")
times.append([0.52, 4.52])
keys.append([-0.256136, -0.25767])

names.append("LElbowRoll")
times.append([0.52, 1, 1.52, 2, 2.52, 3, 3.52, 4, 4.52])
keys.append([-0.684122, -0.269941, -0.684122, -0.269941, -0.684122, -0.269941, -0.684122, -0.269941, -0.665714])

names.append("LElbowYaw")
times.append([0.52, 1, 1.52, 2, 2.52, 3, 3.52, 4, 4.52])
keys.append([-1.17969, -1.06924, -1.17969, -1.06924, -1.17969, -1.06924, -1.17969, -1.06924, -1.17202])

names.append("LHand")
times.append([0.52, 1, 1.52, 2, 2.52, 3, 3.52, 4, 4.52])
keys.append([0.5, 0.7, 0.5, 0.7, 0.5, 0.7, 0.5, 0.7, 0.5016])

names.append("LHipPitch")
times.append([0.52, 4.52])
keys.append([0.40962, 0.408086])

names.append("LHipRoll")
times.append([0.52, 4.52])
keys.append([0.342125, 0.342125])

names.append("LHipYawPitch")
times.append([0.52, 4.52])
keys.append([-0.368118, -0.368118])

names.append("LKneePitch")
times.append([0.52, 4.52])
keys.append([-0.092082, -0.0923279])

names.append("LShoulderPitch")
times.append([0.52, 1, 1.52, 2, 2.52, 3, 3.52, 4, 4.52])
keys.append([-0.837606, -1.13213, -0.837606, -1.13213, -0.837606, -1.13213, -0.837606, -1.13213, -0.845275])

names.append("LShoulderRoll")
times.append([0.52, 1, 1.52, 2, 2.52, 3, 3.52, 4, 4.52])
keys.append([0.249999, 0.154892, 0.249999, 0.154892, 0.249999, 0.154892, 0.249999, 0.154892, 0.239262])

names.append("LWristYaw")
times.append([0.52, 1, 1.52, 2, 2.52, 3, 3.52, 4, 4.52])
keys.append([0.865134, 0.858999, 0.865134, 0.858999, 0.865134, 0.858999, 0.865134, 0.858999, 0.851328])

names.append("RAnklePitch")
times.append([0.52, 4.52])
keys.append([-0.11194, -0.11194])

names.append("RAnkleRoll")
times.append([0.52, 4.52])
keys.append([-0.084328, -0.085862])

names.append("RElbowRoll")
times.append([0.52, 4.52])
keys.append([1.5187, 1.48802])

names.append("RElbowYaw")
times.append([0.52, 4.52])
keys.append([0.842125, 0.852862])

names.append("RHand")
times.append([0.52, 4.52])
keys.append([0.8284, 0.8272])

names.append("RHipPitch")
times.append([0.52, 4.52])
keys.append([0.31903, 0.31903])

names.append("RHipRoll")
times.append([0.52, 4.52])
keys.append([0.105888, 0.105888])

names.append("RKneePitch")
times.append([0.52, 4.52])
keys.append([0.105888, 0.105888])

names.append("RShoulderPitch")
times.append([0.52, 4.52])
keys.append([2.01572, 2.00037])

names.append("RShoulderRoll")
times.append([0.52, 4.52])
keys.append([-0.417291, -0.383541])

names.append("RWristYaw")
times.append([0.52, 4.52])
keys.append([-0.130432, -0.101286])
