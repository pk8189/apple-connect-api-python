"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppClipDefaultExperienceUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    action: typing_extensions.NotRequired[
        typing_extensions.Literal["OPEN", "VIEW", "PLAY"]
    ]


class _SerializerAppClipDefaultExperienceUpdateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    action: typing.Optional[typing_extensions.Literal["OPEN", "VIEW", "PLAY"]] = (
        pydantic.Field(alias="action", default=None)
    )


class AppClipDefaultExperienceUpdateRequestDataRelationshipsReleaseWithAppStoreVersionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appStoreVersions"]]


class _SerializerAppClipDefaultExperienceUpdateRequestDataRelationshipsReleaseWithAppStoreVersionData(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceUpdateRequestDataRelationshipsReleaseWithAppStoreVersionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appStoreVersions"] = pydantic.Field(alias="type")


class AppClipDefaultExperienceCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    action: typing_extensions.NotRequired[
        typing_extensions.Literal["OPEN", "VIEW", "PLAY"]
    ]


class _SerializerAppClipDefaultExperienceCreateRequestDataAttributes(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    action: typing.Optional[typing_extensions.Literal["OPEN", "VIEW", "PLAY"]] = (
        pydantic.Field(alias="action", default=None)
    )


class AppClipDefaultExperienceCreateRequestDataRelationshipsAppClipData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appClips"]]


class _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsAppClipData(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceCreateRequestDataRelationshipsAppClipData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appClips"] = pydantic.Field(alias="type")


class AppClipDefaultExperienceCreateRequestDataRelationshipsAppClipDefaultExperienceTemplateData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["appClipDefaultExperiences"]
    ]


class _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsAppClipDefaultExperienceTemplateData(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceCreateRequestDataRelationshipsAppClipDefaultExperienceTemplateData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appClipDefaultExperiences"] = pydantic.Field(
        alias="type"
    )


class AppClipDefaultExperienceCreateRequestDataRelationshipsReleaseWithAppStoreVersionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appStoreVersions"]]


class _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsReleaseWithAppStoreVersionData(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceCreateRequestDataRelationshipsReleaseWithAppStoreVersionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appStoreVersions"] = pydantic.Field(alias="type")


class AppClipDefaultExperienceUpdateRequestDataRelationshipsReleaseWithAppStoreVersion(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        AppClipDefaultExperienceUpdateRequestDataRelationshipsReleaseWithAppStoreVersionData
    ]


class _SerializerAppClipDefaultExperienceUpdateRequestDataRelationshipsReleaseWithAppStoreVersion(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceUpdateRequestDataRelationshipsReleaseWithAppStoreVersion handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerAppClipDefaultExperienceUpdateRequestDataRelationshipsReleaseWithAppStoreVersionData
    ] = pydantic.Field(alias="data", default=None)


class AppClipDefaultExperienceCreateRequestDataRelationshipsAppClip(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppClipDefaultExperienceCreateRequestDataRelationshipsAppClipData
    ]


class _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsAppClip(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceCreateRequestDataRelationshipsAppClip handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsAppClipData = pydantic.Field(
        alias="data"
    )


class AppClipDefaultExperienceCreateRequestDataRelationshipsAppClipDefaultExperienceTemplate(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        AppClipDefaultExperienceCreateRequestDataRelationshipsAppClipDefaultExperienceTemplateData
    ]


class _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsAppClipDefaultExperienceTemplate(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceCreateRequestDataRelationshipsAppClipDefaultExperienceTemplate handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsAppClipDefaultExperienceTemplateData
    ] = pydantic.Field(alias="data", default=None)


class AppClipDefaultExperienceCreateRequestDataRelationshipsReleaseWithAppStoreVersion(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        AppClipDefaultExperienceCreateRequestDataRelationshipsReleaseWithAppStoreVersionData
    ]


class _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsReleaseWithAppStoreVersion(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceCreateRequestDataRelationshipsReleaseWithAppStoreVersion handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsReleaseWithAppStoreVersionData
    ] = pydantic.Field(alias="data", default=None)


class AppClipDefaultExperienceUpdateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    release_with_app_store_version: typing_extensions.NotRequired[
        AppClipDefaultExperienceUpdateRequestDataRelationshipsReleaseWithAppStoreVersion
    ]


class _SerializerAppClipDefaultExperienceUpdateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceUpdateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    release_with_app_store_version: typing.Optional[
        _SerializerAppClipDefaultExperienceUpdateRequestDataRelationshipsReleaseWithAppStoreVersion
    ] = pydantic.Field(alias="releaseWithAppStoreVersion", default=None)


class AppClipDefaultExperienceCreateRequestDataRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    app_clip: typing_extensions.Required[
        AppClipDefaultExperienceCreateRequestDataRelationshipsAppClip
    ]
    app_clip_default_experience_template: typing_extensions.NotRequired[
        AppClipDefaultExperienceCreateRequestDataRelationshipsAppClipDefaultExperienceTemplate
    ]
    release_with_app_store_version: typing_extensions.NotRequired[
        AppClipDefaultExperienceCreateRequestDataRelationshipsReleaseWithAppStoreVersion
    ]


class _SerializerAppClipDefaultExperienceCreateRequestDataRelationships(
    pydantic.BaseModel
):
    """
    Serializer for AppClipDefaultExperienceCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_clip: _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsAppClip = pydantic.Field(
        alias="appClip"
    )
    app_clip_default_experience_template: typing.Optional[
        _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsAppClipDefaultExperienceTemplate
    ] = pydantic.Field(alias="appClipDefaultExperienceTemplate", default=None)
    release_with_app_store_version: typing.Optional[
        _SerializerAppClipDefaultExperienceCreateRequestDataRelationshipsReleaseWithAppStoreVersion
    ] = pydantic.Field(alias="releaseWithAppStoreVersion", default=None)


class AppClipDefaultExperienceUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        AppClipDefaultExperienceUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    relationships: typing_extensions.NotRequired[
        AppClipDefaultExperienceUpdateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["appClipDefaultExperiences"]
    ]


class _SerializerAppClipDefaultExperienceUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for AppClipDefaultExperienceUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerAppClipDefaultExperienceUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    relationships: typing.Optional[
        _SerializerAppClipDefaultExperienceUpdateRequestDataRelationships
    ] = pydantic.Field(alias="relationships", default=None)
    type: typing_extensions.Literal["appClipDefaultExperiences"] = pydantic.Field(
        alias="type"
    )


class AppClipDefaultExperienceCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        AppClipDefaultExperienceCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        AppClipDefaultExperienceCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["appClipDefaultExperiences"]
    ]


class _SerializerAppClipDefaultExperienceCreateRequestData(pydantic.BaseModel):
    """
    Serializer for AppClipDefaultExperienceCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerAppClipDefaultExperienceCreateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    relationships: _SerializerAppClipDefaultExperienceCreateRequestDataRelationships = (
        pydantic.Field(alias="relationships")
    )
    type: typing_extensions.Literal["appClipDefaultExperiences"] = pydantic.Field(
        alias="type"
    )


class AppClipDefaultExperienceUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppClipDefaultExperienceUpdateRequestData]


class _SerializerAppClipDefaultExperienceUpdateRequest(pydantic.BaseModel):
    """
    Serializer for AppClipDefaultExperienceUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppClipDefaultExperienceUpdateRequestData = pydantic.Field(
        alias="data"
    )


class AppClipDefaultExperienceCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppClipDefaultExperienceCreateRequestData]


class _SerializerAppClipDefaultExperienceCreateRequest(pydantic.BaseModel):
    """
    Serializer for AppClipDefaultExperienceCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppClipDefaultExperienceCreateRequestData = pydantic.Field(
        alias="data"
    )
