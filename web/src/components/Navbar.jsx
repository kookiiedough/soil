import React, { useState } from 'react'
import { Link } from 'react-router-dom'

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <span className="logo-text">BioDynamic Farming</span>
          <span className="offline-badge">Offline</span>
        </Link>

        <div className="menu-icon" onClick={() => setIsMenuOpen(!isMenuOpen)}>
          <i className={isMenuOpen ? 'fas fa-times' : 'fas fa-bars'} />
        </div>

        <ul className={isMenuOpen ? 'nav-menu active' : 'nav-menu'}>
          <li className="nav-item">
            <Link to="/" className="nav-link" onClick={() => setIsMenuOpen(false)}>
              Dashboard
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/soil-analysis" className="nav-link" onClick={() => setIsMenuOpen(false)}>
              Soil Analysis
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/farming-tips" className="nav-link" onClick={() => setIsMenuOpen(false)}>
              Farming Tips
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/file-upload" className="nav-link" onClick={() => setIsMenuOpen(false)}>
              Upload FASTQ
            </Link>
          </li>
        </ul>

        <div className="navbar-actions">
          <Link to="/settings" className="settings-link">
            <i className="fas fa-cog" />
          </Link>
        </div>
      </div>
    </nav>
  )
}

export default Navbar