
message = 'abc a'

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
    
i = 0
for element in message:
  with open("keychain.txt") as f:
    data = f.readlines()[i]
    print(caesarize(element, int(data)))
    i = i + 1