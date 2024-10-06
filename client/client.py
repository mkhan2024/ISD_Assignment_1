"""
Description: A class to manage Client objects.
Author: Apurba Khan
Date: 2024.09.23
"""

from email_validator import validate_email, EmailNotValidError

class Client:
    """
    A class for client.

    Attributes:
        client_number (int): The client_number of the client.
        first_name (str): The first_name of the client.
        last_name (str): The last_name of the client.
        email_address (str): The email address of the client.
    """
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        A method for client's attributes.

        Args:
            client_number (int): numeric
            first_name (str): no blank.
            last_name (str): no blank.
            email_address (str): valid email.

        Returns:
            data type: The return value. Describe what each return value may indicate.

        Raises:
            ValueError (client_number: non-numeric
                        first_name: blank
                        last_name: blank
                        email_address: invalid).
        """
        if not isinstance(client_number, int):
            raise ValueError("client_number must be numeric.")
        self.__client_number = client_number

        if len(first_name.strip()) == 0:
            raise ValueError("first_name cannot be blank.")
        self.__first_name = first_name

        if len(last_name.strip()) == 0:
            raise ValueError("last_name cannot be blank.")
        self.__last_name = last_name

        try:
            validated_email = validate_email(email_address, check_deliverability = False)  
            self.__email_address = email_address
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"
    
    @property
    def client_number(self) -> int:
        """
        Returns:
            int: The client_number.
        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Returns:
            str: The first_name.
        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Returns:
            str: The last_name.
        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Returns:
            str: The email_address.
        """
        return self.__email_address
    
    def __str__(self) -> str:
        """
        A method for return a string.

        Returns:
            str: client_number, first_name, last_name, email_address.
        """
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}"