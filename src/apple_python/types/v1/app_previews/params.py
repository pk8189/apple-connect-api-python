"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppPreviewUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    preview_frame_time_code: typing_extensions.NotRequired[str]
    source_file_checksum: typing_extensions.NotRequired[str]
    uploaded: typing_extensions.NotRequired[bool]


class _SerializerAppPreviewUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for AppPreviewUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    preview_frame_time_code: typing.Optional[str] = pydantic.Field(
        alias="previewFrameTimeCode", default=None
    )
    source_file_checksum: typing.Optional[str] = pydantic.Field(
        alias="sourceFileChecksum", default=None
    )
    uploaded: typing.Optional[bool] = pydantic.Field(alias="uploaded", default=None)


class AppPreviewCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    file_name: typing_extensions.Required[str]
    file_size: typing_extensions.Required[int]
    mime_type: typing_extensions.NotRequired[str]
    preview_frame_time_code: typing_extensions.NotRequired[str]


class _SerializerAppPreviewCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for AppPreviewCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    file_name: str = pydantic.Field(alias="fileName")
    file_size: int = pydantic.Field(alias="fileSize")
    mime_type: typing.Optional[str] = pydantic.Field(alias="mimeType", default=None)
    preview_frame_time_code: typing.Optional[str] = pydantic.Field(
        alias="previewFrameTimeCode", default=None
    )


class AppPreviewCreateRequestDataRelationshipsAppPreviewSetData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appPreviewSets"]]


class _SerializerAppPreviewCreateRequestDataRelationshipsAppPreviewSetData(
    pydantic.BaseModel
):
    """
    Serializer for AppPreviewCreateRequestDataRelationshipsAppPreviewSetData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appPreviewSets"] = pydantic.Field(alias="type")


class AppPreviewUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[AppPreviewUpdateRequestDataAttributes]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appPreviews"]]


class _SerializerAppPreviewUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for AppPreviewUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[_SerializerAppPreviewUpdateRequestDataAttributes] = (
        pydantic.Field(alias="attributes", default=None)
    )
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appPreviews"] = pydantic.Field(alias="type")


class AppPreviewCreateRequestDataRelationshipsAppPreviewSet(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppPreviewCreateRequestDataRelationshipsAppPreviewSetData
    ]


class _SerializerAppPreviewCreateRequestDataRelationshipsAppPreviewSet(
    pydantic.BaseModel
):
    """
    Serializer for AppPreviewCreateRequestDataRelationshipsAppPreviewSet handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppPreviewCreateRequestDataRelationshipsAppPreviewSetData = (
        pydantic.Field(alias="data")
    )


class AppPreviewUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppPreviewUpdateRequestData]


class _SerializerAppPreviewUpdateRequest(pydantic.BaseModel):
    """
    Serializer for AppPreviewUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppPreviewUpdateRequestData = pydantic.Field(alias="data")


class AppPreviewCreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    app_preview_set: typing_extensions.Required[
        AppPreviewCreateRequestDataRelationshipsAppPreviewSet
    ]


class _SerializerAppPreviewCreateRequestDataRelationships(pydantic.BaseModel):
    """
    Serializer for AppPreviewCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_preview_set: _SerializerAppPreviewCreateRequestDataRelationshipsAppPreviewSet = pydantic.Field(
        alias="appPreviewSet"
    )


class AppPreviewCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[AppPreviewCreateRequestDataAttributes]
    relationships: typing_extensions.Required[AppPreviewCreateRequestDataRelationships]
    type: typing_extensions.Required[typing_extensions.Literal["appPreviews"]]


class _SerializerAppPreviewCreateRequestData(pydantic.BaseModel):
    """
    Serializer for AppPreviewCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerAppPreviewCreateRequestDataAttributes = pydantic.Field(
        alias="attributes"
    )
    relationships: _SerializerAppPreviewCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["appPreviews"] = pydantic.Field(alias="type")


class AppPreviewCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppPreviewCreateRequestData]


class _SerializerAppPreviewCreateRequest(pydantic.BaseModel):
    """
    Serializer for AppPreviewCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppPreviewCreateRequestData = pydantic.Field(alias="data")