"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    RequestOptions,
    encode_param,
    QueryParams,
    AsyncBaseClient,
    default_request_options,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_achievements.localizations import models


class LocalizationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_game_center_achievement_images: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "gameCenterAchievementLocalization",
                    "imageAsset",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_game_center_achievement_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "afterEarnedDescription",
                    "beforeEarnedDescription",
                    "gameCenterAchievement",
                    "gameCenterAchievementImage",
                    "locale",
                    "name",
                ]
            ]
        ] = None,
        fields_game_center_achievements: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "archived",
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "groupAchievement",
                    "localizations",
                    "points",
                    "referenceName",
                    "releases",
                    "repeatable",
                    "showBeforeEarned",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievement", "gameCenterAchievementImage"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_achievement_images is not None:
            _query["fields[gameCenterAchievementImages]"] = encode_param(
                fields_game_center_achievement_images, False
            )
        if fields_game_center_achievement_localizations is not None:
            _query["fields[gameCenterAchievementLocalizations]"] = encode_param(
                fields_game_center_achievement_localizations, False
            )
        if fields_game_center_achievements is not None:
            _query["fields[gameCenterAchievements]"] = encode_param(
                fields_game_center_achievements, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterAchievements/{id}/localizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterAchievementLocalizationsResponse,
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
        fields_game_center_achievement_images: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "assetDeliveryState",
                    "fileName",
                    "fileSize",
                    "gameCenterAchievementLocalization",
                    "imageAsset",
                    "uploadOperations",
                    "uploaded",
                ]
            ]
        ] = None,
        fields_game_center_achievement_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "afterEarnedDescription",
                    "beforeEarnedDescription",
                    "gameCenterAchievement",
                    "gameCenterAchievementImage",
                    "locale",
                    "name",
                ]
            ]
        ] = None,
        fields_game_center_achievements: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "archived",
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "groupAchievement",
                    "localizations",
                    "points",
                    "referenceName",
                    "releases",
                    "repeatable",
                    "showBeforeEarned",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievement", "gameCenterAchievementImage"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_achievement_images is not None:
            _query["fields[gameCenterAchievementImages]"] = encode_param(
                fields_game_center_achievement_images, False
            )
        if fields_game_center_achievement_localizations is not None:
            _query["fields[gameCenterAchievementLocalizations]"] = encode_param(
                fields_game_center_achievement_localizations, False
            )
        if fields_game_center_achievements is not None:
            _query["fields[gameCenterAchievements]"] = encode_param(
                fields_game_center_achievements, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterAchievements/{id}/localizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterAchievementLocalizationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
