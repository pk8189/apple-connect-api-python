"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    SyncBaseClient,
    QueryParams,
    encode_param,
    AsyncBaseClient,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_leaderboard_localizations.game_center_leaderboard_image import (
    models,
)


class GameCenterLeaderboardImageClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_game_center_leaderboard_images: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "gameCenterLeaderboardLocalization",
                    "imageAsset",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "formatterOverride",
                    "formatterSuffix",
                    "formatterSuffixSingular",
                    "gameCenterLeaderboard",
                    "gameCenterLeaderboardImage",
                    "locale",
                    "name",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["gameCenterLeaderboardLocalization"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardImageResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_leaderboard_images is not None:
            _query["fields[gameCenterLeaderboardImages]"] = encode_param(
                fields_game_center_leaderboard_images, False
            )
        if fields_game_center_leaderboard_localizations is not None:
            _query["fields[gameCenterLeaderboardLocalizations]"] = encode_param(
                fields_game_center_leaderboard_localizations, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterLeaderboardLocalizations/{id}/gameCenterLeaderboardImage",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardImageResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterLeaderboardImageClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_game_center_leaderboard_images: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "gameCenterLeaderboardLocalization",
                    "imageAsset",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "formatterOverride",
                    "formatterSuffix",
                    "formatterSuffixSingular",
                    "gameCenterLeaderboard",
                    "gameCenterLeaderboardImage",
                    "locale",
                    "name",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["gameCenterLeaderboardLocalization"]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardImageResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_leaderboard_images is not None:
            _query["fields[gameCenterLeaderboardImages]"] = encode_param(
                fields_game_center_leaderboard_images, False
            )
        if fields_game_center_leaderboard_localizations is not None:
            _query["fields[gameCenterLeaderboardLocalizations]"] = encode_param(
                fields_game_center_leaderboard_localizations, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterLeaderboardLocalizations/{id}/gameCenterLeaderboardImage",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardImageResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
