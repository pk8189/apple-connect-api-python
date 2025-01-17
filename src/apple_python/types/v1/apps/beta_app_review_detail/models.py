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


class BetaAppReviewDetailAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    contact_email: typing.Optional[str] = _PydanticField(
        alias="contactEmail", default=None
    )
    contact_first_name: typing.Optional[str] = _PydanticField(
        alias="contactFirstName", default=None
    )
    contact_last_name: typing.Optional[str] = _PydanticField(
        alias="contactLastName", default=None
    )
    contact_phone: typing.Optional[str] = _PydanticField(
        alias="contactPhone", default=None
    )
    demo_account_name: typing.Optional[str] = _PydanticField(
        alias="demoAccountName", default=None
    )
    demo_account_password: typing.Optional[str] = _PydanticField(
        alias="demoAccountPassword", default=None
    )
    demo_account_required: typing.Optional[bool] = _PydanticField(
        alias="demoAccountRequired", default=None
    )
    notes: typing.Optional[str] = _PydanticField(alias="notes", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class BetaAppReviewDetailRelationshipsAppData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["apps"] = _PydanticField(alias="type")


class BetaAppReviewDetailRelationshipsAppLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class DocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: str = _PydanticField(alias="self")


class BetaAppReviewDetailRelationshipsApp(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[BetaAppReviewDetailRelationshipsAppData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[BetaAppReviewDetailRelationshipsAppLinks] = _PydanticField(
        alias="links", default=None
    )


class BetaAppReviewDetailRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app: typing.Optional[BetaAppReviewDetailRelationshipsApp] = _PydanticField(
        alias="app", default=None
    )


class BetaAppReviewDetail(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[BetaAppReviewDetailAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[BetaAppReviewDetailRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["betaAppReviewDetails"] = _PydanticField(
        alias="type"
    )


class BetaAppReviewDetailWithoutIncludesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: BetaAppReviewDetail = _PydanticField(alias="data")
    links: DocumentLinks = _PydanticField(alias="links")
