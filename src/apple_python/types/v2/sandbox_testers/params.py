"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class SandboxTesterV2UpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    interrupt_purchases: typing_extensions.NotRequired[bool]
    subscription_renewal_rate: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "MONTHLY_RENEWAL_EVERY_ONE_HOUR",
            "MONTHLY_RENEWAL_EVERY_THIRTY_MINUTES",
            "MONTHLY_RENEWAL_EVERY_FIFTEEN_MINUTES",
            "MONTHLY_RENEWAL_EVERY_FIVE_MINUTES",
            "MONTHLY_RENEWAL_EVERY_THREE_MINUTES",
        ]
    ]
    territory: typing_extensions.NotRequired[
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
    ]


class _SerializerSandboxTesterV2UpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for SandboxTesterV2UpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    interrupt_purchases: typing.Optional[bool] = pydantic.Field(
        alias="interruptPurchases", default=None
    )
    subscription_renewal_rate: typing.Optional[
        typing_extensions.Literal[
            "MONTHLY_RENEWAL_EVERY_ONE_HOUR",
            "MONTHLY_RENEWAL_EVERY_THIRTY_MINUTES",
            "MONTHLY_RENEWAL_EVERY_FIFTEEN_MINUTES",
            "MONTHLY_RENEWAL_EVERY_FIVE_MINUTES",
            "MONTHLY_RENEWAL_EVERY_THREE_MINUTES",
        ]
    ] = pydantic.Field(alias="subscriptionRenewalRate", default=None)
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
    ] = pydantic.Field(alias="territory", default=None)


class SandboxTesterV2UpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        SandboxTesterV2UpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["sandboxTesters"]]


class _SerializerSandboxTesterV2UpdateRequestData(pydantic.BaseModel):
    """
    Serializer for SandboxTesterV2UpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerSandboxTesterV2UpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["sandboxTesters"] = pydantic.Field(alias="type")


class SandboxTesterV2UpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[SandboxTesterV2UpdateRequestData]


class _SerializerSandboxTesterV2UpdateRequest(pydantic.BaseModel):
    """
    Serializer for SandboxTesterV2UpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerSandboxTesterV2UpdateRequestData = pydantic.Field(alias="data")
