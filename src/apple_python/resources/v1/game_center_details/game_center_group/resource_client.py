"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    QueryParams,
    default_request_options,
    RequestOptions,
    SyncBaseClient,
    AsyncBaseClient,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_details.game_center_group import models


class GameCenterGroupClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
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
        fields_game_center_leaderboards: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "archived",
                    "defaultFormatter",
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "groupLeaderboard",
                    "localizations",
                    "recurrenceDuration",
                    "recurrenceRule",
                    "recurrenceStartDate",
                    "referenceName",
                    "releases",
                    "scoreRangeEnd",
                    "scoreRangeStart",
                    "scoreSortType",
                    "submissionType",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievements",
                    "gameCenterDetails",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                ]
            ]
        ] = None,
        limit_game_center_achievements: typing.Optional[int] = None,
        limit_game_center_details: typing.Optional[int] = None,
        limit_game_center_leaderboard_sets: typing.Optional[int] = None,
        limit_game_center_leaderboards: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterGroupResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
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
        if fields_game_center_leaderboard_sets is not None:
            _query["fields[gameCenterLeaderboardSets]"] = encode_param(
                fields_game_center_leaderboard_sets, False
            )
        if fields_game_center_leaderboards is not None:
            _query["fields[gameCenterLeaderboards]"] = encode_param(
                fields_game_center_leaderboards, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_game_center_achievements is not None:
            _query["limit[gameCenterAchievements]"] = encode_param(
                limit_game_center_achievements, False
            )
        if limit_game_center_details is not None:
            _query["limit[gameCenterDetails]"] = encode_param(
                limit_game_center_details, False
            )
        if limit_game_center_leaderboard_sets is not None:
            _query["limit[gameCenterLeaderboardSets]"] = encode_param(
                limit_game_center_leaderboard_sets, False
            )
        if limit_game_center_leaderboards is not None:
            _query["limit[gameCenterLeaderboards]"] = encode_param(
                limit_game_center_leaderboards, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterDetails/{id}/gameCenterGroup",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterGroupResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterGroupClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
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
        fields_game_center_leaderboards: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "archived",
                    "defaultFormatter",
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "groupLeaderboard",
                    "localizations",
                    "recurrenceDuration",
                    "recurrenceRule",
                    "recurrenceStartDate",
                    "referenceName",
                    "releases",
                    "scoreRangeEnd",
                    "scoreRangeStart",
                    "scoreSortType",
                    "submissionType",
                    "vendorIdentifier",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterAchievements",
                    "gameCenterDetails",
                    "gameCenterLeaderboardSets",
                    "gameCenterLeaderboards",
                ]
            ]
        ] = None,
        limit_game_center_achievements: typing.Optional[int] = None,
        limit_game_center_details: typing.Optional[int] = None,
        limit_game_center_leaderboard_sets: typing.Optional[int] = None,
        limit_game_center_leaderboards: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterGroupResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
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
        if fields_game_center_leaderboard_sets is not None:
            _query["fields[gameCenterLeaderboardSets]"] = encode_param(
                fields_game_center_leaderboard_sets, False
            )
        if fields_game_center_leaderboards is not None:
            _query["fields[gameCenterLeaderboards]"] = encode_param(
                fields_game_center_leaderboards, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit_game_center_achievements is not None:
            _query["limit[gameCenterAchievements]"] = encode_param(
                limit_game_center_achievements, False
            )
        if limit_game_center_details is not None:
            _query["limit[gameCenterDetails]"] = encode_param(
                limit_game_center_details, False
            )
        if limit_game_center_leaderboard_sets is not None:
            _query["limit[gameCenterLeaderboardSets]"] = encode_param(
                limit_game_center_leaderboard_sets, False
            )
        if limit_game_center_leaderboards is not None:
            _query["limit[gameCenterLeaderboards]"] = encode_param(
                limit_game_center_leaderboards, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterDetails/{id}/gameCenterGroup",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterGroupResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
