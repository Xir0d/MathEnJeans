import string

message_chiffre_import = open('message chiffre.txt', 'r')
message_chiffre = message_chiffre_import.readlines()

#Décalage des lettres selon la liste établie précedemment

def caesarize_letter(letter, shift):            
    if 'A' <= letter.upper() <= 'Z':
        start = ord('a') if letter.islower() else ord('A')
        return chr((ord(letter) - start + shift) % 26 + start)
    else:
        return letter

def caesarize(text, shift):
    return ''.join([caesarize_letter(letter, shift) for letter in text])

def uncaesarize(text, shift):
    return ''.join([caesarize_letter(letter, -1 * shift) for letter in text])

message_dechiffre = ''
i = 0
for element in message_chiffre:
  with open("keychain.txt") as f:
    data = f.readlines()[i]
    decalage = str(26 - data)
    message_dechiffre = message_dechiffre + (caesarize(element, int(data)))
    i = i + 1
print(message_dechiffre)
print(data)

#Pour recoder le mesage de base: decaler lel message de 26 lettres (26) - le decalage initiale de la lettre

