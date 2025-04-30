import React, { useState } from 'react'

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null)
  const [isUploading, setIsUploading] = useState(false)
  const [uploadProgress, setUploadProgress] = useState(0)
  const [processingStatus, setProcessingStatus] = useState(null)
  const [analysisResults, setAnalysisResults] = useState(null)
  
  // Function to handle file selection
  const handleFileSelect = (e) => {
    const file = e.target.files[0]
    if (file && file.name.endsWith('.fastq')) {
      setSelectedFile(file)
      setAnalysisResults(null)
      setProcessingStatus(null)
    } else {
      alert('Please select a valid FASTQ file')
    }
  }
  
  // Function to handle file upload and processing
  const handleUpload = (e) => {
    e.preventDefault()
    if (!selectedFile) return
    
    setIsUploading(true)
    setUploadProgress(0)
    
    // Simulate upload progress (in a real app, this would be an actual file upload)
    const uploadInterval = setInterval(() => {
      setUploadProgress(prev => {
        if (prev >= 100) {
          clearInterval(uploadInterval)
          return 100
        }
        return prev + 5
      })
    }, 200)
    
    // Simulate file processing after upload completes
    setTimeout(() => {
      clearInterval(uploadInterval)
      setUploadProgress(100)
      setIsUploading(false)
      
      // Start processing
      setProcessingStatus('processing')
      
      // Simulate processing time (in a real app, this would be actual FASTQ processing)
      setTimeout(() => {
        setProcessingStatus('completed')
        
        // Generate mock analysis results (in a real app, this would come from the ML model)
        setAnalysisResults({
          sampleId: `SAMPLE-${Math.floor(Math.random() * 10000)}`,
          timestamp: new Date().toISOString(),
          fileName: selectedFile.name,
          fileSize: selectedFile.size,
          microbiomeComposition: {
            bacteria: {
              beneficial: 68,
              neutral: 27,
              harmful: 5
            },
            fungi: {
              beneficial: 72,
              neutral: 23,
              harmful: 5
            }
          },
          soilHealthScore: Math.floor(65 + Math.random() * 20),
          dominantSpecies: [
            'Bacillus subtilis',
            'Pseudomonas fluorescens',
            'Trichoderma harzianum',
            'Rhizobium leguminosarum',
            'Azotobacter vinelandii'
          ],
          nutrientCycling: {
            nitrogen: 'High',
            phosphorus: 'Medium',
            potassium: 'Medium'
          },
          recommendations: [
            'Your soil shows good microbial diversity with strong presence of beneficial bacteria',
            'Consider adding compost to further enhance fungal diversity',
            'Nitrogen cycling capacity is high, indicating good fertility potential',
            'Reduce tillage to protect fungal networks in the soil'
          ]
        })
      }, 3000)
    }, 4000)
  }
  
  // Function to reset the form
  const handleReset = () => {
    setSelectedFile(null)
    setIsUploading(false)
    setUploadProgress(0)
    setProcessingStatus(null)
    setAnalysisResults(null)
  }
  
  return (
    <div className="file-upload-container">
      <h1>FASTQ File Analysis</h1>
      <p className="page-subtitle">Upload soil microbiome sequencing data for analysis</p>
      
      <div className="upload-content">
        <div className="upload-section card">
          <h2>Upload FASTQ File</h2>
          <p>Select a FASTQ file containing soil microbiome sequencing data for analysis</p>
          
          <form onSubmit={handleUpload} className="upload-form">
            <div className="file-input-container">
              <input 
                type="file" 
                id="fastq-file" 
                accept=".fastq"
                onChange={handleFileSelect}
                className="file-input"
              />
              <label htmlFor="fastq-file" className="file-label">
                <i className="fas fa-upload"></i>
                <span>{selectedFile ? selectedFile.name : 'Choose FASTQ File'}</span>
              </label>
              {selectedFile && (
                <div className="file-info">
                  <p>File Size: {(selectedFile.size / (1024 * 1024)).toFixed(2)} MB</p>
                </div>
              )}
            </div>
            
            <div className="upload-actions">
              <button 
                type="submit" 
                className="btn" 
                disabled={!selectedFile || isUploading || processingStatus}
              >
                {isUploading ? 'Uploading...' : 'Upload and Analyze'}
              </button>
              <button 
                type="button" 
                className="btn btn-secondary" 
                onClick={handleReset}
                disabled={isUploading}
              >
                Reset
              </button>
            </div>
          </form>
          
          {isUploading && (
            <div className="upload-progress">
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{width: `${uploadProgress}%`}}
                ></div>
              </div>
              <p className="progress-text">{uploadProgress}% Uploaded</p>
            </div>
          )}
          
          {processingStatus === 'processing' && (
            <div className="processing-status">
              <div className="processing-spinner"></div>
              <p>Processing FASTQ data...</p>
              <p className="processing-note">This may take a few minutes depending on file size</p>
            </div>
          )}
        </div>
        
        {analysisResults && (
          <div className="analysis-results card">
            <div className="results-header">
              <h2>Analysis Results</h2>
              <span className="sample-id">Sample ID: {analysisResults.sampleId}</span>
            </div>
            
            <div className="results-summary">
              <div className="health-score">
                <div className="score-circle">
                  <span className="score-value">{analysisResults.soilHealthScore}</span>
                </div>
                <span className="score-label">Soil Health Score</span>
              </div>
              
              <div className="summary-text">
                <p>Your soil sample shows a health score of <strong>{analysisResults.soilHealthScore}</strong>, indicating 
                {analysisResults.soilHealthScore >= 80 ? ' excellent' : 
                  analysisResults.soilHealthScore >= 70 ? ' good' : 
                  analysisResults.soilHealthScore >= 60 ? ' moderate' : ' poor'} microbiome health.</p>
                <p>The analysis identified <strong>{analysisResults.dominantSpecies.length}</strong> dominant beneficial microorganisms 
                that contribute to soil fertility and plant health.</p>
              </div>
            </div>
            
            <div className="microbiome-composition">
              <h3>Microbiome Composition</h3>
              <div className="composition-charts">
                <div className="chart-container">
                  <h4>Bacterial Composition</h4>
                  <div className="pie-chart bacteria-chart">
                    <div className="pie-segment beneficial" style={{transform: `rotate(0deg) skew(${90 - (analysisResults.microbiomeComposition.bacteria.beneficial * 3.6)}deg)`}}></div>
                    <div className="pie-segment neutral" style={{transform: `rotate(${analysisResults.microbiomeComposition.bacteria.beneficial * 3.6}deg) skew(${90 - (analysisResults.microbiomeComposition.bacteria.neutral * 3.6)}deg)`}}></div>
                    <div className="pie-segment harmful" style={{transform: `rotate(${(analysisResults.microbiomeComposition.bacteria.beneficial + analysisResults.microbiomeComposition.bacteria.neutral) * 3.6}deg) skew(${90 - (analysisResults.microbiomeComposition.bacteria.harmful * 3.6)}deg)`}}></div>
                  </div>
                  <div className="chart-legend">
                    <div className="legend-item">
                      <span className="legend-color beneficial"></span>
                      <span>Beneficial: {analysisResults.microbiomeComposition.bacteria.beneficial}%</span>
                    </div>
                    <div className="legend-item">
                      <span className="legend-color neutral"></span>
                      <span>Neutral: {analysisResults.microbiomeComposition.bacteria.neutral}%</span>
                    </div>
                    <div className="legend-item">
                      <span className="legend-color harmful"></span>
                      <span>Harmful: {analysisResults.microbiomeComposition.bacteria.harmful}%</span>
                    </div>
                  </div>
                </div>
                
                <div className="chart-container">
                  <h4>Fungal Composition</h4>
                  <div className="pie-chart fungi-chart">
                    <div className="pie-segment beneficial" style={{transform: `rotate(0deg) skew(${90 - (analysisResults.microbiomeComposition.fungi.beneficial * 3.6)}deg)`}}></div>
                    <div className="pie-segment neutral" style={{transform: `rotate(${analysisResults.microbiomeComposition.fungi.beneficial * 3.6}deg) skew(${90 - (analysisResults.microbiomeComposition.fungi.neutral * 3.6)}deg)`}}></div>
                    <div className="pie-segment harmful" style={{transform: `rotate(${(analysisResults.microbiomeComposition.fungi.beneficial + analysisResults.microbiomeComposition.fungi.neutral) * 3.6}deg) skew(${90 - (analysisResults.microbiomeComposition.fungi.harmful * 3.6)}deg)`}}></div>
                  </div>
                  <div className="chart-legend">
                    <div className="legend-item">
                      <span className="legend-color beneficial"></span>
                      <span>Beneficial: {analysisResults.microbiomeComposition.fungi.beneficial}%</span>
                    </div>
                    <div className="legend-item">
                      <span className="legend-color neutral"></span>
                      <span>Neutral: {analysisResults.microbiomeComposition.fungi.neutral}%</span>
                    </div>
                    <div className="legend-item">
                      <span className="legend-color harmful"></span>
                      <span>Harmful: {analysisResults.microbiomeComposition.fungi.harmful}%</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="dominant-species">
              <h3>Dominant Beneficial Species</h3>
              <ul className="species-list">
                {analysisResults.dominantSpecies.map((species, index) => (
                  <li key={index} className="species-item">{species}</li>
                ))}
              </ul>
            </div>
            
            <div className="nutrient-cycling">
              <h3>Nutrient Cycling Capacity</h3>
              <div className="nutrient-grid">
                <div className="nutrient-item">
                  <span className="nutrient-name">Nitrogen</span>
                  <span className={`nutrient-value ${analysisResults.nutrientCycling.nitrogen.toLowerCase()}`}>
                    {analysisResults.nutrientCycling.nitrogen}
                  </span>
                </div>
                <div className="nutrient-item">
                  <span className="nutrient-name">Phosphorus</span>
                  <span className={`nutrient-value ${analysisResults.nutrientCycling.phosphorus.toLowerCase()}`}>
                    {analysisResults.nutrientCycling.phosphorus}
                  </span>
                </div>
                <div className="nutrient-item">
                  <span className="nutrient-name">Potassium</span>
                  <span className={`nutrient-value ${analysisResults.nutrientCycling.potassium.toLowerCase()}`}>
                    {analysisResults.nutrientCycling.potassium}
                  </span>
                </div>
              </div>
            </div>
            
            <div className="recommendations">
              <h3>Recommendations</h3>
              <ul className="recommendations-list">
                {analysisResults.recommendations.map((recommendation, index) => (
                  <li key={index} className="recommendation-item">{recommendation}</li>
                ))}
              </ul>
            </div>
            
            <div className="results-actions">
              <button className="btn">Download Full Report</button>
              <button className="btn btn-secondary">Save to History</button>
            </div>
          </div>
        )}
      </div>
      
      <div className="upload-info card">
        <h2>About FASTQ Analysis</h2>
        <p>Our system uses advanced machine learning algorithms to analyze soil microbiome data from FASTQ files. The analysis provides insights into:</p>
        
        <ul className="info-list">
          <li>Microbial diversity and composition</li>
          <li>Presence of beneficial and harmful organisms</li>
          <li>Nutrient cycling capacity</li>
          <li>Overall soil health score</li>
          <li>Personalized recommendations for biodynamic farming practices</li>
        </ul>
        
        <div className="info-note">
          <i className="fas fa-info-circle"></i>
          <p>All processing is done locally on your device. No data is sent to external servers, ensuring your data remains private and accessible even without an internet connection.</p>
        </div>
      </div>
    </div>
  )
}

export default FileUpload