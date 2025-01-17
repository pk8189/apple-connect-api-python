"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class CiTestDestination(typing_extensions.TypedDict):
    """
    No description specified
    """

    device_type_identifier: typing_extensions.NotRequired[str]
    device_type_name: typing_extensions.NotRequired[str]
    kind: typing_extensions.NotRequired[typing_extensions.Literal["SIMULATOR", "MAC"]]
    runtime_identifier: typing_extensions.NotRequired[str]
    runtime_name: typing_extensions.NotRequired[str]


class _SerializerCiTestDestination(pydantic.BaseModel):
    """
    Serializer for CiTestDestination handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    device_type_identifier: typing.Optional[str] = pydantic.Field(
        alias="deviceTypeIdentifier", default=None
    )
    device_type_name: typing.Optional[str] = pydantic.Field(
        alias="deviceTypeName", default=None
    )
    kind: typing.Optional[typing_extensions.Literal["SIMULATOR", "MAC"]] = (
        pydantic.Field(alias="kind", default=None)
    )
    runtime_identifier: typing.Optional[str] = pydantic.Field(
        alias="runtimeIdentifier", default=None
    )
    runtime_name: typing.Optional[str] = pydantic.Field(
        alias="runtimeName", default=None
    )


class CiStartConditionFileMatcher(typing_extensions.TypedDict):
    """
    No description specified
    """

    directory: typing_extensions.NotRequired[str]
    file_extension: typing_extensions.NotRequired[str]
    file_name: typing_extensions.NotRequired[str]


class _SerializerCiStartConditionFileMatcher(pydantic.BaseModel):
    """
    Serializer for CiStartConditionFileMatcher handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    directory: typing.Optional[str] = pydantic.Field(alias="directory", default=None)
    file_extension: typing.Optional[str] = pydantic.Field(
        alias="fileExtension", default=None
    )
    file_name: typing.Optional[str] = pydantic.Field(alias="fileName", default=None)


class CiBranchPatternsPatternsItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    is_prefix: typing_extensions.NotRequired[bool]
    pattern: typing_extensions.NotRequired[str]


class _SerializerCiBranchPatternsPatternsItem(pydantic.BaseModel):
    """
    Serializer for CiBranchPatternsPatternsItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    is_prefix: typing.Optional[bool] = pydantic.Field(alias="isPrefix", default=None)
    pattern: typing.Optional[str] = pydantic.Field(alias="pattern", default=None)


class CiTagPatternsPatternsItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    is_prefix: typing_extensions.NotRequired[bool]
    pattern: typing_extensions.NotRequired[str]


class _SerializerCiTagPatternsPatternsItem(pydantic.BaseModel):
    """
    Serializer for CiTagPatternsPatternsItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    is_prefix: typing.Optional[bool] = pydantic.Field(alias="isPrefix", default=None)
    pattern: typing.Optional[str] = pydantic.Field(alias="pattern", default=None)


class CiScheduledStartConditionSchedule(typing_extensions.TypedDict):
    """
    No description specified
    """

    days: typing_extensions.NotRequired[
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
    ]
    frequency: typing_extensions.NotRequired[
        typing_extensions.Literal["WEEKLY", "DAILY", "HOURLY"]
    ]
    hour: typing_extensions.NotRequired[int]
    minute: typing_extensions.NotRequired[int]
    timezone: typing_extensions.NotRequired[str]


class _SerializerCiScheduledStartConditionSchedule(pydantic.BaseModel):
    """
    Serializer for CiScheduledStartConditionSchedule handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
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
    ] = pydantic.Field(alias="days", default=None)
    frequency: typing.Optional[
        typing_extensions.Literal["WEEKLY", "DAILY", "HOURLY"]
    ] = pydantic.Field(alias="frequency", default=None)
    hour: typing.Optional[int] = pydantic.Field(alias="hour", default=None)
    minute: typing.Optional[int] = pydantic.Field(alias="minute", default=None)
    timezone: typing.Optional[str] = pydantic.Field(alias="timezone", default=None)


class CiWorkflowUpdateRequestDataRelationshipsMacOsVersionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["ciMacOsVersions"]]


class _SerializerCiWorkflowUpdateRequestDataRelationshipsMacOsVersionData(
    pydantic.BaseModel
):
    """
    Serializer for CiWorkflowUpdateRequestDataRelationshipsMacOsVersionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["ciMacOsVersions"] = pydantic.Field(alias="type")


class CiWorkflowUpdateRequestDataRelationshipsXcodeVersionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["ciXcodeVersions"]]


class _SerializerCiWorkflowUpdateRequestDataRelationshipsXcodeVersionData(
    pydantic.BaseModel
):
    """
    Serializer for CiWorkflowUpdateRequestDataRelationshipsXcodeVersionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["ciXcodeVersions"] = pydantic.Field(alias="type")


class CiWorkflowCreateRequestDataRelationshipsMacOsVersionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["ciMacOsVersions"]]


class _SerializerCiWorkflowCreateRequestDataRelationshipsMacOsVersionData(
    pydantic.BaseModel
):
    """
    Serializer for CiWorkflowCreateRequestDataRelationshipsMacOsVersionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["ciMacOsVersions"] = pydantic.Field(alias="type")


class CiWorkflowCreateRequestDataRelationshipsProductData(typing_extensions.TypedDict):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["ciProducts"]]


class _SerializerCiWorkflowCreateRequestDataRelationshipsProductData(
    pydantic.BaseModel
):
    """
    Serializer for CiWorkflowCreateRequestDataRelationshipsProductData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["ciProducts"] = pydantic.Field(alias="type")


class CiWorkflowCreateRequestDataRelationshipsRepositoryData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["scmRepositories"]]


class _SerializerCiWorkflowCreateRequestDataRelationshipsRepositoryData(
    pydantic.BaseModel
):
    """
    Serializer for CiWorkflowCreateRequestDataRelationshipsRepositoryData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["scmRepositories"] = pydantic.Field(alias="type")


class CiWorkflowCreateRequestDataRelationshipsXcodeVersionData(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    id: typing_extensions.Required[str]
    type: typing_extensions.Required[typing_extensions.Literal["ciXcodeVersions"]]


class _SerializerCiWorkflowCreateRequestDataRelationshipsXcodeVersionData(
    pydantic.BaseModel
):
    """
    Serializer for CiWorkflowCreateRequestDataRelationshipsXcodeVersionData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(alias="id")
    type: typing_extensions.Literal["ciXcodeVersions"] = pydantic.Field(alias="type")


class CiActionTestConfiguration(typing_extensions.TypedDict):
    """
    No description specified
    """

    kind: typing_extensions.NotRequired[
        typing_extensions.Literal["USE_SCHEME_SETTINGS", "SPECIFIC_TEST_PLANS"]
    ]
    test_destinations: typing_extensions.NotRequired[typing.List[CiTestDestination]]
    test_plan_name: typing_extensions.NotRequired[str]


class _SerializerCiActionTestConfiguration(pydantic.BaseModel):
    """
    Serializer for CiActionTestConfiguration handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    kind: typing.Optional[
        typing_extensions.Literal["USE_SCHEME_SETTINGS", "SPECIFIC_TEST_PLANS"]
    ] = pydantic.Field(alias="kind", default=None)
    test_destinations: typing.Optional[typing.List[_SerializerCiTestDestination]] = (
        pydantic.Field(alias="testDestinations", default=None)
    )
    test_plan_name: typing.Optional[str] = pydantic.Field(
        alias="testPlanName", default=None
    )


class CiFilesAndFoldersRule(typing_extensions.TypedDict):
    """
    No description specified
    """

    matchers: typing_extensions.NotRequired[typing.List[CiStartConditionFileMatcher]]
    mode: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "START_IF_ANY_FILE_MATCHES", "DO_NOT_START_IF_ALL_FILES_MATCH"
        ]
    ]


class _SerializerCiFilesAndFoldersRule(pydantic.BaseModel):
    """
    Serializer for CiFilesAndFoldersRule handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    matchers: typing.Optional[typing.List[_SerializerCiStartConditionFileMatcher]] = (
        pydantic.Field(alias="matchers", default=None)
    )
    mode: typing.Optional[
        typing_extensions.Literal[
            "START_IF_ANY_FILE_MATCHES", "DO_NOT_START_IF_ALL_FILES_MATCH"
        ]
    ] = pydantic.Field(alias="mode", default=None)


class CiBranchPatterns(typing_extensions.TypedDict):
    """
    No description specified
    """

    is_all_match: typing_extensions.NotRequired[bool]
    patterns: typing_extensions.NotRequired[typing.List[CiBranchPatternsPatternsItem]]


class _SerializerCiBranchPatterns(pydantic.BaseModel):
    """
    Serializer for CiBranchPatterns handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    is_all_match: typing.Optional[bool] = pydantic.Field(
        alias="isAllMatch", default=None
    )
    patterns: typing.Optional[typing.List[_SerializerCiBranchPatternsPatternsItem]] = (
        pydantic.Field(alias="patterns", default=None)
    )


class CiManualBranchStartCondition(typing_extensions.TypedDict):
    """
    No description specified
    """

    source: typing_extensions.NotRequired[CiBranchPatterns]


class _SerializerCiManualBranchStartCondition(pydantic.BaseModel):
    """
    Serializer for CiManualBranchStartCondition handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    source: typing.Optional[_SerializerCiBranchPatterns] = pydantic.Field(
        alias="source", default=None
    )


class CiManualPullRequestStartCondition(typing_extensions.TypedDict):
    """
    No description specified
    """

    destination: typing_extensions.NotRequired[CiBranchPatterns]
    source: typing_extensions.NotRequired[CiBranchPatterns]


class _SerializerCiManualPullRequestStartCondition(pydantic.BaseModel):
    """
    Serializer for CiManualPullRequestStartCondition handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    destination: typing.Optional[_SerializerCiBranchPatterns] = pydantic.Field(
        alias="destination", default=None
    )
    source: typing.Optional[_SerializerCiBranchPatterns] = pydantic.Field(
        alias="source", default=None
    )


class CiTagPatterns(typing_extensions.TypedDict):
    """
    No description specified
    """

    is_all_match: typing_extensions.NotRequired[bool]
    patterns: typing_extensions.NotRequired[typing.List[CiTagPatternsPatternsItem]]


class _SerializerCiTagPatterns(pydantic.BaseModel):
    """
    Serializer for CiTagPatterns handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    is_all_match: typing.Optional[bool] = pydantic.Field(
        alias="isAllMatch", default=None
    )
    patterns: typing.Optional[typing.List[_SerializerCiTagPatternsPatternsItem]] = (
        pydantic.Field(alias="patterns", default=None)
    )


class CiPullRequestStartCondition(typing_extensions.TypedDict):
    """
    No description specified
    """

    auto_cancel: typing_extensions.NotRequired[bool]
    destination: typing_extensions.NotRequired[CiBranchPatterns]
    files_and_folders_rule: typing_extensions.NotRequired[CiFilesAndFoldersRule]
    source: typing_extensions.NotRequired[CiBranchPatterns]


class _SerializerCiPullRequestStartCondition(pydantic.BaseModel):
    """
    Serializer for CiPullRequestStartCondition handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    auto_cancel: typing.Optional[bool] = pydantic.Field(
        alias="autoCancel", default=None
    )
    destination: typing.Optional[_SerializerCiBranchPatterns] = pydantic.Field(
        alias="destination", default=None
    )
    files_and_folders_rule: typing.Optional[_SerializerCiFilesAndFoldersRule] = (
        pydantic.Field(alias="filesAndFoldersRule", default=None)
    )
    source: typing.Optional[_SerializerCiBranchPatterns] = pydantic.Field(
        alias="source", default=None
    )


class CiScheduledStartCondition(typing_extensions.TypedDict):
    """
    No description specified
    """

    schedule: typing_extensions.NotRequired[CiScheduledStartConditionSchedule]
    source: typing_extensions.NotRequired[CiBranchPatterns]


class _SerializerCiScheduledStartCondition(pydantic.BaseModel):
    """
    Serializer for CiScheduledStartCondition handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    schedule: typing.Optional[_SerializerCiScheduledStartConditionSchedule] = (
        pydantic.Field(alias="schedule", default=None)
    )
    source: typing.Optional[_SerializerCiBranchPatterns] = pydantic.Field(
        alias="source", default=None
    )


class CiTagStartCondition(typing_extensions.TypedDict):
    """
    No description specified
    """

    auto_cancel: typing_extensions.NotRequired[bool]
    files_and_folders_rule: typing_extensions.NotRequired[CiFilesAndFoldersRule]
    source: typing_extensions.NotRequired[CiTagPatterns]


class _SerializerCiTagStartCondition(pydantic.BaseModel):
    """
    Serializer for CiTagStartCondition handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    auto_cancel: typing.Optional[bool] = pydantic.Field(
        alias="autoCancel", default=None
    )
    files_and_folders_rule: typing.Optional[_SerializerCiFilesAndFoldersRule] = (
        pydantic.Field(alias="filesAndFoldersRule", default=None)
    )
    source: typing.Optional[_SerializerCiTagPatterns] = pydantic.Field(
        alias="source", default=None
    )


class CiWorkflowUpdateRequestDataRelationshipsMacOsVersion(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        CiWorkflowUpdateRequestDataRelationshipsMacOsVersionData
    ]


class _SerializerCiWorkflowUpdateRequestDataRelationshipsMacOsVersion(
    pydantic.BaseModel
):
    """
    Serializer for CiWorkflowUpdateRequestDataRelationshipsMacOsVersion handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerCiWorkflowUpdateRequestDataRelationshipsMacOsVersionData
    ] = pydantic.Field(alias="data", default=None)


class CiWorkflowUpdateRequestDataRelationshipsXcodeVersion(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.NotRequired[
        CiWorkflowUpdateRequestDataRelationshipsXcodeVersionData
    ]


class _SerializerCiWorkflowUpdateRequestDataRelationshipsXcodeVersion(
    pydantic.BaseModel
):
    """
    Serializer for CiWorkflowUpdateRequestDataRelationshipsXcodeVersion handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: typing.Optional[
        _SerializerCiWorkflowUpdateRequestDataRelationshipsXcodeVersionData
    ] = pydantic.Field(alias="data", default=None)


class CiWorkflowCreateRequestDataRelationshipsMacOsVersion(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        CiWorkflowCreateRequestDataRelationshipsMacOsVersionData
    ]


class _SerializerCiWorkflowCreateRequestDataRelationshipsMacOsVersion(
    pydantic.BaseModel
):
    """
    Serializer for CiWorkflowCreateRequestDataRelationshipsMacOsVersion handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerCiWorkflowCreateRequestDataRelationshipsMacOsVersionData = (
        pydantic.Field(alias="data")
    )


class CiWorkflowCreateRequestDataRelationshipsProduct(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        CiWorkflowCreateRequestDataRelationshipsProductData
    ]


class _SerializerCiWorkflowCreateRequestDataRelationshipsProduct(pydantic.BaseModel):
    """
    Serializer for CiWorkflowCreateRequestDataRelationshipsProduct handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerCiWorkflowCreateRequestDataRelationshipsProductData = (
        pydantic.Field(alias="data")
    )


class CiWorkflowCreateRequestDataRelationshipsRepository(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        CiWorkflowCreateRequestDataRelationshipsRepositoryData
    ]


class _SerializerCiWorkflowCreateRequestDataRelationshipsRepository(pydantic.BaseModel):
    """
    Serializer for CiWorkflowCreateRequestDataRelationshipsRepository handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerCiWorkflowCreateRequestDataRelationshipsRepositoryData = (
        pydantic.Field(alias="data")
    )


class CiWorkflowCreateRequestDataRelationshipsXcodeVersion(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[
        CiWorkflowCreateRequestDataRelationshipsXcodeVersionData
    ]


class _SerializerCiWorkflowCreateRequestDataRelationshipsXcodeVersion(
    pydantic.BaseModel
):
    """
    Serializer for CiWorkflowCreateRequestDataRelationshipsXcodeVersion handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerCiWorkflowCreateRequestDataRelationshipsXcodeVersionData = (
        pydantic.Field(alias="data")
    )


class CiAction(typing_extensions.TypedDict):
    """
    No description specified
    """

    action_type: typing_extensions.NotRequired[
        typing_extensions.Literal["BUILD", "ANALYZE", "TEST", "ARCHIVE"]
    ]
    build_distribution_audience: typing_extensions.NotRequired[
        typing_extensions.Literal["INTERNAL_ONLY", "APP_STORE_ELIGIBLE"]
    ]
    destination: typing_extensions.NotRequired[
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
    ]
    is_required_to_pass: typing_extensions.NotRequired[bool]
    name: typing_extensions.NotRequired[str]
    platform_field: typing_extensions.NotRequired[
        typing_extensions.Literal["MACOS", "IOS", "TVOS", "WATCHOS", "VISIONOS"]
    ]
    scheme: typing_extensions.NotRequired[str]
    test_configuration: typing_extensions.NotRequired[CiActionTestConfiguration]


class _SerializerCiAction(pydantic.BaseModel):
    """
    Serializer for CiAction handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    action_type: typing.Optional[
        typing_extensions.Literal["BUILD", "ANALYZE", "TEST", "ARCHIVE"]
    ] = pydantic.Field(alias="actionType", default=None)
    build_distribution_audience: typing.Optional[
        typing_extensions.Literal["INTERNAL_ONLY", "APP_STORE_ELIGIBLE"]
    ] = pydantic.Field(alias="buildDistributionAudience", default=None)
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
    ] = pydantic.Field(alias="destination", default=None)
    is_required_to_pass: typing.Optional[bool] = pydantic.Field(
        alias="isRequiredToPass", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    platform_field: typing.Optional[
        typing_extensions.Literal["MACOS", "IOS", "TVOS", "WATCHOS", "VISIONOS"]
    ] = pydantic.Field(alias="platform", default=None)
    scheme: typing.Optional[str] = pydantic.Field(alias="scheme", default=None)
    test_configuration: typing.Optional[_SerializerCiActionTestConfiguration] = (
        pydantic.Field(alias="testConfiguration", default=None)
    )


class CiBranchStartCondition(typing_extensions.TypedDict):
    """
    No description specified
    """

    auto_cancel: typing_extensions.NotRequired[bool]
    files_and_folders_rule: typing_extensions.NotRequired[CiFilesAndFoldersRule]
    source: typing_extensions.NotRequired[CiBranchPatterns]


class _SerializerCiBranchStartCondition(pydantic.BaseModel):
    """
    Serializer for CiBranchStartCondition handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    auto_cancel: typing.Optional[bool] = pydantic.Field(
        alias="autoCancel", default=None
    )
    files_and_folders_rule: typing.Optional[_SerializerCiFilesAndFoldersRule] = (
        pydantic.Field(alias="filesAndFoldersRule", default=None)
    )
    source: typing.Optional[_SerializerCiBranchPatterns] = pydantic.Field(
        alias="source", default=None
    )


class CiManualTagStartCondition(typing_extensions.TypedDict):
    """
    No description specified
    """

    source: typing_extensions.NotRequired[CiTagPatterns]


class _SerializerCiManualTagStartCondition(pydantic.BaseModel):
    """
    Serializer for CiManualTagStartCondition handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    source: typing.Optional[_SerializerCiTagPatterns] = pydantic.Field(
        alias="source", default=None
    )


class CiWorkflowUpdateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    mac_os_version: typing_extensions.NotRequired[
        CiWorkflowUpdateRequestDataRelationshipsMacOsVersion
    ]
    xcode_version: typing_extensions.NotRequired[
        CiWorkflowUpdateRequestDataRelationshipsXcodeVersion
    ]


class _SerializerCiWorkflowUpdateRequestDataRelationships(pydantic.BaseModel):
    """
    Serializer for CiWorkflowUpdateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mac_os_version: typing.Optional[
        _SerializerCiWorkflowUpdateRequestDataRelationshipsMacOsVersion
    ] = pydantic.Field(alias="macOsVersion", default=None)
    xcode_version: typing.Optional[
        _SerializerCiWorkflowUpdateRequestDataRelationshipsXcodeVersion
    ] = pydantic.Field(alias="xcodeVersion", default=None)


class CiWorkflowCreateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    actions: typing_extensions.Required[typing.List[CiAction]]
    branch_start_condition: typing_extensions.NotRequired[CiBranchStartCondition]
    clean: typing_extensions.Required[bool]
    container_file_path: typing_extensions.Required[str]
    description: typing_extensions.Required[str]
    is_enabled: typing_extensions.Required[bool]
    is_locked_for_editing: typing_extensions.NotRequired[bool]
    manual_branch_start_condition: typing_extensions.NotRequired[
        CiManualBranchStartCondition
    ]
    manual_pull_request_start_condition: typing_extensions.NotRequired[
        CiManualPullRequestStartCondition
    ]
    manual_tag_start_condition: typing_extensions.NotRequired[CiManualTagStartCondition]
    name: typing_extensions.Required[str]
    pull_request_start_condition: typing_extensions.NotRequired[
        CiPullRequestStartCondition
    ]
    scheduled_start_condition: typing_extensions.NotRequired[CiScheduledStartCondition]
    tag_start_condition: typing_extensions.NotRequired[CiTagStartCondition]


class _SerializerCiWorkflowCreateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for CiWorkflowCreateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    actions: typing.List[_SerializerCiAction] = pydantic.Field(alias="actions")
    branch_start_condition: typing.Optional[_SerializerCiBranchStartCondition] = (
        pydantic.Field(alias="branchStartCondition", default=None)
    )
    clean: bool = pydantic.Field(alias="clean")
    container_file_path: str = pydantic.Field(alias="containerFilePath")
    description: str = pydantic.Field(alias="description")
    is_enabled: bool = pydantic.Field(alias="isEnabled")
    is_locked_for_editing: typing.Optional[bool] = pydantic.Field(
        alias="isLockedForEditing", default=None
    )
    manual_branch_start_condition: typing.Optional[
        _SerializerCiManualBranchStartCondition
    ] = pydantic.Field(alias="manualBranchStartCondition", default=None)
    manual_pull_request_start_condition: typing.Optional[
        _SerializerCiManualPullRequestStartCondition
    ] = pydantic.Field(alias="manualPullRequestStartCondition", default=None)
    manual_tag_start_condition: typing.Optional[
        _SerializerCiManualTagStartCondition
    ] = pydantic.Field(alias="manualTagStartCondition", default=None)
    name: str = pydantic.Field(alias="name")
    pull_request_start_condition: typing.Optional[
        _SerializerCiPullRequestStartCondition
    ] = pydantic.Field(alias="pullRequestStartCondition", default=None)
    scheduled_start_condition: typing.Optional[_SerializerCiScheduledStartCondition] = (
        pydantic.Field(alias="scheduledStartCondition", default=None)
    )
    tag_start_condition: typing.Optional[_SerializerCiTagStartCondition] = (
        pydantic.Field(alias="tagStartCondition", default=None)
    )


class CiWorkflowCreateRequestDataRelationships(typing_extensions.TypedDict):
    """
    No description specified
    """

    mac_os_version: typing_extensions.Required[
        CiWorkflowCreateRequestDataRelationshipsMacOsVersion
    ]
    product: typing_extensions.Required[CiWorkflowCreateRequestDataRelationshipsProduct]
    repository: typing_extensions.Required[
        CiWorkflowCreateRequestDataRelationshipsRepository
    ]
    xcode_version: typing_extensions.Required[
        CiWorkflowCreateRequestDataRelationshipsXcodeVersion
    ]


class _SerializerCiWorkflowCreateRequestDataRelationships(pydantic.BaseModel):
    """
    Serializer for CiWorkflowCreateRequestDataRelationships handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mac_os_version: _SerializerCiWorkflowCreateRequestDataRelationshipsMacOsVersion = (
        pydantic.Field(alias="macOsVersion")
    )
    product: _SerializerCiWorkflowCreateRequestDataRelationshipsProduct = (
        pydantic.Field(alias="product")
    )
    repository: _SerializerCiWorkflowCreateRequestDataRelationshipsRepository = (
        pydantic.Field(alias="repository")
    )
    xcode_version: _SerializerCiWorkflowCreateRequestDataRelationshipsXcodeVersion = (
        pydantic.Field(alias="xcodeVersion")
    )


class CiWorkflowUpdateRequestDataAttributes(typing_extensions.TypedDict):
    """
    No description specified
    """

    actions: typing_extensions.NotRequired[typing.List[CiAction]]
    branch_start_condition: typing_extensions.NotRequired[CiBranchStartCondition]
    clean: typing_extensions.NotRequired[bool]
    container_file_path: typing_extensions.NotRequired[str]
    description: typing_extensions.NotRequired[str]
    is_enabled: typing_extensions.NotRequired[bool]
    is_locked_for_editing: typing_extensions.NotRequired[bool]
    manual_branch_start_condition: typing_extensions.NotRequired[
        CiManualBranchStartCondition
    ]
    manual_pull_request_start_condition: typing_extensions.NotRequired[
        CiManualPullRequestStartCondition
    ]
    manual_tag_start_condition: typing_extensions.NotRequired[CiManualTagStartCondition]
    name: typing_extensions.NotRequired[str]
    pull_request_start_condition: typing_extensions.NotRequired[
        CiPullRequestStartCondition
    ]
    scheduled_start_condition: typing_extensions.NotRequired[CiScheduledStartCondition]
    tag_start_condition: typing_extensions.NotRequired[CiTagStartCondition]


class _SerializerCiWorkflowUpdateRequestDataAttributes(pydantic.BaseModel):
    """
    Serializer for CiWorkflowUpdateRequestDataAttributes handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    actions: typing.Optional[typing.List[_SerializerCiAction]] = pydantic.Field(
        alias="actions", default=None
    )
    branch_start_condition: typing.Optional[_SerializerCiBranchStartCondition] = (
        pydantic.Field(alias="branchStartCondition", default=None)
    )
    clean: typing.Optional[bool] = pydantic.Field(alias="clean", default=None)
    container_file_path: typing.Optional[str] = pydantic.Field(
        alias="containerFilePath", default=None
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    is_enabled: typing.Optional[bool] = pydantic.Field(alias="isEnabled", default=None)
    is_locked_for_editing: typing.Optional[bool] = pydantic.Field(
        alias="isLockedForEditing", default=None
    )
    manual_branch_start_condition: typing.Optional[
        _SerializerCiManualBranchStartCondition
    ] = pydantic.Field(alias="manualBranchStartCondition", default=None)
    manual_pull_request_start_condition: typing.Optional[
        _SerializerCiManualPullRequestStartCondition
    ] = pydantic.Field(alias="manualPullRequestStartCondition", default=None)
    manual_tag_start_condition: typing.Optional[
        _SerializerCiManualTagStartCondition
    ] = pydantic.Field(alias="manualTagStartCondition", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    pull_request_start_condition: typing.Optional[
        _SerializerCiPullRequestStartCondition
    ] = pydantic.Field(alias="pullRequestStartCondition", default=None)
    scheduled_start_condition: typing.Optional[_SerializerCiScheduledStartCondition] = (
        pydantic.Field(alias="scheduledStartCondition", default=None)
    )
    tag_start_condition: typing.Optional[_SerializerCiTagStartCondition] = (
        pydantic.Field(alias="tagStartCondition", default=None)
    )


class CiWorkflowCreateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.Required[CiWorkflowCreateRequestDataAttributes]
    relationships: typing_extensions.Required[CiWorkflowCreateRequestDataRelationships]
    type: typing_extensions.Required[typing_extensions.Literal["ciWorkflows"]]


class _SerializerCiWorkflowCreateRequestData(pydantic.BaseModel):
    """
    Serializer for CiWorkflowCreateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: _SerializerCiWorkflowCreateRequestDataAttributes = pydantic.Field(
        alias="attributes"
    )
    relationships: _SerializerCiWorkflowCreateRequestDataRelationships = pydantic.Field(
        alias="relationships"
    )
    type: typing_extensions.Literal["ciWorkflows"] = pydantic.Field(alias="type")


class CiWorkflowUpdateRequestData(typing_extensions.TypedDict):
    """
    No description specified
    """

    attributes: typing_extensions.NotRequired[CiWorkflowUpdateRequestDataAttributes]
    id: typing_extensions.Required[str]
    relationships: typing_extensions.NotRequired[
        CiWorkflowUpdateRequestDataRelationships
    ]
    type: typing_extensions.Required[typing_extensions.Literal["ciWorkflows"]]


class _SerializerCiWorkflowUpdateRequestData(pydantic.BaseModel):
    """
    Serializer for CiWorkflowUpdateRequestData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    attributes: typing.Optional[_SerializerCiWorkflowUpdateRequestDataAttributes] = (
        pydantic.Field(alias="attributes", default=None)
    )
    id: str = pydantic.Field(alias="id")
    relationships: typing.Optional[
        _SerializerCiWorkflowUpdateRequestDataRelationships
    ] = pydantic.Field(alias="relationships", default=None)
    type: typing_extensions.Literal["ciWorkflows"] = pydantic.Field(alias="type")


class CiWorkflowCreateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[CiWorkflowCreateRequestData]


class _SerializerCiWorkflowCreateRequest(pydantic.BaseModel):
    """
    Serializer for CiWorkflowCreateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerCiWorkflowCreateRequestData = pydantic.Field(alias="data")


class CiWorkflowUpdateRequest(typing_extensions.TypedDict):
    """
    No description specified
    """

    data: typing_extensions.Required[CiWorkflowUpdateRequestData]


class _SerializerCiWorkflowUpdateRequest(pydantic.BaseModel):
    """
    Serializer for CiWorkflowUpdateRequest handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    data: _SerializerCiWorkflowUpdateRequestData = pydantic.Field(alias="data")
