# FHIR Terminology Client
A micro-library built on top of [`fhirpy`](https://github.com/beda-software/fhir-py) and [`fhir.resources`](https://github.com/nazrulworld/fhir.resources) bringing [FHIR Terminology](http://hl7.org/fhir/terminology-module.html) at your Python fingertips.


## Why?

FHIR Terminology has become mature and is wide spread but it's hard for Python-developers to interact with:

1. FHIR resources can be deeply nested, `dict`'s lack autocompletion of attributes and validation of types. This makes code error-prone. Some data artifacts in FHIR like the [`Parameters`](http://hl7.org/fhir/Parameters)-resource or [`choice types`](https://www.hl7.org/fhir/formats.html#choice) are manipulate and require lots of boilerplate code.
   
2. REST API calls come with overhead. You need to construct URL's, handle HTTP Headers, or reponse codes, but in the end you only care about the result or want to receive a human-readable exception.

3. You want your code to be readable and increase your developer experience. Clinical Terminology is complex matter, you don't want extra confusion because of technical details.


⚠️ This is work-in-progress. It serves as an example on how to create a lightweight library that increase your developer experirence. However, it is not ready for production yet. We ([Tiro.health](http://tiro.health)) plan to integrate this in our [FHIRKit](http://tiro.health/Tiro-health/fhirkit) but this approach need some validation first.

### A more detailed discussion on this package
This library is the result of a blogpost I've written. Read [the blogpost here](https://axelv.github.io/drafts/fhir-tx-python)

### Looking for a quick example?
Here you have an example notebook: [1.0-validate-snomed-code-in-valueset.ipynb](./examples/1.0-validate-snomed-code-in-valueset.ipynb)


