import React, { useState } from 'react'

const Settings = () => {
  const [settings, setSettings] = useState({
    darkMode: false,
    notifications: true,
    dataStorage: 'local',
    autoAnalysis: true,
    units: 'metric',
    language: 'english'
  })

  const [storageInfo, setStorageInfo] = useState({
    totalSpace: 5000, // MB
    usedSpace: 1250,  // MB
    samples: 12,
    reports: 8
  })

  // Function to handle settings changes
  const handleSettingChange = (setting, value) => {
    setSettings(prev => ({
      ...prev,
      [setting]: value
    }))
  }

  // Function to handle form submission
  const handleSubmit = (e) => {
    e.preventDefault()
    // In a real app, this would save settings to local storage or IndexedDB
    alert('Settings saved successfully!')
  }

  // Function to handle data export
  const handleExportData = () => {
    // In a real app, this would export all user data
    alert('Exporting data...')
  }

  // Function to handle data clearing
  const handleClearData = () => {
    if (window.confirm('Are you sure you want to clear all data? This action cannot be undone.')) {
      // In a real app, this would clear all user data
      setStorageInfo({
        totalSpace: 5000,
        usedSpace: 0,
        samples: 0,
        reports: 0
      })
      alert('All data has been cleared')
    }
  }

  return (
    <div className="settings-container">
      <h1>Settings</h1>
      <p className="page-subtitle">Configure your BioDynamic Farming application</p>
      
      <div className="settings-content">
        <div className="settings-section card">
          <h2>Application Settings</h2>
          
          <form onSubmit={handleSubmit} className="settings-form">
            <div className="settings-group">
              <h3>Interface</h3>
              
              <div className="setting-item">
                <label htmlFor="darkMode" className="toggle-label">
                  Dark Mode
                  <div className="toggle-description">Enable dark color scheme</div>
                </label>
                <div className="toggle-switch">
                  <input
                    type="checkbox"
                    id="darkMode"
                    checked={settings.darkMode}
                    onChange={(e) => handleSettingChange('darkMode', e.target.checked)}
                  />
                  <span className="toggle-slider"></span>
                </div>
              </div>
              
              <div className="setting-item">
                <label htmlFor="language">Language</label>
                <select 
                  id="language" 
                  value={settings.language}
                  onChange={(e) => handleSettingChange('language', e.target.value)}
                >
                  <option value="english">English</option>
                  <option value="spanish">Spanish</option>
                  <option value="french">French</option>
                  <option value="german">German</option>
                </select>
              </div>
              
              <div className="setting-item">
                <label htmlFor="units">Measurement Units</label>
                <select 
                  id="units" 
                  value={settings.units}
                  onChange={(e) => handleSettingChange('units', e.target.value)}
                >
                  <option value="metric">Metric (cm, kg, °C)</option>
                  <option value="imperial">Imperial (in, lb, °F)</option>
                </select>
              </div>
            </div>
            
            <div className="settings-group">
              <h3>Data & Analysis</h3>
              
              <div className="setting-item">
                <label htmlFor="dataStorage">Data Storage Location</label>
                <select 
                  id="dataStorage" 
                  value={settings.dataStorage}
                  onChange={(e) => handleSettingChange('dataStorage', e.target.value)}
                >
                  <option value="local">Local Storage Only</option>
                  <option value="device" disabled>External Device (Coming Soon)</option>
                </select>
              </div>
              
              <div className="setting-item">
                <label htmlFor="autoAnalysis" className="toggle-label">
                  Automatic Analysis
                  <div className="toggle-description">Automatically analyze FASTQ files after upload</div>
                </label>
                <div className="toggle-switch">
                  <input
                    type="checkbox"
                    id="autoAnalysis"
                    checked={settings.autoAnalysis}
                    onChange={(e) => handleSettingChange('autoAnalysis', e.target.checked)}
                  />
                  <span className="toggle-slider"></span>
                </div>
              </div>
              
              <div className="setting-item">
                <label htmlFor="notifications" className="toggle-label">
                  Notifications
                  <div className="toggle-description">Show notifications for completed analyses</div>
                </label>
                <div className="toggle-switch">
                  <input
                    type="checkbox"
                    id="notifications"
                    checked={settings.notifications}
                    onChange={(e) => handleSettingChange('notifications', e.target.checked)}
                  />
                  <span className="toggle-slider"></span>
                </div>
              </div>
            </div>
            
            <div className="settings-actions">
              <button type="submit" className="btn">Save Settings</button>
              <button type="reset" className="btn btn-secondary">Reset to Default</button>
            </div>
          </form>
        </div>
        
        <div className="storage-section card">
          <h2>Storage Management</h2>
          
          <div className="storage-info">
            <div className="storage-meter">
              <div className="storage-bar">
                <div 
                  className="storage-used" 
                  style={{width: `${(storageInfo.usedSpace / storageInfo.totalSpace) * 100}%`}}
                ></div>
              </div>
              <div className="storage-text">
                <span>{(storageInfo.usedSpace / 1000).toFixed(1)} GB used</span>
                <span>of {(storageInfo.totalSpace / 1000).toFixed(1)} GB</span>
              </div>
            </div>
            
            <div className="storage-details">
              <div className="storage-item">
                <span className="storage-label">Soil Samples</span>
                <span className="storage-value">{storageInfo.samples}</span>
              </div>
              <div className="storage-item">
                <span className="storage-label">Analysis Reports</span>
                <span className="storage-value">{storageInfo.reports}</span>
              </div>
            </div>
          </div>
          
          <div className="data-management">
            <h3>Data Management</h3>
            <p>Export or clear your data stored in this application</p>
            
            <div className="data-actions">
              <button className="btn" onClick={handleExportData}>
                <i className="fas fa-download"></i> Export All Data
              </button>
              <button className="btn btn-danger" onClick={handleClearData}>
                <i className="fas fa-trash"></i> Clear All Data
              </button>
            </div>
            
            <div className="data-note">
              <i className="fas fa-info-circle"></i>
              <p>All data is stored locally on your device. Clearing data will remove all soil samples, analysis results, and custom settings.</p>
            </div>
          </div>
        </div>
        
        <div className="about-section card">
          <h2>About</h2>
          
          <div className="about-content">
            <div className="app-info">
              <h3>BioDynamic Farming</h3>
              <p className="version">Version 1.0.0</p>
              <p className="description">An offline-first application for biodynamic farming soil analysis and recommendations</p>
            </div>
            
            <div className="features-list">
              <h3>Features</h3>
              <ul>
                <li>FASTQ file analysis for soil microbiome assessment</li>
                <li>Soil health monitoring and recommendations</li>
                <li>Biodynamic farming tips and resources</li>
                <li>Completely offline functionality</li>
                <li>Local data storage and management</li>
              </ul>
            </div>
            
            <div className="credits">
              <h3>Credits</h3>
              <p>Developed by BioDynamic Farming Team</p>
              <p>Powered by open-source technologies</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Settings