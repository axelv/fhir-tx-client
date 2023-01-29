from typing_extensions import Unpack
from typing import Iterator, TypedDict
from fhirpy.lib import SyncFHIRResource
from fhir_tx_client.util import dict_to_params, params_to_dict
from fhir_tx_client.Parameters import Parameters
from fhir_tx_client.data_types import Coding, CodeableConcept
from .model import ValueSet, ValueSetExpansionContains

class ValidateCodeKwargs(TypedDict):
    coding: Coding
    codeableConcept: CodeableConcept

class SyncValueSet(SyncFHIRResource):

    def expand(self,**kwargs):
        """Expand a ValueSet resource and return a ValueSet resource with the expanded ValueSet.
        https://www.hl7.org/fhir/valueset-operation-expand.html"""
        params = dict_to_params(kwargs)
        result = self.execute(
            "$expand",
            method="POST",
            data=params.dict()
        )
        result_valueset = ValueSet.parse_obj(result)
        return result_valueset


    def validate_code(self, **kwargs:Unpack[ValidateCodeKwargs]):
        """Validate a code against a ValueSet resource.
        https://www.hl7.org/fhir/valueset-operation-validate-code.html"""
        params = dict_to_params(kwargs)
        result = self.execute(
            "$validate-code",
            method="POST",
            data=params.dict()
        )
        result_params = Parameters.parse_obj(result)
        return params_to_dict(result_params)

    def __iterate_codings(self, contains:ValueSetExpansionContains):
        for coding in contains:
            yield Coding(code=coding.code, system=coding.system, display=coding.display)
            if coding.contains:
                yield from self.__iterate_codings(coding.contains)

    def __iter__(self) -> Iterator[Coding]:
        vs:ValueSet = self.expand()
        contains:ValueSetExpansionContains = vs.expansion.contains
        yield from self.__iterate_codings(contains)
        
    
    def __contains__(self, __o: object) -> bool:
        
        if isinstance(__o, Coding):
            response = self.validate_code(coding=__o)
            return response['result']

        if isinstance(__o, CodeableConcept):
            response = self.validate_code(codeableConcept=__o)
            return response['result']

        raise NotImplementedError("Can only check for Coding objects.")