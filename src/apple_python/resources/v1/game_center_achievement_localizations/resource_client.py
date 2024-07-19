"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    AsyncBaseClient,
    encode_param,
    to_encodable,
)
from apple_python.resources.v1.game_center_achievement_localizations.game_center_achievement import (
    GameCenterAchievementClient,
    AsyncGameCenterAchievementClient,
)
from apple_python.resources.v1.game_center_achievement_localizations.game_center_achievement_image import (
    AsyncGameCenterAchievementImageClient,
    GameCenterAchievementImageClient,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_achievement_localizations import params, models


class GameCenterAchievementLocalizationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.game_center_achievement = GameCenterAchievementClient(
            base_client=self._base_client
        )
        self.game_center_achievement_image = GameCenterAchievementImageClient(
            base_client=self._base_client
        )

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.GameCenterAchievementLocalizationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterAchievementLocalizationCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/gameCenterAchievementLocalizations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterAchievementLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.GameCenterAchievementLocalizationUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterAchievementLocalizationUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterAchievementLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterAchievementLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementLocalizationResponse:
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
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterAchievementLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterAchievementLocalizationResponse,
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
            path=f"/v1/gameCenterAchievementLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterAchievementLocalizationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.game_center_achievement = AsyncGameCenterAchievementClient(
            base_client=self._base_client
        )
        self.game_center_achievement_image = AsyncGameCenterAchievementImageClient(
            base_client=self._base_client
        )

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.GameCenterAchievementLocalizationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterAchievementLocalizationCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/gameCenterAchievementLocalizations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterAchievementLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.GameCenterAchievementLocalizationUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterAchievementLocalizationUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterAchievementLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterAchievementLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementLocalizationResponse:
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
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterAchievementLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterAchievementLocalizationResponse,
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
            path=f"/v1/gameCenterAchievementLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)