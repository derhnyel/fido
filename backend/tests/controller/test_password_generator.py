
from app.controllers import PasswordGeneratorController
import string
import pytest
# Test the password generator controller

@pytest.mark.asyncio
async def test_password_length():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        uppercase_allowed=True,
    )
    assert len(password) == 10

@pytest.mark.asyncio
async def test_password_uppercase():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        uppercase_allowed=True,
        lowercase_allowed=False,
        special_characters_allowed=False,
        digits_allowed=False,
    )
    assert all(c.isupper() for c in password)
@pytest.mark.asyncio
async def test_password_lowercase():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        lowercase_allowed=True,
        uppercase_allowed=False,
        special_characters_allowed=False,
        digits_allowed=False,
    )
    assert all(c.islower() for c in password)
@pytest.mark.asyncio
async def test_password_special_characters():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        uppercase_allowed=False,
        special_characters_allowed=True,
        digits_allowed=False,
    )
    assert any(c in string.punctuation for c in password)
@pytest.mark.asyncio    
async def  test_password_digits():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        uppercase_allowed=False,
        special_characters_allowed=False,
        lowercase_allowed=False,
        digits_allowed=True,
    )
    assert any(c in string.digits for c in password)
@pytest.mark.asyncio
async def test_password_startswith():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        uppercase_allowed=False,
        special_characters_allowed=False,
        digits_allowed=True,
        startswith="a",
    )
    assert password.startswith("a")
@pytest.mark.asyncio
async def test_password_endswith():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        uppercase_allowed=False,
        special_characters_allowed=False,
        digits_allowed=True,
        endswith="a",
    )
    assert password.endswith("a")
@pytest.mark.asyncio
async def test_password_must_contain():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        uppercase_allowed=False,
        special_characters_allowed=False,
        digits_allowed=True,
        must_contain="a",
    )
    assert "a" in password
@pytest.mark.asyncio
async def test_password_not_startswith():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        uppercase_allowed=False,
        special_characters_allowed=False,
        digits_allowed=True,
        not_startswith="a",
    )
    assert not password.startswith("a")
@pytest.mark.asyncio
async def test_password_not_endswith():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        uppercase_allowed=False,
        special_characters_allowed=False,
        digits_allowed=True,
        not_endswith="a",
    )
    assert not password.endswith("a")
@pytest.mark.asyncio
async def test_password_must_not_contain():
    password = await PasswordGeneratorController().generate_password(
        length=10,
        uppercase_allowed=False,
        special_characters_allowed=False,
        digits_allowed=True,
        must_not_contain="a",
    )
    assert "a" not in password
@pytest.mark.asyncio
async def test_password_startswith_and_not_startswith():
    try:
        password = await PasswordGeneratorController().generate_password(
            length=10,
            uppercase_allowed=False,
            special_characters_allowed=False,
            digits_allowed=True,
            startswith="a",
            not_startswith="a",
        )
    except ValueError:
        assert True
    else:
        assert False
    
@pytest.mark.asyncio
async def test_password_endswith_and_not_endswith():
    try:
        password = await PasswordGeneratorController().generate_password(
            length=10,
            uppercase_allowed=False,
            special_characters_allowed=False,
            digits_allowed=True,
            endswith="a",
            not_endswith="a",
        )
    except ValueError:
        assert True
    else:
        assert False
@pytest.mark.asyncio
async def test_password_must_contain_and_must_not_contain():
    try:
        password = await PasswordGeneratorController().generate_password(
            length=10,
            uppercase_allowed=False,
            special_characters_allowed=False,
            digits_allowed=True,
            must_contain="a",
            must_not_contain="a",
        )
    except ValueError:
        assert True
    else:
        assert False    
@pytest.mark.asyncio
async def test_password_length_too_short():
    try:
        password = await PasswordGeneratorController().generate_password(
            length=10,
            uppercase_allowed=False,
            special_characters_allowed=False,
            digits_allowed=True,
            startswith="a"*11,
        )
    except ValueError:
        assert True
    else:
        assert False







