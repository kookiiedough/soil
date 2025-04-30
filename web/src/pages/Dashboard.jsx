import React from 'react'

const Dashboard = () => {
  // Sample data for dashboard metrics
  const soilHealthMetrics = {
    organicMatter: 4.2,
    pH: 6.8,
    nitrogen: 'Medium',
    phosphorus: 'High',
    potassium: 'Medium',
    microbiomeHealth: 78
  }

  const recentAnalyses = [
    { id: 1, date: '2023-10-15', type: 'Soil Sample', status: 'Completed', score: 82 },
    { id: 2, date: '2023-09-28', type: 'FASTQ Analysis', status: 'Completed', score: 75 },
    { id: 3, date: '2023-08-12', type: 'Soil Sample', status: 'Completed', score: 68 }
  ]

  return (
    <div className="dashboard-container">
      <h1>Biodynamic Farming Dashboard</h1>
      <p className="dashboard-subtitle">Your offline soil health monitoring system</p>
      
      <div className="dashboard-grid">
        {/* Soil Health Overview Card */}
        <div className="card soil-health-card">
          <h2>Soil Health Overview</h2>
          <div className="health-meter">
            <div className="meter-circle">
              <span className="meter-value">{soilHealthMetrics.microbiomeHealth}%</span>
            </div>
            <span className="meter-label">Overall Health</span>
          </div>
          <div className="metrics-grid">
            <div className="metric-item">
              <span className="metric-label">Organic Matter</span>
              <span className="metric-value">{soilHealthMetrics.organicMatter}%</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">pH Level</span>
              <span className="metric-value">{soilHealthMetrics.pH}</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">Nitrogen</span>
              <span className="metric-value">{soilHealthMetrics.nitrogen}</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">Phosphorus</span>
              <span className="metric-value">{soilHealthMetrics.phosphorus}</span>
            </div>
            <div className="metric-item">
              <span className="metric-label">Potassium</span>
              <span className="metric-value">{soilHealthMetrics.potassium}</span>
            </div>
          </div>
        </div>

        {/* Recent Analyses Card */}
        <div className="card recent-analyses-card">
          <h2>Recent Analyses</h2>
          <div className="analyses-list">
            {recentAnalyses.map(analysis => (
              <div key={analysis.id} className="analysis-item">
                <div className="analysis-header">
                  <span className="analysis-date">{analysis.date}</span>
                  <span className={`analysis-status status-${analysis.status.toLowerCase()}`}>
                    {analysis.status}
                  </span>
                </div>
                <div className="analysis-details">
                  <span className="analysis-type">{analysis.type}</span>
                  <span className="analysis-score">Score: {analysis.score}</span>
                </div>
              </div>
            ))}
          </div>
          <button className="btn view-all-btn">View All Analyses</button>
        </div>

        {/* Quick Actions Card */}
        <div className="card quick-actions-card">
          <h2>Quick Actions</h2>
          <div className="actions-grid">
            <button className="action-btn">
              <i className="fas fa-upload"></i>
              <span>Upload FASTQ</span>
            </button>
            <button className="action-btn">
              <i className="fas fa-flask"></i>
              <span>New Soil Analysis</span>
            </button>
            <button className="action-btn">
              <i className="fas fa-leaf"></i>
              <span>Get Farming Tips</span>
            </button>
            <button className="action-btn">
              <i className="fas fa-download"></i>
              <span>Export Data</span>
            </button>
          </div>
        </div>

        {/* Farming Tips Preview */}
        <div className="card farming-tips-card">
          <h2>Farming Tips</h2>
          <div className="tip-preview">
            <h3>Seasonal Recommendation</h3>
            <p>Based on your soil analysis, consider adding compost to increase organic matter content before the planting season.</p>
          </div>
          <button className="btn secondary-btn">View More Tips</button>
        </div>
      </div>
    </div>
  )
}

export default Dashboard