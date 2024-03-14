from classes import AddressBook, Record


book = AddressBook()

michael = Record("Michael")
michael.add_birthday("13.03.2016")
book.add_record(michael)
    
jane = Record("Jane")
jane.add_birthday("18.03.2016")
book.add_record(jane)
    
oscar = Record("Oscar")
oscar.add_birthday("15.03.2016")
book.add_record(oscar)
    
volodymyr = Record("Volodymyr")
volodymyr.add_birthday("15.05.2016")
book.add_record(volodymyr)
    
stasy = Record("Stacy")
stasy.add_birthday("10.04.2016")
book.add_record(stasy)

melissa = Record("Melissa")
melissa.add_birthday("20.03.2016")
book.add_record(melissa)

angela = Record("Angela")
angela.add_birthday("19.03.2016")
book.add_record(angela)

jane = Record("Jane")
jane.add_phone("2323232323")
jane.add_birthday("16.03.1914")
book.add_record(jane)
    
jane2 = Record("Janee")
jane2.add_phone("1323232329")
jane2.add_birthday("15.03.1914")
book.add_record(jane2)
    
jane3 = Record("Jaine")
jane3.add_phone("9323232329")
book.add_record(jane3)
    
jane4 = Record("Janet")
jane4.add_phone("9323232329")
jane4.add_birthday("10.04.1914")
book.add_record(jane4)
    
# print(book)
book.get_birthdays(3)