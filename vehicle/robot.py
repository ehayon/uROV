from robot_server import MissionControlServer

class Robot:

  def run(self):
    print("Running vehicle code")
    mc = MissionControlServer()
    mc.run()
    print "test.."
  
