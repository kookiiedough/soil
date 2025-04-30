# soil_analyzer.py
# Module for analyzing soil samples and providing recommendations

import uuid
from datetime import datetime
from typing import Dict, Any, List

def analyze_soil_sample(sample_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze a soil sample and provide recommendations based on soil metrics.
    
    Args:
        sample_data: Dictionary containing soil sample data
        
    Returns:
        Dictionary with analysis results and recommendations
    """
    # Generate a unique ID for this analysis
    analysis_id = str(uuid.uuid4())
    
    # Extract soil metrics
    metrics = sample_data.get('metrics', {})
    
    # Calculate soil health score based on metrics
    health_score = calculate_soil_health_score(metrics)
    
    # Generate recommendations
    recommendations = generate_recommendations(metrics, health_score)
    
    # Create analysis result
    result = {
        "id": analysis_id,
        "sample_id": sample_data.get('id', 'unknown'),
        "sample_name": sample_data.get('name', 'Unnamed Sample'),
        "timestamp": datetime.now().isoformat(),
        "health_score": health_score,
        "metrics": metrics,
        "recommendations": recommendations,
        "status": "completed"
    }
    
    return result

def calculate_soil_health_score(metrics: Dict[str, Any]) -> float:
    """
    Calculate a soil health score based on various metrics.
    
    Args:
        metrics: Dictionary of soil metrics
        
    Returns:
        Soil health score (0-100)
    """
    # Initialize score
    score = 0.0
    total_weight = 0.0
    
    # Define metric weights and ideal ranges
    metric_params = {
        "organicMatter": {"weight": 3.0, "ideal": 5.0, "range": 10.0},
        "pH": {"weight": 2.0, "ideal": 6.8, "range": 3.0},
        "nitrogen": {"weight": 1.5, "ideal": 50.0, "range": 100.0},
        "phosphorus": {"weight": 1.5, "ideal": 60.0, "range": 120.0},
        "potassium": {"weight": 1.5, "ideal": 50.0, "range": 100.0},
        "calcium": {"weight": 1.0, "ideal": 1500.0, "range": 3000.0},
        "magnesium": {"weight": 1.0, "ideal": 200.0, "range": 400.0},
        "sulfur": {"weight": 0.8, "ideal": 15.0, "range": 30.0},
        "zinc": {"weight": 0.7, "ideal": 3.0, "range": 6.0},
        "manganese": {"weight": 0.7, "ideal": 12.0, "range": 24.0},
        "copper": {"weight": 0.7, "ideal": 1.8, "range": 3.6},
        "boron": {"weight": 0.7, "ideal": 0.8, "range": 1.6},
        "microbiomeHealth": {"weight": 4.0, "ideal": 100.0, "range": 100.0}
    }
    
    # Calculate score for each metric
    for metric, value in metrics.items():
        if metric in metric_params:
            params = metric_params[metric]
            
            # Calculate how close the value is to the ideal (0-1 scale)
            if metric == "pH":
                # Special case for pH which has an ideal range
                distance = abs(value - params["ideal"])
                normalized_score = max(0, 1 - (distance / (params["range"] / 2)))
            else:
                # For other metrics, higher is generally better up to the ideal
                normalized_score = min(value / params["ideal"], 1.0)
            
            # Add weighted score
            score += normalized_score * params["weight"]
            total_weight += params["weight"]
    
    # Calculate final score (0-100 scale)
    if total_weight > 0:
        final_score = (score / total_weight) * 100
    else:
        final_score = 50.0  # Default score if no metrics are provided
    
    return round(final_score, 1)

def generate_recommendations(metrics: Dict[str, Any], health_score: float) -> List[str]:
    """
    Generate recommendations based on soil metrics and health score.
    
    Args:
        metrics: Dictionary of soil metrics
        health_score: Overall soil health score
        
    Returns:
        List of recommendation strings
    """
    recommendations = []
    
    # Organic matter recommendations
    if "organicMatter" in metrics:
        organic_matter = metrics["organicMatter"]
        if organic_matter < 3.0:
            recommendations.append("Increase organic matter by adding compost, cover crops, or crop residues.")
        elif organic_matter < 5.0:
            recommendations.append("Maintain organic matter with regular additions of compost and minimal tillage.")
    
    # pH recommendations
    if "pH" in metrics:
        ph = metrics["pH"]
        if ph < 6.0:
            recommendations.append("Apply lime to raise soil pH to a more neutral level (6.5-7.0).")
        elif ph > 7.5:
            recommendations.append("Add sulfur or acidic organic matter to lower soil pH.")
    
    # Nutrient recommendations
    if "nitrogen" in metrics and metrics["nitrogen"] < 40:
        recommendations.append("Apply nitrogen-rich amendments like blood meal, fish emulsion, or legume cover crops.")
    
    if "phosphorus" in metrics and metrics["phosphorus"] < 50:
        recommendations.append("Increase phosphorus with bone meal, rock phosphate, or compost.")
    
    if "potassium" in metrics and metrics["potassium"] < 45:
        recommendations.append("Add potassium with wood ash, greensand, or compost.")
    
    if "calcium" in metrics and metrics["calcium"] < 1000:
        recommendations.append("Apply calcium amendments like gypsum or lime (if pH is low).")
    
    if "magnesium" in metrics and metrics["magnesium"] < 150:
        recommendations.append("Add magnesium with dolomitic lime or Epsom salts.")
    
    # Micronutrient recommendations
    micronutrient_deficiency = False
    if "zinc" in metrics and metrics["zinc"] < 2.0:
        micronutrient_deficiency = True
    if "manganese" in metrics and metrics["manganese"] < 8.0:
        micronutrient_deficiency = True
    if "copper" in metrics and metrics["copper"] < 1.0:
        micronutrient_deficiency = True
    if "boron" in metrics and metrics["boron"] < 0.5:
        micronutrient_deficiency = True
    
    if micronutrient_deficiency:
        recommendations.append("Consider applying a balanced micronutrient amendment or seaweed extract.")
    
    # Biodynamic-specific recommendations
    recommendations.append("Apply biodynamic preparation 500 (horn manure) to enhance soil microbial activity.")
    
    if health_score < 60:
        recommendations.append("Consider a full biodynamic treatment with preparations 500-507 to revitalize soil.")
    
    # General recommendations
    recommendations.append("Maintain soil moisture at consistent levels to support microbial activity.")
    recommendations.append("Minimize soil disturbance to protect soil structure and biology.")
    
    return recommendations