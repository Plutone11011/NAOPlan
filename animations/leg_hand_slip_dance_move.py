# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.16, 1.16, 2.36, 3, 3.2, 4.16, 5.12, 5.68, 6.48, 7.2])
keys.append([0.325165, 0.091998, 0.467829, 0.01223, 0.380389, 0.380389, 0.447886, 0.340507, 0.00609404, -0.368202])

names.append("HeadYaw")
times.append([0.16, 1.16, 2.36, 3, 3.2, 4.16, 5.12, 5.68, 6.48, 7.2])
keys.append([0.351244, -0.763974, 0.538392, -0.627448, -0.61671, -0.61671, 0.366584, 0.642704, 0.691793, 0.87127])

names.append("LAnklePitch")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([-0.489898, -0.879534, -0.879534, -0.176962, -0.176962, -0.00361468, -0.308887, 0.0101913, 0.0608078])

names.append("LAnkleRoll")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([-0.194007, -0.0959931, -0.0988987, -0.39968, -0.328998, 0.225266, -0.0139626, 0.139362, 0.0621712])

names.append("LElbowRoll")
times.append([0.24, 1.24, 1.76, 2.44, 3.28, 4.28, 5.2, 5.76, 6.6, 7.36])
keys.append([-1.23636, -0.920358, -0.196309, -0.093532, -0.914223, -0.914223, -0.906552, -1.23943, -0.742414, -0.759288])

names.append("LElbowYaw")
times.append([0.24, 1.24, 1.76, 2.44, 3.28, 4.28, 5.2, 5.76, 6.6, 7.36])
keys.append([-1.20577, 0.877407, 0.507713, 0.500042, 0.883542, 0.883542, -0.259288, 0.207048, 0.447886, -0.506262])

names.append("LHand")
times.append([0.44, 1.08, 3.12, 6.36])
keys.append([0.24148, 0.574934, 0.577116, 0.577479])

names.append("LHipPitch")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([-0.0199139, -0.361995, -0.361995, 0.139622, 0.139622, 0.298877, 0.162632, 0.289672, 0.397335])

names.append("LHipRoll")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([0.389282, 0.754373, 0.754373, 0.631654, 0.631654, -0.359491, -0.397659, -0.195353, -0.077054])

names.append("LHipYawPitch")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([-0.358915, -0.628898, -0.628898, -0.582879, -0.582879, -0.358915, -0.674919, -0.582879, -0.443284])

names.append("LKneePitch")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([0.729549, 1.58552, 1.58552, 0.408943, 0.408943, 0.0292604, 0.849202, 0.181127, 0.0147056])

names.append("LShoulderPitch")
times.append([0.24, 1.24, 1.76, 2.44, 3.28, 4.28, 5.2, 5.76, 6.6, 7.36])
keys.append([1.39436, -0.0706059, 0.394197, 0.394197, -0.019984, -0.019984, 0.926494, 0.555266, 0.139552, -0.243948])

names.append("LShoulderRoll")
times.append([0.24, 1.24, 1.76, 2.44, 3.28, 4.28, 5.2, 5.76, 6.6, 7.36])
keys.append([0.409536, 0.052114, 0.552198, 0.731675, 0.076658, 0.076658, 0.977116, 0.668782, 1.43118, 1.36982])

names.append("LWristYaw")
times.append([0.44, 1.08, 3.12, 6.36])
keys.append([0.550664, -0.231677, -0.236277, -0.22554])

names.append("RAnklePitch")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([-0.00361468, -0.205949, -0.179769, 0.0101913, 0.0101913, -0.489898, -0.86879, -0.176962, -0.0726446])

names.append("RAnkleRoll")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([-0.225266, 0.0680678, 0.0558505, -0.139362, -0.139362, 0.194007, 0.106078, 0.328998, 0.34383])

names.append("RElbowRoll")
times.append([0.24, 1.24, 1.76, 2.44, 3.28, 4.28, 5.2, 5.76, 6.6, 7.36])
keys.append([1.55092, 0.765508, 1.55552, 1.56319, 0.691876, 0.691876, 0.503194, 0.582963, 0.925044, 1.26866])

names.append("RElbowYaw")
times.append([0.24, 1.24, 1.76, 2.44, 3.28, 4.28, 5.2, 5.76, 6.6, 7.36])
keys.append([0.450955, -0.306841, -0.405018, -0.234743, -0.306841, -0.306841, -0.217869, 0.282215, -0.214801, 0.628898])

names.append("RHand")
times.append([0.44, 1.08, 3.12, 6.36])
keys.append([0.469091, 0.808388, 0.810933, 0.81166])

names.append("RHipPitch")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([0.298877, 0.165419, 0.165419, 0.289672, 0.289672, -0.0199139, -0.366879, 0.139622, 0.435402])

names.append("RHipRoll")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([0.359491, 0.382501, 0.382501, 0.195353, 0.195353, -0.389282, -0.734251, -0.631654, -0.488811])

names.append("RKneePitch")
times.append([0.32, 1.32, 1.96, 3.4, 4.04, 4.8, 5.84, 6.76, 7.52])
keys.append([0.0292604, 0.822338, 0.822338, 0.181127, 0.181127, 0.729549, 1.52951, 0.408943, 0.0461345])

names.append("RShoulderPitch")
times.append([0.24, 1.24, 1.76, 2.44, 3.28, 4.28, 5.2, 5.76, 6.6, 7.36])
keys.append([1.16895, 0.247016, 0.254685, 0.273093, 0.179519, 0.179519, 0.728692, 0.90817, 0.211735, 0.289967])

names.append("RShoulderRoll")
times.append([0.24, 1.24, 1.76, 2.44, 3.28, 4.28, 5.2, 5.76, 6.6, 7.36])
keys.append([-0.642787, -0.886694, -0.612108, -0.487854, -1.00941, -1.00941, -0.00924597, -0.303775, -0.047596, -0.04913])

names.append("RWristYaw")
times.append([0.44, 1.08, 3.12, 6.36])
keys.append([1.04921, 0.731675, 0.731675, 0.733209])
