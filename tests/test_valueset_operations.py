from fhir_tx_client import SyncFHIRTerminologyClient
from fhir_tx_client.data_types import Coding, SCTCoding

def test_valueset_expansion():
    """Test ValueSet expansion"""
    client = SyncFHIRTerminologyClient("https://tx.fhir.org/r4/")
    vs = client.resource("ValueSet", id="FHIR-version")
    vs_expanded = vs.expand()
    assert vs_expanded.expansion is not None, "expansion not found in result"
    assert vs_expanded.expansion.contains is not None, "contains not found in expansion"

def test_valueset_validate_code():
    """Test ValueSet validate-code"""
    client = SyncFHIRTerminologyClient("https://tx.fhir.org/r4/")
    vs = client.resource("ValueSet", id="FHIR-version")
    assert vs.validate_code(code="4.0.1", system="http://hl7.org/fhir/FHIR-version")["result"] == True

def test_valueset_contains():
    """Test ValueSet contains"""
    client = SyncFHIRTerminologyClient("https://tx.fhir.org/r4/")
    vs = client.resource("ValueSet", id="FHIR-version")
    assert Coding(code="4.0.1", system="http://hl7.org/fhir/FHIR-version") in vs 

def test_valueset_iterate():
    """Test ValueSet iterate"""
    client = SyncFHIRTerminologyClient("https://tx.fhir.org/r4/")
    vs = client.resource("ValueSet", id="FHIR-version", version="4.0.1")
    assert len(list(vs)) == 22

def test_valueset_container_code():
    client = SyncFHIRTerminologyClient("https://tx.fhir.org/r4/")
    # Refer to a ValueSet by id
    vs_food_type = client.resource("ValueSet", id="modified-foodtype")
    eggs_code = SCTCoding.from_sct_code("102263004 |Eggs (edible)|")
    # Validate a code in a ValueSet
    assert vs_food_type.validate_code(coding=eggs_code)["result"] == True

    

