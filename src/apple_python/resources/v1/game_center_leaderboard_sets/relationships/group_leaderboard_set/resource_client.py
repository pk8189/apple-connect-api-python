"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    AsyncBaseClient,
    default_request_options,
    to_encodable,
    SyncBaseClient,
    RequestOptions,
)
import typing
from apple_python.types.v1.game_center_leaderboard_sets.relationships.group_leaderboard_set import (
    params,
    models,
)


class GroupLeaderboardSetClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def patch(
        self,
        *,
        data: params.GameCenterLeaderboardSetGroupLeaderboardSetLinkageRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardSetGroupLeaderboardSetLinkageRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterLeaderboardSets/{id}/relationships/groupLeaderboardSet",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GameCenterLeaderboardSetGroupLeaderboardSetLinkageResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterLeaderboardSets/{id}/relationships/groupLeaderboardSet",
            auth_names=["itc-bearer-token"],
            cast_to=models.GameCenterLeaderboardSetGroupLeaderboardSetLinkageResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGroupLeaderboardSetClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def patch(
        self,
        *,
        data: params.GameCenterLeaderboardSetGroupLeaderboardSetLinkageRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardSetGroupLeaderboardSetLinkageRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterLeaderboardSets/{id}/relationships/groupLeaderboardSet",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.GameCenterLeaderboardSetGroupLeaderboardSetLinkageResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterLeaderboardSets/{id}/relationships/groupLeaderboardSet",
            auth_names=["itc-bearer-token"],
            cast_to=models.GameCenterLeaderboardSetGroupLeaderboardSetLinkageResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)