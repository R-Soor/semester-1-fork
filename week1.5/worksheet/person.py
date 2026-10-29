# Worksheet 1.5: Person class

from datetime import date

class Person:
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
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
        initial_string=""
        for char in self.name:
            if char==char.upper() and char!=" " and char!="":
                initial_string=initial_string+char
        return initial_string
    def is_birthday(self):
        if date.today()==self.birth:
            return True
        else:
            return False

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
