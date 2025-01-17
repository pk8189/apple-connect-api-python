"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import SyncBaseClient, AsyncBaseClient
from apple_python.resources.v3.app_price_points import (
    AsyncAppPricePointsClient,
    AppPricePointsClient,
)


class V3Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.app_price_points = AppPricePointsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncV3Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.app_price_points = AsyncAppPricePointsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
