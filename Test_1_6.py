import string

str = 'Питон'
str = 'книга без слов'
#str = 'изограмма'
print(str)
length = len(str)

isogram = True
for i in range(length-1): #Проверяем все буквы, начиная с первой до предпоследней
    for j in range(i+1,length): #сравниваем текущую букву со всеми впередистоящими
        if str[i]==str[j] and str[i] != ' ':
            isogram = False
if isogram:
    isogram_str = ''
else:
    isogram_str = 'не'
print('Данная строка', isogram_str, 'является изограммой')