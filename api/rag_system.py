# rag_system.py
# Module for Retrieval Augmented Generation (RAG) system for farming tips

import json
import os
import random
from typing import Dict, Any, List, Optional, Tuple

# In a real application, this would use a vector database and LLM
# For this demo, we'll use a simple in-memory approach with pre-defined content

# Sample knowledge base of farming tips
FARMING_TIPS = [
    {
        "id": 1,
        "title": "Improving Soil Organic Matter",
        "category": "Soil Health",
        "content": "Increasing organic matter in your soil is fundamental to biodynamic farming. Add compost, cover crops, and crop rotations to build soil structure. Aim for at least 5% organic matter content for optimal soil health. Biodynamic preparations 500 (horn manure) and 502-507 (compost preparations) can significantly enhance the decomposition process and improve humus formation.",
        "tags": ["organic matter", "compost", "soil structure", "biodynamic preparations"]
    },
    {
        "id": 2,
        "title": "Managing Soil pH Naturally",
        "category": "Soil Chemistry",
        "content": "Maintain soil pH between 6.0-7.0 for most crops. Use dolomite lime to raise pH in acidic soils, or elemental sulfur to lower pH in alkaline soils. Biodynamic approach considers pH as part of the living system - focus on building soil biology rather than just chemical adjustments. Regular applications of compost and biodynamic preparations help stabilize pH naturally over time.",
        "tags": ["pH", "lime", "sulfur", "soil biology"]
    },
    {
        "id": 3,
        "title": "Biodynamic Planting Calendar",
        "category": "Planting",
        "content": "Follow the biodynamic calendar which aligns planting activities with lunar and cosmic rhythms. Root crops perform best when planted during earth days, leaf crops during water days, flowering plants during air days, and fruiting crops during fire days. This approach recognizes the subtle influences of celestial bodies on plant growth and development.",
        "tags": ["planting calendar", "lunar cycles", "cosmic rhythms"]
    },
    {
        "id": 4,
        "title": "Natural Pest Management",
        "category": "Pest Control",
        "content": "Create a balanced ecosystem to manage pests naturally. Interplant aromatic herbs like basil, mint, and marigold to repel insects. Use biodynamic preparation 501 (horn silica) to strengthen plants against fungal diseases. Encourage beneficial insects by maintaining diverse habitats. Spray fermented nettle tea to deter aphids and strengthen plants against stress.",
        "tags": ["pest control", "beneficial insects", "companion planting", "preparation 501"]
    },
    {
        "id": 5,
        "title": "Water Conservation Techniques",
        "category": "Water Management",
        "content": "Implement water conservation practices such as mulching, drip irrigation, and rainwater harvesting. Biodynamic farms focus on building soil organic matter which improves water retention capacity. Apply horn manure preparation (500) before expected rainfall to maximize water absorption and distribution in the soil profile.",
        "tags": ["water conservation", "mulching", "irrigation", "water retention"]
    },
    {
        "id": 6,
        "title": "Biodynamic Composting",
        "category": "Soil Fertility",
        "content": "Create biodynamic compost by layering green materials (nitrogen-rich) with brown materials (carbon-rich) and adding biodynamic compost preparations 502-507. These preparations made from medicinal herbs enhance the composting process and imbue specific qualities to the finished compost. Turn the pile regularly and maintain proper moisture for optimal decomposition.",
        "tags": ["compost", "biodynamic preparations", "soil fertility", "organic matter"]
    },
    {
        "id": 7,
        "title": "Cover Cropping Strategies",
        "category": "Soil Health",
        "content": "Implement strategic cover cropping to improve soil health. Use legumes like clover and vetch to fix nitrogen, deep-rooted plants like daikon radish to break compaction, and grasses to add organic matter. In biodynamic farming, timing cover crop planting and termination with lunar cycles can enhance their effectiveness.",
        "tags": ["cover crops", "nitrogen fixation", "soil structure", "green manure"]
    },
    {
        "id": 8,
        "title": "Microbiome Enhancement",
        "category": "Soil Biology",
        "content": "Foster a diverse soil microbiome by minimizing tillage, avoiding synthetic chemicals, and applying biodynamic preparations. Horn manure preparation (500) specifically stimulates microbial activity. Consider applying small amounts of well-aged compost as microbial inoculants rather than as a primary nutrient source.",
        "tags": ["microbiome", "soil biology", "microbial diversity", "preparation 500"]
    },
    {
        "id": 9,
        "title": "Crop Rotation Principles",
        "category": "Planting",
        "content": "Follow a 4-7 year crop rotation to break pest cycles and balance soil nutrients. Group crops by plant families and their nutritional needs. In biodynamic farming, consider rotating crops based on the plant part harvested: root crops, followed by leaf crops, then flowering plants, and finally fruiting plants.",
        "tags": ["crop rotation", "plant families", "pest management", "nutrient balance"]
    },
    {
        "id": 10,
        "title": "Biodynamic Preparations Guide",
        "category": "Soil Fertility",
        "content": "The nine biodynamic preparations (500-508) are essential to biodynamic farming. Preparation 500 (horn manure) stimulates soil life and root growth. Preparation 501 (horn silica) enhances light metabolism and plant quality. Preparations 502-507 are compost additives made from medicinal herbs. Preparation 508 (horsetail tea) helps prevent fungal diseases.",
        "tags": ["biodynamic preparations", "horn manure", "horn silica", "compost preparations"]
    },
    {
        "id": 11,
        "title": "Companion Planting for Biodiversity",
        "category": "Planting",
        "content": "Enhance biodiversity and natural pest control through companion planting. Plant aromatic herbs among vegetables to repel pests. Use flowers like marigolds and nasturtiums to attract beneficial insects. The three sisters method (corn, beans, and squash) exemplifies companion planting by combining plants that physically and nutritionally support each other.",
        "tags": ["companion planting", "biodiversity", "pest control", "three sisters"]
    },
    {
        "id": 12,
        "title": "Soil Remineralization",
        "category": "Soil Chemistry",
        "content": "Replenish soil minerals using rock dust, kelp, and other natural amendments. Biodynamic farming recognizes the importance of trace minerals for plant health and nutritional quality. Apply rock dust in small amounts (about 100-200 lbs per acre) every few years to provide slow-release minerals that support microbial activity and plant health.",
        "tags": ["minerals", "rock dust", "trace elements", "remineralization"]
    },
    {
        "id": 13,
        "title": "Biodynamic Tree Care",
        "category": "Pest Control",
        "content": "Care for fruit trees using biodynamic methods. Apply tree paste (a mixture of cow manure, clay, and sand) to trunks to protect against disease and insect damage. Prune during the dormant season on fruit days according to the biodynamic calendar. Spray preparation 501 (horn silica) to enhance fruit quality and disease resistance.",
        "tags": ["tree care", "fruit trees", "tree paste", "pruning"]
    },
    {
        "id": 14,
        "title": "Seed Saving and Selection",
        "category": "Planting",
        "content": "Save seeds from your best-performing plants to develop varieties adapted to your local conditions. In biodynamic farming, seeds are ideally saved during the appropriate moon phase to enhance vitality. Store seeds in cool, dry conditions in paper envelopes or glass jars. Conduct germination tests before planting to ensure viability.",
        "tags": ["seed saving", "local adaptation", "seed storage", "germination"]
    },
    {
        "id": 15,
        "title": "Biodynamic Weed Management",
        "category": "Pest Control",
        "content": "Manage weeds through prevention, competition, and timely intervention. Use mulch, cover crops, and proper spacing to suppress weeds. In biodynamic farming, weeds are seen as indicators of soil conditions - observe which weeds grow to understand soil imbalances. Consider making weed pepper sprays by fermenting problematic weeds to suppress their growth.",
        "tags": ["weed management", "mulching", "cover crops", "weed indicators"]
    }
]

def query_farming_tips(query: str, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """
    Query the farming tips knowledge base using a RAG approach.
    
    Args:
        query: User's query string
        filters: Optional filters to apply (category, tags, etc.)
        
    Returns:
        List of relevant farming tips
    """
    # In a real RAG system, this would:
    # 1. Convert the query to a vector embedding
    # 2. Search a vector database for similar content
    # 3. Retrieve relevant documents
    # 4. Generate a response using an LLM with the retrieved context
    
    # For this demo, we'll use simple keyword matching
    results = search_tips(query, filters)
    
    # Sort results by relevance
    results.sort(key=lambda x: x["relevance"], reverse=True)
    
    # Return only the tip data (without the relevance score)
    return [tip["tip"] for tip in results]

def search_tips(query: str, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """
    Search for farming tips based on query and filters.
    
    Args:
        query: User's query string
        filters: Optional filters to apply
        
    Returns:
        List of tips with relevance scores
    """
    query_terms = query.lower().split()
    results = []
    
    for tip in FARMING_TIPS:
        # Skip if category filter doesn't match
        if filters and "category" in filters and filters["category"] != tip["category"]:
            continue
            
        # Skip if tag filter doesn't match
        if filters and "tags" in filters:
            if not any(tag in tip["tags"] for tag in filters["tags"]):
                continue
        
        # Calculate relevance score
        relevance = calculate_relevance(tip, query_terms)
        
        if relevance > 0:
            results.append({
                "tip": tip,
                "relevance": relevance
            })
    
    # If no results with relevance, return some random tips
    if not results:
        sample_size = min(3, len(FARMING_TIPS))
        random_tips = random.sample(FARMING_TIPS, sample_size)
        results = [{
            "tip": tip,
            "relevance": 0.1  # Low relevance score
        } for tip in random_tips]
    
    return results

def calculate_relevance(tip: Dict[str, Any], query_terms: List[str]) -> float:
    """
    Calculate relevance score of a tip to the query terms.
    
    Args:
        tip: Farming tip dictionary
        query_terms: List of query terms
        
    Returns:
        Relevance score (0-1)
    """
    # Combine all searchable text
    tip_text = f"{tip['title']} {tip['category']} {tip['content']} {' '.join(tip['tags'])}".lower()
    
    # Count matching terms
    matches = sum(1 for term in query_terms if term in tip_text)
    
    # Calculate base relevance score
    if not query_terms:
        return 0.5  # Default score for empty query
    
    base_score = matches / len(query_terms)
    
    # Boost score for title and tag matches
    title_matches = sum(1 for term in query_terms if term in tip['title'].lower())
    tag_matches = sum(1 for term in query_terms if any(term in tag.lower() for tag in tip['tags']))
    
    title_boost = title_matches * 0.3
    tag_boost = tag_matches * 0.2
    
    # Calculate final score (capped at 1.0)
    final_score = min(1.0, base_score + title_boost + tag_boost)
    
    return final_score

# Function to simulate LLM-generated personalized response
def generate_personalized_response(query: str, retrieved_tips: List[Dict[str, Any]]) -> str:
    """
    Generate a personalized response based on the query and retrieved tips.
    In a real application, this would use an LLM like llama-cpp-python.
    
    Args:
        query: User's query string
        retrieved_tips: List of retrieved tips
        
    Returns:
        Generated response string
    """
    # In a real application, this would prompt an LLM with the query and retrieved tips
    # For this demo, we'll return a template response
    
    if not retrieved_tips:
        return "I don't have specific information about that topic in biodynamic farming. Consider exploring our general resources on soil health and biodynamic preparations."
    
    # Get the most relevant tip
    top_tip = retrieved_tips[0]
    
    # Create a simple response template
    response = f"Based on your interest in {top_tip['category'].lower()}, here's what I can tell you:\n\n"
    response += f"{top_tip['content']}\n\n"
    
    # Add information from other tips if available
    if len(retrieved_tips) > 1:
        response += "You might also find these related points helpful:\n"
        for tip in retrieved_tips[1:3]:  # Include up to 2 more tips
            response += f"- {tip['title']}: {tip['content'][:100]}...\n"
    
    # Add a recommendation
    response += "\nFor best results with biodynamic farming, remember to consider the whole farm ecosystem and cosmic rhythms in your practices."
    
    return response