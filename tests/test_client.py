"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: Sion Kim
Date: 2024.09.07
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client

class TestClient(unittest.TestCase):

    def test_init_valid(self):
        """ Test for client with name mangling """
        client = Client(1999, "Sion", "Kim", "skim14@rrc.ca")
        self.assertEqual(1999, client._Client__client_number)
        self.assertEqual("Sion", client._Client__first_name)
        self.assertEqual("Kim", client._Client__last_name)
        self.assertEqual("skim14@rrc.ca", client._Client__email_address)

    def test_init_non_numeric_client_number_raises_exception(self):
        """ Test for non-numeric client number (None) """
        with self.assertRaises(ValueError):
            client = Client(None, "Sion", "Kim", "skim14@rrc.ca")

    def test_init_blank_first_name_raises_exception(self):
        """ Test for blank first name (" ") """
        with self.assertRaises(ValueError):
            client = Client(1999, " ", "Kim", "skim14@rrc.ca")
    
    def test_init_blank_last_name_raises_exception(self):
        """ Test for blank last name (" ") """
        with self.assertRaises(ValueError):
            client = Client(1999, "Sion", " ", "skim14@rrc.ca")

    def test_init_invalid_email_address_sets_default(self):
        """ Test for invalid email address ("skim14") """
        client = Client(1999, "Sion", "Kim", "skim14")
        self.assertEqual("email@pixell-river.com", client._Client__email_address)
            
    def test_retunrs_client_number(self):
        """ Test for return client_number (1999) """
        client = Client(1999, "Sion", "Kim", "skim14@rrc.ca")
        self.assertEqual(1999, client._Client__client_number)

    def test_retunrs_first_name(self):
        """ Test for return first_name ("Sion") """
        client = Client(1999, "Sion", "Kim", "skim14@rrc.ca")
        self.assertEqual("Sion", client._Client__first_name)

    def test_retunrs_last_name(self):
        """ Test for return last_name ("Kim") """
        client = Client(1999, "Sion", "Kim", "skim14@rrc.ca")
        self.assertEqual("Kim", client._Client__last_name)

    def test_retunrs_email_address(self):
        """ Test for return email_address ("skim14@rrc.ca") """
        client = Client(1999, "Sion", "Kim", "skim14@rrc.ca")
        self.assertEqual("skim14@rrc.ca", client._Client__email_address)
    
    def test_retunrs_str_(self):
        """ Test for return expected str format """
        client = Client(1999, "Sion", "Kim", "skim14@rrc.ca")
        self.assertEqual(str(client), "Kim, Sion [1999] - skim14@rrc.ca")