

lista_kont = {"maja":{"haslo":532, "tempIp":"agds", "kontakty":[]}, "ewa":{"haslo":123, "tempIp":"ajds", "kontakty":[]}}

nowyLogin = "stefan"
print lista_kont.has_key(nowyLogin)


lista_kont[nowyLogin] = {}
lista_kont[nowyLogin]["haslo"] = 234
lista_kont[nowyLogin]["tempIp"] = "qjwgehjbaskdj"

lista_kont[nowyLogin]["kontakty"] = []
lista_kont[nowyLogin]["kontakty"].append("maja")
lista_kont[nowyLogin]["kontakty"].append("ewa")


print lista_kont

print lista_kont.has_key(nowyLogin)
