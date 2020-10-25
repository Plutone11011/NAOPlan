from naoqi import ALProxy
from qi import Session
from robot.constants import JOINT_NAMES, NAO_PORT, NAO_IP
from robot.search import NaoNode, NaoState, NaoProblem, StandZero

if __name__ == "__main__":

    motion_proxy = ALProxy("ALMotion", NAO_IP, NAO_PORT)

    session = Session()
    try:
        session.connect("tcp://" + NAO_IP + ":" + str(NAO_PORT))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + NAO_IP + "\" on port " + str(NAO_PORT) + ".\n")

    #first_state = NaoState(motion_proxy)
    # for name in JOINT_NAMES:
    #    print first_state.get_joint_coordinate(name)

    posture_service = session.service("ALRobotPosture")
    posture_service.goToPosture("StandInit", 1.0)
    second_state = NaoState(motion_proxy)
    #problem = NaoProblem(first_state, second_state)
    #print problem.h(first_state)
    # for name in JOINT_NAMES:
    #    print second_state.get_joint_coordinate(name)

