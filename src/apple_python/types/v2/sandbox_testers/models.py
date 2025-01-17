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


class SandboxTesterV2Attributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ac_account_name: typing.Optional[str] = _PydanticField(
        alias="acAccountName", default=None
    )
    apple_pay_compatible: typing.Optional[bool] = _PydanticField(
        alias="applePayCompatible", default=None
    )
    first_name: typing.Optional[str] = _PydanticField(alias="firstName", default=None)
    interrupt_purchases: typing.Optional[bool] = _PydanticField(
        alias="interruptPurchases", default=None
    )
    last_name: typing.Optional[str] = _PydanticField(alias="lastName", default=None)
    subscription_renewal_rate: typing.Optional[
        typing_extensions.Literal[
            "MONTHLY_RENEWAL_EVERY_ONE_HOUR",
            "MONTHLY_RENEWAL_EVERY_THIRTY_MINUTES",
            "MONTHLY_RENEWAL_EVERY_FIFTEEN_MINUTES",
            "MONTHLY_RENEWAL_EVERY_FIVE_MINUTES",
            "MONTHLY_RENEWAL_EVERY_THREE_MINUTES",
        ]
    ] = _PydanticField(alias="subscriptionRenewalRate", default=None)
    territory: typing.Optional[
        typing_extensions.Literal[
            "ABW",
            "AFG",
            "AGO",
            "AIA",
            "ALB",
            "AND",
            "ANT",
            "ARE",
            "ARG",
            "ARM",
            "ASM",
            "ATG",
            "AUS",
            "AUT",
            "AZE",
            "BDI",
            "BEL",
            "BEN",
            "BES",
            "BFA",
            "BGD",
            "BGR",
            "BHR",
            "BHS",
            "BIH",
            "BLR",
            "BLZ",
            "BMU",
            "BOL",
            "BRA",
            "BRB",
            "BRN",
            "BTN",
            "BWA",
            "CAF",
            "CAN",
            "CHE",
            "CHL",
            "CHN",
            "CIV",
            "CMR",
            "COD",
            "COG",
            "COK",
            "COL",
            "COM",
            "CPV",
            "CRI",
            "CUB",
            "CUW",
            "CXR",
            "CYM",
            "CYP",
            "CZE",
            "DEU",
            "DJI",
            "DMA",
            "DNK",
            "DOM",
            "DZA",
            "ECU",
            "EGY",
            "ERI",
            "ESP",
            "EST",
            "ETH",
            "FIN",
            "FJI",
            "FLK",
            "FRA",
            "FRO",
            "FSM",
            "GAB",
            "GBR",
            "GEO",
            "GGY",
            "GHA",
            "GIB",
            "GIN",
            "GLP",
            "GMB",
            "GNB",
            "GNQ",
            "GRC",
            "GRD",
            "GRL",
            "GTM",
            "GUF",
            "GUM",
            "GUY",
            "HKG",
            "HND",
            "HRV",
            "HTI",
            "HUN",
            "IDN",
            "IMN",
            "IND",
            "IRL",
            "IRQ",
            "ISL",
            "ISR",
            "ITA",
            "JAM",
            "JEY",
            "JOR",
            "JPN",
            "KAZ",
            "KEN",
            "KGZ",
            "KHM",
            "KIR",
            "KNA",
            "KOR",
            "KWT",
            "LAO",
            "LBN",
            "LBR",
            "LBY",
            "LCA",
            "LIE",
            "LKA",
            "LSO",
            "LTU",
            "LUX",
            "LVA",
            "MAC",
            "MAR",
            "MCO",
            "MDA",
            "MDG",
            "MDV",
            "MEX",
            "MHL",
            "MKD",
            "MLI",
            "MLT",
            "MMR",
            "MNE",
            "MNG",
            "MNP",
            "MOZ",
            "MRT",
            "MSR",
            "MTQ",
            "MUS",
            "MWI",
            "MYS",
            "MYT",
            "NAM",
            "NCL",
            "NER",
            "NFK",
            "NGA",
            "NIC",
            "NIU",
            "NLD",
            "NOR",
            "NPL",
            "NRU",
            "NZL",
            "OMN",
            "PAK",
            "PAN",
            "PER",
            "PHL",
            "PLW",
            "PNG",
            "POL",
            "PRI",
            "PRT",
            "PRY",
            "PSE",
            "PYF",
            "QAT",
            "REU",
            "ROU",
            "RUS",
            "RWA",
            "SAU",
            "SEN",
            "SGP",
            "SHN",
            "SLB",
            "SLE",
            "SLV",
            "SMR",
            "SOM",
            "SPM",
            "SRB",
            "SSD",
            "STP",
            "SUR",
            "SVK",
            "SVN",
            "SWE",
            "SWZ",
            "SXM",
            "SYC",
            "TCA",
            "TCD",
            "TGO",
            "THA",
            "TJK",
            "TKM",
            "TLS",
            "TON",
            "TTO",
            "TUN",
            "TUR",
            "TUV",
            "TWN",
            "TZA",
            "UGA",
            "UKR",
            "UMI",
            "URY",
            "USA",
            "UZB",
            "VAT",
            "VCT",
            "VEN",
            "VGB",
            "VIR",
            "VNM",
            "VUT",
            "WLF",
            "WSM",
            "YEM",
            "ZAF",
            "ZMB",
            "ZWE",
        ]
    ] = _PydanticField(alias="territory", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


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


class DocumentLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: str = _PydanticField(alias="self")


class SandboxTesterV2(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[SandboxTesterV2Attributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    type: typing_extensions.Literal["sandboxTesters"] = _PydanticField(alias="type")


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class SandboxTesterV2Response(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: SandboxTesterV2 = _PydanticField(alias="data")
    links: DocumentLinks = _PydanticField(alias="links")


class SandboxTestersV2Response(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[SandboxTesterV2] = _PydanticField(alias="data")
    links: PagedDocumentLinks = _PydanticField(alias="links")
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )
