import socket
import sys
import msvcrt
import time

messages = [ 'This is the message. ',
             'It will be sent ',
             'in parts.',
             ]
server_address = ('localhost', 10000)

# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          ]

# Connect the socket to the port where the server is listening
print >>sys.stderr, 'connecting to %s port %s' % server_address
for s in socks:
    s.connect(server_address)


   
      


login = ''
haslo = ''
dzialaj = True
print ("MENU:\n 1-dodaj konto\n 2-usun konto\n 3-koniec programu")
while dzialaj:
    
    time.sleep(1)
    
    for s in socks:
        s.send("odpytanie:odpytanie")
    for s in socks:
        data = s.recv(1024)
    if data != " ":
        print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)


                
    '''message = raw_input("wpisz wiadomosc")
    # Send messages on both sockets
    if message:
        for s in socks:
            print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
            s.send(message)'''

    '''for s in socks:
        data = s.recv(1024)
        print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
        if not data:
            #print >>sys.stderr, 'closing socket', s.getsockname()
            s.close()'''

    x = msvcrt.kbhit()
    if x: 
        print ord(msvcrt.getch())

        #menu = 0      
        print ("MENU:\n 1-dodaj konto\n 2-usun konto\n 3-koniec programu")
        menu = raw_input('wybierz opcje: ')

        
        if menu == '0':
            message = raw_input("wpisz wiadomosc asdf")
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

                
        if menu == '1':
            print("Dodaj konto do srwera")
            login = raw_input('Podaj login: ')
            if lista_kont.has_key(login):
                print ('podany login juz istnieje')
            else:
                haslo = raw_input('Dodaj haslo: ')
                lista_kont[login]=haslo
                print lista_kont

                
        elif menu == '2':
            login = str(raw_input('Ktore konto chcesz usunac?: '))
            if lista_kont.has_key(login):
                haslo = raw_input('Podaj haslo: ')
                if lista_kont[login]==haslo:
                    del lista_kont[login]
                    print lista_kont
                else:
                    print ("zle haslo")
            else:
                print(login,"nie istnieje")

                
        elif menu == '3':
            dzialaj = False
        else:
            print("zla opcja")
        
input("\n\nAby zakonczyc program, nacisnij enter")





'''
    message = raw_input("wpisz wiadomosc")
    # Send messages on both sockets
    if message:
        for s in socks:
            print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
            s.send(message)

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
        if not data:
            print >>sys.stderr, 'closing socket', s.getsockname()
            s.close()

          '''  
