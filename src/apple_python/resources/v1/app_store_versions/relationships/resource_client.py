"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import AsyncBaseClient, SyncBaseClient
from apple_python.resources.v1.app_store_versions.relationships.app_clip_default_experience import (
    AppClipDefaultExperienceClient,
    AsyncAppClipDefaultExperienceClient,
)
from apple_python.resources.v1.app_store_versions.relationships.build import (
    AsyncBuildClient,
    BuildClient,
)


class RelationshipsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.app_clip_default_experience = AppClipDefaultExperienceClient(
            base_client=self._base_client
        )
        self.build = BuildClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncRelationshipsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.app_clip_default_experience = AsyncAppClipDefaultExperienceClient(
            base_client=self._base_client
        )
        self.build = AsyncBuildClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
