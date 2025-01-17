"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import SyncBaseClient, AsyncBaseClient
from apple_python.resources.v1.users.relationships.visible_apps import (
    AsyncVisibleAppsClient,
    VisibleAppsClient,
)


class RelationshipsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.visible_apps = VisibleAppsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncRelationshipsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.visible_apps = AsyncVisibleAppsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
