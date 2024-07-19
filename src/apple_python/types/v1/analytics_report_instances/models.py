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


class AnalyticsReportInstanceAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    granularity: typing.Optional[
        typing_extensions.Literal["DAILY", "WEEKLY", "MONTHLY"]
    ] = _PydanticField(alias="granularity", default=None)
    processing_date: typing.Optional[str] = _PydanticField(
        alias="processingDate", default=None
    )


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class DocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: str = _PydanticField(alias="self")


class AnalyticsReportInstance(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AnalyticsReportInstanceAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    type: typing_extensions.Literal["analyticsReportInstances"] = _PydanticField(
        alias="type"
    )


class AnalyticsReportInstanceResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: AnalyticsReportInstance = _PydanticField(alias="data")
    links: DocumentLinks = _PydanticField(alias="links")