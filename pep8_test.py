"""Operating System functionalities to performs unittests"""
import os
import unittest

def pwd() -> str:
    """this function prints the current working directory"""
    print("\n Working directory is: ",  os.getcwd())


class TestPWD(unittest.TestCase):
    """This class inherits unittest TestCase class"""
    def test_pwd(self):
        """This method tests for working directory using unittest"""
        self.assertNotEqual(pwd(), "")


def assert_test_pwd() -> str:
    """this method tests for working directory using assert"""
    assert pwd() != ""


if __name__ == "__main__":
    while True:
        COMMAND = input("""
        ==== Usage ====
        /user$pep8_test.py
        enter a COMMAND: pwd
        'prints working dir and enerates test result'
        enter a COMMAND: exit
        'exits'
        Other Commands :
            -What is TestPWD
            -What is test_pwd
            -What is assert_test_pwd
        enter a COMMAND : """)

        if COMMAND == "pwd":
            pwd()
            assert_test_pwd()
            print("assert passed ... ")
            unittest.main()
            print("Unittest passed ... ")
        elif COMMAND == "What is TestPWD":
            print(TestPWD.__doc__)
        elif COMMAND == "What is test_pwd":
            print(TestPWD.test_pwd.__doc__)
        elif COMMAND == "What is assert_test_pwd":
            print(assert_test_pwd.__doc__)
        elif COMMAND == "exit":
            break
        else:
            print("Unknown COMMAND ...")
            break
