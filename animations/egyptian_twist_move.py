# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.08, 0.28, 0.48, 0.68, 0.88, 1.08, 1.28, 1.48, 1.68, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6])
keys.append([-0.055266, 0.00349066, -0.073674, 0.00349066, -0.073674, 0.00349066, -0.073674, 0.00349066, -0.073674, 0.00349066, -0.073674, 0.00349066, -0.073674, 0.00349066, -0.073674, 0.00349066, -0.073674])

names.append("HeadYaw")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([1.38209, 1.36215, 1.36215, 1.36215, 1.36215, -1.36215, -1.36215, -1.36215, -1.36215])

names.append("LAnklePitch")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([0.0444441, -0.181053, 0.0444441, -0.181053, 0.0444441, -0.205514, -0.022968, -0.205514, -0.022968])

names.append("LAnkleRoll")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([-0.059784, -0.056716, -0.059784, -0.056716, -0.059784, -0.027654, -0.01078, -0.027654, -0.01078])

names.append("LElbowRoll")
times.append([0.08, 0.28, 0.48, 0.68, 0.88, 1.08, 1.28, 1.48, 1.68, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6])
keys.append([-1.51555, -1.40324, -1.51555, -1.40324, -1.51555, -1.40324, -1.51555, -1.40324, -1.51555, -1.2706, -1.42973, -1.2706, -1.42973, -1.2706, -1.42973, -1.2706, -1.42973])

names.append("LElbowYaw")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([-1.7442, -1.7442, -1.7442, -1.7442, -1.7442, 1.30701, 1.30701, 1.30701, 1.30701])

names.append("LHand")
times.append([0.08, 0.28, 0.48, 0.68, 0.88, 1.08, 1.28, 1.48, 1.68, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6])
keys.append([0.4, 0.5, 0.4, 0.5, 0.4, 0.5, 0.4, 0.5, 0.4, 0.5, 0.3572, 0.5, 0.3572, 0.5, 0.3572, 0.5, 0.3572])

names.append("LHipPitch")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([0.481718, 0.213269, 0.481718, 0.213269, 0.481718, 0.246933, 0.48398, 0.246933, 0.48398])

names.append("LHipRoll")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([0.174919, 0.136568, 0.174919, 0.136568, 0.174919, 0.11194, 0.11194, 0.11194, 0.11194])

names.append("LHipYawPitch")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([-0.665714, -0.694859, -0.665714, -0.694859, -0.665714, -0.694859, -0.665714, -0.694859, -0.665714])

names.append("LKneePitch")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([-0.0537319, 0.408002, -0.0537319, 0.408002, -0.0537319, 0.401949, -0.00456004, 0.401949, -0.00456004])

names.append("LShoulderPitch")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([0.121144, 0.122678, 0.122678, 0.122678, 0.122678, 0.265424, 0.265424, 0.265424, 0.265424])

names.append("LShoulderRoll")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([1.22562, 1.22562, 1.22562, 1.22562, 1.22562, 1.26406, 1.26406, 1.26406, 1.26406])

names.append("LWristYaw")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([1.47106, 1.58611, 1.58611, 1.58611, 1.58611, 1.43587, 1.43587, 1.43587, 1.43587])

names.append("RAnklePitch")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([-0.022968, -0.205514, -0.022968, -0.205514, -0.022968, -0.181053, 0.0444441, -0.181053, 0.0444441])

names.append("RAnkleRoll")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([0.01078, 0.027654, 0.01078, 0.027654, 0.01078, 0.056716, 0.059784, 0.056716, 0.059784])

names.append("RElbowRoll")
times.append([0.08, 0.28, 0.48, 0.68, 0.88, 1.08, 1.28, 1.48, 1.68, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6])
keys.append([1.4282, 1.2706, 1.42973, 1.2706, 1.42973, 1.2706, 1.42973, 1.2706, 1.42973, 1.40324, 1.51555, 1.40324, 1.51555, 1.40324, 1.51555, 1.40324, 1.51555])

names.append("RElbowYaw")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([-1.30701, -1.30701, -1.30701, -1.30701, -1.30701, 1.7442, 1.7442, 1.7442, 1.7442])

names.append("RHand")
times.append([0.08, 0.28, 0.48, 0.68, 0.88, 1.08, 1.28, 1.48, 1.68, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6])
keys.append([0.3552, 0.5, 0.3572, 0.5, 0.3572, 0.5, 0.3572, 0.5, 0.3572, 0.5, 0.4, 0.5, 0.4, 0.5, 0.4, 0.5, 0.4])

names.append("RHipPitch")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([0.48398, 0.246933, 0.48398, 0.246933, 0.48398, 0.213269, 0.481718, 0.213269, 0.481718])

names.append("RHipRoll")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([-0.110406, -0.11194, -0.11194, -0.11194, -0.11194, -0.136568, -0.174919, -0.136568, -0.174919])

names.append("RKneePitch")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([-0.00456004, 0.401949, -0.00456004, 0.401949, -0.00456004, 0.408002, -0.0537319, 0.408002, -0.0537319])

names.append("RShoulderPitch")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([0.265424, 0.265424, 0.265424, 0.265424, 0.265424, 0.122678, 0.122678, 0.122678, 0.122678])

names.append("RShoulderRoll")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([-1.26406, -1.26406, -1.26406, -1.26406, -1.26406, -1.22562, -1.22562, -1.22562, -1.22562])

names.append("RWristYaw")
times.append([0.08, 0.48, 0.88, 1.28, 1.68, 2.4, 2.8, 3.2, 3.6])
keys.append([-1.48495, -1.43587, -1.43587, -1.43587, -1.43587, -1.58611, -1.58611, -1.58611, -1.58611])

