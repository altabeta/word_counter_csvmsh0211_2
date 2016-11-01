import re
import collections
starterText = open('dark.txt', 'r').read()
changedText = re.sub(r'[;:,\.\(\)\'\"\?\!\-\n]', ' ', starterText)
changedText = changedText.lower()
splittedWords = re.split(r' ', changedText)
splittedWords = [x for x in splittedWords if x != '']
commonWords = collections.Counter(splittedWords).most_common(10)
splittedWords2 = [x for x in splittedWords if len(x) == 4]
commonWords2 = collections.Counter(splittedWords2).most_common(10)
print('10 most common words: {cW}'.format(cW = commonWords))
print('10 most common words with 4-symbol length:{cW2}'.format(cW2 = commonWords2))
input('Press enter to continue...')