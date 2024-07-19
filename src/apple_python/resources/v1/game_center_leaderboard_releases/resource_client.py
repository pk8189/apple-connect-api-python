"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    AsyncBaseClient,
    SyncBaseClient,
    QueryParams,
    to_encodable,
    RequestOptions,
    default_request_options,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_leaderboard_releases import params, models


class GameCenterLeaderboardReleasesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.GameCenterLeaderboardReleaseCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardReleaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardReleaseCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/gameCenterLeaderboardReleases",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterLeaderboardReleaseResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
        fields_game_center_leaderboard_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail", "gameCenterLeaderboard", "live"
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["gameCenterDetail", "gameCenterLeaderboard"]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardReleaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_leaderboard_releases is not None:
            _query["fields[gameCenterLeaderboardReleases]"] = encode_param(
                fields_game_center_leaderboard_releases, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterLeaderboardReleases/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardReleaseResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/gameCenterLeaderboardReleases/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterLeaderboardReleasesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.GameCenterLeaderboardReleaseCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardReleaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardReleaseCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/gameCenterLeaderboardReleases",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterLeaderboardReleaseResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
        fields_game_center_leaderboard_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail", "gameCenterLeaderboard", "live"
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal["gameCenterDetail", "gameCenterLeaderboard"]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardReleaseResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_leaderboard_releases is not None:
            _query["fields[gameCenterLeaderboardReleases]"] = encode_param(
                fields_game_center_leaderboard_releases, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterLeaderboardReleases/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardReleaseResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/gameCenterLeaderboardReleases/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
