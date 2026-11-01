# Worksheet 1.5: Person class

from datetime import datetime

class Person:
    """
    Person class with a string name and a date of birth
    """
    def __init__(self, name:str, birth:datetime):
        """
        A Person, with a name and a date of birth.
        """

        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        elif name=="":
            raise ValueError("Name must not be blank")
        try:
            birth = datetime.strptime(birth, "%Y-%M-%D")
        except:
            TypeError("Birth must be in date format")

#        if not isinstance(birth,date):
#            raise TypeError("Birth must be in date format")
        
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
        print(self.birth)
        if datetime.today()==self.birth:
            return True
        else:
            return False


p = Person("alan david jones",(2007,12,16))
print(p.initials())