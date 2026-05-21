# Adjective Typing

A linguistics/NLP project exploring whether English adjectives can be categorized according to semantic adjective-order classes using Roget’s Thesaurus as a source.

## Overview

English adjective order often follows a rough sequence such as opinion, size, age, shape, color, origin, material, and purpose. This project investigates whether adjectives can be grouped into useful semantic categories by processing entries from Roget’s Thesaurus. This can be used for stylometric analysis and authorship attribution studies.

## Project Status

This repository contains a cleaned project version and an archived copy of the original course notebook/code.

## Repository Structure

- `notebooks/` — cleaned analysis notebook
- `src/` — reusable Python code
- `archive/` — original course materials and generated files
- `requirements.txt` — Python dependencies

## Tools Used

- Python
- NLTK
- Jupyter Notebook

## Example Usage

```python
from src.adjective_typing import clean_adjective

clean_adjective("Beautiful!")
# -> "beautiful"
```

## Data Source

[Roget’s Thesaurus via Project Gutenberg](https://www.gutenberg.org/files/10681/10681-h/10681-h.htm).

## Notes

The `archive/` folder preserves the original notebook and converted Python file for reference.
