from robot_server import MissionControlServer
import time
import threading
import global_vars

class Robot:

  global thrust_port
  def run(self):

    mc = MissionControlServer()
    
    mc_thread = threading.Thread(target=mc.run)	
    mc_thread.daemon = True
    mc_thread.start()
  
    while True:
      print "Data = %.2f" % global_vars.thrust_port
      time.sleep(1)

if __name__=="__main__":
  robot = Robot()
  robot.run()
