from fhirpy.base import SyncClient
from fhirpy.lib import SyncFHIRSearchSet, SyncFHIRResource, SyncFHIRReference
from fhir_tx_client.ValueSet import SyncValueSet 

class SyncFHIRTerminologyClient(SyncClient):
    ALLOWED_TYPES = {"ValueSet", "CodeSystem", "ConceptMap"}
    searchset_class = SyncFHIRSearchSet
    resource_class = SyncFHIRResource

    def reference(self, resource_type=None, id=None, reference=None, **kwargs):
        if resource_type and id:
            reference = "{0}/{1}".format(resource_type, id)

        if not reference:
            raise TypeError(
                "Arguments `resource_type` and `id` or `reference` " "are required"
            )
        return SyncFHIRReference(self, reference=reference, **kwargs)

    def resource(self, resource_type=None, **kwargs):
        if resource_type not in self.ALLOWED_TYPES:
            raise TypeError(
                "Resource type `{}` is not allowed. Allowed types: {}".format(
                    resource_type, ", ".join(self.ALLOWED_TYPES)
                )
            )
        if resource_type == "ValueSet":
            return SyncValueSet(self, resource_type=resource_type, **kwargs)
        return super().resource(resource_type, **kwargs)
    
    def ValueSet(self, **kwargs):
        return SyncValueSet(self, "ValueSet", **kwargs)