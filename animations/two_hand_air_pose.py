# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.4, 1.04, 1.72, 2.36, 3.08])
keys.append([0.315962, -0.242414, 0.21932, -0.34826, 0.236194])

names.append("HeadYaw")
times.append([0.4, 1.04, 1.72, 2.36, 3.08])
keys.append([-0.058334, -0.019984, -0.0445279, -0.0568, -0.0690719])

names.append("LAnklePitch")
times.append([0.92, 1.6, 2.96])
keys.append([0.0475121, 0.016832, 0.016832])

names.append("LAnkleRoll")
times.append([0.92, 1.6, 2.96])
keys.append([-0.136484, -0.147222, -0.148756])

names.append("LElbowRoll")
times.append([0.28, 0.96, 1.64, 2.28, 3])
keys.append([-1.54623, -1.35448, -0.699462, -1.54623, -0.506179])

names.append("LElbowYaw")
times.append([0.28, 0.96, 1.64, 2.28, 3])
keys.append([-1.2165, -0.86982, -0.589097, -1.39752, -0.490923])

names.append("LHand")
times.append([0.96, 1.64, 3])
keys.append([0.618182, 0.743636, 0.715296])

names.append("LHipPitch")
times.append([0.92, 1.6, 2.96])
keys.append([-0.161028, 0.021518, -0.288349])

names.append("LHipRoll")
times.append([0.92, 1.6, 2.96])
keys.append([0.105888, 0.14117, 0.138102])

names.append("LHipYawPitch")
times.append([0.92, 1.6, 2.96])
keys.append([-0.355846, -0.305225, -0.355846])

names.append("LKneePitch")
times.append([0.92, 1.6, 2.96])
keys.append([0.154892, 0.110406, 0.332836])

names.append("LShoulderPitch")
times.append([0.28, 0.96, 1.64, 2.28, 3])
keys.append([0.493905, -0.909704, -0.719487, -0.411154, -0.955723])

names.append("LShoulderRoll")
times.append([0.28, 0.96, 1.64, 2.28, 3])
keys.append([0.421808, 0.59515, 0.423342, 1.12438, 0.193243])

names.append("LWristYaw")
times.append([0.96, 1.64, 3])
keys.append([0.575959, 0.314159, 0.31903])

names.append("RAnklePitch")
times.append([0.92, 1.6, 2.96])
keys.append([0.046062, 0.0261199, 0.012314])

names.append("RAnkleRoll")
times.append([0.92, 1.6, 2.96])
keys.append([0.066004, 0.092082, 0.10282])

names.append("RElbowRoll")
times.append([0.2, 0.88, 1.56, 2.2, 2.92])
keys.append([0.579894, 1.37604, 0.607505, 1.45734, 0.605971])

names.append("RElbowYaw")
times.append([0.2, 0.88, 1.56, 2.2, 2.92])
keys.append([0.20398, 0.447886, 0.262272, 0.671851, 0.357381])

names.append("RHand")
times.append([0.88, 1.56, 2.92])
keys.append([0.787273, 0.7, 0.818182])

names.append("RHipPitch")
times.append([0.92, 1.6, 2.96])
keys.append([-0.139636, -0.00771196, -0.233209])

names.append("RHipRoll")
times.append([0.92, 1.6, 2.96])
keys.append([-0.016832, -0.078192, -0.0459781])

names.append("RKneePitch")
times.append([0.92, 1.6, 2.96])
keys.append([0.130432, 0.113558, 0.274628])

names.append("RShoulderPitch")
times.append([0.2, 0.88, 1.56, 2.2, 2.92])
keys.append([-1.12898, -1.13512, -0.880473, -1.01086, -0.970981])

names.append("RShoulderRoll")
times.append([0.2, 0.88, 1.56, 2.2, 2.92])
keys.append([-0.230143, -1.01555, -0.38661, -1.34843, -0.326783])

names.append("RWristYaw")
times.append([0.88, 1.56, 2.92])
keys.append([-0.138102, -0.139636, -0.145772])
