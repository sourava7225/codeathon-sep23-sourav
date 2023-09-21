# Path: ipaddress.py

# Write a program to validate an IP address. Given a string, write a function to check if it is a valid IP address or not. If valid, return true, otherwise return false. Add exception bloacks to the code to handle invalid inputs. Create test scripts as well with 5 scenarios

def ipaddress(ip):

    # Write your code here

    try:

        ip = ip.split(".")

        if len(ip) != 4:

            return False

        for i in ip:

            if int(i) < 0 or int(i) > 255:

                return False

        return True

    except:

        return False
    

#create atleast 5 testcases for the above program

import unittest
from ipaddress import ipaddress

class TestIPAddress(unittest.TestCase):
    def test_valid_input(self):
        ip = "255.255.0.0"
        self.assertTrue(ipaddress(ip),True)
        ip = "555.555.555.555"
        self.assertTrue(ipaddress(ip),False)
        ip = "256.255.0.0"
        self.assertTrue(ipaddress(ip),False)
        ip = "234.533"
        self.assertTrue(ipaddress(ip),False)
        ip = "23"
        self.assertTrue(ipaddress(ip),False)