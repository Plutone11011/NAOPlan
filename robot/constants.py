from numpy import array

JOINT_NAMES = ['HeadYaw', 'HeadPitch', 'LShoulderPitch', 'LShoulderRoll',
               'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand',
               'LHipYawPitch', 'LHipRoll', 'LHipPitch', 'LKneePitch',
               'LAnklePitch', 'LAnkleRoll', 'RHipYawPitch', 'RHipRoll',
               'RHipPitch', 'RKneePitch', 'RAnklePitch', 'RAnkleRoll',
               'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll',
               'RWristYaw', 'RHand']

NAO_IP = '127.0.0.1'
NAO_PORT = 9559

STAND_ZERO = {'HeadPitch': array([-0.00109163, -0.00139174,  0.45948482]),
              'HeadYaw': array([-0.00109163, -0.00139174,  0.45948482]),
              'LAnklePitch': array([-0.00039695,  0.04851333,  0.04507381]),
              'LAnkleRoll': array([-0.00039695,  0.04851333,  0.04507381]),
              'LElbowRoll': array([0.10445692, 0.11235461, 0.42690966]),
              'LElbowYaw': array([0.10445692, 0.11235461, 0.42690966]),
              'LHand': array([0.21714374, 0.10625785, 0.40836954]),
              'LHipPitch': array([-0.00053316,  0.04855896,  0.24797389]),
              'LHipRoll': array([-0.00053316,  0.04855896,  0.24797389]),
              'LHipYawPitch': array([-0.00053316,  0.04855896,  0.24797389]),
              'LKneePitch': array([-0.00046603,  0.04853647,  0.14797385]),
              'LShoulderPitch': array([-2.57502601e-04,  9.65988934e-02,  4.32963312e-01]),
              'LShoulderRoll': array([-2.57502601e-04,  9.65988934e-02,  4.32963312e-01]),
              'LWristYaw': array([0.16025466, 0.10961203, 0.42382851]),
              'RAnklePitch': array([-0.00122995, -0.0514832 ,  0.04509574]),
              'RAnkleRoll': array([-0.00122995, -0.0514832 ,  0.04509574]),
              'RElbowRoll': array([ 0.10255033, -0.11688123,  0.42697448]),
              'RElbowYaw': array([ 0.10255033, -0.11688123,  0.42697448]),
              'RHand': array([ 0.21532409, -0.11259983,  0.40845495]),
              'RHipPitch': array([-0.00136616, -0.05143757,  0.24799582]),
              'RHipRoll': array([-0.00136616, -0.05143757,  0.24799582]),
              'RHipYawPitch': array([-0.00136616, -0.05143757,  0.24799582]),
              'RKneePitch': array([-0.00129903, -0.05146006,  0.14799578]),
              'RShoulderPitch': array([-0.00189019, -0.09939431,  0.43300629]),
              'RShoulderRoll': array([-0.00189019, -0.09939431,  0.43300629]),
              'RWristYaw': array([ 0.15838709, -0.11508944,  0.42390096])}
