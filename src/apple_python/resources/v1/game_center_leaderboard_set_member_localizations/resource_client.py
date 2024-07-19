"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    encode_param,
    RequestOptions,
    to_encodable,
    SyncBaseClient,
    default_request_options,
    QueryParams,
    AsyncBaseClient,
)
from apple_python.resources.v1.game_center_leaderboard_set_member_localizations.game_center_leaderboard import (
    GameCenterLeaderboardClient,
    AsyncGameCenterLeaderboardClient,
)
from apple_python.resources.v1.game_center_leaderboard_set_member_localizations.game_center_leaderboard_set import (
    AsyncGameCenterLeaderboardSetClient,
    GameCenterLeaderboardSetClient,
)
import typing
import typing_extensions
from apple_python.types.v1.game_center_leaderboard_set_member_localizations import (
    models,
    params,
)


class GameCenterLeaderboardSetMemberLocalizationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.game_center_leaderboard = GameCenterLeaderboardClient(
            base_client=self._base_client
        )
        self.game_center_leaderboard_set = GameCenterLeaderboardSetClient(
            base_client=self._base_client
        )

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.GameCenterLeaderboardSetMemberLocalizationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardSetMemberLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardSetMemberLocalizationCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/v1/gameCenterLeaderboardSetMemberLocalizations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterLeaderboardSetMemberLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def patch(
        self,
        *,
        data: params.GameCenterLeaderboardSetMemberLocalizationUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardSetMemberLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardSetMemberLocalizationUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterLeaderboardSetMemberLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterLeaderboardSetMemberLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        filter_game_center_leaderboard_set: typing.List[str],
        filter_game_center_leaderboard: typing.List[str],
        fields_game_center_leaderboard_set_member_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterLeaderboard",
                    "gameCenterLeaderboardSet",
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
                    "gameCenterLeaderboard", "gameCenterLeaderboardSet"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardSetMemberLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["filter[gameCenterLeaderboardSet]"] = encode_param(
            filter_game_center_leaderboard_set, False
        )
        _query["filter[gameCenterLeaderboard]"] = encode_param(
            filter_game_center_leaderboard, False
        )
        if fields_game_center_leaderboard_set_member_localizations is not None:
            _query["fields[gameCenterLeaderboardSetMemberLocalizations]"] = (
                encode_param(
                    fields_game_center_leaderboard_set_member_localizations, False
                )
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
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path="/v1/gameCenterLeaderboardSetMemberLocalizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardSetMemberLocalizationsResponse,
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
            path=f"/v1/gameCenterLeaderboardSetMemberLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGameCenterLeaderboardSetMemberLocalizationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.game_center_leaderboard = AsyncGameCenterLeaderboardClient(
            base_client=self._base_client
        )
        self.game_center_leaderboard_set = AsyncGameCenterLeaderboardSetClient(
            base_client=self._base_client
        )

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.GameCenterLeaderboardSetMemberLocalizationCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardSetMemberLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardSetMemberLocalizationCreateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/v1/gameCenterLeaderboardSetMemberLocalizations",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterLeaderboardSetMemberLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def patch(
        self,
        *,
        data: params.GameCenterLeaderboardSetMemberLocalizationUpdateRequest,
        id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardSetMemberLocalizationResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerGameCenterLeaderboardSetMemberLocalizationUpdateRequest,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PATCH",
            path=f"/v1/gameCenterLeaderboardSetMemberLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            json=_json,
            cast_to=models.GameCenterLeaderboardSetMemberLocalizationResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        filter_game_center_leaderboard_set: typing.List[str],
        filter_game_center_leaderboard: typing.List[str],
        fields_game_center_leaderboard_set_member_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "gameCenterLeaderboard",
                    "gameCenterLeaderboardSet",
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
                    "gameCenterLeaderboard", "gameCenterLeaderboardSet"
                ]
            ]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GameCenterLeaderboardSetMemberLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["filter[gameCenterLeaderboardSet]"] = encode_param(
            filter_game_center_leaderboard_set, False
        )
        _query["filter[gameCenterLeaderboard]"] = encode_param(
            filter_game_center_leaderboard, False
        )
        if fields_game_center_leaderboard_set_member_localizations is not None:
            _query["fields[gameCenterLeaderboardSetMemberLocalizations]"] = (
                encode_param(
                    fields_game_center_leaderboard_set_member_localizations, False
                )
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
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path="/v1/gameCenterLeaderboardSetMemberLocalizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.GameCenterLeaderboardSetMemberLocalizationsResponse,
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
            path=f"/v1/gameCenterLeaderboardSetMemberLocalizations/{id}",
            auth_names=["itc-bearer-token"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
