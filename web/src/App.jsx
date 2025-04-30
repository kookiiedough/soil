import React from 'react'
import { Routes, Route } from 'react-router-dom'
import './App.css'

// Components
import Navbar from './components/Navbar'
import Sidebar from './components/Sidebar'

// Pages
import Dashboard from './pages/Dashboard'
import SoilAnalysis from './pages/SoilAnalysis'
import FarmingTips from './pages/FarmingTips'
import FileUpload from './pages/FileUpload'
import Settings from './pages/Settings'

function App() {
  return (
    <div className="app-container">
      <Navbar />
      <div className="main-content">
        <Sidebar />
        <div className="content-area">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/soil-analysis" element={<SoilAnalysis />} />
            <Route path="/farming-tips" element={<FarmingTips />} />
            <Route path="/file-upload" element={<FileUpload />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </div>
      </div>
    </div>
  )
}

export default App