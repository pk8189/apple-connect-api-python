"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class InAppPurchaseV2UpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    family_sharable: typing_extensions.NotRequired[bool]
    name: typing_extensions.NotRequired[str]
    review_note: typing_extensions.NotRequired[str]


class _SerializerInAppPurchaseV2UpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for InAppPurchaseV2UpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    family_sharable: typing.Optional[bool] = pydantic.Field(
        alias="familySharable", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    review_note: typing.Optional[str] = pydantic.Field(alias="reviewNote", default=None)


class InAppPurchaseV2CreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    family_sharable: typing_extensions.NotRequired[bool]
    in_app_purchase_type: typing_extensions.Required[
        typing_extensions.Literal[
            "CONSUMABLE", "NON_CONSUMABLE", "NON_RENEWING_SUBSCRIPTION"
        ]
    ]
    name: typing_extensions.Required[str]
    product_id: typing_extensions.Required[str]
    review_note: typing_extensions.NotRequired[str]


class _SerializerInAppPurchaseV2CreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for InAppPurchaseV2CreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    family_sharable: typing.Optional[bool] = pydantic.Field(
        alias="familySharable", default=None
    )
    in_app_purchase_type: typing_extensions.Literal[
        "CONSUMABLE", "NON_CONSUMABLE", "NON_RENEWING_SUBSCRIPTION"
    ] = pydantic.Field(alias="inAppPurchaseType")
    name: str = pydantic.Field(alias="name")
    product_id: str = pydantic.Field(alias="productId")
    review_note: typing.Optional[str] = pydantic.Field(alias="reviewNote", default=None)


class InAppPurchaseV2CreateRequestDataRelationshipsAppData(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["apps"]]


class _SerializerInAppPurchaseV2CreateRequestDataRelationshipsAppData(
    pydantic.BaseModel
):
    """
    Serializer for InAppPurchaseV2CreateRequestDataRelationshipsAppData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["apps"] = pydantic.Field(alias="type")


class InAppPurchaseV2UpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        InAppPurchaseV2UpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["inAppPurchases"]]


class _SerializerInAppPurchaseV2UpdateRequestData(pydantic.BaseModel):
    """
    Serializer for InAppPurchaseV2UpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerInAppPurchaseV2UpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["inAppPurchases"] = pydantic.Field(alias="type")


class InAppPurchaseV2CreateRequestDataRelationshipsApp(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        InAppPurchaseV2CreateRequestDataRelationshipsAppData
    ]


class _SerializerInAppPurchaseV2CreateRequestDataRelationshipsApp(pydantic.BaseModel):
    """
    Serializer for InAppPurchaseV2CreateRequestDataRelationshipsApp handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerInAppPurchaseV2CreateRequestDataRelationshipsAppData = (
        pydantic.Field(alias="data")
    )


class InAppPurchaseV2UpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[InAppPurchaseV2UpdateRequestData]


class _SerializerInAppPurchaseV2UpdateRequest(pydantic.BaseModel):
    """
    Serializer for InAppPurchaseV2UpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerInAppPurchaseV2UpdateRequestData = pydantic.Field(alias="data")


class InAppPurchaseV2CreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    app: typing_extensions.Required[InAppPurchaseV2CreateRequestDataRelationshipsApp]


class _SerializerInAppPurchaseV2CreateRequestDataRelationships(pydantic.BaseModel):
    """
    Serializer for InAppPurchaseV2CreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app: _SerializerInAppPurchaseV2CreateRequestDataRelationshipsApp = pydantic.Field(
        alias="app"
    )


class InAppPurchaseV2CreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[InAppPurchaseV2CreateRequestDataAttributes]
    relationships: typing_extensions.Required[
        InAppPurchaseV2CreateRequestDataRelationships
    ]
    type: typing_extensions.Required[typing_extensions.Literal["inAppPurchases"]]


class _SerializerInAppPurchaseV2CreateRequestData(pydantic.BaseModel):
    """
    Serializer for InAppPurchaseV2CreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerInAppPurchaseV2CreateRequestDataAttributes = pydantic.Field(
        alias="attributes"
    )
    relationships: _SerializerInAppPurchaseV2CreateRequestDataRelationships = (
        pydantic.Field(alias="relationships")
    )
    type: typing_extensions.Literal["inAppPurchases"] = pydantic.Field(alias="type")


class InAppPurchaseV2CreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[InAppPurchaseV2CreateRequestData]


class _SerializerInAppPurchaseV2CreateRequest(pydantic.BaseModel):
    """
    Serializer for InAppPurchaseV2CreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerInAppPurchaseV2CreateRequestData = pydantic.Field(alias="data")
