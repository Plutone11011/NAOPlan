# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.08, 0.56, 1.08, 1.6, 2.08, 2.6, 3.08, 3.6])
keys.append([0.4034, 0.532256, 0.0735901, 0.269941, -0.182588, 0.085862, -0.182588, 0.085862])

names.append("HeadYaw")
times.append([0.08, 0.56, 1.08, 1.6, 2.08, 2.6, 3.08, 3.6])
keys.append([-0.426494, -0.20944, 0.039842, -0.14884, -0.122762, -0.128898, -0.122762, -0.128898])

names.append("LAnklePitch")
times.append([0.64, 2.68, 3.68])
keys.append([-0.0112903, -0.121738, -0.121738])

names.append("LAnkleRoll")
times.append([0.64, 2.68, 3.68])
keys.append([-0.193732, 0.0483652, 0.0483652])

names.append("LElbowRoll")
times.append([0.12, 0.6, 1.12, 1.64, 2.12, 2.64, 3.12, 3.64])
keys.append([-0.424876, -0.61049, -0.424876, -0.596684, -0.424876, -0.601287, -0.429478, -0.605888])

names.append("LElbowYaw")
times.append([0.12, 0.6, 1.12, 1.64, 2.12, 2.64, 3.12, 3.64])
keys.append([-1.68591, -1.5233, -1.68591, -1.53097, -1.68591, -1.52484, -1.6767, -1.51717])

names.append("LHand")
times.append([0.04])
keys.append([0.237117])

names.append("LHipPitch")
times.append([0.64, 2.68, 3.68])
keys.append([0.33444, 0.398869, 0.398869])

names.append("LHipRoll")
times.append([0.64, 2.68, 3.68])
keys.append([0.295708, 0.014986, 0.014986])

names.append("LHipYawPitch")
times.append([0.64, 2.68, 3.68])
keys.append([-0.401866, -0.384992, -0.384992])

names.append("LKneePitch")
times.append([0.64, 2.68, 3.68])
keys.append([0.0300457, 0.109814, 0.109814])

names.append("LShoulderPitch")
times.append([0.12, 0.6, 1.12, 1.64, 2.12, 2.64, 3.12, 3.64])
keys.append([1.61066, 1.60299, 1.60912, 1.60912, 1.60912, 1.60452, 1.60452, 1.60606])

names.append("LShoulderRoll")
times.append([0.12, 0.6, 1.12, 1.64, 2.12, 2.64, 3.12, 3.64])
keys.append([0.0904641, 0.0904641, 0.0904641, 0.0904641, 0.091998, 0.0904641, 0.0904641, 0.093532])

names.append("LWristYaw")
times.append([0.04])
keys.append([0.567537])

names.append("RAnklePitch")
times.append([0.64, 2.68, 3.68])
keys.append([-0.0358286, -0.0296928, -0.0296928])

names.append("RAnkleRoll")
times.append([0.64, 2.68, 3.68])
keys.append([-0.0780021, 0.151844, 0.0355138])

names.append("RElbowRoll")
times.append([0.12, 0.6, 1.12, 1.64, 2.12, 2.64, 3.12, 3.64])
keys.append([1.48649, 0.994073, 1.48956, 0.994073, 1.48956, 0.981802, 1.46961, 0.966462])

names.append("RElbowYaw")
times.append([0.12, 0.6, 1.12, 1.64, 2.12, 2.64, 3.12, 3.64])
keys.append([0.757754, 2.0944, 0.75622, 2.07853, 0.743948, 2.07239, 0.74088, 2.07699])

names.append("RHand")
times.append([0.04, 0.56, 1.08, 1.84, 2.6, 3.32])
keys.append([0.247273, 0.630909, 0.370909, 0.723636, 0.469091, 0.749091])

names.append("RHipPitch")
times.append([0.64, 2.68, 3.68])
keys.append([0.397054, 0.409325, 0.409325])

names.append("RHipRoll")
times.append([0.64, 2.68, 3.68])
keys.append([0.0511575, -0.148262, -0.148262])

names.append("RKneePitch")
times.append([0.64, 2.68, 3.68])
keys.append([0.0307944, 0.0292604, 0.0292604])

names.append("RShoulderPitch")
times.append([0.12, 0.6, 1.12, 1.64, 2.12, 2.64, 3.12, 3.64])
keys.append([1.3561, 1.45427, 1.38524, 1.44967, 1.40058, 1.45734, 1.41899, 1.46961])

names.append("RShoulderRoll")
times.append([0.12, 0.6, 1.12, 1.64, 2.12, 2.64, 3.12, 3.64])
keys.append([-0.570689, -0.0706059, -0.55535, -0.0767419, -0.543078, -0.073674, -0.526205, -0.067538])

names.append("RWristYaw")
times.append([0.04])
keys.append([1.04921])

