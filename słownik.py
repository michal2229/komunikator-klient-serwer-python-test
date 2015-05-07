lista_kont = {"maja":11, "ola":22, "ala":33}
print lista_kont
login = ''
haslo = ''
dzialaj = True
while dzialaj:
    print ("MENU:\n 1-dodaj konto\n 2-usun konto\n 3-koniec programu")
    menu = raw_input('wybierz opcje: ')
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


