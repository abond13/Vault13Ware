
from datetime import datetime
from datetime import timedelta
from collections import UserDict
from AddressBook import AddressBook, Name, Birthday, Record
# from colorama import Fore

class DictSortable(UserDict):
    def sort_keys(self) -> dict:
        """
        Sort the dictionary through key values (int or datetime, for example)
        """
        sorted_dict = {}
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            sorted_dict[key] = self.data[key]
        return sorted_dict

# def date_to_MMYY(date: datetime.date) -> str:
#     """
#     Just converts a date to a readable string: datetime(2024, 3, 1) -> 'March, 2024'
#     """
#     return f"{date.strftime("%B, %Y")}"

def get_days(today: datetime.date, quantity: int) -> datetime.date:
    """
    Generator of dates within some amount days from today
    """
    count = 0
    while count < quantity:
        yield today
        today += timedelta(days=1)
        count += 1

def get_birthdays(records: AddressBook, quantity: int):
    """
    Function recieves an AddressBook object and number of days to look ahead.\n
    Prints out birthdays of contacts within the range of days.
    Returns nothing.
    """
    today = datetime.today().date()
    calendar = {}
    
    # Going to work with the next structure: (dict of dicts)
    #
    # {
    #   'March, 2024' : { 12: ['Brandon','Olivia'], 27: ['Gregor'] }
    #   'April, 2024' : { 3: ['Viktor'], 14: ['Sofia'], 18: ['Thomas', 'Andrea', 'Magnus'] }                       
    # }
    
    for record in records.values():
        birthday_date = record.birthday
        name = record.name
        for day in get_days(today, quantity):    
            if (birthday_date.month, birthday_date.day) == (day.month, day.day):
            
                # set keys for the outer and inner dictionaries
                key_outer = datetime(day.year, day.month, day=1).date()        # This is datetime.date, but we will print out 'March, 2024'
                key_inner = birthday_date.day
            
                # if there is no such key - create it!
                try:
                    calendar[key_outer]
                except KeyError:
                    calendar[key_outer] = {}
                
                    # it's time to fill in the inner dictionary:
                if len(calendar[key_outer]) == 0:
                    calendar[key_outer][key_inner] = [name] 
                else:
                    try:
                        # if there is already such cell with given month and day - append new name
                        calendar[key_outer][key_inner].append(name)
                    except KeyError:
                        # if there is no such key for inner dictionary - also create it
                        calendar[key_outer][key_inner] = [name]

    # Don't forget to sort our dictionaries by date
    calendar = DictSortable(calendar)
    calendar = calendar.sort_keys()
    for key_outer, inner_dict in calendar.items():
        inner_dict = DictSortable(inner_dict)
        inner_dict = inner_dict.sort_keys()
        print(key_outer.strftime("%B, %Y"))
        for key_inner, name_list in inner_dict.items():
            print(f"{key_inner}: {", ".join([name.value for name in name_list])}")
        print()


if __name__ == "__main__":
    
    book = AddressBook()
    
    michael = Record("Michael")
    michael.add_birthday("15.03.2016")
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

    get_birthdays(book, 30)

    