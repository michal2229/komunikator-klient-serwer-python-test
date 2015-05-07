import select
import socket
import sys
import Queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

# Sockets from which we expect to read
inputs = [ server ]

# Sockets to which we expect to write
outputs = [ ]

# Outgoing message queues (socket:Queue)
message_queues = {}

lista_kont = {}
lista_zalogowanych = []
komunikat = ""


lista_kont = {"maja":{"haslo":"777", "tempIp":None, "kontakty":[]}, "ewa":{"haslo":"777", "tempIp":None, "kontakty":[]}}


def dodajKonto(login, haslo):
    if lista_kont.has_key(login):
        return False
    else:
        lista_kont[login] = {}
        lista_kont[login]["haslo"] = haslo
        lista_kont[login]["tempIp"] = None
        lista_kont[login]["kontakty"] = []
        return True

def usunKonto(login, haslo):
    if lista_kont.has_key(login):
        if lista_kont[login]["haslo"] == haslo:
            del lista_kont[login]
            return True
        else:
            print "Niepoprawne haslo"
            return False
    else:
        print "Konto nie istnieje"
        return False

def sprawdzDaneLogowania(login, haslo):
    if lista_kont.has_key(login):
        if lista_kont[login]["haslo"] == haslo:
            return True
        else:
            return False
    else:
        return False


while inputs:

    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, '\nwaiting for the next event'
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    # Handle inputs
    for s in readable:

        if s is server:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            print >>sys.stderr, 'new connection from', client_address
            connection.setblocking(0)
            inputs.append(connection)

            # Give the connection a queue for data we want to send
            message_queues[connection] = Queue.Queue()

        else:
            data = s.recv(1024) # odczyt wiadomosci z klienta
            if data:
                komunikat = "domyslny komunikat, czyli cos jest nie tak"

                komenda = data.split(":")
                print "komenda = " + komenda[0]

                if komenda[0] == "zaloguj":
                    dane_komendy = komenda[1].split(";")
                    
                    if sprawdzDaneLogowania(dane_komendy[0], dane_komendy[1]):
                        lista_kont[dane_komendy[0]]["tempIp"] = s
                        lista_zalogowanych.append(dane_komendy[0])
                        komunikat = "zalogowano"
                    else:
                        komunikat =  "bledne dane logowania"
                        
                    
                    print "logowanie"
                    


                    
                elif komenda[0] == "wyloguj":
                    print "wylogowanie"
                    dane_komendy = komenda[1].split(";")
                    
                    if dane_komendy[0] in lista_zalogowanych:
                        lista_kont[dane_komendy[0]]["tempIp"] = None
                        lista_zalogowanych.remove(dane_komendy[0])
                        komunikat = "wylogowano"
                    else:
                        komunikat =  "bledne dane logowania"


                    
                elif komenda[0] == "dodajKonto":
                    dane_komendy = komenda[1].split(";")
                    
                    if dodajKonto(dane_komendy[0], dane_komendy[1]):
                        komunikat = "dodano konto"
                    else:
                        komunikat = "blad podczas dodawania konta"
                    print lista_kont
                    


                    
                elif komenda[0] == "usunKonto":
                    dane_komendy = komenda[1].split(";")
                    
                    if usunKonto(dane_komendy[0], dane_komendy[1]):
                        komunikat = "usunieto konto"
                    else:
                        komunikat = "blad podczas usuwania konta"
                    print lista_kont


                    
                elif komenda[0] == "dodajKontakt":
                    print "dodanie kontaktu"



                    
                elif komenda[0] == "usunKontakt":
                    print "usuwanie kontaktu"



                    
                elif komenda[0] == "wyslijWiadomosc":
                    dane_komendy = komenda[1].split(";")
                    
                    if dane_komendy[0] in lista_zalogowanych:
                        message_queues[ lista_kont[dane_komendy[0]]["tempIp"]].put(dane_komendy[1])
                        komunikat = "wiadomosc wyslano"
                    else:
                        komunikat =  "uzytkownik " + dane_komendy[0] + " nie jest zalogowany"
                    


                    
                elif komenda[0] == "pobierzKontakty":
                    print "pobieranie kontkatow"



                    
                elif komenda[0] == "sprawdzZnajmosc":
                    print "sprawdzanie"

                elif komenda[0] == "odpytanie":
                    komunikat = " "

                    
                else:
                    komunikat = "nie ma takiej komendy"


                print lista_kont
           
                print >>sys.stderr, 'received "%s" from %s' % (data, s.getpeername())
                message_queues[s].put(komunikat) #message_queues[s].put(data) # odpowiedz na zapytanie
                # Add output channel for response


                
                if s not in outputs:
                    outputs.append(s)








            else:
                # Interpret empty result as closed connection
                print >>sys.stderr, 'closing', client_address, 'after reading no data'
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # Remove message queue
                del message_queues[s]

                # Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            # No messages waiting so stop checking for writability.
            print >>sys.stderr, 'output queue for', s.getpeername(), 'is empty'
            outputs.remove(s)
        else:
            print >>sys.stderr, 'sending "%s" to %s' % (next_msg, s.getpeername())
            s.send(next_msg)

    # Handle "exceptional conditions"
    for s in exceptional:
        print >>sys.stderr, 'handling exceptional condition for', s.getpeername()
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove message queue
        del message_queues[s]


        
