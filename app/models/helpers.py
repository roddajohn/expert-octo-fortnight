""" Helpers file

Currently defines the:
 DuplicateException

"""

class DuplicateException(Exception):
    """ Exception when you are adding something that already exists in a given collection """
    pass

class UserNotFoundException(Exception):
    """ Exception when a user is not found although it needs to be found """
    pass

class DataNotFound(Exception):
    """ Exception when user attempting to add data which really shouldn't be added """
    pass

class DataWrongType(Exception):
    """ Exception when a user is adding data which is the wrong type for the data """
