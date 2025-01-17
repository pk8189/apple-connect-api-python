"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appStoreVersions"]]


class _SerializerAppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionData(
    pydantic.BaseModel
):
    """
    Serializer for AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appStoreVersions"] = pydantic.Field(alias="type")


class AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionExperimentTreatmentData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["appStoreVersionExperimentTreatments"]
    ]


class _SerializerAppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionExperimentTreatmentData(
    pydantic.BaseModel
):
    """
    Serializer for AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionExperimentTreatmentData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appStoreVersionExperimentTreatments"] = (
        pydantic.Field(alias="type")
    )


class AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersion(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionData
    ]


class _SerializerAppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersion(
    pydantic.BaseModel
):
    """
    Serializer for AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersion handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionData = pydantic.Field(
        alias="data"
    )


class AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionExperimentTreatment(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionExperimentTreatmentData
    ]


class _SerializerAppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionExperimentTreatment(
    pydantic.BaseModel
):
    """
    Serializer for AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionExperimentTreatment handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionExperimentTreatmentData = pydantic.Field(
        alias="data"
    )


class AppStoreVersionPromotionCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    app_store_version: typing_extensions.Required[
        AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersion
    ]
    app_store_version_experiment_treatment: typing_extensions.Required[
        AppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionExperimentTreatment
    ]


class _SerializerAppStoreVersionPromotionCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for AppStoreVersionPromotionCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_store_version: _SerializerAppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersion = pydantic.Field(
        alias="appStoreVersion"
    )
    app_store_version_experiment_treatment: _SerializerAppStoreVersionPromotionCreateRequestDataRelationshipsAppStoreVersionExperimentTreatment = pydantic.Field(
        alias="appStoreVersionExperimentTreatment"
    )


class AppStoreVersionPromotionCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    relationships: typing_extensions.Required[
        AppStoreVersionPromotionCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["appStoreVersionPromotions"]
    ]


class _SerializerAppStoreVersionPromotionCreateRequestData(pydantic.BaseModel):
    """
    Serializer for AppStoreVersionPromotionCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    relationships: _SerializerAppStoreVersionPromotionCreateRequestDataRelationships = (
        pydantic.Field(alias="relationships")
    )
    type: typing_extensions.Literal["appStoreVersionPromotions"] = pydantic.Field(
        alias="type"
    )


class AppStoreVersionPromotionCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppStoreVersionPromotionCreateRequestData]


class _SerializerAppStoreVersionPromotionCreateRequest(pydantic.BaseModel):
    """
    Serializer for AppStoreVersionPromotionCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppStoreVersionPromotionCreateRequestData = pydantic.Field(
        alias="data"
    )
