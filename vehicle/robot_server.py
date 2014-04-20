import SocketServer
import global_vars

class MissionControlServerHandler(SocketServer.BaseRequestHandler):

  def handle(self):
    
    while True:
      self.data = self.request.recv(1024).strip()

      if self.data == None:
        break

      if not self.data: break

      print "received: " + self.data
      global_vars.thrust_port = float(self.data)
      # just send back the same data, but upper-cased


class MissionControlServer:

  def run(self):
    HOST, PORT = "0.0.0.0", 9002
    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer((HOST, PORT), MissionControlServerHandler)
    server.serve_forever()
