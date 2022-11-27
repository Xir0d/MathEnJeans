def count_letters(word):
    return len(word) - word.count(' ')

word = 'test'
print(count_letters(word))