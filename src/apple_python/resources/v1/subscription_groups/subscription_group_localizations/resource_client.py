"""File Generated by Sideko (sideko.dev)"""

from apple_python.core import (
    default_request_options,
    AsyncBaseClient,
    SyncBaseClient,
    encode_param,
    QueryParams,
    RequestOptions,
)
import typing
import typing_extensions
from apple_python.types.v1.subscription_groups.subscription_group_localizations import (
    models,
)


class SubscriptionGroupLocalizationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        id: str,
        fields_subscription_group_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "customAppName", "locale", "name", "state", "subscriptionGroup"
                ]
            ]
        ] = None,
        fields_subscription_groups: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "referenceName",
                    "subscriptionGroupLocalizations",
                    "subscriptions",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["subscriptionGroup"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionGroupLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_group_localizations is not None:
            _query["fields[subscriptionGroupLocalizations]"] = encode_param(
                fields_subscription_group_localizations, False
            )
        if fields_subscription_groups is not None:
            _query["fields[subscriptionGroups]"] = encode_param(
                fields_subscription_groups, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionGroups/{id}/subscriptionGroupLocalizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionGroupLocalizationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncSubscriptionGroupLocalizationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        id: str,
        fields_subscription_group_localizations: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "customAppName", "locale", "name", "state", "subscriptionGroup"
                ]
            ]
        ] = None,
        fields_subscription_groups: typing.Optional[
            typing.List[
                typing_extensions.Literal[
                    "app",
                    "referenceName",
                    "subscriptionGroupLocalizations",
                    "subscriptions",
                ]
            ]
        ] = None,
        include: typing.Optional[
            typing.List[typing_extensions.Literal["subscriptionGroup"]]
        ] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionGroupLocalizationsResponse:
        """
        no description available
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if fields_subscription_group_localizations is not None:
            _query["fields[subscriptionGroupLocalizations]"] = encode_param(
                fields_subscription_group_localizations, False
            )
        if fields_subscription_groups is not None:
            _query["fields[subscriptionGroups]"] = encode_param(
                fields_subscription_groups, False
            )
        if include is not None:
            _query["include"] = encode_param(include, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/v1/subscriptionGroups/{id}/subscriptionGroupLocalizations",
            auth_names=["itc-bearer-token"],
            query_params=_query,
            cast_to=models.SubscriptionGroupLocalizationsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
