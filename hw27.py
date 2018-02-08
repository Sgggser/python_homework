import random
import string


def permute(text, NUM_OF_SYMBOLS=3): # returns permuted text
    word_list = text.split(' ')
    for word in word_list:
        if len(word) != 1:
            begin_symbols = 2 if word[0] in string.punctuation else 1
            end_symbols = 2 if word[-1] in string.punctuation else 1
            length = len(word[begin_symbols: -end_symbols])
            word_middle = word[(begin_symbols): -end_symbols]
            triples = [word_middle[NUM_OF_SYMBOLS*i:NUM_OF_SYMBOLS*(i + 1)] for i in range(length // NUM_OF_SYMBOLS)]
            if length % NUM_OF_SYMBOLS != 0:
                last_piece = word_middle[-(length % NUM_OF_SYMBOLS):]
                triples.append(last_piece)
            for i in range(len(triples)):
                letter_list = [triples[i][ii] for ii in range(len(triples[i]))]
                random.shuffle(letter_list)
                triples[i]=''.join(letter_list)
            word_middle = ''.join(triples)
            word_list[word_list.index(word)] = ('%s%s%s' % (word[: begin_symbols], word_middle, word[-end_symbols:]))
    return ' '.join(word_list)


novost = 'На Французском бульваре построят еще одну высотку. Под угрозой — уникальный «дом судей» с императорскими коронами.'
print(permute(novost, 3))