import socket, sys

HOST = '127.0.0.1'
PORT = 2013
counter = 0

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mySocket.bind((HOST, PORT))
except socket.error:
	print("La liaison du socket a l adresse choisie a achoua.")
	sys.exit

while 1:
	print("Serveur pret, en attente de requetes ...")
	mySocket.listen(2)

	connexion, adresse = mySocket.accept()
	counter +=1
	print("Client connecte, adresse IP %s, port %s" % (adresse[0], adresse[1]))

	msgServeur ="Vous etes connecte au serveur Marcel. Envoyez vos messages."
	connexion.send(msgServeur.encode("Utf8"))
	msgClient = connexion.recv(1024).decode("Utf8")
	while 1:
		print("Client>", msgClient)
		if msgClient.upper() == "FIN" or msgClient =="":
			break
		msgServeur = input("Serveur> ")
		connexion.send(msgServeur.encode("Utf8"))
		msgClient = connexion.recv(1024).decode("Utf8")

	connexion.send("fin".encode("Utf8"))
	print("Connexion interrompue.")
	connexion.close()
	ch = input("<R>ecommencer <T>erminer ? ")
	if ch.upper() =='T':
		break
