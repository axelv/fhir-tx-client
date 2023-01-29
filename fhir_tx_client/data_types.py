from datetime import date, datetime
from pydantic import Field
from fhir.resources import codeableconcept as fhir
from fhir.resources import fhirtypes
from fhir.resources.coding import Coding

PYTHON_PRIMITIVE_TO_FHIR_TYPE_MAP = {
    bool: fhirtypes.Boolean,
    str: fhirtypes.String,
    int: fhirtypes.Integer,
    float: fhirtypes.Decimal,
    bytes: fhirtypes.Base64Binary,
    datetime: fhirtypes.DateTime,
    date: fhirtypes.Date,
}

ALLOWED_PYTHON_TYPES = tuple(PYTHON_PRIMITIVE_TO_FHIR_TYPE_MAP.keys())

class SCTCoding(Coding):
    system: fhirtypes.Uri = Field(
        "http://snomed.info/sct",
        alias="system",
        const=True,
        title="Identity of the terminology system",
        description=(
            "The identification of the code system that defines the meaning of the "
            "symbol in the code."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def from_sct_code(cls, token:str):
        parts = token.split("|")
        if len(parts) == 1:
            code = parts[0]
            return cls(code=code.strip())
        else:
            code, *other = parts
            return cls(code=code.strip(), display=other[0].strip())

class CodeableConcept(fhir.CodeableConcept):
    text: fhirtypes.String = Field(
        None,
        alias="text",
        title="Plain text representation of the concept",
        description=(
            "A human language representation of the concept as "
            "seen/selected/uttered by the user who entered the data and/or which "
            "represents the intended meaning of the user."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    coding: list[Coding] = Field(
        [],
        alias="coding",
        title="Code defined by a terminology system",
        description=(
            "A reference to a code defined by a terminology system."
        ),
        # if property is element of this resource.
        element_property=True,
    )