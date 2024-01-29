from core.security import PasswordHandler, SecurityHandler
from core.exceptions import UnauthorizedException


def test_auth():
    basic_auth  = SecurityHandler["basic"]
    basic_auth.set_credentials("admin", "password")
   
    credentials = lambda x: x
    credentials.username = "admin"
    credentials.password = "password"
    assert basic_auth.verify(credentials) == True

    credentials.username = "admin"
    credentials.password = "wrong_password"
    try:
        basic_auth.verify(credentials)
    except Exception as e:
        assert isinstance(e, UnauthorizedException)
    
    credentials.username = "wrong_username"
    credentials.password = "password"  
    try:
        basic_auth.verify(credentials)
    except Exception as e:
        assert isinstance(e, UnauthorizedException)
    
    credentials.username = "wrong_username"
    credentials.password = "wrong_password"
    try:
        basic_auth.verify(credentials)
    except Exception as e:
        assert isinstance(e, UnauthorizedException)
