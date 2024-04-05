##🔥MOJO REFACTOR w/ 🤗 Hugging Face "urchade/gliner_base" by Snyata
### ### TO BE COMPLETED AS OF SAT 6 APR 2024 ###
# Original Knowledge Graph Creator command line tool: kgcreator
[!Mark Watson - KGCreator](https://github.com/mark-watson/kgcreator)

[![PyPI](https://img.shields.io/pypi/v/kgcreator.svg)](https://pypi.org/project/kgcreator/)
[![Changelog](https://img.shields.io/github/v/release/mark-watson/kgcreator?include_prereleases&label=changelog)](https://github.com/mark-watson/kgcreator/releases)
[![Tests](https://github.com/mark-watson/kgcreator/workflows/Test/badge.svg)](https://github.com/mark-watson/kgcreator/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/mark-watson/kgcreator/blob/master/LICENSE)

### Knowledge Graph Creator: converts text to RDF triples.

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
