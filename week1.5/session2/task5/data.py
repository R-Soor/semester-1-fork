# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """
        self.data=[]
        with open(filename,"r") as current_file:
            for line in current_file:
                self.data.append(line)
    def __len__(self):
        """
        Returns the size of this Dataset.
        """
        return len(self.data)
    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        return self.data[index]
    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        length=self.__len__()
        sum=0
        for items in self.data:
            sum+=items
        mean=sum/length

        return mean
    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
        sorted_data=sorted(self.data)

        median = self.sorted_data[len(sorted_data)//2]