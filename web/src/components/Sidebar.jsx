import React from 'react'
import { NavLink } from 'react-router-dom'

const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h3>BioDynamic Farming</h3>
      </div>
      <div className="sidebar-menu">
        <NavLink to="/" className={({ isActive }) => isActive ? 'sidebar-item active' : 'sidebar-item'}>
          <i className="fas fa-home"></i>
          <span>Dashboard</span>
        </NavLink>
        <NavLink to="/soil-analysis" className={({ isActive }) => isActive ? 'sidebar-item active' : 'sidebar-item'}>
          <i className="fas fa-flask"></i>
          <span>Soil Analysis</span>
        </NavLink>
        <NavLink to="/farming-tips" className={({ isActive }) => isActive ? 'sidebar-item active' : 'sidebar-item'}>
          <i className="fas fa-leaf"></i>
          <span>Farming Tips</span>
        </NavLink>
        <NavLink to="/file-upload" className={({ isActive }) => isActive ? 'sidebar-item active' : 'sidebar-item'}>
          <i className="fas fa-upload"></i>
          <span>Upload FASTQ</span>
        </NavLink>
        <NavLink to="/settings" className={({ isActive }) => isActive ? 'sidebar-item active' : 'sidebar-item'}>
          <i className="fas fa-cog"></i>
          <span>Settings</span>
        </NavLink>
      </div>
      <div className="sidebar-footer">
        <div className="offline-status">
          <span className="status-indicator"></span>
          <span>Offline Mode</span>
        </div>
      </div>
    </div>
  )
}

export default Sidebar