from naoqi import ALProxy
from qi import Session
# rest of setup code...

if __name__ == "__main__":
    motion_proxy = ALProxy("ALMotion", "127.0.0.1", 9559)
    print motion_proxy.getBodyNames("Body")
    distance_differences = {}
    for name in motion_proxy.getBodyNames("Body"):
        distance_differences.setdefault(name, motion_proxy.getPosition(name, 1, True)[:3])


    session = Session()
    try:
        session.connect("tcp://127.0.0.1:" + str(9559))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + "127.0.0.1" + "\" on port " + str(9559) + ".\n")

    # normally would have to create posture service
    posture_service = session.service("ALRobotPosture")
    posture_service.goToPosture("StandZero", 1.0)

    for name in motion_proxy.getBodyNames("Body"):
        distance_differences[name] = motion_proxy.getPosition(name, 1, True)[:3]

    for name, val in distance_differences.items():
        if val != 0:
            print name

