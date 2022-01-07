import pytest
import unittest   # The test framework

from kata import *

class Test_kata(unittest.TestCase):

    def test_apply_1(self):
        input = "foo:poo:buu:puu"
        args  = apply01(input)
        
        assert(args[0] == "foo")
        assert(args[1] == "poo")
        assert(args[2] == "buu")
        assert(args[3] == "puu")

    def test_apply_2(self):
        input =  "123457"
        result = apply02(input)
        assert( result == True)

        result = apply03("hello world")
        assert( result == True)

        result = apply03("hello world 123")
        assert( result == True)

        result = apply03("hello world")
        assert( result == True)

    def test_apply_3(self):
        input =  "hello world"

        result = apply03(input)
        assert( result == True)

        result = apply03(input.toUpperCase())
        assert( result == False)

        result = apply03("12345")
        assert( result == True)

        result = apply03("Hello World")
        assert( result == False)

        result = apply03("geekshubs")
        assert( result == True)

        result = apply03("academy")
        assert( result == True)

    def test_apply_4(self):
        result = apply04("HELLO WORLD")
        assert( result == True)

    def test_apply_41(self):
        result = apply04("12345")
        assert( result == False)

    def test_apply_42(self):
        result = apply04("Hello World")
        assert( result == True)

    def test_apply_43(self):
        result = apply04("geekshubs")
        assert( result == False)

    def test_apply_44(self):
        result = apply04("academy")
        assert( result == False)

    def test_apply_5(self):
        input =  "hello world"

        result = apply05(input)
        assert( result == True)

        result = apply05(input.toUpperCase())
        assert( result == True)

        result = apply05("12345")
        assert( result == False)

        result = apply05("Hello World")
        assert( result == True)

        result = apply05("geekshubs")
        assert( result == True)

        result = apply05("academy")
        assert( result == True)

        result = apply05("HELLO WORLD")
        assert( result == True)

        result = apply05("12345")
        assert( result == False)

        result = apply05("Hello World")
        assert( result == True)

        result = apply05("geekshubs")
        assert( result == True)

        result = apply05("academy")
        assert( result == True)

        result = apply05("123")
        assert( result == False)

        result = apply05("5678")
        assert( result == False)

    def test_apply_6(self):
        input =  "123457"
        result = apply06(input)
        assert( result == True)

        result = apply06("hello world")
        assert( result == False)

        result = apply06("hello world 123")
        assert( result == False)

        result = apply06("hello world")
        assert( result == False)

    def test_apply_7(self):
        result = apply07("hello world ")
        assert( result == True)

    def test_apply_71(self):
        result = apply07("hello world")
        assert( result == True)

    def test_apply_73(self):

        result = apply07("Hello World")
        assert( result == True)

    def test_apply_74(self):
        result = apply07("geekshubs ")
        assert( result == True)

    def test_apply_75(self):
        result = apply07("academy ")
        assert( result == True)


    def test_apply_9(self):
        result = apply09("20200102")
        assert( result == False)

    def test_apply_99(self):
        result = apply09("01-02-2222")
        assert( result == True)

    def test_apply_98(self):
        result = apply09("010-02-2222")
        assert( result == False)


    def test_apply_97(self):
        result = apply09("00-022-2222")
        assert( result == False)

    def test_apply_96(self):
        result = apply09("05-02-222")
        assert( result == False)

    def test_apply_95(self):
        result = apply09("05-02-22")
        assert( result == False)

    def test_apply_94(self):
        result = apply09("05-02-2")
        assert( result == False)

    def test_apply_93(self):
        result = apply09("5-02-22")
        assert( result == False)


    def test_apply_92(self):
        result = apply09("5-0-2")
        assert( result == False)

    def test_apply_91(self):
        result = apply09("30-02-2222")
        assert( result == True)

    def test_apply_10(self):
        result = apply10("test.pptx")
        assert( result == True)

        result = apply10("test.doc")
        assert( result == True)

        result = apply10("test.word")
        assert( result == True)

        result = apply10("testgmailcom")
        assert( result == False)

    def test_apply_11(self):
        result = apply11("test@gmail.com")
        assert( result == True)

        result = apply11("testgmail.com")
        assert( result == False)

        result = apply11("test@gmailcom")
        assert( result == False)

        result = apply11("testgmailcom")
        assert( result == False)


if __name__ == '__main__':
	unittest.main()