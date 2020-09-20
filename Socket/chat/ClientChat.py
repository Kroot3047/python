import socket, sys

HOST = '127.0.0.1'
PORT = 2013

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mySocket.connect((HOST, PORT))
except socket.error:
	print("La connexion a echoue.")
	sys.exit()

print("Connexion etablie avec le serveur.")

msgServeur = mySocket.recv(1024).decode("Utf8")

while 1:
	if msgServeur.upper() == "FIN" or msgServeur =="":
		break
	print("Serveur>", msgServeur)
	msgClient = input("Client> ")
	mySocket.send(msgClient.encode("Utf8"))
	msgServeur = mySocket.recv(1024).decode("Utf8")

print("Connexion interrompue.")
mySocket.close()