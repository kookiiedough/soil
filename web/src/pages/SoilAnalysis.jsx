import React, { useState } from 'react'

const SoilAnalysis = () => {
  const [selectedSample, setSelectedSample] = useState(null)
  
  // Sample data for soil analysis
  const soilSamples = [
    {
      id: 1,
      name: 'North Field',
      date: '2023-10-15',
      metrics: {
        organicMatter: 4.2,
        pH: 6.8,
        nitrogen: 42,
        phosphorus: 65,
        potassium: 48,
        calcium: 1250,
        magnesium: 180,
        sulfur: 15,
        zinc: 3.2,
        manganese: 12,
        copper: 1.8,
        boron: 0.8,
        microbiomeHealth: 78
      }
    },
    {
      id: 2,
      name: 'South Field',
      date: '2023-09-28',
      metrics: {
        organicMatter: 3.8,
        pH: 7.2,
        nitrogen: 38,
        phosphorus: 52,
        potassium: 55,
        calcium: 1400,
        magnesium: 210,
        sulfur: 12,
        zinc: 2.8,
        manganese: 10,
        copper: 1.5,
        boron: 0.6,
        microbiomeHealth: 72
      }
    },
    {
      id: 3,
      name: 'East Garden',
      date: '2023-08-12',
      metrics: {
        organicMatter: 5.1,
        pH: 6.5,
        nitrogen: 48,
        phosphorus: 58,
        potassium: 42,
        calcium: 1100,
        magnesium: 160,
        sulfur: 18,
        zinc: 3.5,
        manganese: 14,
        copper: 2.0,
        boron: 0.9,
        microbiomeHealth: 85
      }
    }
  ]

  // Function to handle sample selection
  const handleSampleSelect = (sample) => {
    setSelectedSample(sample)
  }

  // Function to get health status based on value
  const getHealthStatus = (value) => {
    if (value >= 75) return 'Excellent'
    if (value >= 60) return 'Good'
    if (value >= 40) return 'Fair'
    return 'Poor'
  }

  // Function to get color class based on value
  const getColorClass = (value) => {
    if (value >= 75) return 'excellent'
    if (value >= 60) return 'good'
    if (value >= 40) return 'fair'
    return 'poor'
  }

  return (
    <div className="soil-analysis-container">
      <h1>Soil Health Analysis</h1>
      <p className="page-subtitle">View and analyze your soil samples</p>
      
      <div className="analysis-content">
        <div className="samples-list card">
          <h2>Your Soil Samples</h2>
          <div className="samples-grid">
            {soilSamples.map(sample => (
              <div 
                key={sample.id} 
                className={`sample-card ${selectedSample?.id === sample.id ? 'selected' : ''}`}
                onClick={() => handleSampleSelect(sample)}
              >
                <h3>{sample.name}</h3>
                <p className="sample-date">Analyzed: {sample.date}</p>
                <div className="sample-preview">
                  <div className="health-indicator">
                    <div 
                      className={`indicator-circle ${getColorClass(sample.metrics.microbiomeHealth)}`}
                    >
                      {sample.metrics.microbiomeHealth}%
                    </div>
                  </div>
                  <div className="preview-metrics">
                    <div className="preview-metric">
                      <span>pH:</span> {sample.metrics.pH}
                    </div>
                    <div className="preview-metric">
                      <span>Organic:</span> {sample.metrics.organicMatter}%
                    </div>
                  </div>
                </div>
                <button className="btn">View Details</button>
              </div>
            ))}
            <div className="sample-card add-new">
              <div className="add-icon">
                <i className="fas fa-plus"></i>
              </div>
              <h3>Add New Sample</h3>
              <p>Upload a new soil analysis</p>
              <button className="btn btn-secondary">Upload</button>
            </div>
          </div>
        </div>

        {selectedSample ? (
          <div className="analysis-details card">
            <h2>{selectedSample.name} - Detailed Analysis</h2>
            <p className="analysis-date">Sample analyzed on {selectedSample.date}</p>
            
            <div className="health-overview">
              <div className="health-meter">
                <div className={`meter-circle ${getColorClass(selectedSample.metrics.microbiomeHealth)}`}>
                  <span className="meter-value">{selectedSample.metrics.microbiomeHealth}%</span>
                </div>
                <span className="meter-label">Overall Soil Health</span>
                <span className={`health-status ${getColorClass(selectedSample.metrics.microbiomeHealth)}`}>
                  {getHealthStatus(selectedSample.metrics.microbiomeHealth)}
                </span>
              </div>
              
              <div className="health-summary">
                <p>This soil sample shows {getHealthStatus(selectedSample.metrics.microbiomeHealth).toLowerCase()} overall health with 
                {selectedSample.metrics.organicMatter}% organic matter content. The pH level of {selectedSample.metrics.pH} is 
                {selectedSample.metrics.pH < 6.5 ? 'slightly acidic' : selectedSample.metrics.pH > 7.5 ? 'slightly alkaline' : 'neutral'}.</p>
                
                <p>Based on this analysis, this soil is suitable for most {selectedSample.metrics.pH < 6.5 ? 'acid-loving plants like blueberries and potatoes' : 
                selectedSample.metrics.pH > 7.5 ? 'alkaline-tolerant plants like asparagus and beets' : 'common garden vegetables and flowers'}.</p>
              </div>
            </div>
            
            <div className="metrics-detail">
              <h3>Detailed Metrics</h3>
              <div className="metrics-grid">
                <div className="metric-group">
                  <h4>Primary Nutrients</h4>
                  <div className="metric-item">
                    <span className="metric-label">Nitrogen (N)</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${selectedSample.metrics.nitrogen}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.nitrogen} ppm</span>
                    </div>
                  </div>
                  <div className="metric-item">
                    <span className="metric-label">Phosphorus (P)</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${selectedSample.metrics.phosphorus}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.phosphorus} ppm</span>
                    </div>
                  </div>
                  <div className="metric-item">
                    <span className="metric-label">Potassium (K)</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${selectedSample.metrics.potassium}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.potassium} ppm</span>
                    </div>
                  </div>
                </div>
                
                <div className="metric-group">
                  <h4>Secondary Nutrients</h4>
                  <div className="metric-item">
                    <span className="metric-label">Calcium (Ca)</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${(selectedSample.metrics.calcium/2000)*100}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.calcium} ppm</span>
                    </div>
                  </div>
                  <div className="metric-item">
                    <span className="metric-label">Magnesium (Mg)</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${(selectedSample.metrics.magnesium/300)*100}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.magnesium} ppm</span>
                    </div>
                  </div>
                  <div className="metric-item">
                    <span className="metric-label">Sulfur (S)</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${(selectedSample.metrics.sulfur/20)*100}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.sulfur} ppm</span>
                    </div>
                  </div>
                </div>
                
                <div className="metric-group">
                  <h4>Micronutrients</h4>
                  <div className="metric-item">
                    <span className="metric-label">Zinc (Zn)</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${(selectedSample.metrics.zinc/5)*100}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.zinc} ppm</span>
                    </div>
                  </div>
                  <div className="metric-item">
                    <span className="metric-label">Manganese (Mn)</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${(selectedSample.metrics.manganese/20)*100}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.manganese} ppm</span>
                    </div>
                  </div>
                  <div className="metric-item">
                    <span className="metric-label">Copper (Cu)</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${(selectedSample.metrics.copper/3)*100}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.copper} ppm</span>
                    </div>
                  </div>
                  <div className="metric-item">
                    <span className="metric-label">Boron (B)</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${(selectedSample.metrics.boron/1.5)*100}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.boron} ppm</span>
                    </div>
                  </div>
                </div>
                
                <div className="metric-group">
                  <h4>Physical Properties</h4>
                  <div className="metric-item">
                    <span className="metric-label">Organic Matter</span>
                    <div className="metric-bar-container">
                      <div className="metric-bar" style={{width: `${(selectedSample.metrics.organicMatter/10)*100}%`}}></div>
                      <span className="metric-value">{selectedSample.metrics.organicMatter}%</span>
                    </div>
                  </div>
                  <div className="metric-item">
                    <span className="metric-label">pH Level</span>
                    <div className="ph-scale">
                      <div className="ph-marker" style={{left: `${((selectedSample.metrics.pH-4)/10)*100}%`}}></div>
                      <div className="ph-labels">
                        <span>4.0</span>
                        <span>5.5</span>
                        <span>7.0</span>
                        <span>8.5</span>
                        <span>10.0</span>
                      </div>
                    </div>
                    <span className="metric-value">{selectedSample.metrics.pH}</span>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="recommendations">
              <h3>Recommendations</h3>
              <ul className="recommendations-list">
                {selectedSample.metrics.organicMatter < 4 && (
                  <li>Increase organic matter by adding compost or cover crops</li>
                )}
                {selectedSample.metrics.pH < 6.0 && (
                  <li>Apply lime to raise soil pH to a more neutral level</li>
                )}
                {selectedSample.metrics.pH > 7.5 && (
                  <li>Add sulfur or acidic organic matter to lower soil pH</li>
                )}
                {selectedSample.metrics.nitrogen < 40 && (
                  <li>Apply nitrogen-rich amendments like blood meal or fish emulsion</li>
                )}
                {selectedSample.metrics.phosphorus < 50 && (
                  <li>Increase phosphorus with bone meal or rock phosphate</li>
                )}
                {selectedSample.metrics.potassium < 45 && (
                  <li>Add potassium with wood ash or greensand</li>
                )}
                <li>Maintain soil moisture at consistent levels to support microbial activity</li>
                <li>Minimize soil disturbance to protect soil structure and biology</li>
              </ul>
            </div>
            
            <div className="analysis-actions">
              <button className="btn">Download Report</button>
              <button className="btn btn-secondary">Compare Samples</button>
            </div>
          </div>
        ) : (
          <div className="analysis-placeholder card">
            <div className="placeholder-content">
              <i className="fas fa-flask placeholder-icon"></i>
              <h3>Select a Sample</h3>
              <p>Choose a soil sample from the list to view detailed analysis</p>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default SoilAnalysis