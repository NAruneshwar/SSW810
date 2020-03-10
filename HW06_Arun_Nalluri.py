class SortedQueue:
    """ A queue that serves customers in alphabetical order """
    def __init__(self):
        """ initialize the SortedQueue """
        self.name = list()

    def add(self, name):
        """ add a name to the queue """
        self.name.append(name)
        self.name.sort()
       

    def next(self):
        """ remove and return the first name from the queue 
            or None if the queue is empty 
        """
        if len(self.name) == 0:
            return None
        return(self.name.pop(0))

    def __str__(self):
        """ return a comma separated string with the names in the queue """
        return(", ".join(self.name))