from RobotManager import RobotManager


def main():
    robotManager = RobotManager()
    #planManager = PlanManager()
    print("Inititiating robot")
    robotManager.robotConnect()
    robotManager.initRobot()
    robotManager.planning()
    robotManager.onFinish()

if __name__=='__main__':
    main()
    #first_state = NaoState(motion_proxy)
    # for name in JOINT_NAMES:
    #    print first_state.get_joint_coordinate(name)


    #problem = NaoProblem(first_state, second_state)
    #print problem.h(first_state)
    # for name in JOINT_NAMES:
    #    print second_state.get_joint_coordinate(name)
