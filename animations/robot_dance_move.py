# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.16, 0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.76, 3.84, 4.44, 6.2, 7.96, 9.12, 9.68])
keys.append([0.514872, 0.454021, -0.093616, -0.0874799, -0.093616, -0.093616, 0.514872, 0.453786, 0.514872, -0.3735, -0.3735, -0.3735, -0.349066, 0.514872])

names.append("HeadYaw")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.84, 4.44, 4.72, 5.32, 5.6, 6.2, 6.48, 7.08, 7.36, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([0.421808, -0.136568, -0.130432, -0.127364, -0.127364, 0.00302603, -0.00924597, -0.15708, -0.207694, 0.1309, 0.20944, -0.15708, -0.207694, 0.1309, 0.20944, -0.15708, -0.207694, 0.1309, 0.20944, 0.20398])

names.append("LAnklePitch")
times.append([0.36, 1.36, 1.52, 2.04, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([-0.2102, -0.016916, -0.016916, 0.0244346, 0.049046, 0.056716, 0.260738, 0.294486, 0.294486, 0.294486, 0.332836])

names.append("LAnkleRoll")
times.append([0.36, 1.36, 1.52, 2.04, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([0.019984, -0.0981341, -0.0981341, -0.1309, -0.049046, -0.049046, -0.0199001, -0.0183661, -0.0183661, -0.0183661, -0.0291041])

names.append("LElbowRoll")
times.append([0.36, 1.36, 1.52, 2.52, 2.6, 2.68, 3.2, 3.68, 3.76, 3.84, 4.44, 4.72, 5.32, 5.6, 6.2, 6.48, 7.08, 7.36, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([-0.263807, -1.52015, -1.50174, -1.41277, -1.54462, -1.41277, -1.54462, -1.35908, -1.49749, -1.34988, -1.54462, -1.54462, -0.657989, -0.610865, -1.54462, -1.54462, -0.657989, -0.553269, -1.54462, -1.54462, -0.610865, -0.411898, -1.35612])

names.append("LElbowYaw")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.2, 3.68, 3.84, 4.44, 6.2, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([-1.36377, -1.53864, -1.54171, -0.147306, -0.147306, -1.61443, -0.698011, -0.725624, -0.719487, -0.719487, -0.631809, -0.631809, -0.690259, -0.690259, -0.684206])

names.append("LHand")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.2, 3.68, 3.84, 4.44, 6.2, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([0.7316, 0.7316, 0.7316, 0.7328, 0.7324, 0.9, 0.7348, 0.736, 0.7356, 0.7356, 0.7356, 0.7356, 0.8168, 0.8168, 0.8156])

names.append("LHipPitch")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([-0.558334, -0.0643861, -0.0643861, 0.136568, 0.139636, -0.338973, -0.432547, -0.432547, -0.432547, -0.523053])

names.append("LHipRoll")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([0.135034, 0.20253, 0.20253, 0.030722, 0.032256, -0.0367741, -0.04291, -0.04291, -0.04291, -0.0459781])

names.append("LHipYawPitch")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([-0.71787, -0.592082, -0.592082, -0.18864, -0.185572, -0.211651, -0.205514, -0.205514, -0.205514, -0.222388])

names.append("LKneePitch")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([0.868202, 0.408002, 0.408002, -0.0923279, -0.092082, -0.0923279, -0.084412, -0.084412, -0.084412, -0.0923279])

names.append("LShoulderPitch")
times.append([0.16, 0.36, 1.36, 1.44, 1.52, 2.52, 2.68, 3.2, 3.68, 3.84, 4.44, 6.2, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([1.43466, 1.49254, -0.047596, -0.207694, -0.029188, 0.213183, 0.213183, 0.860447, 1.72264, 1.71037, 1.71344, 1.71344, 1.71344, 1.71344, 1.68591, 1.68591, 1.69656])

names.append("LShoulderRoll")
times.append([0.36, 1.36, 1.44, 1.52, 2.52, 2.6, 2.68, 3.2, 3.68, 3.76, 3.84, 4.44, 4.72, 6.2, 6.48, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([0.308291, 1.16426, 1.27584, 1.14586, 0.024502, -0.0610865, 0.022968, 1.26711, 1.26858, 1.32645, 1.18421, 1.32645, 1.15017, 1.32645, 1.15017, 0.872665, 0.780162, 1.32645, 1.32645, 1.32645])

names.append("LWristYaw")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.2, 3.68, 3.84, 4.44, 6.2, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([0.51845, 0.116542, 0.128814, 0.237728, 0.237728, 0.626573, 0.0720561, 0.0720561, 0.0735901, 0.0735901, 0.0735901, 0.0735901, 0.182588, 0.182588, 0.187106])

names.append("RAnklePitch")
times.append([0.36, 1.36, 1.52, 2.04, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([0.121228, 0.0568, 0.0568, 0.0453786, 0.0614019, 0.066004, 0.271559, 0.316046, 0.316046, 0.316046, 0.360533])

names.append("RAnkleRoll")
times.append([0.36, 1.36, 1.52, 2.04, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([0.0245859, -0.11194, -0.11194, -0.00174533, 0.04913, 0.04913, 0.029188, 0.0245859, 0.0245859, 0.0245859, 0.029188])

names.append("RElbowRoll")
times.append([0.36, 1.36, 1.44, 1.52, 2.52, 2.68, 3.68, 3.76, 3.84, 4.44, 4.72, 5.32, 5.6, 6.2, 6.48, 7.08, 7.36, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([0.081344, 1.36377, 1.54462, 1.33616, 1.52637, 1.52791, 1.30087, 1.4591, 1.30241, 0.724312, 0.610865, 1.48877, 1.54462, 0.724312, 0.610865, 1.54462, 1.54462, 0.610865, 0.411898, 1.54462, 1.54462, 1.54462])

names.append("RElbowYaw")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.2, 3.68, 3.84, 4.44, 6.2, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([1.08296, 0.24233, 0.23466, 1.48947, 1.48947, 1.5516, 0.605888, 0.694859, 0.690259, 0.690259, 0.690259, 0.690259, 0.631809, 0.631809, 0.635035])

names.append("RHand")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.84, 4.44, 6.2, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([0.816, 0.816, 0.816, 0.8156, 0.8156, 0.8156, 0.8156, 0.8168, 0.8168, 0.8168, 0.8168, 0.7356, 0.7356, 0.7368])

names.append("RHipPitch")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([0.289883, 0.418739, 0.418739, 0.15029, 0.154892, -0.340591, -0.435699, -0.438765, -0.438765, -0.532339])

names.append("RHipRoll")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([0.233209, 0.145772, 0.145772, -0.039842, -0.039842, 0.0184499, 0.019984, 0.019984, 0.019984, 0.021518])

names.append("RKneePitch")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.84, 7.08, 9.12, 9.68])
keys.append([-0.091998, -0.0923279, -0.091998, -0.0923279, -0.0923279, -0.0923279, -0.085862, -0.0889301, -0.0889301, -0.091998])

names.append("RShoulderPitch")
times.append([0.16, 0.36, 1.36, 1.52, 2.52, 2.6, 2.68, 3.2, 3.68, 3.84, 4.44, 6.2, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([1.06814, 1.15208, 0.757838, 0.80079, -0.12728, -0.207694, -0.12728, 0.755728, 1.68898, 1.67517, 1.68591, 1.68591, 1.68591, 1.68591, 1.71344, 1.71344, 1.70432])

names.append("RShoulderRoll")
times.append([0.36, 1.36, 1.44, 1.52, 2.52, 2.6, 2.68, 3.2, 3.68, 3.76, 3.84, 4.44, 5.32, 5.6, 6.2, 7.08, 7.36, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([0.237728, -0.032256, -0.1309, -0.021518, -1.126, -1.32645, -1.126, -1.32645, -1.25639, -1.32645, -1.22417, -1.32645, -1.32645, -1.2514, -1.32645, -1.32645, -1.15017, -1.32645, -1.32645, -0.872665, -0.780162, -1.32645])

names.append("RWristYaw")
times.append([0.36, 1.36, 1.52, 2.52, 2.68, 3.68, 3.84, 4.44, 6.2, 7.96, 8.24, 8.84, 9.12, 9.68])
keys.append([-0.493989, 0.941834, 0.915757, -0.211735, -0.211735, -0.181053, -0.184122, -0.182588, -0.182588, -0.182588, -0.182588, -0.0735901, -0.0735901, -0.10282])