from httpx import AsyncClient
import base64

from core.config import config


async def _create_user_and_login(
    client: AsyncClient
) -> None:
    await client.post("/", )

    encoded_credentials = base64.b64encode(
        f"{config.BASIC_AUTH_USERNAME}:{config.BASIC_AUTH_PASSWORD}".encode("utf-8")
    ).decode("utf-8")

    client.headers.update({"Authorization": f"Basic {encoded_credentials}"})

    return None


__all__ = ["_create_user_and_login"]
