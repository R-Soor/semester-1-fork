# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """

        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated

        if not isinstance(pounds,int):
            raise TypeError("pounds must be an integer")
        elif pounds<0:
            raise ValueError("pounds must be greater than 0")
        
        if not isinstance(pence, int):
            raise TypeError("pence must be an integer")
        elif pence<0 or pence>99:
            raise ValueError("pence must be between 0 and 99")
        
        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')
        if self.pence<10:
            return f"£{self.pounds}.0{self.pence}"
        else:
            return f"£{self.pounds}.{self.pence}"


    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
        total_pounds=0
        total_pence=0
        if not isinstance(other, Money):
            raise TypeError("You must use 2 instance of Money")
        else:
            if (self.pence+other.pence)>99:
                total_pence=self.pence+other.pence-100
                total_pounds=1
            else:
                total_pence=self.pence+other.pence
            total_pounds+=(self.pounds+other.pounds)

        sum = Money(total_pounds, total_pence)
        return sum