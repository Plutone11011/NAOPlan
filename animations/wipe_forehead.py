# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.92, 1.64, 3.24, 3.92, 4.48, 5.04])
keys.append([-0.0261199, 0.427944, 0.308291, 0.11194, -0.013848, 0.061318])

names.append("HeadYaw")
times.append([0.92, 1.64, 3.24, 3.92, 4.48, 5.04])
keys.append([-0.234743, -0.622845, -0.113558, -0.00617796, -0.027654, -0.036858])

names.append("LElbowRoll")
times.append([0.76, 1.48, 3.08, 3.76, 4.32, 4.88])
keys.append([-0.866668, -0.868202, -0.822183, -0.992455, -0.966378, -0.990923])

names.append("LElbowYaw")
times.append([0.76, 1.48, 3.08, 3.76, 4.32, 4.88])
keys.append([-0.957257, -0.823801, -1.00788, -0.925044, -1.24412, -0.960325])

names.append("LHand")
times.append([1.48, 3.08, 3.76, 4.88])
keys.append([0.132026, 0.132026, 0.132026, 0.132026])

names.append("LShoulderPitch")
times.append([0.76, 1.48, 3.08, 3.76, 4.32, 4.88])
keys.append([0.863599, 0.858999, 0.888144, 0.929562, 1.017, 0.977116])

names.append("LShoulderRoll")
times.append([0.76, 1.48, 3.08, 3.76, 4.32, 4.88])
keys.append([0.286815, 0.230059, 0.202446, 0.406468, 0.360449, 0.31903])

names.append("LWristYaw")
times.append([1.48, 3.08, 3.76, 4.88])
keys.append([0.386526, 0.386526, 0.386526, 0.386526])

names.append("RElbowRoll")
times.append([0.6, 1.32, 2.92, 3.6, 4.16, 4.72])
keys.append([1.28093, 1.39752, 1.57239, 1.24105, 1.22571, 0.840674])

names.append("RElbowYaw")
times.append([0.6, 1.32, 2.92, 3.6, 4.16, 4.72])
keys.append([-0.128898, -0.285367, -0.15651, 0.754686, 1.17193, 0.677985])

names.append("RHand")
times.append([1.32, 2.92, 3.6, 4.72])
keys.append([0.166571, 0.166208, 0.166571, 0.166208])

names.append("RShoulderPitch")
times.append([0.6, 1.32, 2.92, 3.6, 4.16, 4.72])
keys.append([0.0767419, -0.59515, -0.866668, -0.613558, 0.584497, 0.882091])

names.append("RShoulderRoll")
times.append([0.6, 1.32, 2.92, 3.6, 4.16, 4.72])
keys.append([-0.019984, -0.019984, -0.615176, -0.833004, -0.224006, -0.214801])

names.append("RWristYaw")
times.append([1.32, 2.92, 3.6, 4.72])
keys.append([-0.058334, -0.0521979, -0.067538, -0.038392])
