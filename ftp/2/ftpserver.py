from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("admin", "586290929699", "home", perm="elradfmw")
authorizer.add_anonymous("home/anonymous", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()