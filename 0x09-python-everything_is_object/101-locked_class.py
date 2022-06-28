"""Module for class that prevent dynamic attribute"""


class LockedClass:
    """LockedClass"""
    __slots__ = ['first_name']

    def __init__(self) -> None:
        """Init method"""
        pass