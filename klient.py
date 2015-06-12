import socket
import sys
import time
import select

server_address = ('localhost', 8036)

# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          ]

# Connect the socket to the port where the server is listening
print >>sys.stderr, 'connecting to %s port %s' % server_address
for s in socks:
    s.connect(server_address)


   
      


login = ''
haslo = ''
lista_znajomych = []

print ("MENU:\n 1-dodaj konto\n 2-usun konto\n 3-zaloguj\n 4-wyloguj\n 5-dodaj kontakt\n 7-wyslij wiadomosc\n 8-pobierz liste zalogowanych\n 6-pobierz liste znajomych \n 9 - koniec\n \nwybierz opcje:")

dzialaj = True

while dzialaj:
    
    time.sleep(1)
    
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            non_blocking_input = sys.stdin.readline() # wyswietla to co wpisalam tutaj numer opcji z menu 
            print("Wybralas opcje: {}".format(non_blocking_input))
                
            if non_blocking_input.startswith('1'):
                print("Dodaj konto do srwera")
                login = raw_input('Podaj login: ')
                haslo = raw_input('Dodaj haslo: ')

                message = "dodajKonto:"+login+";"+haslo # generowanie zapytania do serwera

                # Send messages on both sockets
                if message:
                    for s in socks:
                        print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
                        s.send(message)
                for s in socks:
                    data = s.recv(1024)
                print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
                if not data:
                    #print >>sys.stderr, 'closing socket', s.getsockname()
                    s.close()
                
            elif non_blocking_input.startswith('2'):
                print("usuwanie konta z serwera")
                login = raw_input('Podaj login: ')
                haslo = raw_input('Dodaj haslo: ')

                message = "usunKonto:"+login+";"+haslo
                if message:
                    for s in socks:
                        print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
                        s.send(message)
                for s in socks:
                    data = s.recv(1024)
                print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
                if not data:
                    #print >>sys.stderr, 'closing socket', s.getsockname()
                    s.close()

            elif non_blocking_input.startswith('3'):
                print("logowanie do serwera")
                login = raw_input('Podaj login: ')
                haslo = raw_input('Dodaj haslo: ')

                message = "zaloguj:"+login+";"+haslo
                if message:
                    for s in socks:
                        print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
                        s.send(message)
                for s in socks:
                    data = s.recv(1024)
                print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
                if not data:
                    #print >>sys.stderr, 'closing socket', s.getsockname()
                    s.close()

            elif non_blocking_input.startswith('4'):
                print("wylogowanie")
                login = raw_input('Podaj login: ')
                haslo = raw_input('Dodaj haslo: ')

                message = "wyloguj:"+login+";"+haslo
                if message:
                    for s in socks:
                        print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
                        s.send(message)
                for s in socks:
                    data = s.recv(1024)
                print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
                if not data:
                    #print >>sys.stderr, 'closing socket', s.getsockname()
                    s.close()

            elif non_blocking_input.startswith('5'):
                print("dodaj znajomego")
                login = raw_input('Podaj login: ')
                loginZnajomego = raw_input('Podaj login znajomego: ')
                
                
                message = "dodajKontakt:"+login+";"+loginZnajomego
                if message:
                    for s in socks:
                        print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
                        s.send(message)
                for s in socks:
                    data = s.recv(1024)
                print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
                if not data:
                    #print >>sys.stderr, 'closing socket', s.getsockname()
                    s.close()

        
        
            elif non_blocking_input.startswith('7'):
                print("wysylanie wiadomosci")
                login0 = raw_input('Podaj swoj login: ')
                login = raw_input('Podaj login do ktorego chcesz wyslac wiadomosc: ')
                wiadomosc = raw_input('wiadomosc: ')

                message = "wyslijWiadomosc:"+login0+"."+login+";"+wiadomosc
                if message:
                    for s in socks:
                        print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
                        s.send(message)
                for s in socks:
                    data = s.recv(1024)
                print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
                if not data:
                    #print >>sys.stderr, 'closing socket', s.getsockname()
                    s.close()

            elif non_blocking_input.startswith('8'):
                message = "pobierzListe:"
                if message:
                    for s in socks:
                        print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
                        s.send(message)
                for s in socks:
                    data = s.recv(1024)
                print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
                if not data:
                    #print >>sys.stderr, 'closing socket', s.getsockname()
                    s.close()

            elif non_blocking_input.startswith('6'):
                login = raw_input('Podaj login: ')
                message = "pobierzKontakty:"+login
                if message:
                    for s in socks:
                        print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
                        s.send(message)
                for s in socks:
                    data = s.recv(1024)
                print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
                if not data:
                    #print >>sys.stderr, 'closing socket', s.getsockname()
                    s.close()
        
            elif non_blocking_input.startswith('9'):
                dzialaj = False
            else:
                print("zla opcja")
  
    
    
    
            
	print ("MENU:\n 1-dodaj konto\n 2-usun konto\n 3-zaloguj\n 4-wyloguj\n 5-dodaj kontakt\n 7-wyslij wiadomosc\n 8-pobierz liste zalogowanych\n 6-pobierz liste znajomych \n 9 - koniec\n \nwybierz opcje:")
        






