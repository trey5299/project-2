from datetime import date

from cis301.phonebill.abstract_phonecall import AbstractPhoneCall


class Phonecall(AbstractPhoneCall):

    def __init__(self, caller, callee, startdate, enddate, endtime, starttime):
        self.__caller = caller
        self.__callee = callee
        self.__startdate = startdate
        self.__enddate = enddate
        self.__endtime = endtime
        self.__starttime = starttime

    def get_caller(self) -> str:
        return self.__caller

    def get_callee(self) -> str:
        return self.__callee

    def get_starttime(self) -> str:
        return self.__startdate

    def get_endtime(self) -> str:
        return self.__enddate

    def get_startdate(self) -> str:
        return self.__startdate

    def get_enddate(self) -> str:
        return self.__enddate







