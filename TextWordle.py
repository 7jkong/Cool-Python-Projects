# Looks hard? Read my comments to see what each line says.
# Please only change the words and references.

HiddenWord = 'EPOXY'

words = { # This dictionary prints the words. Leave lines blank if nessasary.
    'word1' : 'GHOST',
    'word2' : 'CLOUD',
    'word3' : 'PRONE',
    'word4' : 'EVOKE',
    'word5' : 'EBONY',
    'word6' : 'EPOXY'
}

textReferences = { # This dictonary contains the highlights in text after the word is printed. Leave lines blank if nessasary.
    'textReference1' : 'wwgww',
    'textReference2' : 'wwgww',
    'textReference3' : 'ywgwy',
    'textReference4' : 'gwgww',
    'textReference5' : 'gwgwg',
    'textReference6' : 'ggggg'
}

print('') # This prints a blank line.
print(f'{words["word1"]} leads to {textReferences["textReference1"]}.') # This refers to the dictionaries and prints it.
print(f'{words["word2"]} leads to {textReferences["textReference2"]}.')
print(f'{words["word3"]} leads to {textReferences["textReference3"]}.')
print(f'{words["word4"]} leads to {textReferences["textReference4"]}.')
print(f'{words["word5"]} leads to {textReferences["textReference5"]}.')
print(f'{words["word6"]} leads to {textReferences["textReference6"]}.')
print('')
print(f'The hidden word is {HiddenWord}')

# Looks complicated but it's actually easy.
