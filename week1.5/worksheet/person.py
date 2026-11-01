# Worksheet 1.5: Person class
from datetime import date

class Person:
    """
    Person class with a string name and a date of birth
    """
    def __init__(self, name:str, birth:date):
        """
        A Person, with a name and a date of birth.
        """

        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        elif name=="":
            raise ValueError("Name must not be blank")
        if not isinstance(birth,date):
            raise TypeError("Birth must be in date format")

        self.name=name
        self.birth=birth
    def initials(self):
        """
        Returns the upper case value of the initals of the persons name
        """
        initial_string=""
        add_next_character=True
        for char in self.name:
            if char.upper()==char.lower():
                add_next_character=True
            else:
                if add_next_character==True:
                    initial_string=initial_string+char
                    add_next_character=False
        return initial_string.upper()
    def is_birthday(self):
        """
        Returns true if today is equal to the persons birthday
        """
        if date.today().month==self.birth.month and date.today().day==self.birth.day:
            return True
        else:
            return False
