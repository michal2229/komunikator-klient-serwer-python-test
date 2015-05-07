lista_kontaktow = ["maja", "ola"] 
kontakt = ''

def dodaj_kontakt(kontakt):
    return lista_kontaktow.append(kontakt)
def usun_kontakt():
    return lista_kontaktow.remove(kontakt)


dzialaj = True
while dzialaj:
    print ("MENU:\n 1-dodaj kontakt\n 2-usun kontakt\n 3-koniec programu")
    menu = raw_input('wybierz opcje: ')
    if menu == '1':
        dodaj_kontakt(kontakt=raw_input('dodaj kontakt: '))
        print lista_kontaktow
    elif menu == '2':
        print lista_kontaktow
        kontakt = str(raw_input('Ktory kontakt chcesz usunac?: '))
        if kontakt in lista_kontaktow:
            usun_kontakt()
            print lista_kontaktow
        else:
            print(kontakt,"nie ma na liscie")
    elif menu == '3':
        dzialaj = False
    else:
        print("zla opcja")
    
input("\n\nAby zakonczyc program, nacisnij enter")
