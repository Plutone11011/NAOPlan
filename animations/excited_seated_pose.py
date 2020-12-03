# Choregraphe simplified export in Python.
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.64, 1.08, 1.48, 2.56, 3.32])
keys.append([0.237728, -0.168782, -0.280764, -0.150374, -0.18719])

names.append("HeadYaw")
times.append([0.64, 1.08, 1.48, 2.56, 3.32])
keys.append([-0.046062, -0.0798099, -0.0537319, -0.07214, -0.030722])

"""names.append("LAnklePitch")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([-0.131966, -0.121228, -0.168782, -0.12583, 0.121144])

names.append("LAnkleRoll")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([-0.021434, -0.033706, -0.0827941, -0.032172, -0.087396])
"""
names.append("LElbowRoll")
times.append([0.56, 1, 1.4, 1.6, 1.72, 2.16, 2.48, 3.24])
keys.append([-1.45266, -0.759288, -1.38516, -0.994838, -1.36675, -1.20428, -0.759288, -0.381923])

names.append("LElbowYaw")
times.append([0.56, 1, 1.2, 1.4, 1.6, 1.72, 2.48, 3.24])
keys.append([-0.794654, -1.16128, -1.58825, -0.76244, -1.309, -0.770111, -1.14901, -1.13827])

names.append("LHand")
times.append([0.56, 1, 1.4, 2.48, 3.24])
keys.append([0.110208, 0.110208, 0.8, 0.109844, 0.109117])
"""
names.append("LHipPitch")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([-0.300622, -0.061318, -0.200912, -0.06592, 0.208666])

names.append("LHipRoll")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([0.038392, 0.058334, 0.14884, 0.0521979, 0.0982179])

names.append("LHipYawPitch")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([-0.406468, -0.446352, -0.461692, -0.44175, -0.315962])

names.append("LKneePitch")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([0.644238, 0.443284, 0.579811, 0.440216, -0.0923461])
"""
names.append("LShoulderPitch")
times.append([0.56, 1, 1.4, 1.72, 2.48, 3.24])
keys.append([1.14892, 1.45572, 0.668782, 0.704064, 1.45726, 1.48947])

names.append("LShoulderRoll")
times.append([0.56, 1, 1.4, 1.72, 2.48, 3.24])
keys.append([0.156426, 0.236194, 0.00869999, 0.0352401, 0.217786, 0.0827941])

names.append("LWristYaw")
times.append([0.56, 1, 1.4, 2.48, 3.24])
keys.append([-0.124296, -0.12583, -0.296706, -0.131966, -0.139636])
"""
names.append("RAnklePitch")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([-0.110406, -0.0735901, -0.091998, -0.0812601, 0.105888])

names.append("RAnkleRoll")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([0.032256, 0.0568, -0.00149204, 0.058334, 0.046062])
"""
names.append("RElbowRoll")
times.append([0.48, 0.92, 1.4, 1.6, 1.72, 2.08, 2.4, 3.16])
keys.append([1.51563, 0.937317, 1.38678, 1.09956, 1.36223, 1.32645, 0.940383, 0.451038])

names.append("RElbowYaw")
times.append([0.48, 0.92, 1.2, 1.4, 1.6, 1.72, 2.4, 3.16])
keys.append([1.01393, 1.32687, 1.71042, 0.857465, 1.36136, 0.868202, 1.31766, 1.49561])

names.append("RHand")
times.append([0.48, 0.92, 1.4, 2.4, 3.16])
keys.append([0.226207, 0.226207, 0.763636, 0.224389, 0.221844])
"""
names.append("RHipPitch")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([-0.268493, -0.0414599, -0.0537319, -0.036858, 0.217786])

names.append("RHipRoll")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([-0.0291041, -0.0720561, 0.055266, -0.0735901, -0.061318])

names.append("RKneePitch")
times.append([0.52, 0.96, 1.6, 2.44, 3.2])
keys.append([0.586029, 0.369736, 0.382007, 0.366667, -0.0797261])
"""
names.append("RShoulderPitch")
times.append([0.48, 0.92, 1.4, 1.72, 2.4, 3.16])
keys.append([1.43587, 1.60307, 0.768577, 0.808459, 1.59387, 1.55859])

names.append("RShoulderRoll")
times.append([0.48, 0.92, 1.4, 1.72, 2.4, 3.16])
keys.append([-0.227074, -0.222472, -0.0353239, -0.0629359, -0.213269, -0.0506639])

names.append("RWristYaw")
times.append([0.48, 0.92, 1.4, 2.4, 3.16])
keys.append([-0.00771196, -0.00924597, 0.279253, -0.00924597, -0.00617796])
