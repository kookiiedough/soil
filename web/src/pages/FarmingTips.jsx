import React, { useState } from 'react'

const FarmingTips = () => {
  const [query, setQuery] = useState('')
  const [isSearching, setIsSearching] = useState(false)
  const [searchResults, setSearchResults] = useState([])
  
  // Sample farming tips data (in a real app, this would come from the RAG system)
  const farmingTipsData = [
    {
      id: 1,
      title: 'Improving Soil Organic Matter',
      category: 'Soil Health',
      content: 'Increasing organic matter in your soil is fundamental to biodynamic farming. Add compost, cover crops, and crop rotations to build soil structure. Aim for at least 5% organic matter content for optimal soil health. Biodynamic preparations 500 (horn manure) and 502-507 (compost preparations) can significantly enhance the decomposition process and improve humus formation.',
      tags: ['organic matter', 'compost', 'soil structure', 'biodynamic preparations']
    },
    {
      id: 2,
      title: 'Managing Soil pH Naturally',
      category: 'Soil Chemistry',
      content: 'Maintain soil pH between 6.0-7.0 for most crops. Use dolomite lime to raise pH in acidic soils, or elemental sulfur to lower pH in alkaline soils. Biodynamic approach considers pH as part of the living system - focus on building soil biology rather than just chemical adjustments. Regular applications of compost and biodynamic preparations help stabilize pH naturally over time.',
      tags: ['pH', 'lime', 'sulfur', 'soil biology']
    },
    {
      id: 3,
      title: 'Biodynamic Planting Calendar',
      category: 'Planting',
      content: 'Follow the biodynamic calendar which aligns planting activities with lunar and cosmic rhythms. Root crops perform best when planted during earth days, leaf crops during water days, flowering plants during air days, and fruiting crops during fire days. This approach recognizes the subtle influences of celestial bodies on plant growth and development.',
      tags: ['planting calendar', 'lunar cycles', 'cosmic rhythms']
    },
    {
      id: 4,
      title: 'Natural Pest Management',
      category: 'Pest Control',
      content: 'Create a balanced ecosystem to manage pests naturally. Interplant aromatic herbs like basil, mint, and marigold to repel insects. Use biodynamic preparation 501 (horn silica) to strengthen plants against fungal diseases. Encourage beneficial insects by maintaining diverse habitats. Spray fermented nettle tea to deter aphids and strengthen plants against stress.',
      tags: ['pest control', 'beneficial insects', 'companion planting', 'preparation 501']
    },
    {
      id: 5,
      title: 'Water Conservation Techniques',
      category: 'Water Management',
      content: 'Implement water conservation practices such as mulching, drip irrigation, and rainwater harvesting. Biodynamic farms focus on building soil organic matter which improves water retention capacity. Apply horn manure preparation (500) before expected rainfall to maximize water absorption and distribution in the soil profile.',
      tags: ['water conservation', 'mulching', 'irrigation', 'water retention']
    },
    {
      id: 6,
      title: 'Biodynamic Composting',
      category: 'Soil Fertility',
      content: 'Create biodynamic compost by layering green materials (nitrogen-rich) with brown materials (carbon-rich) and adding biodynamic compost preparations 502-507. These preparations made from medicinal herbs enhance the composting process and imbue specific qualities to the finished compost. Turn the pile regularly and maintain proper moisture for optimal decomposition.',
      tags: ['compost', 'biodynamic preparations', 'soil fertility', 'organic matter']
    },
    {
      id: 7,
      title: 'Cover Cropping Strategies',
      category: 'Soil Health',
      content: 'Implement strategic cover cropping to improve soil health. Use legumes like clover and vetch to fix nitrogen, deep-rooted plants like daikon radish to break compaction, and grasses to add organic matter. In biodynamic farming, timing cover crop planting and termination with lunar cycles can enhance their effectiveness.',
      tags: ['cover crops', 'nitrogen fixation', 'soil structure', 'green manure']
    },
    {
      id: 8,
      title: 'Microbiome Enhancement',
      category: 'Soil Biology',
      content: 'Foster a diverse soil microbiome by minimizing tillage, avoiding synthetic chemicals, and applying biodynamic preparations. Horn manure preparation (500) specifically stimulates microbial activity. Consider applying small amounts of well-aged compost as microbial inoculants rather than as a primary nutrient source.',
      tags: ['microbiome', 'soil biology', 'microbial diversity', 'preparation 500']
    }
  ]

  // Function to handle search
  const handleSearch = (e) => {
    e.preventDefault()
    if (!query.trim()) return
    
    setIsSearching(true)
    
    // Simulate search delay (in a real app, this would be an API call to the RAG system)
    setTimeout(() => {
      // Simple search implementation (in a real app, this would use the RAG system)
      const results = farmingTipsData.filter(tip => {
        const searchableText = `${tip.title} ${tip.category} ${tip.content} ${tip.tags.join(' ')}`.toLowerCase()
        return searchableText.includes(query.toLowerCase())
      })
      
      setSearchResults(results)
      setIsSearching(false)
    }, 800)
  }

  return (
    <div className="farming-tips-container">
      <h1>Biodynamic Farming Tips</h1>
      <p className="page-subtitle">Discover sustainable farming practices based on your soil conditions</p>
      
      <div className="search-section card">
        <h2>Ask about Biodynamic Farming</h2>
        <p>Enter keywords or questions about biodynamic farming practices, soil health, or crop management</p>
        
        <form onSubmit={handleSearch} className="search-form">
          <div className="search-input-container">
            <input 
              type="text" 
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="e.g., How to improve soil organic matter?"
              className="search-input"
            />
            <button type="submit" className="search-btn" disabled={isSearching}>
              {isSearching ? <i className="fas fa-spinner fa-spin"></i> : <i className="fas fa-search"></i>}
            </button>
          </div>
        </form>
        
        <div className="popular-queries">
          <h3>Popular Topics:</h3>
          <div className="query-tags">
            <span className="query-tag" onClick={() => setQuery('soil health')}>Soil Health</span>
            <span className="query-tag" onClick={() => setQuery('biodynamic preparations')}>Biodynamic Preparations</span>
            <span className="query-tag" onClick={() => setQuery('planting calendar')}>Planting Calendar</span>
            <span className="query-tag" onClick={() => setQuery('pest management')}>Pest Management</span>
            <span className="query-tag" onClick={() => setQuery('composting')}>Composting</span>
          </div>
        </div>
      </div>
      
      <div className="tips-results">
        {isSearching ? (
          <div className="loading-container">
            <div className="loading-spinner"></div>
            <p>Searching for farming tips...</p>
          </div>
        ) : searchResults.length > 0 ? (
          <div className="search-results">
            <h2>Search Results for "{query}"</h2>
            <div className="tips-grid">
              {searchResults.map(tip => (
                <div key={tip.id} className="tip-card card">
                  <div className="tip-category">{tip.category}</div>
                  <h3>{tip.title}</h3>
                  <p className="tip-content">{tip.content}</p>
                  <div className="tip-tags">
                    {tip.tags.map((tag, index) => (
                      <span key={index} className="tip-tag">{tag}</span>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        ) : query ? (
          <div className="no-results card">
            <i className="fas fa-leaf no-results-icon"></i>
            <h3>No tips found for "{query}"</h3>
            <p>Try different keywords or browse our featured tips below</p>
          </div>
        ) : null}
        
        <div className="featured-tips">
          <h2>Featured Farming Tips</h2>
          <div className="tips-grid">
            {farmingTipsData.slice(0, 4).map(tip => (
              <div key={tip.id} className="tip-card card">
                <div className="tip-category">{tip.category}</div>
                <h3>{tip.title}</h3>
                <p className="tip-content">{tip.content}</p>
                <div className="tip-tags">
                  {tip.tags.map((tag, index) => (
                    <span key={index} className="tip-tag">{tag}</span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      
      <div className="tips-resources card">
        <h2>Biodynamic Resources</h2>
        <p>Access these resources offline for more in-depth information about biodynamic farming practices</p>
        
        <div className="resources-grid">
          <div className="resource-item">
            <i className="fas fa-book resource-icon"></i>
            <h3>Biodynamic Planting Calendar</h3>
            <p>Monthly guide for planting based on cosmic rhythms</p>
            <button className="btn btn-secondary">View Calendar</button>
          </div>
          
          <div className="resource-item">
            <i className="fas fa-flask resource-icon"></i>
            <h3>Preparation Guides</h3>
            <p>How to make and apply biodynamic preparations</p>
            <button className="btn btn-secondary">View Guides</button>
          </div>
          
          <div className="resource-item">
            <i className="fas fa-seedling resource-icon"></i>
            <h3>Crop Rotation Plans</h3>
            <p>Sample rotation plans for various farm sizes</p>
            <button className="btn btn-secondary">View Plans</button>
          </div>
          
          <div className="resource-item">
            <i className="fas fa-cloud-rain resource-icon"></i>
            <h3>Water Management</h3>
            <p>Techniques for efficient water use in biodynamic systems</p>
            <button className="btn btn-secondary">View Techniques</button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default FarmingTips