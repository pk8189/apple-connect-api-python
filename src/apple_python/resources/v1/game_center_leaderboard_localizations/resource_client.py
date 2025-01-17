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
from apple_python.resources.v1.game_center_leaderboard_localizations.game_center_leaderboard_image import (
    GameCenterLeaderboardImageClient,
    AsyncGameCenterLeaderboardImageClient,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_leaderboard_localizations import params, models


class GameCenterLeaderboardLocalizationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.game_center_leaderboard_image = GameCenterLeaderboardImageClient(
            base_client=self._base_client
        )

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.GameCenterLeaderboardLocalizationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardLocalizationCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/gameCenterLeaderboardLocalizations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterLeaderboardLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.GameCenterLeaderboardLocalizationUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardLocalizationUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterLeaderboardLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterLeaderboardLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
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
            typing.List[
                typing_extensions.Literal[
                    "gameCenterLeaderboard", "gameCenterLeaderboardImage"
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardLocalizationResponse:
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
            path=f"/v1/gameCenterLeaderboardLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardLocalizationResponse,
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
            path=f"/v1/gameCenterLeaderboardLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterLeaderboardLocalizationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.game_center_leaderboard_image = AsyncGameCenterLeaderboardImageClient(
            base_client=self._base_client
        )

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.GameCenterLeaderboardLocalizationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardLocalizationCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/gameCenterLeaderboardLocalizations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterLeaderboardLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.GameCenterLeaderboardLocalizationUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardLocalizationUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterLeaderboardLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterLeaderboardLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
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
            typing.List[
                typing_extensions.Literal[
                    "gameCenterLeaderboard", "gameCenterLeaderboardImage"
                ]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardLocalizationResponse:
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
            path=f"/v1/gameCenterLeaderboardLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardLocalizationResponse,
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
            path=f"/v1/gameCenterLeaderboardLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
