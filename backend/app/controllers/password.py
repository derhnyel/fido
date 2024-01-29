import secrets
import string
import random
from functools import partial


upper_letters:str = string.ascii_uppercase
lower_letters:str = string.ascii_lowercase
digits:str = string.digits
special_chars:str = string.punctuation

class PasswordGeneratorController:
    # Generate a password with the given parameters
    async def generate_password(self,length=8, special_characters_allowed=True, digits_allowed=True, uppercase_allowed=True, lowercase_allowed=True,startswith:str="",endswith :str="",must_contain :str="",not_startswith:str="",not_endswith :str="",must_not_contain :str="") -> str:
        """
        Generates a password with the given parameters
        Args:
            length: The length of the password
            special_characters_allowed: If special characters should be used (e.g. !@#$%^&*()_+) :bool
            digits_allowed: If digits should be used (e.g. 1234567890) :bool
            uppercase_allowed: If upper letters should be used (e.g. ABCDEFGHIJKLMNOPQRSTUVWXYZ) :bool
            lowercase_allowed: If lower letters should be used (e.g. abcdefghijklmnopqrstuvwxyz) :bool
            startswith: If the password should start with the given string:str
            endswith: If the password should end with the given string :str
            must_contain: If the password must contain the given string :str
            not_startswith: If the password should not start with the given string :str
            not_endswith: If the password should not end with the given string :str
            must_not_contain: If the password must not contain the given string/characters :str
        Returns:
            The generated password :str
        """
        global upper_letters,lower_letters,digits,special_chars
        # Check if length is valid
        if length <= 0:
            raise ValueError("Password length must be greater than 0")
        if not special_characters_allowed and not digits_allowed and not uppercase_allowed and not lowercase_allowed:
            raise ValueError("At least one character type must be selected")
        original_lenght = length
        posibilities = []
        password = ""
        final_password = "{start}{password}{end}"
        if special_characters_allowed:
            posibilities.append(1)
        if digits_allowed:
            posibilities.append(2)
        if uppercase_allowed:
            posibilities.append(3)
        if lowercase_allowed:
            posibilities.append(4)
        if (startswith and not_startswith) and startswith == not_startswith: # This will only check for the pattern not the individual characters
            raise ValueError("Startswith and Not_startswith must not be the same characters")
        if (endswith and not_endswith) and endswith == not_endswith :
            raise ValueError("Endswith and Not_endswith must not be the same characters")
        if (must_contain and must_not_contain) and must_contain == must_not_contain:
            raise ValueError("Must_contain and Must_not_contain must not be the same characters")
        if startswith:
            # Check if startswith is too long
            length-=len(startswith)
            if length < 0:
                raise ValueError(f"Password length must be at least {original_lenght}. Startswith is too long")
        if endswith:
            # Check if endswith is too long
            length-=len(startswith)
            if length < 0:
                raise ValueError(f"Password length must be at least {original_lenght}. Endswith is too long")
        if must_contain:
            # Check if must_contain is too long
            password+=must_contain
            if len(password) > length:
                raise ValueError(f"Password length must be at least {original_lenght}. Must contain is too long")
        if not_startswith or not_endswith or must_not_contain: # Remove characters from the character sets that are not allowed to be used
            for char in set(not_startswith+endswith+must_not_contain): # Remove duplicates
                if char.isupper() :
                    upper_letters = upper_letters.replace(char,"")
                elif char.islower():
                    lower_letters = lower_letters.replace(char,"")
                elif char.isdigit():
                    digits = digits.replace(char,"")
                elif char in special_chars:
                    special_chars = special_chars.replace(char,"")
        iterations = 0
        while True:
            if iterations > 1: # Only shuffle after first iteration to make sure all possibilities are used at least once
                random.shuffle(posibilities) 
            for i in range(len(posibilities)):
                if len(password) >= length:
                    break
                possibility = posibilities[i]
                if possibility == 1:
                    password+=secrets.choice(special_chars)
                elif possibility == 2:
                    password+=secrets.choice(digits)
                elif possibility == 3:
                    password+=secrets.choice(upper_letters)
                elif possibility == 4:
                    password+=secrets.choice(lower_letters)
            if len(password) >= length:
                # Shuffle password to make sure that the first characters are not always the same type of character 
                list_pass = list(password)
                random.shuffle(list_pass)
                password = ''.join(list_pass)
                break
            iterations+=1
        final_password = final_password.format(start=startswith,password=password,end=endswith)
        return final_password
    
    def __call__(self):
        return partial(self.generate_password)
