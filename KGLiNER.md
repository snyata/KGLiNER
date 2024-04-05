##🔥MOJO REFACTOR w/ 🤗 Hugging Face "urchade/gliner_base" by Snyata
##  ### TO BE COMPLETED AS OF SAT 6 APR 2024 ###
### Original Knowledge Graph Creator command line tool: kgcreator
#### [!Mark Watson - KGCreator](https://github.com/mark-watson/kgcreator)

#### Below is the KGLiNER basic outline
[![PyPI](https://img.shields.io/pypi/v/kgcreator.svg)](https://pypi.org/project/kgcreator/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/snyata/KGLiNER/blob/main/LICENSE)

## KGLiNER: converts text to RDF triples

### Additional Functionality in progress
- Exploration of the Modular AI Mojo language for improved performance.
- Portkey AI Gateway for managing LLM interactions.
- LLM Benchmarks with BenchLLM
- Generalized use of NER to identify Nodes and Edges
  - AI Gateway calls an LLM with the respective information in it.
      - Design: Multi-step process to ensure that  similar structural realtionships are found in the setup.
    - Use of the ```urchade/gliner_base``` model on Hugging Face
    - 



The Knowledge Graph Creator (kgcreator) is a tool for automating the generation of RDF data for Knowledge Graphs from raw text data read from an input directory path.

The Knowledge Graph Creator creates an output file containing RDF triples suitable for loading into any linked data/semantic web data store.

This Python command line utility is one of the example programs in my book
[Practical Python Artificial Intelligence Programming](https://leanpub.com/pythonai) that is available on [Leanpub.com](https://leanpub.com/pythonai) or available (in the future, this book is under development) to read for free on my web site [https://markwatson.com](https://markwatson.com).


## Notes on generating Neo4J graph data

Start by identifying:

- Names of entities (node labels).
- Names of relationships.
- Names of properties for nodes and relationships.
- Constraints to be defined.
- Indexes required.
- The most important queries?
