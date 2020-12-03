import time

# Choregraphe bezier export in Python.
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.4, 0.56, 0.8, 0.92, 1.12, 1.48, 2.68])
keys.append([-0.455639, -0.168782, -0.572224, -0.374338, -0.621313, 0.375789, -0.176453])

names.append("HeadYaw")
times.append([0.4, 0.56, 0.8, 0.92, 1.12, 1.48, 2.68])
keys.append([-0.0690719, -0.0798099, -0.0353239, -0.0353239, -0.030722, -0.032256, -0.016916])

names.append("LAnklePitch")
times.append([1.16, 1.68, 2.56])
keys.append([-0.136568, -0.023052, 0.0720561])

names.append("LAnkleRoll")
times.append([1.16, 1.68, 2.56])
keys.append([-0.11961, -0.067454, -0.107338])

names.append("LElbowRoll")
times.append([1.04, 1.32, 2.6])
keys.append([-0.636569, -0.720938, -0.61049])

names.append("LElbowYaw")
times.append([1.04, 1.32, 2.6])
keys.append([-1.77334, -0.897433, -1.21344])

names.append("LHand")
times.append([2.6])
keys.append([0.234])

names.append("LHipPitch")
times.append([1.16, 1.68, 2.56])
keys.append([0.154976, -0.0643861, 0.205598])

names.append("LHipRoll")
times.append([1.16, 1.68, 2.56])
keys.append([0.128898, 0.082878, 0.11049])

names.append("LHipYawPitch")
times.append([1.16, 1.68, 2.56])
keys.append([-0.286815, -0.338973, -0.161028])

names.append("LKneePitch")
times.append([1.16, 1.68, 2.56])
keys.append([0.371186, 0.37272, -0.0890139])

names.append("LShoulderPitch")
times.append([1.04, 1.32, 2.6])
keys.append([1.51095, 1.27318, 1.59839])

names.append("LShoulderRoll")
times.append([1.04, 1.32, 2.6])
keys.append([0.29602, 0.0551821, 0.13495])

names.append("LWristYaw")
times.append([2.6])
keys.append([0.0996681])

names.append("RAnklePitch")
times.append([1.16, 1.68, 2.56])
keys.append([-0.323633, -0.144154, 0.0629359])

names.append("RAnkleRoll")
times.append([1.16, 1.68, 2.56])
keys.append([0.127364, 0.0767419, 0.066004])

names.append("RElbowRoll")
times.append([1.04, 1.32, 2, 2.52])
keys.append([0.891296, 1.46348, 1.00705, 0.44797])

names.append("RElbowYaw")
times.append([1.04, 1.32, 2.52])
keys.append([1.12591, 0.294486, 1.175])

names.append("RHand")
times.append([2.52])
keys.append([0.406])

names.append("RHipPitch")
times.append([1.16, 1.68, 2.56])
keys.append([0.141086, -0.0798099, 0.18864])

names.append("RHipRoll")
times.append([1.16, 1.68, 2.56])
keys.append([-0.233125, -0.122678, -0.067454])

names.append("RKneePitch")
times.append([1.16, 1.68, 2.56])
keys.append([0.544613, 0.493989, -0.075124])

names.append("RShoulderPitch")
times.append([1.04, 1.32, 2.52])
keys.append([0.90817, 0.242414, 1.49262])

names.append("RShoulderRoll")
times.append([1.04, 1.32, 2.52])
keys.append([-0.653526, -0.0261199, -0.0874799])

names.append("RWristYaw")
times.append([2.52])
keys.append([0.174835])
