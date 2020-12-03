# Choregraphe bezier export in Python.

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.64, 1.12, 2, 7.92, 14.32, 15.72, 16.2, 16.72])
keys.append([-0.118682, -0.395814, -0.421891, -0.537561, -0.306841, -0.37127, -0.0942478, -0.236277])

names.append("HeadYaw")
times.append([1.12, 2, 14.32, 15.72, 16.72])
keys.append([0.656511, 0.719404, -0.851412, -0.885159, -0.00617796])

names.append("LAnklePitch")
times.append([1, 1.88, 7.8, 14.2, 15.6, 16.6])
keys.append([0.0981341, 0.101202, -0.167552, 0.04291, 0.0536481, 0.04291])

names.append("LAnkleRoll")
times.append([1, 1.88, 14.2, 15.6, 16.6])
keys.append([-0.153358, -0.151824, 0.039926, 0.038392, -0.0735901])

names.append("LElbowRoll")
times.append([1.04, 1.92, 7.84, 14.24, 15.64, 16.64])
keys.append([-1.30846, -1.33761, -0.418879, -0.584411, -0.461692, -0.208583])

names.append("LElbowYaw")
times.append([1.04, 1.92, 7.84, 14.24, 15.64, 16.64])
keys.append([-0.34826, -0.346725, -0.720821, -0.530805, -0.569155, -0.63205])

names.append("LHand")
times.append([1.04, 1.92, 7.84, 14.24, 15.64, 16.64])
keys.append([0.4188, 0.4188, 0.68, 0.418, 0.418, 0.418])

names.append("LHipPitch")
times.append([1, 1.88, 14.2, 15.6, 16.6])
keys.append([0.214801, 0.213269, 0.314512, 0.309909, 0.288433])

names.append("LHipRoll")
times.append([1, 1.88, 14.2, 15.6, 16.6])
keys.append([0.168782, 0.167248, -0.0444441, -0.041376, 0.0782759])

names.append("LHipYawPitch")
times.append([1, 1.88, 7.8, 14.2, 15.6, 16.6])
keys.append([-0.263807, -0.262272, -0.378736, -0.260738, -0.263807, -0.265341])

names.append("LKneePitch")
times.append([1, 1.88, 7.8, 14.2, 15.6, 16.6])
keys.append([-0.092082, -0.090548, 0.233874, -0.0923279, -0.0923279, -0.090548])

names.append("LShoulderPitch")
times.append([1.04, 1.92, 14.24, 15.64, 16.64])
keys.append([1.21642, 1.17654, 1.42044, 1.42504, 1.39897])

names.append("LShoulderRoll")
times.append([1.04, 1.92, 7.84, 14.24, 15.64, 16.64])
keys.append([0.085862, 0.052114, 0.296706, 0.131882, 0.0981341, 0.010696])

names.append("LWristYaw")
times.append([1.04, 1.92, 7.84, 14.24, 15.64, 16.64])
keys.append([0.265341, 0.31903, -0.994838, -0.20253, -0.204064, -0.0629359])

names.append("RAnklePitch")
times.append([1, 1.88, 7.8, 14.2, 15.6, 16.6])
keys.append([0.0521979, 0.055266, -0.167552, 0.0537319, 0.058334, 0.0353239])

names.append("RAnkleRoll")
times.append([1, 1.88, 14.2, 15.6, 16.6])
keys.append([-0.0720561, -0.0720561, 0.0951499, 0.092082, -0.013764])

names.append("RElbowRoll")
times.append([0.96, 1.84, 14.16, 15.56, 16.56])
keys.append([0.345191, 0.289967, 0.740964, 0.589097, 0.27923])

names.append("RElbowYaw")
times.append([0.96, 1.84, 14.16, 15.56, 16.56])
keys.append([1.21795, 1.23176, 0.915757, 0.849794, 0.84826])

names.append("RHand")
times.append([0.96, 1.84, 7.76, 14.16, 15.56, 16.56])
keys.append([0.5612, 0.5612, 0.62, 0.5604, 0.5604, 0.5604])

names.append("RHipPitch")
times.append([1, 1.88, 14.2, 15.6, 16.6])
keys.append([0.25767, 0.259204, 0.288349, 0.262272, 0.285283])

names.append("RHipRoll")
times.append([1, 1.88, 14.2, 15.6, 16.6])
keys.append([0.0859459, 0.0859459, -0.116542, -0.115008, 0.01078])

names.append("RKneePitch")
times.append([1, 1.88, 7.8, 14.2, 15.6, 16.6])
keys.append([-0.091998, -0.0904641, 0.233874, -0.0889301, -0.0904641, -0.091998])

names.append("RShoulderPitch")
times.append([0.96, 1.84, 14.16, 15.56, 16.56])
keys.append([1.53864, 1.54478, 1.48342, 1.49262, 1.46194])

names.append("RShoulderRoll")
times.append([0.96, 1.84, 7.76, 14.16, 15.56, 16.56])
keys.append([-0.067538, -0.066004, -0.267035, 0.00916204, 0.00762803, 0.010696])

names.append("RWristYaw")
times.append([0.96, 1.84, 7.76, 14.16, 15.56, 16.56])
keys.append([-0.112024, -0.081344, 0.829031, 0.084328, -4.19617e-05, 0.033706])