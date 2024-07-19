"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    default_request_options,
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    encode_param,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_leaderboard_sets.localizations import models


class LocalizationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_game_center_leaderboard_set_images: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "gameCenterLeaderboardSetLocalization",
                    "imageAsset",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_set_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterLeaderboardSet",
                    "gameCenterLeaderboardSetImage",
                    "locale",
                    "name",
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_sets: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "gameCenterLeaderboards",
                    "groupLeaderboardSet",
                    "localizations",
                    "referenceName",
                    "releases",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterLeaderboardSet", "gameCenterLeaderboardSetImage"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardSetLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_leaderboard_set_images is not None:
            _query["fields[gameCenterLeaderboardSetImages]"] = encode_param(
                fields_game_center_leaderboard_set_images, False
            )
        if fields_game_center_leaderboard_set_localizations is not None:
            _query["fields[gameCenterLeaderboardSetLocalizations]"] = encode_param(
                fields_game_center_leaderboard_set_localizations, False
            )
        if fields_game_center_leaderboard_sets is not None:
            _query["fields[gameCenterLeaderboardSets]"] = encode_param(
                fields_game_center_leaderboard_sets, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterLeaderboardSets/{id}/localizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardSetLocalizationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncLocalizationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_game_center_leaderboard_set_images: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "gameCenterLeaderboardSetLocalization",
                    "imageAsset",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_set_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterLeaderboardSet",
                    "gameCenterLeaderboardSetImage",
                    "locale",
                    "name",
                ]
            ]
        ] = None,
        fields_game_center_leaderboard_sets: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "gameCenterLeaderboards",
                    "groupLeaderboardSet",
                    "localizations",
                    "referenceName",
                    "releases",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterLeaderboardSet", "gameCenterLeaderboardSetImage"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardSetLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_leaderboard_set_images is not None:
            _query["fields[gameCenterLeaderboardSetImages]"] = encode_param(
                fields_game_center_leaderboard_set_images, False
            )
        if fields_game_center_leaderboard_set_localizations is not None:
            _query["fields[gameCenterLeaderboardSetLocalizations]"] = encode_param(
                fields_game_center_leaderboard_set_localizations, False
            )
        if fields_game_center_leaderboard_sets is not None:
            _query["fields[gameCenterLeaderboardSets]"] = encode_param(
                fields_game_center_leaderboard_sets, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterLeaderboardSets/{id}/localizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardSetLocalizationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)