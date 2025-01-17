"""File Generated by Sideko (sideko.dev)"""

import httpx
import typing
from apple_python.environment import Environment
from apple_python.core import SyncBaseClient, AsyncBaseClient, AuthBearer
from apple_python.resources.v1 import AsyncV1Client, V1Client
from apple_python.resources.v2 import AsyncV2Client, V2Client
from apple_python.resources.v3 import V3Client, AsyncV3Client


class Client:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.DEFAULT,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        token: typing.Optional[str] = None,
    ):
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.Client(timeout=timeout) if httpx_client is None else httpx_client
            ),
        )

        # register auth methods (keep comment for code generation)
        self._base_client.register_auth("itc-bearer-token", AuthBearer(val=token))

        # register sync resources (keep comment for code generation)
        self.v1 = V1Client(base_client=self._base_client)
        self.v2 = V2Client(base_client=self._base_client)
        self.v3 = V3Client(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncClient:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.DEFAULT,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        token: typing.Optional[str] = None,
    ):
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.AsyncClient(timeout=timeout)
                if httpx_client is None
                else httpx_client
            ),
        )

        # register auth methods (keep comment for code generation)
        self._base_client.register_auth("itc-bearer-token", AuthBearer(val=token))

        # register async resources (keep comment for code generation)
        self.v1 = AsyncV1Client(base_client=self._base_client)
        self.v2 = AsyncV2Client(base_client=self._base_client)
        self.v3 = AsyncV3Client(base_client=self._base_client)

    # register async api methods (keep comment for code generation)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")
