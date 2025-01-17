"""File Generated by Sideko (sideko.dev)"""

import io
import typing
import typing_extensions
from pydantic import (
    BaseModel as _PydanticBaseModel,
    Field as _PydanticField,
    ConfigDict as _PydanticConfigDict,
)

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class ProfileAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_date: typing.Optional[str] = _PydanticField(
        alias="createdDate", default=None
    )
    expiration_date: typing.Optional[str] = _PydanticField(
        alias="expirationDate", default=None
    )
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    platform_field: typing.Optional[typing_extensions.Literal["IOS", "MAC_OS"]] = (
        _PydanticField(alias="platform", default=None)
    )
    profile_content: typing.Optional[str] = _PydanticField(
        alias="profileContent", default=None
    )
    profile_state: typing.Optional[typing_extensions.Literal["ACTIVE", "INVALID"]] = (
        _PydanticField(alias="profileState", default=None)
    )
    profile_type: typing.Optional[
        typing_extensions.Literal[
            "IOS_APP_DEVELOPMENT",
            "IOS_APP_STORE",
            "IOS_APP_ADHOC",
            "IOS_APP_INHOUSE",
            "MAC_APP_DEVELOPMENT",
            "MAC_APP_STORE",
            "MAC_APP_DIRECT",
            "TVOS_APP_DEVELOPMENT",
            "TVOS_APP_STORE",
            "TVOS_APP_ADHOC",
            "TVOS_APP_INHOUSE",
            "MAC_CATALYST_APP_DEVELOPMENT",
            "MAC_CATALYST_APP_STORE",
            "MAC_CATALYST_APP_DIRECT",
        ]
    ] = _PydanticField(alias="profileType", default=None)
    uuid_field: typing.Optional[str] = _PydanticField(alias="uuid", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class ProfileRelationshipsBundleIdData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["bundleIds"] = _PydanticField(alias="type")


class ProfileRelationshipsBundleIdLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class ProfileRelationshipsCertificatesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["certificates"] = _PydanticField(alias="type")


class ProfileRelationshipsCertificatesLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class PagingInformationPaging(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    limit: int = _PydanticField(alias="limit")
    total: typing.Optional[int] = _PydanticField(alias="total", default=None)


class ProfileRelationshipsDevicesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["devices"] = _PydanticField(alias="type")


class ProfileRelationshipsDevicesLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class PagedDocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    first: typing.Optional[str] = _PydanticField(alias="first", default=None)
    next: typing.Optional[str] = _PydanticField(alias="next", default=None)
    self: str = _PydanticField(alias="self")


class ProfileRelationshipsBundleId(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[ProfileRelationshipsBundleIdData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[ProfileRelationshipsBundleIdLinks] = _PydanticField(
        alias="links", default=None
    )


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class ProfileRelationshipsDevices(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[ProfileRelationshipsDevicesDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[ProfileRelationshipsDevicesLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class ProfileRelationshipsCertificates(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[ProfileRelationshipsCertificatesDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[ProfileRelationshipsCertificatesLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class ProfileRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bundle_id: typing.Optional[ProfileRelationshipsBundleId] = _PydanticField(
        alias="bundleId", default=None
    )
    certificates: typing.Optional[ProfileRelationshipsCertificates] = _PydanticField(
        alias="certificates", default=None
    )
    devices: typing.Optional[ProfileRelationshipsDevices] = _PydanticField(
        alias="devices", default=None
    )


class Profile(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[ProfileAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[ProfileRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["profiles"] = _PydanticField(alias="type")


class ProfilesWithoutIncludesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[Profile] = _PydanticField(alias="data")
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
