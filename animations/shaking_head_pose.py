# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.24, 0.92, 1.28, 1.6, 1.96, 2.28, 2.56, 2.84, 3.12, 3.48, 4.04, 4.48])
keys.append([-0.320648, 0.259876, -0.392432, 0.230731, -0.363768, 0.1451, -0.310897, 0.113427, -0.138207, 0.201243, 0.153801, -0.177985])

names.append("HeadYaw")
times.append([0.24, 0.92, 1.28, 1.6, 1.96, 2.28, 2.56, 2.84, 3.12, 3.48, 4.48])
keys.append([-0.10282, -0.194861, -0.165714, -0.075208, -0.012314, -4.19617e-05, -0.032256, -0.0429939, -0.055266, 0.032172, -0.00157596])

names.append("LAnklePitch")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([-0.242414, -0.242414, -0.242414, 0.067454])

names.append("LAnkleRoll")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([-0.162562, -0.162562, -0.162562, -0.110406])

names.append("LElbowRoll")
times.append([0.16, 0.84, 1.52, 2.2, 2.76, 3.4, 4.4])
keys.append([-1.54776, -1.0216, -1.15199, -1.20261, -0.937231, -1.25784, -0.590548])

names.append("LElbowYaw")
times.append([0.16, 0.84, 1.52, 2.2, 2.76, 3.4, 4.4])
keys.append([-1.19656, -1.16128, -0.940383, -0.934249, -0.903567, -0.791585, -1.2165])

names.append("LHand")
times.append([0.84, 1.52, 2.2, 3.4, 4.4])
keys.append([0.688387, 0.6992, 0.6992, 0.684, 0.232025])

names.append("LHipPitch")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([-0.805309, -0.805309, -0.805309, 0.211735])

names.append("LHipRoll")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([0.090548, 0.090548, 0.090548, 0.121228])

names.append("LHipYawPitch")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([-0.463226, -0.463226, -0.463226, -0.14262])

names.append("LKneePitch")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([0.998592, 0.998592, 0.998592, -0.092082])

names.append("LShoulderPitch")
times.append([0.16, 0.84, 1.52, 2.2, 2.76, 3.4, 4.4])
keys.append([0.34971, 1.41124, 1.33914, 1.43885, 1.52015, 1.37289, 1.59685])

names.append("LShoulderRoll")
times.append([0.16, 0.84, 1.52, 2.2, 2.76, 3.4, 4.4])
keys.append([0.461692, 0.368118, 0.412605, 0.415673, 0.363515, 0.412605, 0.174835])

names.append("LWristYaw")
times.append([0.84, 1.52, 2.2, 3.4, 4.4])
keys.append([0.282215, -0.276162, -0.188724, 0.0429101, 0.116542])

names.append("RAnklePitch")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([-0.223922, -0.223922, -0.223922, 0.0767419])

names.append("RAnkleRoll")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([0.090548, 0.090548, 0.090548, 0.066004])

names.append("RElbowRoll")
times.append([0.08, 0.76, 1.44, 2.12, 2.68, 3.32, 4.32])
keys.append([1.54938, 0.676537, 0.89283, 1.00174, 0.797722, 1.1352, 0.440299])

names.append("RElbowYaw")
times.append([0.08, 0.76, 1.44, 2.12, 2.68, 3.32, 4.32])
keys.append([1.62907, 0.093532, 0.450955, 0.466294, 0.513848, 0.639635, 1.17347])

names.append("RHand")
times.append([0.76, 1.44, 2.12, 3.32, 4.32])
keys.append([0.514873, 0.6944, 0.7988, 0.5424, 0.410207])

names.append("RHipPitch")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([-0.799256, -0.799256, -0.799256, 0.193243])

names.append("RHipRoll")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([0.00924586, 0.00924586, 0.00924586, -0.0735901])

names.append("RKneePitch")
times.append([0.8, 2.16, 3.24, 4.56])
keys.append([0.960325, 0.960325, 0.960325, -0.076658])

names.append("RShoulderPitch")
times.append([0.08, 0.76, 1.44, 2.12, 2.68, 3.32, 4.32])
keys.append([0.158044, 0.320648, 1.05083, 1.16281, 1.22878, 1.23798, 1.48342])

names.append("RShoulderRoll")
times.append([0.08, 0.76, 1.44, 2.12, 2.68, 3.32, 4.32])
keys.append([-0.900499, -0.205598, -0.362067, -0.415757, -0.351328, -0.37127, -0.122762])

names.append("RWristYaw")
times.append([0.76, 1.44, 2.12, 3.32, 4.32])
keys.append([-0.22554, 0.662646, 0.529187, 0.0873961, 0.161028])
