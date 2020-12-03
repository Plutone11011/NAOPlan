# Choregraphe simplified export in Python.
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.84, 2, 2.8, 3.44, 4.08, 4.68, 5.64, 6.64])
keys.append([0.05058, -0.411154, -0.217869, -0.37127, 0.00149204, 0.147222, -0.227074, -0.2102])

names.append("HeadYaw")
times.append([0.84, 2, 2.8, 3.44, 4.08, 4.68, 5.64, 6.64])
keys.append([-0.0598679, -0.0445279, -0.0506639, -0.0614019, -0.289967, -0.362067, -0.0429939, -0.00924597])

"""names.append("LAnklePitch")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([-0.116626, -0.047596, 0.091998, 0.068988])

names.append("LAnkleRoll")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([-0.0827941, -0.20398, -0.171766, -0.107338])"""

names.append("LElbowRoll")
times.append([0.76, 1.92, 2.72, 3.36, 4, 4.6, 5.56, 6.56])
keys.append([-1.56004, -0.305225, -1.03541, -0.309826, -1.07683, -0.455555, -1.55237, -0.592082])

names.append("LElbowYaw")
times.append([0.76, 1.92, 2.72, 3.36, 4, 4.6, 5.56, 6.56])
keys.append([-1.00021, -0.513931, -1.08918, -0.799256, -1.18122, -0.687274, -2.07862, -1.22417])

names.append("LHand")
times.append([0.76, 1.92, 2.72, 4, 5.56, 6.56])
keys.append([0.229844, 0.174935, 0.174571, 0.174935, 0.174208, 0.232025])

"""names.append("LHipPitch")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([-0.171766, 0.440299, 0.270025, 0.205598])

names.append("LHipRoll")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([0.081344, 0.22554, 0.184122, 0.112024])

names.append("LHipYawPitch")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([-0.322099, -0.243864, -0.271475, -0.15796])

names.append("LKneePitch")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([0.452489, -0.0923461, -0.090548, -0.090548])"""

names.append("LShoulderPitch")
times.append([0.76, 1.92, 2.72, 3.36, 4, 4.6, 5.56, 6.56])
keys.append([0.765425, -1.28553, -0.721022, -1.15514, -0.417291, -1.12446, 0.97865, 1.59839])

names.append("LShoulderRoll")
times.append([0.76, 1.92, 2.72, 3.36, 4, 4.6, 5.56, 6.56])
keys.append([0.699462, 0.409536, 0.823715, 0.492371, 0.81758, 0.42641, 0.317496, 0.177901])

names.append("LWristYaw")
times.append([0.76, 1.92, 2.72, 4, 5.56, 6.56])
keys.append([0.091998, -0.038392, -0.036858, -0.314159, -0.300706, 0.0981341])

"""names.append("RAnklePitch")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([-0.095066, -0.0735901, 0.0568, 0.0690719])

names.append("RAnkleRoll")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([0.0629359, 0.196393, 0.176453, 0.066004])"""

names.append("RElbowRoll")
times.append([0.68, 1.84, 2.64, 3.28, 3.92, 4.52, 5.48, 6.48])
keys.append([1.54631, 0.388144, 1.14441, 0.415757, 1.26406, 0.526205, 1.54785, 0.440299])

names.append("RElbowYaw")
times.append([0.68, 1.84, 2.64, 3.28, 3.92, 4.52, 5.48, 6.48])
keys.append([1.48794, 0.691793, 1.12745, 0.828318, 1.35295, 0.860533, 1.90672, 1.17193])

names.append("RHand")
times.append([0.68, 1.84, 2.64, 3.92, 5.48, 6.48])
keys.append([0.40948, 0.192389, 0.192753, 0.193116, 0.192753, 0.40948])

"""names.append("RHipPitch")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([-0.168782, 0.483168, 0.303691, 0.18864])

names.append("RHipRoll")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([-0.05825, -0.240796, -0.210117, -0.067454])

names.append("RKneePitch")
times.append([0.72, 2.68, 4.56, 6.52])
keys.append([0.417291, -0.103083, -0.091998, -0.0705221])"""

names.append("RShoulderPitch")
times.append([0.68, 1.84, 2.64, 3.28, 3.92, 4.52, 5.48, 6.48])
keys.append([0.829935, -1.28085, -0.59515, -1.11671, -0.306757, -1.00013, 0.921975, 1.48189])

names.append("RShoulderRoll")
times.append([0.68, 1.84, 2.64, 3.28, 3.92, 4.52, 5.48, 6.48])
keys.append([-0.533873, -0.411154, -0.799256, -0.428028, -0.842209, -0.550747, -0.521602, -0.121228])

names.append("RWristYaw")
times.append([0.68, 1.84, 2.64, 3.92, 5.48, 6.48])
keys.append([0.185572, -0.036858, -0.032256, 0.139626, 0.147222, 0.164096])