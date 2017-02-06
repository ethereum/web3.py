class Empty(object):
    def __bool__(self):
        return False

    def __nonzero__(self):
        return False


empty = Empty()
