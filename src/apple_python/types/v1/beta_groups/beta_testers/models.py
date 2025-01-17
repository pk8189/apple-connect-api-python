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


class BetaTesterAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email_field: typing.Optional[str] = _PydanticField(alias="email", default=None)
    first_name: typing.Optional[str] = _PydanticField(alias="firstName", default=None)
    invite_type: typing.Optional[typing_extensions.Literal["EMAIL", "PUBLIC_LINK"]] = (
        _PydanticField(alias="inviteType", default=None)
    )
    last_name: typing.Optional[str] = _PydanticField(alias="lastName", default=None)
    state: typing.Optional[
        typing_extensions.Literal[
            "NOT_INVITED", "INVITED", "ACCEPTED", "INSTALLED", "REVOKED"
        ]
    ] = _PydanticField(alias="state", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BetaTesterRelationshipsAppsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["apps"] = _PydanticField(alias="type")


class BetaTesterRelationshipsAppsLinks(_PydanticBaseModel):
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


class BetaTesterRelationshipsBetaGroupsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["betaGroups"] = _PydanticField(alias="type")


class BetaTesterRelationshipsBetaGroupsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BetaTesterRelationshipsBuildsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["builds"] = _PydanticField(alias="type")


class BetaTesterRelationshipsBuildsLinks(_PydanticBaseModel):
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


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class BetaTesterRelationshipsBetaGroups(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[BetaTesterRelationshipsBetaGroupsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[BetaTesterRelationshipsBetaGroupsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class BetaTesterRelationshipsBuilds(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[BetaTesterRelationshipsBuildsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[BetaTesterRelationshipsBuildsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class BetaTesterRelationshipsApps(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[typing.List[BetaTesterRelationshipsAppsDataItem]] = (
        _PydanticField(alias="data", default=None)
    )
    links: typing.Optional[BetaTesterRelationshipsAppsLinks] = _PydanticField(
        alias="links", default=None
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class BetaTesterRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    apps: typing.Optional[BetaTesterRelationshipsApps] = _PydanticField(
        alias="apps", default=None
    )
    beta_groups: typing.Optional[BetaTesterRelationshipsBetaGroups] = _PydanticField(
        alias="betaGroups", default=None
    )
    builds: typing.Optional[BetaTesterRelationshipsBuilds] = _PydanticField(
        alias="builds", default=None
    )


class BetaTester(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[BetaTesterAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[BetaTesterRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["betaTesters"] = _PydanticField(alias="type")


class BetaTestersWithoutIncludesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[BetaTester] = _PydanticField(alias="data")
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
