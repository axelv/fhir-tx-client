from pydantic import Field
from fhir.resources import parameters as fhir
from fhir.resources import fhirtypes

class ParametersParameter(fhir.ParametersParameter):
    pass

class Parameters(fhir.Parameters):
    """Parameters resource"""
    resource_type = Field("Parameters", const=True)
    parameter: list[fhirtypes.ParametersParameterType] = Field(
        [],
        alias="parameter",
        title="Operation Parameter",
        description="A parameter passed to or received from the operation.",
        # if property is element of this resource.
        element_property=True,
    )