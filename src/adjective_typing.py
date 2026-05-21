"""
Adjective categorization utilities.

This module contains reusable functions extracted from the
analysis notebook.
"""
from src.adjective_typing import (
    clean_adjective,
    clean_adjective_list,
    build_lookup
)

import re
from collections import defaultdict


def clean_adjective(word):
    """Normalize adjective formatting."""
    return re.sub(r"[^a-zA-Z\\- ]", "", word).strip().lower()


def clean_adjective_list(words):
    """Clean and deduplicate adjective lists."""
    cleaned = [clean_adjective(word) for word in words]
    return sorted(set(word for word in cleaned if word))


def build_lookup(categories):
    """Build adjective → category lookup."""
    lookup = defaultdict(list)

    for category, adjectives in categories.items():
        for adjective in clean_adjective_list(adjectives):
            lookup[adjective].append(category)

    return dict(lookup)
