"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class InAppPurchaseAvailabilityCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    available_in_new_territories: typing_extensions.Required[bool]


class _SerializerInAppPurchaseAvailabilityCreateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for InAppPurchaseAvailabilityCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    available_in_new_territories: bool = pydantic.Field(
        alias="availableInNewTerritories"
    )


class InAppPurchaseAvailabilityCreateRequestDataRelationshipsAvailableTerritoriesDataItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["territories"]]


class _SerializerInAppPurchaseAvailabilityCreateRequestDataRelationshipsAvailableTerritoriesDataItem(
    pydantic.BaseModel
):
    """
    Serializer for InAppPurchaseAvailabilityCreateRequestDataRelationshipsAvailableTerritoriesDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["territories"] = pydantic.Field(alias="type")


class InAppPurchaseAvailabilityCreateRequestDataRelationshipsInAppPurchaseData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["inAppPurchases"]]


class _SerializerInAppPurchaseAvailabilityCreateRequestDataRelationshipsInAppPurchaseData(
    pydantic.BaseModel
):
    """
    Serializer for InAppPurchaseAvailabilityCreateRequestDataRelationshipsInAppPurchaseData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["inAppPurchases"] = pydantic.Field(alias="type")


class InAppPurchaseAvailabilityCreateRequestDataRelationshipsAvailableTerritories(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        typing.List[
            InAppPurchaseAvailabilityCreateRequestDataRelationshipsAvailableTerritoriesDataItem
        ]
    ]


class _SerializerInAppPurchaseAvailabilityCreateRequestDataRelationshipsAvailableTerritories(
    pydantic.BaseModel
):
    """
    Serializer for InAppPurchaseAvailabilityCreateRequestDataRelationshipsAvailableTerritories handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.List[
        _SerializerInAppPurchaseAvailabilityCreateRequestDataRelationshipsAvailableTerritoriesDataItem
    ] = pydantic.Field(alias="data")


class InAppPurchaseAvailabilityCreateRequestDataRelationshipsInAppPurchase(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        InAppPurchaseAvailabilityCreateRequestDataRelationshipsInAppPurchaseData
    ]


class _SerializerInAppPurchaseAvailabilityCreateRequestDataRelationshipsInAppPurchase(
    pydantic.BaseModel
):
    """
    Serializer for InAppPurchaseAvailabilityCreateRequestDataRelationshipsInAppPurchase handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerInAppPurchaseAvailabilityCreateRequestDataRelationshipsInAppPurchaseData = pydantic.Field(
        alias="data"
    )


class InAppPurchaseAvailabilityCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    available_territories: typing_extensions.Required[
        InAppPurchaseAvailabilityCreateRequestDataRelationshipsAvailableTerritories
    ]
    in_app_purchase: typing_extensions.Required[
        InAppPurchaseAvailabilityCreateRequestDataRelationshipsInAppPurchase
    ]


class _SerializerInAppPurchaseAvailabilityCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for InAppPurchaseAvailabilityCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    available_territories: _SerializerInAppPurchaseAvailabilityCreateRequestDataRelationshipsAvailableTerritories = pydantic.Field(
        alias="availableTerritories"
    )
    in_app_purchase: _SerializerInAppPurchaseAvailabilityCreateRequestDataRelationshipsInAppPurchase = pydantic.Field(
        alias="inAppPurchase"
    )


class InAppPurchaseAvailabilityCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        InAppPurchaseAvailabilityCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        InAppPurchaseAvailabilityCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["inAppPurchaseAvailabilities"]
    ]


class _SerializerInAppPurchaseAvailabilityCreateRequestData(pydantic.BaseModel):
    """
    Serializer for InAppPurchaseAvailabilityCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerInAppPurchaseAvailabilityCreateRequestDataAttributes = (
        pydantic.Field(alias="attributes")
    )
    relationships: _SerializerInAppPurchaseAvailabilityCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["inAppPurchaseAvailabilities"] = pydantic.Field(
        alias="type"
    )


class InAppPurchaseAvailabilityCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[InAppPurchaseAvailabilityCreateRequestData]


class _SerializerInAppPurchaseAvailabilityCreateRequest(pydantic.BaseModel):
    """
    Serializer for InAppPurchaseAvailabilityCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerInAppPurchaseAvailabilityCreateRequestData = pydantic.Field(
        alias="data"
    )
