import random


def permute(text): # returns permuted text
    word_list = text.split(' ')
    for word in word_list:
        if word[0] == '"':
            begin_symbols = 2
        else:
            begin_symbols = 1

        if word[-1] in ',"?.!/;:':
            end_symbols = 2
        else:
            end_symbols = 1

        word_middle = (word[begin_symbols: -end_symbols])
        new_tripples = []
        length = len(word_middle)
        triples = [word_middle[3*i:3+3*i] for i in range(length // 3)]
        if length % 3 != 0:
            last_piece = word_middle[-(length % 3):]
            triples.append(last_piece)
        for i in range(len(triples)):
            tripple = []
            for letter in triples[i]:
                tripple.append(letter)
            random.shuffle(tripple)
            new_tripples.append(''.join(tripple))
        word_middle = ''.join(new_tripples)
        word_list[word_list.index(word)] = ('%s%s%s' % (word[: begin_symbols], word_middle, word[-end_symbols:]))

    return ' '.join(word_list)


novost = 'Патрулировать улицы теперь станет намного удобнее, по крайней мере полицейским Ширяевского участка Раздельнянского отдела полиции ГУНП в Одесской области, которые получили новенький патрульный автомобиль "Рено Сандеро"'
print(permute(novost))