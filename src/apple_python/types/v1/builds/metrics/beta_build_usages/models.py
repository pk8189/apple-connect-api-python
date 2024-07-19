"""File Generated by Sideko (sideko.dev)"""

import io
import typing

from pydantic import (
    BaseModel as _PydanticBaseModel,
    Field as _PydanticField,
    ConfigDict as _PydanticConfigDict,
)

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class BetaBuildUsagesV1MetricResponseDataItemDataPointsValues(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    crash_count: typing.Optional[int] = _PydanticField(alias="crashCount", default=None)
    feedback_count: typing.Optional[int] = _PydanticField(
        alias="feedbackCount", default=None
    )
    install_count: typing.Optional[int] = _PydanticField(
        alias="installCount", default=None
    )
    invite_count: typing.Optional[int] = _PydanticField(
        alias="inviteCount", default=None
    )
    session_count: typing.Optional[int] = _PydanticField(
        alias="sessionCount", default=None
    )


class BetaBuildUsagesV1MetricResponseDataItemDimensionsBundleIdsLinks(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    group_by: typing.Optional[str] = _PydanticField(alias="groupBy", default=None)


class PagedDocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    first: typing.Optional[str] = _PydanticField(alias="first", default=None)
    next: typing.Optional[str] = _PydanticField(alias="next", default=None)
    self: str = _PydanticField(alias="self")


class PagingInformationPaging(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    limit: int = _PydanticField(alias="limit")
    total: typing.Optional[int] = _PydanticField(alias="total", default=None)


class BetaBuildUsagesV1MetricResponseDataItemDataPoints(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    end: typing.Optional[str] = _PydanticField(alias="end", default=None)
    start: typing.Optional[str] = _PydanticField(alias="start", default=None)
    values: typing.Optional[BetaBuildUsagesV1MetricResponseDataItemDataPointsValues] = (
        _PydanticField(alias="values", default=None)
    )


class BetaBuildUsagesV1MetricResponseDataItemDimensionsBundleIds(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    links: typing.Optional[
        BetaBuildUsagesV1MetricResponseDataItemDimensionsBundleIdsLinks
    ] = _PydanticField(alias="links", default=None)


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class BetaBuildUsagesV1MetricResponseDataItemDimensions(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bundle_ids: typing.Optional[
        BetaBuildUsagesV1MetricResponseDataItemDimensionsBundleIds
    ] = _PydanticField(alias="bundleIds", default=None)


class BetaBuildUsagesV1MetricResponseDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data_points: typing.Optional[BetaBuildUsagesV1MetricResponseDataItemDataPoints] = (
        _PydanticField(alias="dataPoints", default=None)
    )
    dimensions: typing.Optional[BetaBuildUsagesV1MetricResponseDataItemDimensions] = (
        _PydanticField(alias="dimensions", default=None)
    )


class BetaBuildUsagesV1MetricResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[BetaBuildUsagesV1MetricResponseDataItem] = _PydanticField(
        alias="data"
    )
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
