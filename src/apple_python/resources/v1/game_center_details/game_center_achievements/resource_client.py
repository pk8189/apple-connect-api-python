"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    SyncBaseClient,
    encode_param,
    RequestOptions,
    AsyncBaseClient,
    QueryParams,
    default_request_options,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_details.game_center_achievements import models


class GameCenterAchievementsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
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
        fields_game_center_details: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "achievementReleases",
                    "app",
                    "arcadeEnabled",
                    "challengeEnabled",
                    "defaultGroupLeaderboard",
                    "defaultLeaderboard",
                    "gameCenterAchievements",
                    "gameCenterAppVersions",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                    "leaderboardReleases",
                    "leaderboardSetReleases",
                ]
            ]
        ] = None,
        fields_game_center_groups: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievements",
                    "gameCenterDetails",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                    "referenceName",
                ]
            ]
        ] = None,
        filter_archived: typing.Optional[typing.List[str]] = None,
        filter_id: typing.Optional[typing.List[str]] = None,
        filter_reference_name: typing.Optional[typing.List[str]] = None,
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
        limit: typing.Optional[int] = None,
        limit_localizations: typing.Optional[int] = None,
        limit_releases: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementsResponse:
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
        if fields_game_center_details is not None:
            _query["fields[gameCenterDetails]"] = encode_param(
                fields_game_center_details, False
            )
        if fields_game_center_groups is not None:
            _query["fields[gameCenterGroups]"] = encode_param(
                fields_game_center_groups, False
            )
        if filter_archived is not None:
            _query["filter[archived]"] = encode_param(filter_archived, False)
        if filter_id is not None:
            _query["filter[id]"] = encode_param(filter_id, False)
        if filter_reference_name is not None:
            _query["filter[referenceName]"] = encode_param(filter_reference_name, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_localizations is not None:
            _query["limit[localizations]"] = encode_param(limit_localizations, False)
        if limit_releases is not None:
            _query["limit[releases]"] = encode_param(limit_releases, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterDetails/{id}/gameCenterAchievements",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterAchievementsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterAchievementsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
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
        fields_game_center_details: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "achievementReleases",
                    "app",
                    "arcadeEnabled",
                    "challengeEnabled",
                    "defaultGroupLeaderboard",
                    "defaultLeaderboard",
                    "gameCenterAchievements",
                    "gameCenterAppVersions",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                    "leaderboardReleases",
                    "leaderboardSetReleases",
                ]
            ]
        ] = None,
        fields_game_center_groups: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievements",
                    "gameCenterDetails",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                    "referenceName",
                ]
            ]
        ] = None,
        filter_archived: typing.Optional[typing.List[str]] = None,
        filter_id: typing.Optional[typing.List[str]] = None,
        filter_reference_name: typing.Optional[typing.List[str]] = None,
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
        limit: typing.Optional[int] = None,
        limit_localizations: typing.Optional[int] = None,
        limit_releases: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterAchievementsResponse:
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
        if fields_game_center_details is not None:
            _query["fields[gameCenterDetails]"] = encode_param(
                fields_game_center_details, False
            )
        if fields_game_center_groups is not None:
            _query["fields[gameCenterGroups]"] = encode_param(
                fields_game_center_groups, False
            )
        if filter_archived is not None:
            _query["filter[archived]"] = encode_param(filter_archived, False)
        if filter_id is not None:
            _query["filter[id]"] = encode_param(filter_id, False)
        if filter_reference_name is not None:
            _query["filter[referenceName]"] = encode_param(filter_reference_name, False)
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if limit_localizations is not None:
            _query["limit[localizations]"] = encode_param(limit_localizations, False)
        if limit_releases is not None:
            _query["limit[releases]"] = encode_param(limit_releases, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterDetails/{id}/gameCenterAchievements",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterAchievementsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)