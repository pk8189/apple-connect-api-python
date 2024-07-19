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
from apple_python.types.v1.game_center_groups.game_center_leaderboards import models


class GameCenterLeaderboardsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
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
        fields_game_center_leaderboard_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail", "gameCenterLeaderboard", "live"
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
        filter_archived: typing.Optional[typing.List[str]] = None,
        filter_id: typing.Optional[typing.List[str]] = None,
        filter_reference_name: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "groupLeaderboard",
                    "localizations",
                    "releases",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_game_center_leaderboard_sets: typing.Optional[int] = None,
        limit_localizations: typing.Optional[int] = None,
        limit_releases: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_details is not None:
            _query["fields[gameCenterDetails]"] = encode_param(
                fields_game_center_details, False
            )
        if fields_game_center_groups is not None:
            _query["fields[gameCenterGroups]"] = encode_param(
                fields_game_center_groups, False
            )
        if fields_game_center_leaderboard_localizations is not None:
            _query["fields[gameCenterLeaderboardLocalizations]"] = encode_param(
                fields_game_center_leaderboard_localizations, False
            )
        if fields_game_center_leaderboard_releases is not None:
            _query["fields[gameCenterLeaderboardReleases]"] = encode_param(
                fields_game_center_leaderboard_releases, False
            )
        if fields_game_center_leaderboard_sets is not None:
            _query["fields[gameCenterLeaderboardSets]"] = encode_param(
                fields_game_center_leaderboard_sets, False
            )
        if fields_game_center_leaderboards is not None:
            _query["fields[gameCenterLeaderboards]"] = encode_param(
                fields_game_center_leaderboards, False
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
        if limit_game_center_leaderboard_sets is not None:
            _query["limit[gameCenterLeaderboardSets]"] = encode_param(
                limit_game_center_leaderboard_sets, False
            )
        if limit_localizations is not None:
            _query["limit[localizations]"] = encode_param(limit_localizations, False)
        if limit_releases is not None:
            _query["limit[releases]"] = encode_param(limit_releases, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterGroups/{id}/gameCenterLeaderboards",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterLeaderboardsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
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
        fields_game_center_leaderboard_releases: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail", "gameCenterLeaderboard", "live"
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
        filter_archived: typing.Optional[typing.List[str]] = None,
        filter_id: typing.Optional[typing.List[str]] = None,
        filter_reference_name: typing.Optional[typing.List[str]] = None,
        include: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterDetail",
                    "gameCenterGroup",
                    "gameCenterLeaderboardSets",
                    "groupLeaderboard",
                    "localizations",
                    "releases",
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        limit_game_center_leaderboard_sets: typing.Optional[int] = None,
        limit_localizations: typing.Optional[int] = None,
        limit_releases: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_game_center_details is not None:
            _query["fields[gameCenterDetails]"] = encode_param(
                fields_game_center_details, False
            )
        if fields_game_center_groups is not None:
            _query["fields[gameCenterGroups]"] = encode_param(
                fields_game_center_groups, False
            )
        if fields_game_center_leaderboard_localizations is not None:
            _query["fields[gameCenterLeaderboardLocalizations]"] = encode_param(
                fields_game_center_leaderboard_localizations, False
            )
        if fields_game_center_leaderboard_releases is not None:
            _query["fields[gameCenterLeaderboardReleases]"] = encode_param(
                fields_game_center_leaderboard_releases, False
            )
        if fields_game_center_leaderboard_sets is not None:
            _query["fields[gameCenterLeaderboardSets]"] = encode_param(
                fields_game_center_leaderboard_sets, False
            )
        if fields_game_center_leaderboards is not None:
            _query["fields[gameCenterLeaderboards]"] = encode_param(
                fields_game_center_leaderboards, False
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
        if limit_game_center_leaderboard_sets is not None:
            _query["limit[gameCenterLeaderboardSets]"] = encode_param(
                limit_game_center_leaderboard_sets, False
            )
        if limit_localizations is not None:
            _query["limit[localizations]"] = encode_param(limit_localizations, False)
        if limit_releases is not None:
            _query["limit[releases]"] = encode_param(limit_releases, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/gameCenterGroups/{id}/gameCenterLeaderboards",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
