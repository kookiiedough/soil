# fastq_processor.py
# Module for processing FASTQ files and analyzing soil microbiome data

import os
import json
import random
from datetime import datetime
from typing import Dict, Any, List, Tuple

def process_fastq_file(file_path: str, file_id: str) -> None:
    """
    Process a FASTQ file to analyze soil microbiome composition.
    This is a simplified simulation of FASTQ processing for demonstration purposes.
    In a real application, this would use bioinformatics libraries to process the file.
    
    Args:
        file_path: Path to the uploaded FASTQ file
        file_id: Unique identifier for this file processing job
    """
    # Create a status file to track processing
    status_file = f"{os.path.dirname(file_path)}/{file_id}_status.json"
    
    # Update status to processing
    update_processing_status(status_file, "processing", "FASTQ file processing started")
    
    try:
        # Get file info
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        
        # In a real application, we would perform these steps:
        # 1. Quality control and trimming
        # 2. Alignment to reference database
        # 3. Taxonomic classification
        # 4. Diversity analysis
        # 5. Functional prediction
        
        # For this demo, we'll simulate the processing with random data
        # Simulate processing time
        # time.sleep(5)  # Uncomment in a real application
        
        # Generate analysis results
        analysis_results = generate_microbiome_analysis(file_name, file_size)
        
        # Save results to file
        results_file = f"data/analysis_results/{file_id}.json"
        with open(results_file, "w") as f:
            json.dump(analysis_results, f)
        
        # Update status to completed
        update_processing_status(status_file, "completed", "FASTQ file processing completed successfully")
        
    except Exception as e:
        # Update status to failed
        update_processing_status(status_file, "failed", f"Error processing FASTQ file: {str(e)}")
        raise

def update_processing_status(status_file: str, status: str, message: str) -> None:
    """
    Update the processing status file.
    
    Args:
        status_file: Path to the status file
        status: Current status (processing, completed, failed)
        message: Status message
    """
    status_data = {
        "status": status,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    
    with open(status_file, "w") as f:
        json.dump(status_data, f)

def generate_microbiome_analysis(file_name: str, file_size: int) -> Dict[str, Any]:
    """
    Generate a simulated microbiome analysis result.
    In a real application, this would be based on actual FASTQ file analysis.
    
    Args:
        file_name: Name of the processed file
        file_size: Size of the file in bytes
        
    Returns:
        Dictionary with analysis results
    """
    # Generate random microbiome composition
    bacteria_comp = generate_composition_data()
    fungi_comp = generate_composition_data(beneficial_bias=0.1)  # Slightly more beneficial fungi
    
    # Calculate soil health score based on microbiome composition
    soil_health_score = calculate_health_score(bacteria_comp, fungi_comp)
    
    # Generate dominant species list
    dominant_species = generate_dominant_species(soil_health_score)
    
    # Generate nutrient cycling capacity
    nutrient_cycling = generate_nutrient_cycling(soil_health_score)
    
    # Generate recommendations
    recommendations = generate_recommendations(bacteria_comp, fungi_comp, soil_health_score)
    
    # Create analysis result
    result = {
        "sample_id": f"SAMPLE-{random.randint(10000, 99999)}",
        "timestamp": datetime.now().isoformat(),
        "file_name": file_name,
        "file_size": file_size,
        "microbiome_composition": {
            "bacteria": {
                "beneficial": bacteria_comp[0],
                "neutral": bacteria_comp[1],
                "harmful": bacteria_comp[2]
            },
            "fungi": {
                "beneficial": fungi_comp[0],
                "neutral": fungi_comp[1],
                "harmful": fungi_comp[2]
            }
        },
        "soil_health_score": soil_health_score,
        "dominant_species": dominant_species,
        "nutrient_cycling": nutrient_cycling,
        "recommendations": recommendations
    }
    
    return result

def generate_composition_data(beneficial_bias: float = 0) -> Tuple[float, float, float]:
    """
    Generate random composition data for bacteria or fungi.
    
    Args:
        beneficial_bias: Bias towards beneficial microbes (positive value)
        
    Returns:
        Tuple of (beneficial, neutral, harmful) percentages
    """
    # Base values with some randomness
    beneficial = 60 + random.uniform(-10, 20) + beneficial_bias * 100
    harmful = 5 + random.uniform(-2, 10) - beneficial_bias * 50
    
    # Ensure values are within reasonable ranges
    beneficial = max(40, min(85, beneficial))
    harmful = max(1, min(20, harmful))
    
    # Calculate neutral to make total 100%
    neutral = 100 - beneficial - harmful
    
    # Round to integers
    beneficial = round(beneficial)
    neutral = round(neutral)
    harmful = round(harmful)
    
    # Adjust if needed to ensure sum is 100
    if beneficial + neutral + harmful != 100:
        neutral += 100 - (beneficial + neutral + harmful)
    
    return (beneficial, neutral, harmful)

def calculate_health_score(bacteria_comp: Tuple[float, float, float], fungi_comp: Tuple[float, float, float]) -> float:
    """
    Calculate soil health score based on microbiome composition.
    
    Args:
        bacteria_comp: Bacterial composition (beneficial, neutral, harmful)
        fungi_comp: Fungal composition (beneficial, neutral, harmful)
        
    Returns:
        Soil health score (0-100)
    """
    # Weight bacteria and fungi contributions
    bacteria_weight = 0.6
    fungi_weight = 0.4
    
    # Calculate scores
    bacteria_score = (bacteria_comp[0] * 1.0 + bacteria_comp[1] * 0.5 - bacteria_comp[2] * 1.0)
    fungi_score = (fungi_comp[0] * 1.0 + fungi_comp[1] * 0.5 - fungi_comp[2] * 1.0)
    
    # Combine scores
    combined_score = (bacteria_score * bacteria_weight + fungi_score * fungi_weight)
    
    # Normalize to 0-100 scale
    normalized_score = (combined_score / 100) * 100
    
    # Add some randomness
    final_score = normalized_score + random.uniform(-5, 5)
    
    # Ensure score is within 0-100 range
    final_score = max(0, min(100, final_score))
    
    return round(final_score, 1)

def generate_dominant_species(health_score: float) -> List[str]:
    """
    Generate a list of dominant beneficial species based on health score.
    
    Args:
        health_score: Soil health score
        
    Returns:
        List of species names
    """
    # Pool of beneficial species
    beneficial_bacteria = [
        "Bacillus subtilis",
        "Pseudomonas fluorescens",
        "Azotobacter vinelandii",
        "Rhizobium leguminosarum",
        "Bradyrhizobium japonicum",
        "Nitrosomonas europaea",
        "Nitrobacter winogradskyi",
        "Lactobacillus plantarum",
        "Streptomyces griseus",
        "Arthrobacter globiformis"
    ]
    
    beneficial_fungi = [
        "Trichoderma harzianum",
        "Glomus intraradices",
        "Aspergillus niger",
        "Penicillium bilaiae",
        "Beauveria bassiana",
        "Metarhizium anisopliae",
        "Saccharomyces cerevisiae",
        "Pisolithus tinctorius",
        "Glomus mosseae",
        "Phanerochaete chrysosporium"
    ]
    
    # Determine number of species based on health score
    if health_score >= 80:
        num_species = random.randint(7, 10)
    elif health_score >= 60:
        num_species = random.randint(5, 7)
    else:
        num_species = random.randint(3, 5)
    
    # Select species
    bacteria_count = int(num_species * 0.6)
    fungi_count = num_species - bacteria_count
    
    selected_bacteria = random.sample(beneficial_bacteria, min(bacteria_count, len(beneficial_bacteria)))
    selected_fungi = random.sample(beneficial_fungi, min(fungi_count, len(beneficial_fungi)))
    
    return selected_bacteria + selected_fungi

def generate_nutrient_cycling(health_score: float) -> Dict[str, str]:
    """
    Generate nutrient cycling capacity based on health score.
    
    Args:
        health_score: Soil health score
        
    Returns:
        Dictionary with nutrient cycling capacities
    """
    # Determine nutrient cycling capacity based on health score
    if health_score >= 80:
        nitrogen = "High"
        phosphorus = random.choice(["High", "Medium"])
        potassium = random.choice(["High", "Medium"])
    elif health_score >= 60:
        nitrogen = random.choice(["High", "Medium"])
        phosphorus = "Medium"
        potassium = random.choice(["Medium", "Low"])
    else:
        nitrogen = random.choice(["Medium", "Low"])
        phosphorus = random.choice(["Medium", "Low"])
        potassium = "Low"
    
    return {
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium
    }

def generate_recommendations(bacteria_comp: Tuple[float, float, float], 
                            fungi_comp: Tuple[float, float, float], 
                            health_score: float) -> List[str]:
    """
    Generate recommendations based on microbiome composition and health score.
    
    Args:
        bacteria_comp: Bacterial composition (beneficial, neutral, harmful)
        fungi_comp: Fungal composition (beneficial, neutral, harmful)
        health_score: Soil health score
        
    Returns:
        List of recommendation strings
    """
    recommendations = []
    
    # General recommendation based on health score
    if health_score >= 80:
        recommendations.append("Your soil shows excellent microbial diversity with strong presence of beneficial microorganisms.")
        recommendations.append("Continue your current management practices to maintain this healthy soil ecosystem.")
    elif health_score >= 60:
        recommendations.append("Your soil shows good microbial diversity with a healthy balance of beneficial microorganisms.")
        recommendations.append("Consider minor adjustments to further enhance soil biology.")
    else:
        recommendations.append("Your soil shows reduced microbial diversity and could benefit from biological amendments.")
        recommendations.append("Consider significant changes to your soil management practices.")
    
    # Specific recommendations based on composition
    if bacteria_comp[0] < 60:
        recommendations.append("Increase beneficial bacteria by applying compost tea or bacterial inoculants.")
    
    if fungi_comp[0] < 60:
        recommendations.append("Enhance fungal diversity by adding compost, mulch, or fungal inoculants.")
    
    if bacteria_comp[2] > 10 or fungi_comp[2] > 10:
        recommendations.append("Reduce harmful microorganisms by improving drainage and avoiding overwatering.")
    
    # Biodynamic-specific recommendations
    recommendations.append("Apply biodynamic preparation 500 (horn manure) to stimulate soil microbial activity.")
    
    if fungi_comp[0] < 50:
        recommendations.append("Use biodynamic preparation 507 (valerian) to stimulate phosphorus cycling and fungal activity.")
    
    # Management recommendations
    recommendations.append("Reduce tillage to protect fungal networks in the soil.")
    recommendations.append("Maintain soil moisture at consistent levels to support microbial activity.")
    
    return recommendations