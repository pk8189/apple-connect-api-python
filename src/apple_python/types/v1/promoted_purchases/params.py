"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PromotedPurchaseUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    enabled: typing_extensions.NotRequired[bool]
    visible_for_all_users: typing_extensions.NotRequired[bool]


class _SerializerPromotedPurchaseUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for PromotedPurchaseUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    visible_for_all_users: typing.Optional[bool] = pydantic.Field(
        alias="visibleForAllUsers", default=None
    )


class PromotedPurchaseCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    enabled: typing_extensions.NotRequired[bool]
    visible_for_all_users: typing_extensions.Required[bool]


class _SerializerPromotedPurchaseCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for PromotedPurchaseCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    visible_for_all_users: bool = pydantic.Field(alias="visibleForAllUsers")


class PromotedPurchaseCreateRequestDataRelationshipsAppData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["apps"]]


class _SerializerPromotedPurchaseCreateRequestDataRelationshipsAppData(
    pydantic.BaseModel
):
    """
    Serializer for PromotedPurchaseCreateRequestDataRelationshipsAppData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["apps"] = pydantic.Field(alias="type")


class PromotedPurchaseCreateRequestDataRelationshipsInAppPurchaseV2Data(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["inAppPurchases"]]


class _SerializerPromotedPurchaseCreateRequestDataRelationshipsInAppPurchaseV2Data(
    pydantic.BaseModel
):
    """
    Serializer for PromotedPurchaseCreateRequestDataRelationshipsInAppPurchaseV2Data handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["inAppPurchases"] = pydantic.Field(alias="type")


class PromotedPurchaseCreateRequestDataRelationshipsSubscriptionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["subscriptions"]]


class _SerializerPromotedPurchaseCreateRequestDataRelationshipsSubscriptionData(
    pydantic.BaseModel
):
    """
    Serializer for PromotedPurchaseCreateRequestDataRelationshipsSubscriptionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["subscriptions"] = pydantic.Field(alias="type")


class PromotedPurchaseUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        PromotedPurchaseUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["promotedPurchases"]]


class _SerializerPromotedPurchaseUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for PromotedPurchaseUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerPromotedPurchaseUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["promotedPurchases"] = pydantic.Field(alias="type")


class PromotedPurchaseCreateRequestDataRelationshipsApp(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        PromotedPurchaseCreateRequestDataRelationshipsAppData
    ]


class _SerializerPromotedPurchaseCreateRequestDataRelationshipsApp(pydantic.BaseModel):
    """
    Serializer for PromotedPurchaseCreateRequestDataRelationshipsApp handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerPromotedPurchaseCreateRequestDataRelationshipsAppData = (
        pydantic.Field(alias="data")
    )


class PromotedPurchaseCreateRequestDataRelationshipsInAppPurchaseV2(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        PromotedPurchaseCreateRequestDataRelationshipsInAppPurchaseV2Data
    ]


class _SerializerPromotedPurchaseCreateRequestDataRelationshipsInAppPurchaseV2(
    pydantic.BaseModel
):
    """
    Serializer for PromotedPurchaseCreateRequestDataRelationshipsInAppPurchaseV2 handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerPromotedPurchaseCreateRequestDataRelationshipsInAppPurchaseV2Data
    ] = pydantic.Field(alias="data", default=None)


class PromotedPurchaseCreateRequestDataRelationshipsSubscription(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        PromotedPurchaseCreateRequestDataRelationshipsSubscriptionData
    ]


class _SerializerPromotedPurchaseCreateRequestDataRelationshipsSubscription(
    pydantic.BaseModel
):
    """
    Serializer for PromotedPurchaseCreateRequestDataRelationshipsSubscription handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerPromotedPurchaseCreateRequestDataRelationshipsSubscriptionData
    ] = pydantic.Field(alias="data", default=None)


class PromotedPurchaseUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[PromotedPurchaseUpdateRequestData]


class _SerializerPromotedPurchaseUpdateRequest(pydantic.BaseModel):
    """
    Serializer for PromotedPurchaseUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerPromotedPurchaseUpdateRequestData = pydantic.Field(alias="data")


class PromotedPurchaseCreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    app: typing_extensions.Required[PromotedPurchaseCreateRequestDataRelationshipsApp]
    in_app_purchase_v2: typing_extensions.NotRequired[
        PromotedPurchaseCreateRequestDataRelationshipsInAppPurchaseV2
    ]
    subscription: typing_extensions.NotRequired[
        PromotedPurchaseCreateRequestDataRelationshipsSubscription
    ]


class _SerializerPromotedPurchaseCreateRequestDataRelationships(pydantic.BaseModel):
    """
    Serializer for PromotedPurchaseCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app: _SerializerPromotedPurchaseCreateRequestDataRelationshipsApp = pydantic.Field(
        alias="app"
    )
    in_app_purchase_v2: typing.Optional[
        _SerializerPromotedPurchaseCreateRequestDataRelationshipsInAppPurchaseV2
    ] = pydantic.Field(alias="inAppPurchaseV2", default=None)
    subscription: typing.Optional[
        _SerializerPromotedPurchaseCreateRequestDataRelationshipsSubscription
    ] = pydantic.Field(alias="subscription", default=None)


class PromotedPurchaseCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[PromotedPurchaseCreateRequestDataAttributes]
    relationships: typing_extensions.Required[
        PromotedPurchaseCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[typing_extensions.Literal["promotedPurchases"]]


class _SerializerPromotedPurchaseCreateRequestData(pydantic.BaseModel):
    """
    Serializer for PromotedPurchaseCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerPromotedPurchaseCreateRequestDataAttributes = pydantic.Field(
        alias="attributes"
    )
    relationships: _SerializerPromotedPurchaseCreateRequestDataRelationships = (
        pydantic.Field(alias="relationships")
    )
    type: typing_extensions.Literal["promotedPurchases"] = pydantic.Field(alias="type")


class PromotedPurchaseCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[PromotedPurchaseCreateRequestData]


class _SerializerPromotedPurchaseCreateRequest(pydantic.BaseModel):
    """
    Serializer for PromotedPurchaseCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerPromotedPurchaseCreateRequestData = pydantic.Field(alias="data")
