def test_lookup_customer_by_name(customer):
    customer.phonebill.search("Trey")
    customer.assertsearch(customer.phonebill.search("Trey"))


class PhoneCall(object):
    pass


def test_project2():
    phonecall = PhoneCall("Sam")
    assert phonecall.get_caller() is "Sam"


class Student(object):
    pass


def test_student():
    s= Student("Joe", '"Operating Systems", "", "Data Structures"', '3.2')
    assert type (s, Student)

def test_student_says():
    s= Student("John", '"Calculus", "Database Systems", "Biology"', "3.8")
    assert type (s.says(), ("This class is too much work"))

def test_phonecall():
    customer = "6778892999"
    phonecall = customer
    assert phonecall


def test_lookup_callee(callee):
    callee.phonecall.search("Jim")
    callee.assertsearch(callee.phonecall.search("Jim"))




