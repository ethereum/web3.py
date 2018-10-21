class Empty:
    def __bool__(self) -> bool:
        return False

    def __nonzero__(self) -> bool:
        return False


empty = Empty()
