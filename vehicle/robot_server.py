import SocketServer

class MissionControlServerHandler(SocketServer.BaseRequestHandler):

  def handler(self):
    self.data = self.request.recv(1024).strip()
    print "{} wrote:".format(self.client_address[0])
    print self.data
    self.request.sendall((self.data.upper()))

class MissionControlServer:

  def run(self):
    HOST, PORT = "127.0.0.1", 9000

    server = SocketServer.TCPServer((HOST, PORT), MissionControlServerHandler)
    server.serve_forever()
