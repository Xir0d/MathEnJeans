import string

message_chiffre = input('Message à décoder: ')


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
    data =  int(data)
    data = -data
    message_dechiffre = str(message_dechiffre) + (caesarize(element, data))
    i = i + 1
print('\033[92mVoici le message déchiffré: ' + '\033[93m' + message_dechiffre + '\033[0m')
