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


class CiTestDestination(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    device_type_identifier: typing.Optional[str] = _PydanticField(
        alias="deviceTypeIdentifier", default=None
    )
    device_type_name: typing.Optional[str] = _PydanticField(
        alias="deviceTypeName", default=None
    )
    kind: typing.Optional[typing_extensions.Literal["SIMULATOR", "MAC"]] = (
        _PydanticField(alias="kind", default=None)
    )
    runtime_identifier: typing.Optional[str] = _PydanticField(
        alias="runtimeIdentifier", default=None
    )
    runtime_name: typing.Optional[str] = _PydanticField(
        alias="runtimeName", default=None
    )


class CiStartConditionFileMatcher(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    directory: typing.Optional[str] = _PydanticField(alias="directory", default=None)
    file_extension: typing.Optional[str] = _PydanticField(
        alias="fileExtension", default=None
    )
    file_name: typing.Optional[str] = _PydanticField(alias="fileName", default=None)


class CiBranchPatternsPatternsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    is_prefix: typing.Optional[bool] = _PydanticField(alias="isPrefix", default=None)
    pattern: typing.Optional[str] = _PydanticField(alias="pattern", default=None)


class CiTagPatternsPatternsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    is_prefix: typing.Optional[bool] = _PydanticField(alias="isPrefix", default=None)
    pattern: typing.Optional[str] = _PydanticField(alias="pattern", default=None)


class CiScheduledStartConditionSchedule(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    days: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "SUNDAY",
                "MONDAY",
                "TUESDAY",
                "WEDNESDAY",
                "THURSDAY",
                "FRIDAY",
                "SATURDAY",
            ]
        ]
    ] = _PydanticField(alias="days", default=None)
    frequency: typing.Optional[
        typing_extensions.Literal["WEEKLY", "DAILY", "HOURLY"]
    ] = _PydanticField(alias="frequency", default=None)
    hour: typing.Optional[int] = _PydanticField(alias="hour", default=None)
    minute: typing.Optional[int] = _PydanticField(alias="minute", default=None)
    timezone: typing.Optional[str] = _PydanticField(alias="timezone", default=None)


class ResourceLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class CiWorkflowRelationshipsMacOsVersionData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["ciMacOsVersions"] = _PydanticField(alias="type")


class CiWorkflowRelationshipsMacOsVersionLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class CiWorkflowRelationshipsProductData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["ciProducts"] = _PydanticField(alias="type")


class CiWorkflowRelationshipsProductLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class CiWorkflowRelationshipsRepositoryData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["scmRepositories"] = _PydanticField(alias="type")


class CiWorkflowRelationshipsRepositoryLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class CiWorkflowRelationshipsXcodeVersionData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["ciXcodeVersions"] = _PydanticField(alias="type")


class CiWorkflowRelationshipsXcodeVersionLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class CiProductAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_date: typing.Optional[str] = _PydanticField(
        alias="createdDate", default=None
    )
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    product_type: typing.Optional[typing_extensions.Literal["APP", "FRAMEWORK"]] = (
        _PydanticField(alias="productType", default=None)
    )


class CiProductRelationshipsAppData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["apps"] = _PydanticField(alias="type")


class CiProductRelationshipsAppLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class CiProductRelationshipsBundleIdData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["bundleIds"] = _PydanticField(alias="type")


class CiProductRelationshipsBundleIdLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class CiProductRelationshipsPrimaryRepositoriesDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["scmRepositories"] = _PydanticField(alias="type")


class CiProductRelationshipsPrimaryRepositoriesLinks(_PydanticBaseModel):
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


class ScmRepositoryAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    http_clone_url: typing.Optional[str] = _PydanticField(
        alias="httpCloneUrl", default=None
    )
    last_accessed_date: typing.Optional[str] = _PydanticField(
        alias="lastAccessedDate", default=None
    )
    owner_name: typing.Optional[str] = _PydanticField(alias="ownerName", default=None)
    repository_name: typing.Optional[str] = _PydanticField(
        alias="repositoryName", default=None
    )
    ssh_clone_url: typing.Optional[str] = _PydanticField(
        alias="sshCloneUrl", default=None
    )


class ScmRepositoryRelationshipsDefaultBranchData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["scmGitReferences"] = _PydanticField(alias="type")


class ScmRepositoryRelationshipsDefaultBranchLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class ScmRepositoryRelationshipsScmProviderData(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["scmProviders"] = _PydanticField(alias="type")


class ScmRepositoryRelationshipsScmProviderLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class CiXcodeVersionAttributesTestDestinationsItemAvailableRuntimesItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    runtime_identifier: typing.Optional[str] = _PydanticField(
        alias="runtimeIdentifier", default=None
    )
    runtime_name: typing.Optional[str] = _PydanticField(
        alias="runtimeName", default=None
    )


class CiXcodeVersionRelationshipsMacOsVersionsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["ciMacOsVersions"] = _PydanticField(alias="type")


class CiXcodeVersionRelationshipsMacOsVersionsLinks(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    related: typing.Optional[str] = _PydanticField(alias="related", default=None)
    self: typing.Optional[str] = _PydanticField(alias="self", default=None)


class CiMacOsVersionAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    version: typing.Optional[str] = _PydanticField(alias="version", default=None)


class CiMacOsVersionRelationshipsXcodeVersionsDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = _PydanticField(alias="id")
    type: typing_extensions.Literal["ciXcodeVersions"] = _PydanticField(alias="type")


class CiMacOsVersionRelationshipsXcodeVersionsLinks(_PydanticBaseModel):
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


class CiActionTestConfiguration(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    kind: typing.Optional[
        typing_extensions.Literal["USE_SCHEME_SETTINGS", "SPECIFIC_TEST_PLANS"]
    ] = _PydanticField(alias="kind", default=None)
    test_destinations: typing.Optional[typing.List[CiTestDestination]] = _PydanticField(
        alias="testDestinations", default=None
    )
    test_plan_name: typing.Optional[str] = _PydanticField(
        alias="testPlanName", default=None
    )


class CiFilesAndFoldersRule(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    matchers: typing.Optional[typing.List[CiStartConditionFileMatcher]] = (
        _PydanticField(alias="matchers", default=None)
    )
    mode: typing.Optional[
        typing_extensions.Literal[
            "START_IF_ANY_FILE_MATCHES", "DO_NOT_START_IF_ALL_FILES_MATCH"
        ]
    ] = _PydanticField(alias="mode", default=None)


class CiBranchPatterns(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    is_all_match: typing.Optional[bool] = _PydanticField(
        alias="isAllMatch", default=None
    )
    patterns: typing.Optional[typing.List[CiBranchPatternsPatternsItem]] = (
        _PydanticField(alias="patterns", default=None)
    )


class CiManualBranchStartCondition(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    source: typing.Optional[CiBranchPatterns] = _PydanticField(
        alias="source", default=None
    )


class CiManualPullRequestStartCondition(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    destination: typing.Optional[CiBranchPatterns] = _PydanticField(
        alias="destination", default=None
    )
    source: typing.Optional[CiBranchPatterns] = _PydanticField(
        alias="source", default=None
    )


class CiTagPatterns(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    is_all_match: typing.Optional[bool] = _PydanticField(
        alias="isAllMatch", default=None
    )
    patterns: typing.Optional[typing.List[CiTagPatternsPatternsItem]] = _PydanticField(
        alias="patterns", default=None
    )


class CiPullRequestStartCondition(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    auto_cancel: typing.Optional[bool] = _PydanticField(
        alias="autoCancel", default=None
    )
    destination: typing.Optional[CiBranchPatterns] = _PydanticField(
        alias="destination", default=None
    )
    files_and_folders_rule: typing.Optional[CiFilesAndFoldersRule] = _PydanticField(
        alias="filesAndFoldersRule", default=None
    )
    source: typing.Optional[CiBranchPatterns] = _PydanticField(
        alias="source", default=None
    )


class CiScheduledStartCondition(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    schedule: typing.Optional[CiScheduledStartConditionSchedule] = _PydanticField(
        alias="schedule", default=None
    )
    source: typing.Optional[CiBranchPatterns] = _PydanticField(
        alias="source", default=None
    )


class CiTagStartCondition(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    auto_cancel: typing.Optional[bool] = _PydanticField(
        alias="autoCancel", default=None
    )
    files_and_folders_rule: typing.Optional[CiFilesAndFoldersRule] = _PydanticField(
        alias="filesAndFoldersRule", default=None
    )
    source: typing.Optional[CiTagPatterns] = _PydanticField(
        alias="source", default=None
    )


class CiWorkflowRelationshipsMacOsVersion(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[CiWorkflowRelationshipsMacOsVersionData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[CiWorkflowRelationshipsMacOsVersionLinks] = _PydanticField(
        alias="links", default=None
    )


class CiWorkflowRelationshipsProduct(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[CiWorkflowRelationshipsProductData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[CiWorkflowRelationshipsProductLinks] = _PydanticField(
        alias="links", default=None
    )


class CiWorkflowRelationshipsRepository(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[CiWorkflowRelationshipsRepositoryData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[CiWorkflowRelationshipsRepositoryLinks] = _PydanticField(
        alias="links", default=None
    )


class CiWorkflowRelationshipsXcodeVersion(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[CiWorkflowRelationshipsXcodeVersionData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[CiWorkflowRelationshipsXcodeVersionLinks] = _PydanticField(
        alias="links", default=None
    )


class CiProductRelationshipsApp(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[CiProductRelationshipsAppData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[CiProductRelationshipsAppLinks] = _PydanticField(
        alias="links", default=None
    )


class CiProductRelationshipsBundleId(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[CiProductRelationshipsBundleIdData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[CiProductRelationshipsBundleIdLinks] = _PydanticField(
        alias="links", default=None
    )


class PagingInformation(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    paging: PagingInformationPaging = _PydanticField(alias="paging")


class ScmRepositoryRelationshipsDefaultBranch(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[ScmRepositoryRelationshipsDefaultBranchData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[ScmRepositoryRelationshipsDefaultBranchLinks] = (
        _PydanticField(alias="links", default=None)
    )


class ScmRepositoryRelationshipsScmProvider(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[ScmRepositoryRelationshipsScmProviderData] = _PydanticField(
        alias="data", default=None
    )
    links: typing.Optional[ScmRepositoryRelationshipsScmProviderLinks] = _PydanticField(
        alias="links", default=None
    )


class CiXcodeVersionAttributesTestDestinationsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    available_runtimes: typing.Optional[
        typing.List[CiXcodeVersionAttributesTestDestinationsItemAvailableRuntimesItem]
    ] = _PydanticField(alias="availableRuntimes", default=None)
    device_type_identifier: typing.Optional[str] = _PydanticField(
        alias="deviceTypeIdentifier", default=None
    )
    device_type_name: typing.Optional[str] = _PydanticField(
        alias="deviceTypeName", default=None
    )
    kind: typing.Optional[typing_extensions.Literal["SIMULATOR", "MAC"]] = (
        _PydanticField(alias="kind", default=None)
    )


class CiXcodeVersionRelationshipsMacOsVersions(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[CiXcodeVersionRelationshipsMacOsVersionsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[CiXcodeVersionRelationshipsMacOsVersionsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class CiMacOsVersionRelationshipsXcodeVersions(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[CiMacOsVersionRelationshipsXcodeVersionsDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[CiMacOsVersionRelationshipsXcodeVersionsLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class CiAction(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    action_type: typing.Optional[
        typing_extensions.Literal["BUILD", "ANALYZE", "TEST", "ARCHIVE"]
    ] = _PydanticField(alias="actionType", default=None)
    build_distribution_audience: typing.Optional[
        typing_extensions.Literal["INTERNAL_ONLY", "APP_STORE_ELIGIBLE"]
    ] = _PydanticField(alias="buildDistributionAudience", default=None)
    destination: typing.Optional[
        typing_extensions.Literal[
            "ANY_IOS_DEVICE",
            "ANY_IOS_SIMULATOR",
            "ANY_TVOS_DEVICE",
            "ANY_TVOS_SIMULATOR",
            "ANY_WATCHOS_DEVICE",
            "ANY_WATCHOS_SIMULATOR",
            "ANY_MAC",
            "ANY_MAC_CATALYST",
            "ANY_VISIONOS_DEVICE",
            "ANY_VISIONOS_SIMULATOR",
        ]
    ] = _PydanticField(alias="destination", default=None)
    is_required_to_pass: typing.Optional[bool] = _PydanticField(
        alias="isRequiredToPass", default=None
    )
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    platform_field: typing.Optional[
        typing_extensions.Literal["MACOS", "IOS", "TVOS", "WATCHOS", "VISIONOS"]
    ] = _PydanticField(alias="platform", default=None)
    scheme: typing.Optional[str] = _PydanticField(alias="scheme", default=None)
    test_configuration: typing.Optional[CiActionTestConfiguration] = _PydanticField(
        alias="testConfiguration", default=None
    )


class CiBranchStartCondition(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    auto_cancel: typing.Optional[bool] = _PydanticField(
        alias="autoCancel", default=None
    )
    files_and_folders_rule: typing.Optional[CiFilesAndFoldersRule] = _PydanticField(
        alias="filesAndFoldersRule", default=None
    )
    source: typing.Optional[CiBranchPatterns] = _PydanticField(
        alias="source", default=None
    )


class CiManualTagStartCondition(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    source: typing.Optional[CiTagPatterns] = _PydanticField(
        alias="source", default=None
    )


class CiWorkflowRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    mac_os_version: typing.Optional[CiWorkflowRelationshipsMacOsVersion] = (
        _PydanticField(alias="macOsVersion", default=None)
    )
    product: typing.Optional[CiWorkflowRelationshipsProduct] = _PydanticField(
        alias="product", default=None
    )
    repository: typing.Optional[CiWorkflowRelationshipsRepository] = _PydanticField(
        alias="repository", default=None
    )
    xcode_version: typing.Optional[CiWorkflowRelationshipsXcodeVersion] = (
        _PydanticField(alias="xcodeVersion", default=None)
    )


class CiProductRelationshipsPrimaryRepositories(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.Optional[
        typing.List[CiProductRelationshipsPrimaryRepositoriesDataItem]
    ] = _PydanticField(alias="data", default=None)
    links: typing.Optional[CiProductRelationshipsPrimaryRepositoriesLinks] = (
        _PydanticField(alias="links", default=None)
    )
    meta: typing.Optional[PagingInformation] = _PydanticField(
        alias="meta", default=None
    )


class ScmRepositoryRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default_branch: typing.Optional[ScmRepositoryRelationshipsDefaultBranch] = (
        _PydanticField(alias="defaultBranch", default=None)
    )
    scm_provider: typing.Optional[ScmRepositoryRelationshipsScmProvider] = (
        _PydanticField(alias="scmProvider", default=None)
    )


class CiXcodeVersionAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    test_destinations: typing.Optional[
        typing.List[CiXcodeVersionAttributesTestDestinationsItem]
    ] = _PydanticField(alias="testDestinations", default=None)
    version: typing.Optional[str] = _PydanticField(alias="version", default=None)


class CiXcodeVersionRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    mac_os_versions: typing.Optional[CiXcodeVersionRelationshipsMacOsVersions] = (
        _PydanticField(alias="macOsVersions", default=None)
    )


class CiMacOsVersionRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    xcode_versions: typing.Optional[CiMacOsVersionRelationshipsXcodeVersions] = (
        _PydanticField(alias="xcodeVersions", default=None)
    )


class CiWorkflowAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actions: typing.Optional[typing.List[CiAction]] = _PydanticField(
        alias="actions", default=None
    )
    branch_start_condition: typing.Optional[CiBranchStartCondition] = _PydanticField(
        alias="branchStartCondition", default=None
    )
    clean: typing.Optional[bool] = _PydanticField(alias="clean", default=None)
    container_file_path: typing.Optional[str] = _PydanticField(
        alias="containerFilePath", default=None
    )
    description: typing.Optional[str] = _PydanticField(
        alias="description", default=None
    )
    is_enabled: typing.Optional[bool] = _PydanticField(alias="isEnabled", default=None)
    is_locked_for_editing: typing.Optional[bool] = _PydanticField(
        alias="isLockedForEditing", default=None
    )
    last_modified_date: typing.Optional[str] = _PydanticField(
        alias="lastModifiedDate", default=None
    )
    manual_branch_start_condition: typing.Optional[CiManualBranchStartCondition] = (
        _PydanticField(alias="manualBranchStartCondition", default=None)
    )
    manual_pull_request_start_condition: typing.Optional[
        CiManualPullRequestStartCondition
    ] = _PydanticField(alias="manualPullRequestStartCondition", default=None)
    manual_tag_start_condition: typing.Optional[CiManualTagStartCondition] = (
        _PydanticField(alias="manualTagStartCondition", default=None)
    )
    name: typing.Optional[str] = _PydanticField(alias="name", default=None)
    pull_request_start_condition: typing.Optional[CiPullRequestStartCondition] = (
        _PydanticField(alias="pullRequestStartCondition", default=None)
    )
    scheduled_start_condition: typing.Optional[CiScheduledStartCondition] = (
        _PydanticField(alias="scheduledStartCondition", default=None)
    )
    tag_start_condition: typing.Optional[CiTagStartCondition] = _PydanticField(
        alias="tagStartCondition", default=None
    )


class CiProductRelationships(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app: typing.Optional[CiProductRelationshipsApp] = _PydanticField(
        alias="app", default=None
    )
    bundle_id: typing.Optional[CiProductRelationshipsBundleId] = _PydanticField(
        alias="bundleId", default=None
    )
    primary_repositories: typing.Optional[CiProductRelationshipsPrimaryRepositories] = (
        _PydanticField(alias="primaryRepositories", default=None)
    )


class ScmRepository(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[ScmRepositoryAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[ScmRepositoryRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["scmRepositories"] = _PydanticField(alias="type")


class CiXcodeVersion(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[CiXcodeVersionAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[CiXcodeVersionRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["ciXcodeVersions"] = _PydanticField(alias="type")


class CiMacOsVersion(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[CiMacOsVersionAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[CiMacOsVersionRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["ciMacOsVersions"] = _PydanticField(alias="type")


class CiWorkflow(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[CiWorkflowAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[CiWorkflowRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["ciWorkflows"] = _PydanticField(alias="type")


class CiProduct(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[CiProductAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    relationships: typing.Optional[CiProductRelationships] = _PydanticField(
        alias="relationships", default=None
    )
    type: typing_extensions.Literal["ciProducts"] = _PydanticField(alias="type")


class CiWorkflowResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: CiWorkflow = _PydanticField(alias="data")
    included: typing.Optional[
        typing.List[
            typing.Union[CiProduct, ScmRepository, CiXcodeVersion, CiMacOsVersion]
        ]
    ] = _PydanticField(alias="included", default=None)
    links: DocumentLinks = _PydanticField(alias="links")
