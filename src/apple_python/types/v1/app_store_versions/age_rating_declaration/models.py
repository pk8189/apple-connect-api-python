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


class AgeRatingDeclarationAttributes(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    age_rating_override: typing.Optional[
        typing_extensions.Literal["NONE", "SEVENTEEN_PLUS", "UNRATED"]
    ] = _PydanticField(alias="ageRatingOverride", default=None)
    alcohol_tobacco_or_drug_use_or_references: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="alcoholTobaccoOrDrugUseOrReferences", default=None)
    contests: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="contests", default=None)
    gambling: typing.Optional[bool] = _PydanticField(alias="gambling", default=None)
    gambling_and_contests: typing.Optional[bool] = _PydanticField(
        alias="gamblingAndContests", default=None
    )
    gambling_simulated: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="gamblingSimulated", default=None)
    horror_or_fear_themes: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="horrorOrFearThemes", default=None)
    kids_age_band: typing.Optional[
        typing_extensions.Literal["FIVE_AND_UNDER", "SIX_TO_EIGHT", "NINE_TO_ELEVEN"]
    ] = _PydanticField(alias="kidsAgeBand", default=None)
    mature_or_suggestive_themes: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="matureOrSuggestiveThemes", default=None)
    medical_or_treatment_information: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="medicalOrTreatmentInformation", default=None)
    profanity_or_crude_humor: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="profanityOrCrudeHumor", default=None)
    seventeen_plus: typing.Optional[bool] = _PydanticField(
        alias="seventeenPlus", default=None
    )
    sexual_content_graphic_and_nudity: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="sexualContentGraphicAndNudity", default=None)
    sexual_content_or_nudity: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="sexualContentOrNudity", default=None)
    unrestricted_web_access: typing.Optional[bool] = _PydanticField(
        alias="unrestrictedWebAccess", default=None
    )
    violence_cartoon_or_fantasy: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="violenceCartoonOrFantasy", default=None)
    violence_realistic: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(alias="violenceRealistic", default=None)
    violence_realistic_prolonged_graphic_or_sadistic: typing.Optional[
        typing_extensions.Literal["NONE", "INFREQUENT_OR_MILD", "FREQUENT_OR_INTENSE"]
    ] = _PydanticField(
        alias="violenceRealisticProlongedGraphicOrSadistic", default=None
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


class AgeRatingDeclaration(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    attributes: typing.Optional[AgeRatingDeclarationAttributes] = _PydanticField(
        alias="attributes", default=None
    )
    id: str = _PydanticField(alias="id")
    links: typing.Optional[ResourceLinks] = _PydanticField(alias="links", default=None)
    type: typing_extensions.Literal["ageRatingDeclarations"] = _PydanticField(
        alias="type"
    )


class AgeRatingDeclarationWithoutIncludesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: AgeRatingDeclaration = _PydanticField(alias="data")
    links: DocumentLinks = _PydanticField(alias="links")
