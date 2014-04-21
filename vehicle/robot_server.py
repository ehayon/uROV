import SocketServer
import global_vars

class MissionControlServerHandler(SocketServer.BaseRequestHandler):

  def handle(self):
    
    while True:
      self.data = self.request.recv(1024).strip()

      if self.data == None:
        break

      if not self.data: break

      cmd = self.data.split()
      if cmd[0] == '/set_thrust':
        global_vars.thrust['port'] = float(cmd[1].split(',')[0])
        global_vars.thrust['starboard'] = float(cmd[1].split(',')[1])
        global_vars.thrust['heave_bow'] = float(cmd[1].split(',')[2])
        global_vars.thrust['heave_stern'] = float(cmd[1].split(',')[3])
        print "Updated thrust vector to [%s]" % cmd[1]
      # global_vars.thrust_port = float(self.data)
      # just send back the same data, but upper-cased


class MissionControlServer:

  def run(self):
    HOST, PORT = "0.0.0.0", 9002
    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer((HOST, PORT), MissionControlServerHandler)
    server.serve_forever()
