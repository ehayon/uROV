import SocketServer
import time
import threading

global_var = "Test"

class MCHandler(SocketServer.BaseRequestHandler):

  def handle(self):
    global global_var 

    while True:
      self.data = self.request.recv(1024).strip()

      if self.data == None:
        break

      global_var = self.data
      # just send back the same data, but upper-cased
      self.request.sendall(self.data.upper())
    

class ThrusterController:

  global global_var
  def run(self):
    while True:
      print(global_var)
      time.sleep(0.1)

if __name__ == "__main__":
  HOST, PORT = "0.0.0.0", 9999

  SocketServer.TCPServer.allow_reuse_address = True

  server = SocketServer.TCPServer((HOST, PORT), MCHandler)

  server_thread = threading.Thread(target=server.serve_forever)
  server_thread.daemon = True
  server_thread.start()

  thruster_controller = ThrusterController()
  
  tc_thread = threading.Thread(target=thruster_controller.run) 
  tc_thread.daemon = True
  tc_thread.start()

  while True:
    time.sleep(1)
