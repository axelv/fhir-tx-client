from pydantic import Field
from fhir.resources import valueset as fhir
from fhir.resources import fhirtypes

class ValueSetComposeInclude(fhir.ValueSetComposeInclude):
    system: fhirtypes.Uri | None = None
    version: fhirtypes.String | None = None
    concept: list[fhir.ValueSetComposeIncludeConcept] = Field(
        None,
        alias="concept",
        title="A concept defined in the system",
        description="Specifies a concept to be included or excluded.",
        # if property is element of this resource.
        element_property=True,
    )
    filter: list[fhir.ValueSetComposeIncludeFilter] = Field(
        [],
        alias="filter",
        title="Select codes/concepts by their properties (including relationships)",
        description=(
            "Select concepts by specify a matching criterion based on the properties"
            " (including relationships) defined by the system, or on filters defined"
            " by the system. If multiple filters are specified, they SHALL all be "
            "true."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    valueSet: list[fhirtypes.Canonical] = Field(
        [],
        alias="valueSet",
        title="Select the contents included in this value set",
        description=(
            "Selects the concepts found in this value set (based on its value set "
            "definition). This is an absolute URI that is a reference to "
            "ValueSet.url.  If multiple value sets are specified this includes the "
            "union of the contents of all of the referenced value sets."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["ValueSet"],
    )

class ValueSetCompose(fhir.ValueSetCompose):
    include: list[ValueSetComposeInclude] = Field(
        [],
        alias="include",
        title="Include one or more codes from a code system or other value set(s)",
        description=(
            "Include one or more codes from a code system or other value set(s)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    exclude: list[ValueSetComposeInclude] = Field(
        [],
        alias="exclude",
        title="Explicitly exclude codes",
        description=(
            "Explicitly exclude codes from a code system or other value set(s)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lockedDate: fhirtypes.Date | None = Field(
        None,
        alias="lockedDate",
        title="When value set defines its own codes",
        description=(
            "If a lockedDate is defined, then the server may assume all references to"
            " concepts defined by the system to be consistent with the version of "
            "the code system as of the locked date.  Note: This is not the same as "
            "the version of the code system resource - the lockedDate refers to the "
            "version of the code system content, not the version of the code system "
            "resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    inactive: bool | None = Field(
        None,
        alias="inactive",
        title="Whether inactive codes are in the value set",
        description=(
            "Whether inactive codes - codes that are not approved for current use - "
            "are in the value set. If inactive = true, inactive codes are to be "
            "included, if inactive = false they are not to be included. If absent, "
            "the behavior is determined by the implementation, but the concept of "
            "inactive codes is supported."
        ),
        # if property is element of this resource.
        element_property=True,
    )

class ValueSetExpansionContains(fhir.ValueSetExpansionContains):
    system: fhirtypes.Uri | None = Field(
        None,
        alias="system",
        title="System value for the code",
        description=(
            "The system that defines the meaning of the symbol in the code. If the "
            "system is a URL, it SHALL be absolute, that is, it SHALL be a literal "
            "address at which at which an authoritative instance of the system "
            "definition exists and SHALL remain constant over time. If no system is "
            "specified, the system is not identified."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    abstract: bool | None = Field(
        None,
        alias="abstract",
        title="If user cannot select this entry",
        description=(
            "If true, this entry is included in the expansion for navigational "
            "purposes, and the user cannot select the code directly as a proper "
            "selection. (If the value set defines a post-composition grammar, it "
            "can be used to check that the selected codes are properly related.)"
        ),
        # if property is element of this resource.
        element_property=True,
    )
    inactive: bool | None = Field(
        None,
        alias="inactive",
        title="If concept is inactive in the code system",
        description=(
            "If true, this entry of the expansion is not included in the value set "
            "definition, and it cannot be selected as a proper value for this "
            "element. This entry may still be included for reasons such as "
            "navigational support, or to make the expansion self-contained."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version: fhirtypes.String | None = Field(
        None,
        alias="version",
        title="Version in which this code/display is defined",
        description=(
            "The version of this code system that defined this code and display - "
            "may be omitted if not relevant in this context."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    code: fhirtypes.Code | None = Field(
        None,
        alias="code",
        title="Code - if blank, this is not a selectable code",
        description=(
            "A code - a text symbol - that uniquely identifies the concept within the"
            " code system."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    display: fhirtypes.String | None = Field(
        None,
        alias="display",
        title="User display for the concept",
        description=(
            "The recommended display for this item in the expansion."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contains: list[fhirtypes.ValueSetExpansionContainsType] = Field(
        [],
        alias="contains",
        title="Codes contained under this entry",
        description=(
            "Other codes and entries contained under this entry in the hierarchy."
        ),
        # if property is element of this resource.
        element_property=True,
    )
ValueSetExpansionContains.update_forward_refs()

class ValueSetExpansion(fhir.ValueSetExpansion):
    identifier: fhirtypes.Uri | None = Field(
        None,
        alias="identifier",
        title="Uniquely identifies this expansion",
        description=(
            "An identifier that uniquely identifies this expansion of the valueset "
            "vs the base valueset, based on the identifier of the value set plus the"
            " expansion parameters. This is a business identifier used to refer to "
            "this particular expansion of the valueset."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    timestamp: fhirtypes.DateTime | None = Field(
        None,
        alias="timestamp",
        title="Time ValueSet expansion happened",
        description=(
            "The time at which the expansion was produced by the expanding system."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    total: fhirtypes.Integer | None = Field(
        None,
        alias="total",
        title="Total number of codes in the expansion",
        description=(
            "The total number of concepts in the expansion. If the number of "
            "concept nodes in this resource is less than the stated number, then "
            "the server can return more using the offset parameter."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    offset: fhirtypes.Integer | None = Field(
        None,
        alias="offset",
        title="Offset at which this resource starts",
        description=(
            "If paging is being used, the offset at which this resource starts.  "
            "I.e. this resource is a partial view into the expansion. If paging is "
            "not being used, this element SHALL NOT be present."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    parameter: list[fhir.ValueSetExpansionParameter] = Field(
        [],
        alias="parameter",
        title="Parameter that controlled the expansion process",
        description=(
            "A parameter that controlled the expansion process. These parameters "
            "may be used by users of expanded value sets to check whether the "
            "expansion is suitable for a particular purpose, or to pick the correct"
            " expansion."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contains: list[ValueSetExpansionContains] = Field(
        [],
        alias="contains",
        title="Codes in the value set",
        description=(
            "The codes that are contained in the value set expansion."
        ),
        # if property is element of this resource.
        element_property=True,
    )
ValueSetExpansion.update_forward_refs()

class ValueSet(fhir.ValueSet):
    resourceType: str = Field("ValueSet", const=True)
    url: fhirtypes.Uri = Field(
        None,
        alias="url",
        title=(
            "Canonical identifier for this value set, represented as a URI "
            "(globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this value set when it is "
            "referenced in a specification, model, design or an instance; also "
            "called its canonical identifier. This SHOULD be globally unique and "
            "SHOULD be a literal address at which at which an authoritative "
            "instance of this value set is (or will be) published. This URL can be "
            "the target of a canonical reference. It SHALL remain the same when the"
            " value set is stored on different servers."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    version: fhirtypes.String = Field(
        None,
        alias="version",
        title="Business version of the value set",
        description=(
            "The identifier that is used to identify this version of the value set "
            "when it is referenced in a specification, model, design or instance. "
            "This is an arbitrary value managed by the value set author and is not "
            "expected to be globally unique. For example, it might be a timestamp "
            "(e.g. yyyymmdd) if a managed version is not available. There is also "
            "no expectation that versions can be placed in a lexicographical "
            "sequence."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Name for this value set (computer friendly)",
        description=(
            "A natural language name identifying the value set. This name should be"
            " usable as an identifier for the module by machine processing "
            "applications such as code generation."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    identifier: list[fhirtypes.IdentifierType] = Field(
        [],
        alias="identifier",
        title="Additional identifier for the value set (business identifier)",
        description=(
            "A formal identifier that is used to identify this value set when it is"
            " represented in other formats, or referenced in a specification, "
            "model, design or an instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    immutable: bool = Field(
        None,
        alias="immutable",
        title=(
            "Indicates whether or not any change to the content logical definition "
            "may occur"
        ),
        description=(
            "If this is set to 'true', then no new versions of the content logical "
            "definition can be created.  Note: Other metadata might still change."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    title: fhirtypes.String = Field(
        None,
        alias="title",
        title="Name for this value set (human friendly)",
        description="A short, descriptive, user-friendly title for the value set.",
        # if property is element of this resource.
        element_property=True,
    )
    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this value set. Enables tracking the life-cycle of the "
            "content. The status of the value set applies to the value set "
            "definition (ValueSet.compose) and the associated ValueSet metadata. "
            "Expansions do not have a state."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["draft", "active", "retired", "unknown"],
    )
    experimental: bool = Field(
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this value set is authored for "
            "testing purposes (or education/evaluation/marketing) and is not "
            "intended to be used for genuine usage."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    publisher: fhirtypes.String = Field(
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the value "
            "set."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    contact: list[fhirtypes.ContactDetailType] = Field(
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    copyright: fhirtypes.Markdown = Field(
        None,
        alias="copyright",
        title="Use and/or publishing restrictions",
        description=(
            "A copyright statement relating to the value set and/or its contents. "
            "Copyright statements are generally legal restrictions on the use and "
            "publishing of the value set."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date (and optionally time) when the value set was created or "
            "revised (e.g. the 'content logical definition')."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    lockedDate: fhirtypes.Date = Field(
        None,
        alias="lockedDate",
        title="Fixed date for references with no specified version (transitive)",
        description=(
            "The Locked Date is  the effective date that is used to determine the "
            "version of all referenced Code Systems and Value Set Definitions "
            "included in the compose that are not already tied to a specific "
            "version."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description: fhirtypes.Markdown = Field(
        None,
        alias="description",
        title="Natural language description of the value set",
        description=(
            "A free text natural language description of the value set from a "
            "consumer's perspective. The textual description specifies the span of "
            "meanings for concepts to be included within the Value Set Expansion, "
            "and also may specify the intended use and limitations of the Value "
            "Set."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    useContext: list[fhirtypes.UsageContextType] = Field(
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate value set instances."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    jurisdiction: list[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="jurisdiction",
        title="Intended jurisdiction for value set (if applicable)",
        description=(
            "A legal or geographic region in which the value set is intended to be "
            "used."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    immutable: bool = Field(
        None,
        alias="immutable",
        title=(
            "Indicates whether or not any change to the content logical definition "
            "may occur"
        ),
        description=(
            "If this is set to 'true', then no new versions of the content logical "
            "definition can be created.  Note: Other metadata might still change."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    purpose: fhirtypes.Markdown = Field(
        None,
        alias="purpose",
        title="Why this value set is defined",
        description=(
            "Explanation of why this value set is needed and why it has been "
            "designed as it has."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    compose: ValueSetCompose = Field(
        None,
        alias="compose",
        title="Content logical definition of the value set (CLD)",
        description=(
            "A set of criteria that define the contents of the value set by "
            "including or excluding codes selected from the specified code "
            "system(s) that the value set draws from. This is also known as the "
            "Content Logical Definition (CLD)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    expansion: ValueSetExpansion = Field(
        None,
        alias="expansion",
        title='Used when the value set is "expanded"',
        description=(
            'A value set can also be "expanded", where the value set is turned into'
            " a simple collection of enumerated codes. This element holds the "
            "expansion, if it has been performed."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    


