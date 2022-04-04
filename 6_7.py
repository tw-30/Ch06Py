words = input("Enter a sentence: " ).lower()

letter_count = dict()

for l in words:
    if l != " ":
        if l in letter_count:
            letter_count[l] += 1
        else:
            letter_count[l] = 1

print('Letter\tCount')
for l in sorted(letter_count.keys()):
    print('{}\t\t{}'.format(l,letter_count[l]))

alphabet = set('abcdefghijklmnopqrstuvqxyz')

alphabet_not_in_text = alphabet.difference(letter_count.keys())
print("Alphabet not in the text are", alphabet_not_in_text)