"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class AppCustomProductPageUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    name: typing_extensions.NotRequired[str]
    visible: typing_extensions.NotRequired[bool]


class _SerializerAppCustomProductPageUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for AppCustomProductPageUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    visible: typing.Optional[bool] = pydantic.Field(alias="visible", default=None)


class AppCustomProductPageCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    name: typing_extensions.Required[str]


class _SerializerAppCustomProductPageCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for AppCustomProductPageCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: str = pydantic.Field(alias="name")


class AppCustomProductPageCreateRequestDataRelationshipsAppData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["apps"]]


class _SerializerAppCustomProductPageCreateRequestDataRelationshipsAppData(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageCreateRequestDataRelationshipsAppData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["apps"] = pydantic.Field(alias="type")


class AppCustomProductPageCreateRequestDataRelationshipsAppCustomProductPageVersionsDataItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["appCustomProductPageVersions"]
    ]


class _SerializerAppCustomProductPageCreateRequestDataRelationshipsAppCustomProductPageVersionsDataItem(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageCreateRequestDataRelationshipsAppCustomProductPageVersionsDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appCustomProductPageVersions"] = pydantic.Field(
        alias="type"
    )


class AppCustomProductPageCreateRequestDataRelationshipsAppStoreVersionTemplateData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appStoreVersions"]]


class _SerializerAppCustomProductPageCreateRequestDataRelationshipsAppStoreVersionTemplateData(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageCreateRequestDataRelationshipsAppStoreVersionTemplateData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appStoreVersions"] = pydantic.Field(alias="type")


class AppCustomProductPageCreateRequestDataRelationshipsCustomProductPageTemplateData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appCustomProductPages"]]


class _SerializerAppCustomProductPageCreateRequestDataRelationshipsCustomProductPageTemplateData(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageCreateRequestDataRelationshipsCustomProductPageTemplateData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appCustomProductPages"] = pydantic.Field(
        alias="type"
    )


class AppCustomProductPageLocalizationInlineCreateAttributes(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    locale_field: typing_extensions.Required[str]
    promotional_text: typing_extensions.NotRequired[str]


class _SerializerAppCustomProductPageLocalizationInlineCreateAttributes(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageLocalizationInlineCreateAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    locale_field: str = pydantic.Field(alias="locale")
    promotional_text: typing.Optional[str] = pydantic.Field(
        alias="promotionalText", default=None
    )


class AppCustomProductPageLocalizationInlineCreateRelationshipsAppCustomProductPageVersionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["appCustomProductPageVersions"]
    ]


class _SerializerAppCustomProductPageLocalizationInlineCreateRelationshipsAppCustomProductPageVersionData(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageLocalizationInlineCreateRelationshipsAppCustomProductPageVersionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appCustomProductPageVersions"] = pydantic.Field(
        alias="type"
    )


class AppCustomProductPageVersionInlineCreateAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    deep_link: typing_extensions.NotRequired[str]


class _SerializerAppCustomProductPageVersionInlineCreateAttributes(pydantic.BaseModel):
    """
    Serializer for AppCustomProductPageVersionInlineCreateAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    deep_link: typing.Optional[str] = pydantic.Field(alias="deepLink", default=None)


class AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appCustomProductPages"]]


class _SerializerAppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageData(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appCustomProductPages"] = pydantic.Field(
        alias="type"
    )


class AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageLocalizationsDataItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[
        typing_extensions.Literal["appCustomProductPageLocalizations"]
    ]


class _SerializerAppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageLocalizationsDataItem(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageLocalizationsDataItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appCustomProductPageLocalizations"] = (
        pydantic.Field(alias="type")
    )


class AppCustomProductPageUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        AppCustomProductPageUpdateRequestDataAttributes
    ]
    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["appCustomProductPages"]]


class _SerializerAppCustomProductPageUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for AppCustomProductPageUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerAppCustomProductPageUpdateRequestDataAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["appCustomProductPages"] = pydantic.Field(
        alias="type"
    )


class AppCustomProductPageCreateRequestDataRelationshipsApp(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.Required[
        AppCustomProductPageCreateRequestDataRelationshipsAppData
    ]


class _SerializerAppCustomProductPageCreateRequestDataRelationshipsApp(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageCreateRequestDataRelationshipsApp handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppCustomProductPageCreateRequestDataRelationshipsAppData = (
        pydantic.Field(alias="data")
    )


class AppCustomProductPageCreateRequestDataRelationshipsAppCustomProductPageVersions(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        typing.List[
            AppCustomProductPageCreateRequestDataRelationshipsAppCustomProductPageVersionsDataItem
        ]
    ]


class _SerializerAppCustomProductPageCreateRequestDataRelationshipsAppCustomProductPageVersions(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageCreateRequestDataRelationshipsAppCustomProductPageVersions handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[
            _SerializerAppCustomProductPageCreateRequestDataRelationshipsAppCustomProductPageVersionsDataItem
        ]
    ] = pydantic.Field(alias="data", default=None)


class AppCustomProductPageCreateRequestDataRelationshipsAppStoreVersionTemplate(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        AppCustomProductPageCreateRequestDataRelationshipsAppStoreVersionTemplateData
    ]


class _SerializerAppCustomProductPageCreateRequestDataRelationshipsAppStoreVersionTemplate(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageCreateRequestDataRelationshipsAppStoreVersionTemplate handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerAppCustomProductPageCreateRequestDataRelationshipsAppStoreVersionTemplateData
    ] = pydantic.Field(alias="data", default=None)


class AppCustomProductPageCreateRequestDataRelationshipsCustomProductPageTemplate(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        AppCustomProductPageCreateRequestDataRelationshipsCustomProductPageTemplateData
    ]


class _SerializerAppCustomProductPageCreateRequestDataRelationshipsCustomProductPageTemplate(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageCreateRequestDataRelationshipsCustomProductPageTemplate handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerAppCustomProductPageCreateRequestDataRelationshipsCustomProductPageTemplateData
    ] = pydantic.Field(alias="data", default=None)


class AppCustomProductPageLocalizationInlineCreateRelationshipsAppCustomProductPageVersion(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        AppCustomProductPageLocalizationInlineCreateRelationshipsAppCustomProductPageVersionData
    ]


class _SerializerAppCustomProductPageLocalizationInlineCreateRelationshipsAppCustomProductPageVersion(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageLocalizationInlineCreateRelationshipsAppCustomProductPageVersion handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerAppCustomProductPageLocalizationInlineCreateRelationshipsAppCustomProductPageVersionData
    ] = pydantic.Field(alias="data", default=None)


class AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPage(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageData
    ]


class _SerializerAppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPage(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPage handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerAppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageData
    ] = pydantic.Field(alias="data", default=None)


class AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageLocalizations(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        typing.List[
            AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageLocalizationsDataItem
        ]
    ]


class _SerializerAppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageLocalizations(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageLocalizations handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[
            _SerializerAppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageLocalizationsDataItem
        ]
    ] = pydantic.Field(alias="data", default=None)


class AppCustomProductPageUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppCustomProductPageUpdateRequestData]


class _SerializerAppCustomProductPageUpdateRequest(pydantic.BaseModel):
    """
    Serializer for AppCustomProductPageUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppCustomProductPageUpdateRequestData = pydantic.Field(
        alias="data"
    )


class AppCustomProductPageCreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    app: typing_extensions.Required[
        AppCustomProductPageCreateRequestDataRelationshipsApp
    ]
    app_custom_product_page_versions: typing_extensions.NotRequired[
        AppCustomProductPageCreateRequestDataRelationshipsAppCustomProductPageVersions
    ]
    app_store_version_template: typing_extensions.NotRequired[
        AppCustomProductPageCreateRequestDataRelationshipsAppStoreVersionTemplate
    ]
    custom_product_page_template: typing_extensions.NotRequired[
        AppCustomProductPageCreateRequestDataRelationshipsCustomProductPageTemplate
    ]


class _SerializerAppCustomProductPageCreateRequestDataRelationships(pydantic.BaseModel):
    """
    Serializer for AppCustomProductPageCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app: _SerializerAppCustomProductPageCreateRequestDataRelationshipsApp = (
        pydantic.Field(alias="app")
    )
    app_custom_product_page_versions: typing.Optional[
        _SerializerAppCustomProductPageCreateRequestDataRelationshipsAppCustomProductPageVersions
    ] = pydantic.Field(alias="appCustomProductPageVersions", default=None)
    app_store_version_template: typing.Optional[
        _SerializerAppCustomProductPageCreateRequestDataRelationshipsAppStoreVersionTemplate
    ] = pydantic.Field(alias="appStoreVersionTemplate", default=None)
    custom_product_page_template: typing.Optional[
        _SerializerAppCustomProductPageCreateRequestDataRelationshipsCustomProductPageTemplate
    ] = pydantic.Field(alias="customProductPageTemplate", default=None)


class AppCustomProductPageLocalizationInlineCreateRelationships(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    app_custom_product_page_version: typing_extensions.NotRequired[
        AppCustomProductPageLocalizationInlineCreateRelationshipsAppCustomProductPageVersion
    ]


class _SerializerAppCustomProductPageLocalizationInlineCreateRelationships(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageLocalizationInlineCreateRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_custom_product_page_version: typing.Optional[
        _SerializerAppCustomProductPageLocalizationInlineCreateRelationshipsAppCustomProductPageVersion
    ] = pydantic.Field(alias="appCustomProductPageVersion", default=None)


class AppCustomProductPageVersionInlineCreateRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    app_custom_product_page: typing_extensions.NotRequired[
        AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPage
    ]
    app_custom_product_page_localizations: typing_extensions.NotRequired[
        AppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageLocalizations
    ]


class _SerializerAppCustomProductPageVersionInlineCreateRelationships(
    pydantic.BaseModel
):
    """
    Serializer for AppCustomProductPageVersionInlineCreateRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    app_custom_product_page: typing.Optional[
        _SerializerAppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPage
    ] = pydantic.Field(alias="appCustomProductPage", default=None)
    app_custom_product_page_localizations: typing.Optional[
        _SerializerAppCustomProductPageVersionInlineCreateRelationshipsAppCustomProductPageLocalizations
    ] = pydantic.Field(alias="appCustomProductPageLocalizations", default=None)


class AppCustomProductPageCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        AppCustomProductPageCreateRequestDataAttributes
    ]
    relationships: typing_extensions.Required[
        AppCustomProductPageCreateRequestDataRelationships
    ]
    type: typing_extensions.Required[typing_extensions.Literal["appCustomProductPages"]]


class _SerializerAppCustomProductPageCreateRequestData(pydantic.BaseModel):
    """
    Serializer for AppCustomProductPageCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerAppCustomProductPageCreateRequestDataAttributes = (
        pydantic.Field(alias="attributes")
    )
    relationships: _SerializerAppCustomProductPageCreateRequestDataRelationships = (
        pydantic.Field(alias="relationships")
    )
    type: typing_extensions.Literal["appCustomProductPages"] = pydantic.Field(
        alias="type"
    )


class AppCustomProductPageLocalizationInlineCreate(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[
        AppCustomProductPageLocalizationInlineCreateAttributes
    ]
    id: typing_extensions.NotRequired[str]
    relationships: typing_extensions.NotRequired[
        AppCustomProductPageLocalizationInlineCreateRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["appCustomProductPageLocalizations"]
    ]


class _SerializerAppCustomProductPageLocalizationInlineCreate(pydantic.BaseModel):
    """
    Serializer for AppCustomProductPageLocalizationInlineCreate handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerAppCustomProductPageLocalizationInlineCreateAttributes = (
        pydantic.Field(alias="attributes")
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    relationships: typing.Optional[
        _SerializerAppCustomProductPageLocalizationInlineCreateRelationships
    ] = pydantic.Field(alias="relationships", default=None)
    type: typing_extensions.Literal["appCustomProductPageLocalizations"] = (
        pydantic.Field(alias="type")
    )


class AppCustomProductPageVersionInlineCreate(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[
        AppCustomProductPageVersionInlineCreateAttributes
    ]
    id: typing_extensions.NotRequired[str]
    relationships: typing_extensions.NotRequired[
        AppCustomProductPageVersionInlineCreateRelationships
    ]
    type: typing_extensions.Required[
        typing_extensions.Literal["appCustomProductPageVersions"]
    ]


class _SerializerAppCustomProductPageVersionInlineCreate(pydantic.BaseModel):
    """
    Serializer for AppCustomProductPageVersionInlineCreate handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[
        _SerializerAppCustomProductPageVersionInlineCreateAttributes
    ] = pydantic.Field(alias="attributes", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    relationships: typing.Optional[
        _SerializerAppCustomProductPageVersionInlineCreateRelationships
    ] = pydantic.Field(alias="relationships", default=None)
    type: typing_extensions.Literal["appCustomProductPageVersions"] = pydantic.Field(
        alias="type"
    )


class AppCustomProductPageCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[AppCustomProductPageCreateRequestData]
    included: typing_extensions.NotRequired[
        typing.List[
            typing.Union[
                AppCustomProductPageLocalizationInlineCreate,
                AppCustomProductPageVersionInlineCreate,
            ]
        ]
    ]


class _SerializerAppCustomProductPageCreateRequest(pydantic.BaseModel):
    """
    Serializer for AppCustomProductPageCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerAppCustomProductPageCreateRequestData = pydantic.Field(
        alias="data"
    )
    included: typing.Optional[
        typing.List[
            typing.Union[
                _SerializerAppCustomProductPageLocalizationInlineCreate,
                _SerializerAppCustomProductPageVersionInlineCreate,
            ]
        ]
    ] = pydantic.Field(alias="included", default=None)