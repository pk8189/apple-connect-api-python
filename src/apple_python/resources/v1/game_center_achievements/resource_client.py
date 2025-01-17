"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    QueryParams,
    to_encodable,
    SyncBaseClient,
    AsyncBaseClient,
    encode_param,
    RequestOptions,
)
from apple_python.resources.v1.game_center_achievements.group_achievement import (
    GroupAchievementClient,
    AsyncGroupAchievementClient,
)
from apple_python.resources.v1.game_center_achievements.localizations import (
    AsyncLocalizationsClient,
    LocalizationsClient,
)
from apple_python.resources.v1.game_center_achievements.relationships import (
    AsyncRelationshipsClient,
    RelationshipsClient,
)
from apple_python.resources.v1.game_center_achievements.releases import (
    AsyncReleasesClient,
    ReleasesClient,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_achievements import models, params


class GameCenterAchievementsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.group_achievement = GroupAchievementClient(base_client=self._base_client)
        self.localizations = LocalizationsClient(base_client=self._base_client)
        self.relationships = RelationshipsClient(base_client=self._base_client)
        self.releases = ReleasesClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.GameCenterAchievementCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerGameCenterAchievementCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/gameCenterAchievements",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterAchievementResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.GameCenterAchievementUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerGameCenterAchievementUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterAchievements/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterAchievementResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        id: str,
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
        fields_game_center_achievement_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievement", "gameCenterDetail", "live"
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
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "groupAchievement",
                    "localizations",
                    "releases",
                ]
            ]
        ] = None,
        limit_localizations: typing.Optional[int] = None,
        limit_releases: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_achievement_localizations is not None:
            _query["fields[gameCenterAchievementLocalizations]"] = encode_param(
                fields_game_center_achievement_localizations, False
            )
        if fields_game_center_achievement_releases is not None:
            _query["fields[gameCenterAchievementReleases]"] = encode_param(
                fields_game_center_achievement_releases, False
            )
        if fields_game_center_achievements is not None:
            _query["fields[gameCenterAchievements]"] = encode_param(
                fields_game_center_achievements, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_localizations is not None:
            _query["limit[localizations]"] = encode_param(limit_localizations, False)
        if limit_releases is not None:
            _query["limit[releases]"] = encode_param(limit_releases, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterAchievements/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterAchievementResponse,
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
            path=f"/v1/gameCenterAchievements/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterAchievementsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.group_achievement = AsyncGroupAchievementClient(
            base_client=self._base_client
        )
        self.localizations = AsyncLocalizationsClient(base_client=self._base_client)
        self.relationships = AsyncRelationshipsClient(base_client=self._base_client)
        self.releases = AsyncReleasesClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.GameCenterAchievementCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerGameCenterAchievementCreateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/gameCenterAchievements",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterAchievementResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.GameCenterAchievementUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerGameCenterAchievementUpdateRequest
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterAchievements/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterAchievementResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        id: str,
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
        fields_game_center_achievement_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievement", "gameCenterDetail", "live"
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
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "groupAchievement",
                    "localizations",
                    "releases",
                ]
            ]
        ] = None,
        limit_localizations: typing.Optional[int] = None,
        limit_releases: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_achievement_localizations is not None:
            _query["fields[gameCenterAchievementLocalizations]"] = encode_param(
                fields_game_center_achievement_localizations, False
            )
        if fields_game_center_achievement_releases is not None:
            _query["fields[gameCenterAchievementReleases]"] = encode_param(
                fields_game_center_achievement_releases, False
            )
        if fields_game_center_achievements is not None:
            _query["fields[gameCenterAchievements]"] = encode_param(
                fields_game_center_achievements, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_localizations is not None:
            _query["limit[localizations]"] = encode_param(limit_localizations, False)
        if limit_releases is not None:
            _query["limit[releases]"] = encode_param(limit_releases, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterAchievements/{id}",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterAchievementResponse,
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
            path=f"/v1/gameCenterAchievements/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
