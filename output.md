# Namespaces
```
**bibo:** http://purl.org/ontology/bibo/
**cc:** http://creativecommons.org/ns#
**dc:** http://purl.org/dc/elements/1.1/
**dcterms:** http://purl.org/dc/terms/
**eprints:** http://www.ukoln.ac.uk/repositories/digirep/index/Eprints_Type_Vocabulary_Encoding_Scheme#
**fabio:** http://purl.org/spar/fabio#
**geonames:** http://www.geonames.org/ontology#
**iana:** http://www.iana.org/assignments/media-types/
**lang:** http://id.loc.gov/vocabulary/iso639-2/
**mrel:** http://id.loc.gov/vocabulary/relators/
**naf:** http://id.loc.gov/authorities/names/
**obo:** http://purl.obolibrary.org/obo/
**pcdm:** http://pcdm.org/models#
**prism:** http://prismstandard.org/namespaces/basic/3.0/
**rdf:** http://www.w3.org/1999/02/22-rdf-syntax-ns#
**rdfs:** http://www.w3.org/2000/01/rdf-schema#
**skos:** http://www.w3.org/2004/02/skos/core#
**status:** http://www.w3.org/2003/06/sw-vocab-status/ns#
**owl:** http://www.w3.org/2002/07/owl#
**tgn:** http://vocab.getty.edu/tgn/
**ual:** http://terms.library.ualberta.ca/
**vivo:** http://vivoweb.org/ontology/core#
**works:** http://pcdm.org/works#
**xsd:** http://www.w3.org/2001/XMLSchema#
```
# predicates
```
## pcdm:fileOf
## rdfs:comment
### Links from a File to its containing Object.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### is file of
## rdfs:range
## rdfs:subPropertyOf
## owl:inverseOf
## pcdm:hasFile
## rdfs:comment
### Links to a File contained by this Object.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### has file
## rdfs:range
## rdfs:subPropertyOf
## pcdm:hasMember
## rdfs:comment
### Links to a subsidiary Object or Collection. Typically used to link
          to component parts, such as a book linking to a page.  Note on transitivity: hasMember is
          not defined as transitive, but applications may treat it as transitive as local needs
          dictate.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### has member
## rdfs:range
## rdfs:subPropertyOf
## owl:inverseOf
## pcdm:hasRelatedObject
## rdfs:comment
### Links to a related Object that is not a component part, such as an object representing a donor agreement or policies that govern the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### has related object
## rdfs:range
## rdfs:subPropertyOf
## owl:inverseOf
## pcdm:memberOf
## rdfs:comment
### Links from an Object or Collection to a containing Object or Collection.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### is member of
## rdfs:range
## rdfs:subPropertyOf
## pcdm:relatedObjectOf
## rdfs:comment
### Links from an Object to a Object or Collection that it is related to.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### is related object of
## rdfs:range
## rdfs:subPropertyOf
## prism:doi
## rdfs:comment
### The Digital Object Identifier, DOI, for the article.
## rdfs:domain
## rdfs:isDefinedBy
### http://prismstandard.org/namespaces/basic/3.0
## rdfs:label
### Digital Object Identifier
## rdfs:range
## dc:Contributor
## dcterms:description
### Examples of a Contributor include a person, an organization, or a service. Typically, the name of a Contributor should be used to indicate the entity.
## dcterms:hasVersion
### http://dublincore.org/usage/terms/history/#contributor-006
## rdfs:comment
### An entity responsible for making contributions to the resource.
## rdfs:domain
## rdfs:isDefinedBy
### http://purl.org/dc/elements/1.1/
## rdfs:label
### Contributor
## rdfs:range
## dc:Creator
## dcterms:description
### Examples of a Creator include a person, an organization, or a service. Typically, the name of a Creator should be used to indicate the entity.
## dcterms:hasVersion
### http://dublincore.org/usage/terms/history/#creator-006
## rdfs:comment
### An entity primarily responsible for making the resource.
## rdfs:domain
## rdfs:isDefinedBy
### http://purl.org/dc/elements/1.1/
## rdfs:label
### Creator
## rdfs:range
## dc:Rights
## dcterms:description
### Typically, rights information includes a statement about various property rights associated with the resource, including intellectual property rights.
## dcterms:hasVersion
### http://dublincore.org/usage/terms/history/#rights-006
## rdfs:comment
### Information about rights held in and over the resource.
## rdfs:domain
## rdfs:isDefinedBy
### http://purl.org/dc/elements/1.1/
## rdfs:label
### Rights
## rdfs:range
## dc:Subject
## dcterms:description
### Typically, the subject will be represented using keywords, key phrases, or classification codes. Recommended best practice is to use a controlled vocabulary.
## dcterms:hasVersion
### http://dublincore.org/usage/terms/history/#subject-007
## rdfs:comment
### The topic of the resource.
## rdfs:domain
## rdfs:isDefinedBy
### http://purl.org/dc/elements/1.1/
## rdfs:label
### Subject
## rdfs:range
## dcterms:abstract
## dcterms:hasVersion
## rdfs:comment
### A summary of the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Abstract
## rdfs:range
## rdfs:subPropertyOf
## dcterms:alternative
## dcterms:description
### The distinction between titles and alternative titles is application-specific.
## dcterms:hasVersion
## rdfs:comment
### An alternative name for the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Alternative Title
## rdfs:range
## rdfs:subPropertyOf
## dcterms:created
## dcterms:hasVersion
## rdfs:comment
### Date of creation of the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Date Created
## rdfs:range
## rdfs:subPropertyOf
## dcterms:date
## dcterms:dateAccepted
## dcterms:description
### Examples of resources to which a Date Accepted may be relevant are a thesis (accepted by a university department) or an article (accepted by a journal).
## dcterms:hasVersion
## rdfs:comment
### Date of acceptance of the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Date Accepted
## rdfs:range
## rdfs:subPropertyOf
## dcterms:dateSubmitted
## dcterms:description
### Examples of resources to which a Date Submitted may be relevant are a thesis (submitted to a university department) or an article (submitted to a journal).
## dcterms:hasVersion
## rdfs:comment
### Date of submission of the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Date Submitted
## rdfs:range
## rdfs:subPropertyOf
## dcterms:description
## dcterms:description
### Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.
## dcterms:hasVersion
## rdfs:comment
### An account of the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Description
## rdfs:range
## rdfs:subPropertyOf
## dcterms:identifier
## dcterms:description
### Recommended best practice is to identify the resource by means of a string conforming to a formal identification system. 
## dcterms:hasVersion
## rdfs:comment
### An unambiguous reference to the resource within a given context.
## rdfs:isDefinedBy
## rdfs:label
### Identifier
## rdfs:range
## rdfs:subPropertyOf
## dcterms:isVersionOf
## dcterms:description
### Changes in version imply substantive changes in content rather than differences in format.
## dcterms:hasVersion
## rdfs:comment
### A related resource of which the described resource is a version, edition, or adaptation.
## rdfs:isDefinedBy
## rdfs:label
### Is Version Of
## rdfs:subPropertyOf
## skos:note
### This term is intended to be used with non-literal values as defined in the DCMI Abstract Model (http://dublincore.org/documents/abstract-model/).  As of December 2007, the DCMI Usage Board is seeking a way to express this intention with a formal range declaration.
## dcterms:language
## dcterms:description
### Recommended best practice is to use a controlled vocabulary such as RFC 4646 [RFC4646].
## dcterms:hasVersion
## rdfs:comment
### A language of the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Language
## rdfs:range
## rdfs:subPropertyOf
## dcterms:license
## dcterms:hasVersion
## rdfs:comment
### A legal document giving official permission to do something with the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### License
## rdfs:range
## rdfs:subPropertyOf
## dcterms:modified
## dcterms:hasVersion
## rdfs:comment
### Date on which the resource was changed.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Date Modified
## rdfs:range
## rdfs:subPropertyOf
## dcterms:relation
## dcterms:description
### Recommended best practice is to identify the related resource by means of a string conforming to a formal identification system. 
## dcterms:hasVersion
## rdfs:comment
### A related resource.
## rdfs:isDefinedBy
## rdfs:label
### Relation
## rdfs:subPropertyOf
## skos:note
### This term is intended to be used with non-literal values as defined in the DCMI Abstract Model (http://dublincore.org/documents/abstract-model/).  As of December 2007, the DCMI Usage Board is seeking a way to express this intention with a formal range declaration.
## dcterms:source
## dcterms:description
### The described resource may be derived from the related resource in whole or in part. Recommended best practice is to identify the related resource by means of a string conforming to a formal identification system.
## dcterms:hasVersion
## rdfs:comment
### A related resource from which the described resource is derived.
## rdfs:isDefinedBy
## rdfs:label
### Source
## rdfs:subPropertyOf
## skos:note
### This term is intended to be used with non-literal values as defined in the DCMI Abstract Model (http://dublincore.org/documents/abstract-model/).  As of December 2007, the DCMI Usage Board is seeking a way to express this intention with a formal range declaration.
## dcterms:spatial
## dcterms:hasVersion
## rdfs:comment
### Spatial characteristics of the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Spatial Coverage
## rdfs:range
## rdfs:subPropertyOf
## dcterms:temporal
## dcterms:hasVersion
## rdfs:comment
### Temporal characteristics of the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Temporal Coverage
## rdfs:range
## rdfs:subPropertyOf
## dcterms:title
## dcterms:hasVersion
## rdfs:comment
### A name given to the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Title
## rdfs:range
## rdfs:subPropertyOf
## dcterms:type
## dcterms:description
### Recommended best practice is to use a controlled vocabulary such as the DCMI Type Vocabulary [DCMITYPE]. To describe the file format, physical medium, or dimensions of the resource, use the Format element.
## dcterms:hasVersion
## rdfs:comment
### The nature or genre of the resource.
## rdfs:domain
## rdfs:isDefinedBy
## rdfs:label
### Type
## rdfs:range
## rdfs:subPropertyOf
## bibo:degree
## obo:IAO_0000112
### The source of the public description and this info is found here:  http://bibotools.googlecode.com/svn/bibo-ontology/trunk/doc/index.html.  Bibo considers this term "unstable".  The bibo editorial note is: "We are not defining, using an enumeration, the range of the bibo:degree to the defined list of bibo:ThesisDegree. We won't do it because we want people to be able to define new degress if needed by some special usecases. Creating such an enumeration would restrict this to happen."
## rdfs:comment
### The thesis degree.
## rdfs:domain
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### degree
### related degree
## rdfs:range
## rdfs:subPropertyOf
## status:term_status
### unstable
## skos:editorialNote
### We are not defining, using an enumeration, the range of the bibo:degree to the defined list of bibo:ThesisDegree. We won't do it because we want people to be able to define new degress if needed by some special usecases. Creating such an enumeration would restrict this to happen.
## http://www.w3.org/2008/05/skos#editorialNote
### We are not defining, using an enumeration, the range of the bibo:degree to the defined list of bibo:ThesisDegree. We won't do it because we want people to be able to define new degress if needed by some special usecases. Creating such an enumeration would restrict this to happen.
### [editor: Zach Schoenberger; date: 22-08-2017] Currently being used with literal. To bring in line with vocab, instances of 'thesis degree' need to be used, minted in ual namespace.
## bibo:status
## rdfs:comment
### The publication status of (typically academic) content.
## rdfs:domain
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### status
## rdfs:range
## rdfs:subPropertyOf
## status:term_status
### stable
## skos:editorialNote
### We are not defining, using an enumeration, the range of the bibo:status to the defined list of bibo:DocumentStatus. We won't do it because we want people to be able to define new status if needed by some special usecases. Creating such an enumeration would restrict this to happen.
## ual:Dissertant
## ual:indexWith
## rdfs:comment
### A person responsible for making the thesis.
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Dissertant
## rdfs:range
## rdfs:subPropertyOf
## ual:ark
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Archival Resource Key ID
## rdfs:range
## ual:commiteeMember
## rdfs:comment
### A person who was a member of a group of persons responsible for evaluating and approving the student's thesis.
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Commitee Member
## rdfs:range
## ual:department
## rdfs:comment
### A distinct, usually specialized educational unit within an educational organization responsible for the degree program to which the graduating student belonged.
### Example: "Department of Biological Sciences" or "Department of Chemistry"
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Department
## rdfs:range
## ual:depositor
## rdfs:comment
### User responsible for depositing the resource
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Depositor
## rdfs:range
## owl:deprecated
### true
## ual:fedora3Handle
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Fedora 3 Handle
## rdfs:range
## owl:deprecated
### true
## ual:fedora3UUID
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Fedora 3 UUID
## rdfs:range
## owl:deprecated
### true
## ual:graduationDate
## rdfs:comment
### Date student graduated from degree program.
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Graduation Date
## rdfs:range
## ual:institution
## ual:preferredValue
### http://id.loc.gov/authorities/names/n79058482
## rdfs:comment
### The University where the graduating student was enrolled.
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Institution
## ual:nnaFile
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Northern North America Filename
## rdfs:range
## ual:nnaItem
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Northern North America Item ID
## rdfs:range
## ual:proquest
## rdfs:comment
### Proquest Id for legacy thesis
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Proquest
## rdfs:range
## owl:backwardCompatibleWith
### http://terms.library.library.ca/identifiers/proquest
## owl:deprecated
### true
## ual:specialization
## rdfs:comment
### Example: "Microbiology and Biotechnology"; "Comparative Literature"
### Subject focus of degree awarded.
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Specialization
## rdfs:range
## ual:supervisor
## rdfs:comment
### Person responsible for the role of advising the graduating student.
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Supervisor
## rdfs:range
## ual:thesisLevel
## rdfs:comment
### The degree credential awarded
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Thesis Level
## rdfs:range
## ual:unicorn
## rdfs:domain
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Unicorn
```
# values
```
## lang:eng
## skos:preflabel
### English
## lang:fre
## skos:preflabel
### French
## lang:ger
## skos:preflabel
### German
## lang:ipk
## skos:preflabel
### Inupiaq
## lang:ita
## skos:preflabel
### Italian
## lang:jpn
## skos:preflabel
### Japanese
## lang:por
## skos:preflabel
### Portuguese
## lang:rus
## skos:preflabel
### Russian
## lang:spa
## skos:preflabel
### Spanish
## lang:ukr
## skos:preflabel
### Ukranian
## lang:vie
## skos:preflabel
### Vietnamese
## lang:zho
## skos:preflabel
### Chinese
## lang:zxx
## skos:preflabel
### No linguistic content
```
# vocab
```
## cc:License
## rdfs:comment
### a set of requests/permissions to users of a Work, e.g. a copyright license, the public domain, information for distributors
## rdfs:isDefinedBy
### https://creativecommons.org/ns#
## rdfs:label
### License
## rdfs:subClassOf
## pcdm:AlternateOrder
## rdfs:comment
### 
        An AlternateOrder is an alternate ordering of its parent's members.  It should only order the
        parent's members, and otherwise has all of the features of ordering (some members may be
        omitted from the order, members may appear more than once in the order, etc.).
      
## rdfs:isDefinedBy
## rdfs:label
### Alternate Order
## rdfs:subClassOf
## pcdm:Collection
## rdfs:comment
### 
        A Collection is a group of resources. Collections have descriptive metadata, access metadata,
        and may links to works and/or collections. By default, member works and collections are an
        unordered set, but can be ordered using the ORE Proxy class.
      
## rdfs:isDefinedBy
## rdfs:label
### Collection
## rdfs:subClassOf
## pcdm:File
## rdfs:comment
### 
        A File is a sequence of binary data and is described by some accompanying metadata.
        The metadata typically includes at least basic technical metadata (size, content type,
        modification date, etc.), but can also include properties related to preservation,
        digitization process, provenance, etc. Files MUST be contained by exactly one Object.
      
## rdfs:isDefinedBy
## rdfs:label
### File
## rdfs:subClassOf
## pcdm:Object
## rdfs:comment
### 
        An Object is an intellectual entity, sometimes called a "work", "digital object", etc.
        Objects have descriptive metadata, access metadata, may contain files and other Objects as
        member "components". Each level of a work is therefore represented by an Object instance,
        and is capable of standing on its own, being linked to from Collections and other Objects.
        Member Objects can be ordered using the ORE Proxy class.
      
## rdfs:isDefinedBy
## rdfs:label
### Object
## rdfs:subClassOf
## works:FileSet
## rdfs:comment
### 
      A group of related Files, typically a single master File and its derivatives.
    
## rdfs:isDefinedBy
## rdfs:label
### FileSet
## rdfs:subClassOf
## works:Range
## rdfs:comment
### 
      A section of a Work, corresponding to a IIIF Range.  Has member FileSets representing the
      physical parts of the Work are part of the section (e.g., which pages are in a chapter).
    
## rdfs:isDefinedBy
## rdfs:label
### Range
## rdfs:subClassOf
## skos:closeMatch
## works:TopRange
## rdfs:comment
### 
      A logical ordering of the component parts of a Work, corresponding to a IIIF Range with
      the "top" viewing hint.  Has member Ranges that represent the logical structure, such
      as chapters within a book, scenes in a film, etc.
    
## rdfs:isDefinedBy
## rdfs:label
### TopRange
## rdfs:subClassOf
## skos:closeMatch
## works:Work
## rdfs:comment
### 
      A work or intellectual entity, such as a book, film, dissertation, etc.
      Works have member FileSets representing their physical structure (e.g., pages in a book),
      and related TopRanges representing their logical structure or structures (e.g., sections
      and chapters in a book).
    
## rdfs:isDefinedBy
## rdfs:label
### Work
## rdfs:subClassOf
## dcterms:Agent
## rdfs:label
### Agent
## rdfs:subClassOf
## dcterms:LicenseDocument
## rdfs:label
### License Document
## rdfs:subClassOf
## bibo:Article
## rdfs:comment
### A written composition in prose, usually nonfiction, on a specific topic, forming an independent part of a book or other publication, as a newspaper or magazine.
## rdfs:isDefinedBy
## rdfs:label
### Article
## rdfs:subClassOf
## status:term_status
### stable
## skos:preflabel
### Journal Article
## bibo:Book
## rdfs:comment
### A written or printed work of fiction or nonfiction, usually on sheets of paper fastened or bound together within covers.
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### Book
## rdfs:subClassOf
## status:term_status
### stable
## bibo:BookSection
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### Book Section
## rdfs:subClassOf
## bibo:Chapter
## rdfs:comment
### A chapter of a book.
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### Chapter
## rdfs:subClassOf
## status:term_status
### unstable
## skos:preflabel
### Chapter
## bibo:Conference
## rdfs:subClassOf
## bibo:Document
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### Document
## rdfs:subClassOf
## bibo:DocumentStatus
## rdfs:comment
### The status of the publication of a document.
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### Document Status
## rdfs:subClassOf
## status:term_status
### stable
## bibo:Image
## rdfs:comment
### A document that presents visual or diagrammatic information.
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### Image
## rdfs:subClassOf
## status:term_status
### stable
## bibo:Report
## rdfs:comment
### A document describing an account or statement describing in detail an event, situation, or the like, usually as the result of observation, inquiry, etc..
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### Report
## rdfs:subClassOf
## status:term_status
### stable
## bibo:Thesis
## rdfs:comment
### A document created to summarize research findings associated with the completion of an academic degree.
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### Thesis
## rdfs:subClassOf
## status:term_status
### stable
## bibo:ThesisDegree
## rdfs:comment
### The academic degree of a Thesis
## rdfs:isDefinedBy
### http://purl.org/ontology/bibo/
## rdfs:label
### Thesis degree
## rdfs:subClassOf
## status:term_status
### stable
## http://purl.org/spar/fabio/DoctoralThesis
## rdfs:comment
### A thesis reporting the research undertaken during a period of graduate study leading to a doctoral degree.
## rdfs:isDefinedBy
### http://purl.org/spar/fabio/
## rdfs:label
### doctoral thesis
## rdfs:subClassOf
## owl:disjointWith
## http://purl.org/spar/fabio/MastersThesis
## rdfs:comment
### A thesis reporting a research project undertaken as part of a graduate course of education leading to a master's degree.
## rdfs:isDefinedBy
### http://purl.org/spar/fabio/
## rdfs:label
### master's thesis
## rdfs:subClassOf
## http://purl.org/spar/fabio/Thesis
## rdfs:subClassOf
## http://terms.library.ualbera.ca/PCDM
## ual:Concept
## ual:RepositoryObject
## rdfs:label
### Repository Object
## ual:learningObject
## rdfs:comment
### a collection of content items, practice items, and assessment items that are combined based on a single learning objective
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Learning Object
## rdfs:subClassOf
## ual:researchMaterial
## rdfs:comment
### a resource that cannot be neatly defined within the scope of any other type (i.e. "other")
## rdfs:isDefinedBy
### http://terms.library.ualberta.ca
## rdfs:label
### Research Material
## rdfs:subClassOf
## vivo:ConferencePaper
## obo:IAO_0000115
### A paper presented at a conference; optionally collected into a Proceedings or a special Journal issue
## rdfs:label
### Conference Paper
## rdfs:subClassOf
## vivo:ConferencePoster
## obo:IAO_0000115
### The digital file (or physical equivalent), if available after the conference, vs. the act of attending/presenting: use ConferencePresentation for information about date/time/location/name of the event where the poster was presented
## rdfs:label
### Conference Poster
## rdfs:subClassOf
## vivo:Dataset
## obo:IAO_0000112
### US Patent Data; US Job Data
## obo:IAO_0000115
### A named collection of data, usually containing only one type of data
## rdfs:label
### Dataset
## rdfs:subClassOf
## vivo:Review
## obo:IAO_0000115
### An article reviewing one or more other information resources (a book, one or more other articles, movies, etc)
## rdfs:label
### Review
## rdfs:subClassOf
## http://www.openarchives.org/ore/terms/Aggregation
## rdfs:subClassOf
## rdfs:Class
## rdfs:label
### Class
## rdfs:subClassOf
```
