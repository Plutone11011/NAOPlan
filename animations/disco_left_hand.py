# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.52, 1.32, 2.24, 3.04, 3.88, 4.68, 5.56, 6.36, 7.68])
keys.append([-0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.17185])

names.append("HeadYaw")
times.append([0.52, 1.32, 2.24, 3.04, 3.88, 4.68, 5.56, 6.36, 7.68])
keys.append([0.745256, -0.289725, 0.745256, -0.289725, 0.745256, -0.289725, 0.745256, -0.289725, 0.00916195])

names.append("LAnklePitch")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([0.092082, 0.082878, 0.092082, 0.082878, 0.092082, 0.082878, 0.092082, 0.082878, 0.0873961])

names.append("LAnkleRoll")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([-0.26389, 0.0904641, -0.26389, 0.0904641, -0.26389, 0.0904641, -0.26389, 0.0904641, -0.121144])

names.append("LElbowRoll")
times.append([0, 0.6, 1, 1.4, 1.88, 2.32, 2.72, 3.12, 3.6, 3.96, 4.36, 4.76, 5.24, 5.64, 6.04, 6.44, 6.92, 7.76])
keys.append([-1.54462, -0.138102, -1.309, -0.257754, -1.4591, -0.138102, -1.309, -0.257754, -1.4591, -0.138102, -1.309, -0.257754, -1.4591, -0.138102, -1.309, -0.257754, -1.4591, -0.424876])

names.append("LElbowYaw")
times.append([0, 0.6, 1, 1.4, 1.88, 2.32, 2.72, 3.12, 3.6, 3.96, 4.36, 4.76, 5.24, 5.64, 6.04, 6.44, 6.92, 7.76])
keys.append([-1.65632, 0.851412, 0.0750492, 0.00157596, 0.460767, 0.851412, 0.0750492, 0.00157596, 0.460767, 0.851412, 0.0750492, 0.00157596, 0.460767, 0.851412, 0.0750492, 0.00157596, -0.682424, -1.21037])

names.append("LHand")
times.append([0, 0.6, 1, 1.4, 1.88, 2.32, 2.72, 3.12, 3.6, 3.96, 4.36, 4.76, 5.24, 5.64, 6.04, 6.44, 6.92, 7.76])
keys.append([0.13, 0.678, 0.3, 0.6784, 0.3, 0.678, 0.3, 0.6784, 0.3, 0.678, 0.3, 0.6784, 0.3, 0.678, 0.3, 0.6784, 0.3, 0.2968])

names.append("LHipPitch")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([0.101202, 0.259204, 0.101202, 0.259204, 0.101202, 0.259204, 0.101202, 0.259204, 0.139636])

names.append("LHipRoll")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([0.297554, -0.14117, 0.297554, -0.14117, 0.297554, -0.14117, 0.297554, -0.14117, 0.10282])

names.append("LHipYawPitch")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([-0.37272, -0.357381, -0.37272, -0.357381, -0.37272, -0.357381, -0.37272, -0.357381, -0.170232])

names.append("LKneePitch")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([-0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0782759])

names.append("LShoulderPitch")
times.append([0, 0.6, 1.4, 2.32, 3.12, 3.96, 4.76, 5.64, 6.44, 7.24, 7.76])
keys.append([1.21475, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, 1.06465, 1.47106])

names.append("LShoulderRoll")
times.append([0, 0.6, 1, 1.4, 1.88, 2.32, 2.72, 3.12, 3.6, 3.96, 4.36, 4.76, 5.24, 5.64, 6.04, 6.44, 6.92, 7.76])
keys.append([0.165806, 0.328317, 0.595157, -0.314159, 0.595157, 0.328317, 0.595157, -0.314159, 0.595157, 0.328317, 0.595157, -0.314159, 0.595157, 0.328317, 0.595157, -0.314159, 0.595157, 0.153358])

names.append("LWristYaw")
times.append([0.6, 1.4, 2.32, 3.12, 3.96, 4.76, 5.64, 6.44, 7.76])
keys.append([-0.107338, -0.400331, -0.107338, -0.400331, -0.107338, -0.400331, -0.107338, -0.400331, 0.0827939])

names.append("RAnklePitch")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([0.0444441, 0.161028, 0.0444441, 0.161028, 0.0444441, 0.161028, 0.0444441, 0.161028, 0.093616])

names.append("RAnkleRoll")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([-0.062936, 0.248467, -0.062936, 0.248467, -0.062936, 0.248467, -0.062936, 0.248467, 0.119694])

names.append("RElbowRoll")
times.append([0, 0.52, 1.32, 2.24, 3.04, 3.88, 4.68, 5.56, 6.36, 6.96, 7.28, 7.68])
keys.append([1.54462, 0.369652, 0.202446, 0.369652, 0.202446, 0.369652, 0.202446, 0.369652, 0.202446, 0.82205, 0.886627, 0.429562])

names.append("RElbowYaw")
times.append([0, 0.52, 1.32, 2.24, 3.04, 3.88, 4.68, 5.56, 6.36, 6.96, 7.28, 7.68])
keys.append([1.65632, 0.380475, 0.618244, 0.380475, 0.618244, 0.380475, 0.618244, 0.380475, 0.618244, 1.57952, 1.03323, 1.21028])

names.append("RHand")
times.append([0, 0.52, 1.32, 2.24, 3.04, 3.88, 4.68, 5.56, 6.36, 7.28, 7.68])
keys.append([0.13, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.24, 0.2976])

names.append("RHipPitch")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([0.185656, 0.147306, 0.185656, 0.147306, 0.185656, 0.147306, 0.185656, 0.147306, 0.131882])

names.append("RHipRoll")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([0.144154, -0.329852, 0.144154, -0.329852, 0.144154, -0.329852, 0.144154, -0.329852, -0.0966001])

names.append("RHipYawPitch")
times.append([0.44, 2.16, 3.8, 5.48, 7.6])
keys.append([-0.37272, -0.37272, -0.37272, -0.37272, -0.170232])

names.append("RKneePitch")
times.append([0.44, 1.24, 2.16, 2.96, 3.8, 4.6, 5.48, 6.28, 7.6])
keys.append([-0.090548, -0.0798099, -0.090548, -0.0798099, -0.090548, -0.0798099, -0.090548, -0.0798099, -0.091998])

names.append("RShoulderPitch")
times.append([0, 0.52, 1.32, 2.24, 3.04, 3.88, 4.68, 5.56, 6.36, 7.28, 7.68])
keys.append([1.21475, 1.74718, 1.85611, 1.74718, 1.85611, 1.74718, 1.85611, 1.74718, 1.85611, 1.18508, 1.47268])

names.append("RShoulderRoll")
times.append([0, 0.52, 1.32, 2.24, 3.04, 3.88, 4.68, 5.56, 6.36, 6.96, 7.68])
keys.append([-0.165806, -0.24233, -0.196309, -0.24233, -0.196309, -0.24233, -0.196309, -0.24233, -0.196309, -0.455531, -0.16418])

names.append("RWristYaw")
times.append([0.52, 1.32, 2.24, 3.04, 3.88, 4.68, 5.56, 6.36, 7.68])
keys.append([0.395814, 0.420357, 0.395814, 0.420357, 0.395814, 0.420357, 0.395814, 0.420357, 0.108872])