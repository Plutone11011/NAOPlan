# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.8, 1.4, 3.4, 4.2, 5, 5.8, 6.6, 7.4, 8.2, 8.8, 9.4, 9.96, 10.64, 11.2, 11.8, 12.4, 12.96, 13.48])
keys.append([0.253073, -0.299172, 0.0453786, -0.33292, -0.0537319, 0.0698132, -0.0537319, 0.0645772, 0.302157, 0.110406, -0.012314, -0.1335, 0.0966, 0.303691, 0.207048, -0.112024, 0.191986, -0.11816])

names.append("HeadYaw")
times.append([1.4, 3.4, 4.2, 5, 5.8, 6.6, 7.4, 8.2, 8.8, 9.4, 9.96, 10.64, 11.2, 11.8, 12.4, 13.48])
keys.append([-0.055266, -0.574213, -0.046062, -0.0245859, -0.029188, -0.0245859, -0.029188, -0.151908, -0.219404, -0.165714, 0.170232, 0.4034, 0.176367, -0.14884, -0.266959, 0.257754])

names.append("LAnklePitch")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([0.233125, 0.233125, 0.145688, 0.110406, -0.10282, 0.110406, 0.049046, -0.193327, -0.259288, -0.0506639, -0.392746, -0.38661, -0.405018, -0.274628, -0.342125, 0.05058])

names.append("LAnkleRoll")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([-0.0643861, -0.0643861, -0.0705221, -0.0812601, -0.076658, -0.0812601, -0.25767, -0.408002, -0.0889301, 0.142704, 0.239346, -0.01223, -0.289883, -0.223922, -0.00302603, 0.121228])

names.append("LElbowRoll")
times.append([1.36, 3.36, 4.16, 4.56, 4.96, 5.36, 5.76, 6.16, 6.56, 6.96, 7.36, 7.76, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 12.92, 13.44])
keys.append([-0.893609, -0.872804, -0.236194, -0.818559, -0.239262, -0.506145, -0.265341, -0.818559, -0.239262, -0.506145, -0.265341, -1.17635, -1.36982, -0.88661, -0.299088, -0.858999, -1.27471, -0.084328, -0.860533, -0.262272, -0.87441, -0.233209])

names.append("LElbowYaw")
times.append([1.36, 3.36, 4.16, 4.56, 4.96, 5.36, 5.76, 6.16, 6.56, 6.96, 7.36, 7.76, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 13.44])
keys.append([-0.267035, -0.274628, -1.44047, -2.08567, -1.4466, -0.310669, -1.44047, -2.08567, -1.4466, -0.310669, -1.44047, -2.08567, -1.37297, -1.62301, -1.46808, -0.613642, -0.455639, -0.455639, -0.464844, -0.320648, -0.136484])

names.append("LHand")
times.append([1.36, 3.36, 4.16, 4.56, 4.96, 5.36, 5.76, 6.16, 6.56, 6.96, 7.36, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 13.44])
keys.append([0.8148, 0.814, 0.8148, 0.6, 0.8148, 0.6, 0.8148, 0.6, 0.8148, 0.6, 0.8148, 0.6016, 0.6032, 0.6032, 0.6032, 0.6028, 0.6028, 0.6028, 0.6044, 0.568])

names.append("LHipPitch")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([-0.196309, -0.197844, 0.023052, 0.122762, -0.358915, 0.122762, 0.084412, -0.0827941, -0.00302603, -0.00762803, -0.501576, -0.852862, -0.602819, -0.360449, -0.444818, 0.030722])

names.append("LHipRoll")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([0.023052, 0.021518, 0.04913, 0.0690719, 0.0506639, 0.0690719, 0.22554, 0.532339, 0.1335, -0.233125, -0.228525, -0.00609404, 0.504728, 0.354396, -0.059784, -0.297554])

names.append("LHipYawPitch")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([-0.223922, -0.223922, -0.210117, -0.208583, -0.222388, -0.208583, -0.147222, -0.153358, -0.130348, -0.148756, -0.145688, -0.161028, -0.162562, -0.11961, -0.124212, -0.11961])

names.append("LKneePitch")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([-0.092082, -0.0923279, -0.092082, -0.092082, 0.46476, -0.092082, -0.055266, 0.395731, 0.415673, 0.115008, 0.931096, 1.19188, 1.00013, 0.681054, 0.799172, -0.019984])

names.append("LShoulderPitch")
times.append([1.36, 3.36, 4.16, 4.96, 5.76, 6.56, 7.36, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 13.44])
keys.append([1.5585, 1.58151, 1.59072, 1.57844, 1.57998, 1.57844, 1.57998, 2.08007, 1.95428, 1.80855, 1.79167, 1.82235, 1.82081, 1.83155, 1.5631, 1.54631])

names.append("LShoulderRoll")
times.append([1.36, 3.36, 4.16, 4.56, 4.96, 5.36, 5.76, 6.16, 6.56, 6.96, 7.36, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 12.92, 13.44])
keys.append([1.02007, 0.949504, 1.02774, 0.82205, 1.1704, 1.32645, 0.793036, 0.82205, 1.1704, 1.32645, 0.793036, 0.36505, 0.381923, 0.268407, 0.74088, 1.2425, 1.15353, 1.22869, 0.352778, 0.780162, 0.177985])

names.append("LWristYaw")
times.append([1.36, 3.36, 4.16, 4.56, 4.96, 5.36, 5.76, 6.16, 6.56, 6.96, 7.36, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 13.44])
keys.append([-0.0537319, -0.046062, -0.0445279, 0.401426, -0.224006, -1.52542, -0.214801, 0.401426, -0.224006, -1.52542, -0.214801, -0.058334, -0.030722, -0.030722, -0.012314, -0.00464395, -0.00771196, 0.00609404, 0.122678, 0.023052])

names.append("RAnklePitch")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([0.253151, 0.253151, 0.162646, 0.121228, -0.0889301, 0.121228, -0.210117, 0.01078, -0.010696, -0.061318, -0.249999, -0.34971, -0.237728, 0.0568, -0.361981, -0.282215])

names.append("RAnkleRoll")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([0.0445279, 0.0445279, 0.046062, 0.0598679, 0.055266, 0.0598679, -0.15029, -0.245399, 0.055266, 0.270025, 0.326783, 0.0614019, -0.141086, -0.124212, 0.0767419, 0.214801])

names.append("RElbowRoll")
times.append([1.36, 3.36, 4.16, 4.56, 4.96, 5.36, 5.76, 6.16, 6.56, 6.96, 7.36, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 12.92, 13.44])
keys.append([0.97913, 0.289725, 0.14117, 0.506145, 0.12583, 0.818559, 0.151908, 0.506145, 0.12583, 0.818559, 0.151908, 0.29457, 0.734827, 1.04009, 0.536942, 0.067538, 0.765508, 0.271559, 0.208666, 0.780162, 0.28068])

names.append("RElbowYaw")
times.append([1.36, 3.36, 4.16, 4.56, 4.96, 5.36, 5.76, 6.16, 6.56, 6.96, 7.36, 7.76, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 13.44])
keys.append([0.417134, 0.246091, 1.67815, 0.310669, 1.66895, 2.08567, 1.66435, 0.310669, 1.66895, 2.08567, 1.66435, 2.08567, 1.40203, 1.31613, 0.733209, 0.53379, 0.561403, 0.259204, 0.039842, 0.141086, 0.325251])

names.append("RHand")
times.append([1.36, 3.36, 4.16, 4.56, 4.96, 5.36, 5.76, 6.16, 6.56, 6.96, 7.36, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 13.44])
keys.append([0.736, 0.9, 0.736, 0.5, 0.736, 0.5, 0.736, 0.5, 0.736, 0.5, 0.736, 0.5664, 0.568, 0.568, 0.5676, 0.568, 0.568, 0.5676, 0.568, 0.6036])

names.append("RHipPitch")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([-0.200996, -0.200996, 0.016832, 0.124212, -0.352862, 0.124212, -0.136568, 0.167164, 0.20398, -0.12583, -0.420357, -0.859083, -0.296104, 0.030638, -0.48632, -0.366667])

names.append("RHipRoll")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([-0.00916204, -0.00916204, -0.0291041, -0.049046, -0.033706, -0.049046, 0.14884, 0.374338, -0.00302603, -0.325165, -0.299088, -0.04291, 0.37127, 0.286901, -0.110406, -0.357381])

names.append("RKneePitch")
times.append([1.32, 3.32, 4.12, 4.92, 5.72, 6.52, 8.12, 8.72, 9.32, 9.88, 10.56, 11.12, 11.72, 12.32, 12.88, 13.4])
keys.append([-0.0923279, -0.091998, -0.087396, -0.091998, 0.458707, -0.091998, 0.440299, -0.0275701, -0.024502, 0.24088, 0.725624, 1.16588, 0.587563, -0.016832, 0.86982, 0.699545])

names.append("RShoulderPitch")
times.append([1.36, 3.36, 4.16, 4.96, 5.76, 6.56, 7.36, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 13.44])
keys.append([1.62608, 1.63375, 1.65063, 1.65216, 1.65063, 1.65216, 1.65063, 1.69665, 1.78868, 1.82397, 1.82703, 1.8209, 1.52944, 1.46041, 1.54171, 1.56771])

names.append("RShoulderRoll")
times.append([1.36, 3.36, 4.16, 4.56, 4.96, 5.36, 5.76, 6.16, 6.56, 6.96, 7.36, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 12.92, 13.44])
keys.append([-0.997141, -1.04894, -0.966462, -1.32645, -1.19043, -0.82205, -0.814596, -1.32645, -1.19043, -0.82205, -0.814596, -0.213269, -0.345191, -0.661195, -1.11833, -1.17509, -0.748635, -0.181053, -0.2102, -0.82205, -0.352778])

names.append("RWristYaw")
times.append([1.36, 3.36, 4.16, 4.56, 4.96, 5.36, 5.76, 6.16, 6.56, 6.96, 7.36, 8.16, 8.76, 9.36, 9.92, 10.6, 11.16, 11.76, 12.36, 13.44])
keys.append([0.0663225, 0.0837758, 0.122173, 1.52542, 0.12728, -0.401426, 0.151824, 1.52542, 0.12728, -0.401426, 0.151824, 0.185572, 0.182504, 0.18097, -0.0521979, -0.027654, -0.029188, -0.032256, 0.00916204, -0.113474])