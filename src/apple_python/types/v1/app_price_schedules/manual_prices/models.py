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


class AppPriceV2Attributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    end_date: typing.Optional[str] = _PydanticField(alias="endDate", default=None)
    manual: typing.Optional[bool] = _PydanticField(alias="manual", default=None)
    start_date: typing.Optional[str] = _PydanticField(alias="startDate", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppPriceV2RelationshipsAppPricePointData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["appPricePoints"] = _PydanticField(alias="type")


class AppPriceV2RelationshipsAppPricePointLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppPriceV2RelationshipsTerritoryData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["territories"] = _PydanticField(alias="type")


class AppPriceV2RelationshipsTerritoryLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppPricePointV3Attributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    customer_price: typing.Optional[str] = _PydanticField(
        alias="customerPrice", default=None
    )
    proceeds: typing.Optional[str] = _PydanticField(alias="proceeds", default=None)


class AppPricePointV3RelationshipsAppData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["apps"] = _PydanticField(alias="type")


class AppPricePointV3RelationshipsAppLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class AppPricePointV3RelationshipsTerritoryData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["territories"] = _PydanticField(alias="type")


class AppPricePointV3RelationshipsTerritoryLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class TerritoryAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    currency: typing.Optional[str] = _PydanticField(alias="currency", default=None)


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


class AppPriceV2RelationshipsAppPricePoint(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppPriceV2RelationshipsAppPricePointData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppPriceV2RelationshipsAppPricePointLinks] = _PydanticField(
        alias="links", default=None
    )


class AppPriceV2RelationshipsTerritory(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppPriceV2RelationshipsTerritoryData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppPriceV2RelationshipsTerritoryLinks] = _PydanticField(
        alias="links", default=None
    )


class AppPricePointV3RelationshipsApp(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppPricePointV3RelationshipsAppData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppPricePointV3RelationshipsAppLinks] = _PydanticField(
        alias="links", default=None
    )


class AppPricePointV3RelationshipsTerritory(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[AppPricePointV3RelationshipsTerritoryData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[AppPricePointV3RelationshipsTerritoryLinks] = _PydanticField(
        alias="links", default=None
    )


class Territory(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[TerritoryAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    type: typing_extensions.Literal["territories"] = _PydanticField(alias="type")


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class AppPriceV2Relationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_price_point: typing.Optional[AppPriceV2RelationshipsAppPricePoint] = (
        _PydanticField(alias="appPricePoint", default=None)
    )
    territory: typing.Optional[AppPriceV2RelationshipsTerritory] = _PydanticField(
        alias="territory", default=None
    )


class AppPricePointV3Relationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app: typing.Optional[AppPricePointV3RelationshipsApp] = _PydanticField(
        alias="app", default=None
    )
    territory: typing.Optional[AppPricePointV3RelationshipsTerritory] = _PydanticField(
        alias="territory", default=None
    )


class AppPriceV2(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppPriceV2Attributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppPriceV2Relationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["appPrices"] = _PydanticField(alias="type")


class AppPricePointV3(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AppPricePointV3Attributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[AppPricePointV3Relationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["appPricePoints"] = _PydanticField(alias="type")


class AppPricesV2Response(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[AppPriceV2] = _PydanticField(alias="data")
    included: typing.Optional[typing.List[typing.Union[AppPricePointV3, Territory]]] = (
        _PydanticField(alias="included", default=None)
    )
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )