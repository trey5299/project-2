from typing import List

from cis301.phonebill.abstract_phonebill import AbstractPhoneBill, T


class PhoneBill(AbstractPhoneBill):

    def __init__(self, customername, uid ):
        self.__customername = None
        self.__customername = customername
        self.__phonecalls = list()

    def __init__(self,customername):
        self.__customername = customername

    def get_phonecalls(self) -> List[T]:
        return self.get_phonecalls

    def add_phonecall(self, phonecall):
        return self.__phonecall

    def get_customer(self) -> str:
        return self.__customername

