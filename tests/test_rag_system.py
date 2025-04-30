# MIT License
#
# Copyright (c) 2023 Biodynamic Offline
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

import pytest

from api.rag_system import query_farming_tips, search_tips, calculate_relevance


def test_calculate_relevance():
    """Test relevance calculation."""
    tip = {
        "title": "Soil Health",
        "category": "Soil",
        "content": "Improve soil health with organic matter",
        "tags": ["soil", "organic"]
    }
    
    # Test exact match
    assert calculate_relevance(tip, ["soil"]) > 0
    assert calculate_relevance(tip, ["organic"]) > 0
    
    # Test no match
    assert calculate_relevance(tip, ["water"]) == 0
    
    # Test empty query
    assert calculate_relevance(tip, []) == 0.5


def test_search_tips():
    """Test tip search functionality."""
    # Test with matching query
    results = search_tips("soil health", {"category": "Soil Health"})
    assert len(results) > 0
    assert all("tip" in result for result in results)
    assert all("relevance" in result for result in results)
    
    # Test with no matches
    results = search_tips("nonexistent", {})
    assert len(results) > 0  # Should return random tips
    
    # Test with category filter
    results = search_tips("soil", {"category": "Pest Control"})
    assert all(result["tip"]["category"] == "Pest Control" for result in results)


def test_query_farming_tips():
    """Test farming tips query functionality."""
    # Test with matching query
    tips = query_farming_tips("soil health")
    assert len(tips) > 0
    assert all("title" in tip for tip in tips)
    assert all("category" in tip for tip in tips)
    assert all("content" in tip for tip in tips)
    assert all("tags" in tip for tip in tips)
    
    # Test with category filter
    tips = query_farming_tips("soil", {"category": "Soil Health"})
    assert all(tip["category"] == "Soil Health" for tip in tips)
    
    # Test with tag filter
    tips = query_farming_tips("soil", {"tags": ["organic matter"]})
    assert all(any(tag in tip["tags"] for tag in ["organic matter"]) for tip in tips) 