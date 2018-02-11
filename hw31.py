import pickle


running = True

#------------------------------------------------------------------------------
phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321"},
              {"name": "Stoyan", "surname": "Draganov", "age": 30, "phone_number":"+380505679034"}
             ]



#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    try:
        print ("| %s:   %20s |" % (user_field, entry[user_field]))
    except Exception:
        printError("User field can be here...")
    print ()

#------------------------------------------------------------------------------
def add_user_field_phonebook():
    global user_field
    user_field = input('Введите новое поле (например "Skype"): ')
    for entry in phone_book:
        entry[user_field] = input('Введите %s для %s %s: ' % (user_field, entry['name'], entry['surname']))


#------------------------------------------------------------------------------
def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")
    pass


#------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    name_del = str(input('Введите имя для удаления записи: '))
    counter = 0
    while len(phone_book) > counter:
        if phone_book[counter]['name'] == name_del:
            del(phone_book[counter])
        else:
            counter += 1
    pass


#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))
    return len(phone_book)


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    phone_book.sort(key=lambda elem: elem['age'])
    print_phonebook()



#------------------------------------------------------------------------------
def print_phonebook_alphabetic():
    phone_book.sort(key=lambda elem: elem['surname'])
    print_phonebook()



#------------------------------------------------------------------------------
def increase_age():
    inc_age = int(input('Введите увеличение возраста: '))
    for entry in phone_book:
        entry['age'] += inc_age



#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    sum_age = 0
    for entry in phone_book:
        sum_age += int(entry["age"])
    print(sum_age/count_all_entries_in_phonebook())



#------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


#------------------------------------------------------------------------------
def exit():
      global running
      running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     6 - Delete entry by name")
      print("     7 - The number of entries in the phonebook")
      print("     8 - Avr. age of all persons")
      print("     9 - Increase age by num. of years")
      print("-----------------------------")
      print("     a - Print phonebook in alphabetic order")
      print("     u - Add userfield")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:

            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,

                  'a':  print_phonebook_alphabetic,
                  'u':  add_user_field_phonebook,
                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }


            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()