from fhir.resources.fhirtypes import FHIRAbstractModel, Primitive
from fhirpy.base.utils import AttrDict
from fhir_tx_client.Parameters import Parameters, ParametersParameter
from fhir_tx_client.data_types import PYTHON_PRIMITIVE_TO_FHIR_TYPE_MAP

def dict_to_params(data: dict) -> Parameters:
    """Convert a dictionary to a Parameters resource"""
    params = Parameters(parameter=[])
    for key, value in data.items():
        if isinstance(value, tuple(PYTHON_PRIMITIVE_TO_FHIR_TYPE_MAP.keys())):
            for python_type, fhir_type in PYTHON_PRIMITIVE_TO_FHIR_TYPE_MAP.items():
                if isinstance(value, python_type):
                    value = fhir_type(value)
                    break
        if isinstance(value, FHIRAbstractModel):
            value_key = "value" + value.resource_type[0].upper() + value.resource_type[1:]
        elif isinstance(value, Primitive):
            fhir_type_name = value.fhir_type_name()
            value_key = "value" + fhir_type_name[0].upper() + fhir_type_name[1:]
        else:
            raise TypeError(f"Expected a subclass of FHIRAbstractModel, got {type(value)}. Please make use of the types defined in fhir.resources.fhirtypes.")
        params.parameter.append(ParametersParameter(**{"name":key, value_key:value}))
    return params

def params_to_dict(params: Parameters) -> dict:
    """Convert a Parameters resource to a dictionary"""
    params_dict = {}
    for param in params.parameter:
        name_entry, value_entry = param.dict(exclude_none=True).items()
        if name_entry[1] in params_dict:
            raise ValueError("Duplicate parameter name %s" % name_entry[1])
        params_dict[name_entry[1]] = value_entry[1]
    return AttrDict(**params_dict)
