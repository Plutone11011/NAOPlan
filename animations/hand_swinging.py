# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.64, 1.6, 2.6, 3.56])
keys.append([-0.30224, -0.30224, -0.30224, -0.30224])

names.append("HeadYaw")
times.append([0.64, 1.6, 2.6, 3.56])
keys.append([-0.621227, 0.621227, -0.621227, 0.621227])

names.append("LAnklePitch")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([0.207694, 0.162052, 0.207694, 0.162052])

names.append("LAnkleRoll")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([0.00437015, -0.0927629, 0.00437015, -0.0927629])

names.append("LElbowRoll")
times.append([0.68, 1.16, 1.64, 2.12, 2.64, 3.12, 3.6, 4.08])
keys.append([-0.628982, -0.43263, -0.0183661, -0.601287, -0.628982, -0.43263, -0.0183661, -0.601287])

names.append("LElbowYaw")
times.append([0.68, 1.16, 1.64, 2.12, 2.64, 3.12, 3.6, 4.08])
keys.append([-0.369652, -0.575208, -0.213269, -0.538476, -0.369652, -0.575208, -0.213269, -0.538476])

names.append("LHand")
times.append([0.6, 1.36, 1.56, 2.32, 2.56, 3.32, 3.52, 4.28])
keys.append([0.811297, 0.81166, 0.577479, 0.577843, 0.811297, 0.81166, 0.577479, 0.577843])

names.append("LHipPitch")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([-0.354607, -0.400345, -0.354607, -0.400345])

names.append("LHipRoll")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([-0.18615, 0.0119179, -0.18615, 0.0119179])

names.append("LHipYawPitch")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([-0.506179, -0.506179, -0.506179, -0.506179])

names.append("LKneePitch")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([0.0538045, 0.0591916, 0.0538045, 0.0591916])

names.append("LShoulderPitch")
times.append([0.68, 1.16, 1.64, 2.12, 2.64, 3.12, 3.6, 4.08])
keys.append([0.823801, 0.987938, 0.88661, 1.03081, 0.823801, 0.987938, 0.88661, 1.03081])

names.append("LShoulderRoll")
times.append([0.68, 1.16, 1.64, 2.12, 2.64, 3.12, 3.6, 4.08])
keys.append([0.019984, 0.242414, 0.863599, 0.358915, 0.019984, 0.242414, 0.863599, 0.358915])

names.append("LWristYaw")
times.append([0.6, 1.36, 1.56, 2.32, 2.56, 3.32, 3.52, 4.28])
keys.append([0.0445279, 0.0414599, -0.372804, -0.374338, 0.0445279, 0.0414599, -0.372804, -0.374338])

names.append("RAnklePitch")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([0.162052, 0.207694, 0.162052, 0.207694])

names.append("RAnkleRoll")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([0.0927629, -0.00437015, 0.0927629, -0.00437015])

names.append("RElbowRoll")
times.append([0.04, 0.68, 1.16, 1.64, 2.12, 2.64, 3.12, 3.6, 4.08, 4.6])
keys.append([0.527739, 0.0183661, 0.601287, 0.628982, 0.43263, 0.0183661, 0.601287, 0.628982, 0.43263, 0.527739])

names.append("RElbowYaw")
times.append([0.04, 0.68, 1.16, 1.64, 2.12, 2.64, 3.12, 3.6, 4.08, 4.6])
keys.append([2.0856, 0.213269, 0.538476, 0.369652, 0.575208, 0.213269, 0.538476, 0.369652, 0.575208, 2.0856])

names.append("RHand")
times.append([0.6, 1.36, 1.56, 2.32, 2.56, 3.32, 3.52, 4.28])
keys.append([0.577479, 0.577843, 0.811297, 0.81166, 0.577479, 0.577843, 0.811297, 0.81166])

names.append("RHipPitch")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([-0.400345, -0.354607, -0.400345, -0.354607])

names.append("RHipRoll")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([-0.0119179, 0.18615, -0.0119179, 0.18615])

names.append("RKneePitch")
times.append([0.72, 1.68, 2.68, 3.64])
keys.append([0.0591916, 0.0538045, 0.0591916, 0.0538045])

names.append("RShoulderPitch")
times.append([0.04, 0.68, 1.16, 1.64, 2.12, 2.64, 3.12, 3.6, 4.08, 4.6])
keys.append([1.01095, 0.88661, 1.03081, 0.823801, 0.987938, 0.88661, 1.03081, 0.823801, 0.987938, 1.01095])

names.append("RShoulderRoll")
times.append([0.04, 0.68, 1.16, 1.64, 2.12, 2.64, 3.12, 3.6, 4.08, 4.6])
keys.append([-0.17185, -0.863599, -0.358915, -0.019984, -0.242414, -0.863599, -0.358915, -0.019984, -0.242414, -0.17185])

names.append("RWristYaw")
times.append([0.6, 1.36, 1.56, 2.32, 2.56, 3.32, 3.52, 4.28])
keys.append([0.372804, 0.374338, -0.0445279, -0.0414599, 0.372804, 0.374338, -0.0445279, -0.0414599])