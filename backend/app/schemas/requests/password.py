from pydantic import BaseModel, constr, validator
class RequestPassword(BaseModel):
    length: int 
    special_characters: bool = True
    digits: bool = True
    uppercase: bool = True
    lowercase: bool = True
    startswith:  constr(min_length=0, max_length=64)  = ""
    endswith:  constr(min_length=0, max_length=64) = ""
    must_contain:  constr(min_length=0, max_length=64) = ""
    not_startswith:  constr(min_length=0, max_length=64) = ""
    not_endswith:  constr(min_length=0, max_length=64) = ""
    must_not_contain:  constr(min_length=0, max_length=64) = ""


    @validator("length")
    def lenght_not_zero(cls, v):
        if v <= 0 or v > 64:
            raise ValueError("Password length must be greater than 0 and less than 64")
        return v
    
    @validator("uppercase")
    def one_must_be_true(cls, upper,values):
        if not any([upper,
        values.get("lowercase"),
        values.get("digits"),
        values.get("special_characters")]):
            raise ValueError("At least one character type must be selected")
        return upper
    
    @validator("not_startswith")
    def check_startswith(cls,startswith, values):
        not_startswith = values.get("startswith")
        if (startswith and not_startswith) and startswith == not_startswith: # This will only check for the pattern not the individual characters or thier frequency
            raise ValueError("Startswith and Not_startswith must not be the same characters")
        return startswith

    @validator("not_endswith")
    def check_endswith(cls,endswith, values):
        not_endswith = values.get("endswith")
        if (endswith and not_endswith) and endswith == not_endswith :
            raise ValueError("Endswith and Not_endswith must not be the same characters")
        return endswith

    @validator("must_contain")
    def check_must_contain(cls,must_contain, values):
        must_not_contain = values.get("must_not_contain")
        if (must_contain and must_not_contain) and must_contain == must_not_contain:
            raise ValueError("Must_contain and Must_not_contain must not be the same characters")
        return must_contain
    
    @validator("startswith")
    def check_startswith_length(cls, startswith, values):
        length = values.get("length")
        if startswith:
            # Check if startswith is too long
            if length < len(startswith):
                raise ValueError(f"Password length must be at least {length}. Startswith is too long")
        return startswith
    
    @validator("endswith")
    def check_endswith_length(cls, endswith, values):
        length = values.get("length")
        if endswith:
            # Check if endswith is too long
            if length < len(endswith):
                raise ValueError(f"Password length must be at least {length}. Endswith is too long")
        return endswith
    
    @validator("must_contain")
    def check_must_contain_length(cls, must_contain, values):
        length = values.get("length")
        if must_contain:
            # Check if must_contain is too long
            if length < len(must_contain):
                raise ValueError(f"Password length must be at least {length}. Must contain is too long")
        return must_contain
