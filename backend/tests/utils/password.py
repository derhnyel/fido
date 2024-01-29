def create_fake_password(
    length: int = 10,
    uppercase_allowed: bool = True,
    special_characters_allowed: bool = True,
    lowercase: bool = True,
    digits_allowed: bool = True,
    startswith: str = "",
    endswith: str = "",
    must_contain: str = "",
    not_startswith: str = "",
    not_endswith: str = "",
    must_not_contain: str = "",
) -> dict:
    """
    Create a fake password.
    Returns:
        str: The fake password.
    """
    return dict(
            length=length,
            uppercase=uppercase_allowed,
            special_characters=special_characters_allowed,
            lowercase = lowercase,
            digits=digits_allowed,
            startswith=startswith,
            endswith=endswith,
            must_contain=must_contain,
            not_startswith=not_startswith,
            not_endswith=not_endswith,
            must_not_contain=must_not_contain,
        )
    
