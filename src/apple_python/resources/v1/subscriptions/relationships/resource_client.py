"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import AsyncBaseClient, SyncBaseClient
from apple_python.resources.v1.subscriptions.relationships.introductory_offers import (
    IntroductoryOffersClient,
    AsyncIntroductoryOffersClient,
)
from apple_python.resources.v1.subscriptions.relationships.prices import (
    PricesClient,
    AsyncPricesClient,
)


class RelationshipsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.introductory_offers = IntroductoryOffersClient(
            base_client=self._base_client
        )
        self.prices = PricesClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncRelationshipsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.introductory_offers = AsyncIntroductoryOffersClient(
            base_client=self._base_client
        )
        self.prices = AsyncPricesClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
