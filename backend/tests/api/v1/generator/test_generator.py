import pytest
from httpx import AsyncClient
from tests.utils.login import _create_user_and_login
from tests.utils.password import create_fake_password



@pytest.mark.asyncio
async def test_generate_password(client: AsyncClient) -> None:
    """Test task creation."""
    await _create_user_and_login(client)

    fake_task = create_fake_password(
        length=10,
        uppercase_allowed=True,
        lowercase = True,
        digits_allowed=True,
        special_characters_allowed=True
    )
    response = await client.post("/v1/generate-password", json=fake_task)
    assert response.status_code == 200
    assert response.json()["password"] is not None
    

@pytest.mark.asyncio
async def test_generate_password_invalid_length(client: AsyncClient) -> None:
    """Test generate password with invalid length."""
    await _create_user_and_login(client)

    fake_task = create_fake_password(
        length=0,
        uppercase_allowed=True,
        lowercase = True,
        digits_allowed=True,
        special_characters_allowed=True
    )
    response = await client.post("/v1/generate-password", json=fake_task)
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Password length must be greater than 0 and less than 64"

@pytest.mark.asyncio
async def test_generate_password_invalid_uppercase(client: AsyncClient) -> None:
    """Test generate password with invalid uppercase."""
    await _create_user_and_login(client)

    fake_task = create_fake_password(
        length=10,
        uppercase_allowed=False,
        lowercase = False,
        digits_allowed=False,
        special_characters_allowed=False
    )
    response = await client.post("/v1/generate-password", json=fake_task)
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] =="At least one character type must be selected"