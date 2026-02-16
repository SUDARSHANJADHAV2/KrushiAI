document.addEventListener("DOMContentLoaded", function () {
  // Mobile menu toggle
  const menuBtn = document.querySelector('#menu-btn');
  const navbar = document.querySelector('.navbar');
  
  if (menuBtn) {
    menuBtn.addEventListener('click', () => {
      navbar.classList.toggle('active');
      menuBtn.classList.toggle('fa-times');
    });
  }
  
  // Scroll to top button functionality
  const scrollTopBtn = document.querySelector('.scroll-top');
  
  if (scrollTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        scrollTopBtn.classList.add('active');
      } else {
        scrollTopBtn.classList.remove('active');
      }
    });
    
    scrollTopBtn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
  
  // Smooth scroll for all navigation links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      if (this.getAttribute('href') !== '#') {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
          // Close mobile menu if open
          if (navbar && navbar.classList.contains('active')) {
            navbar.classList.remove('active');
            if (menuBtn) menuBtn.classList.remove('fa-times');
          }
          
          window.scrollTo({
            top: targetElement.offsetTop - 80,
            behavior: 'smooth'
          });
        }
      }
    });
  });
  
  // Table search functionality
  const searchInput = document.querySelector('.search-input');
  if (searchInput) {
    searchInput.addEventListener('keyup', function() {
      const searchTerm = this.value.toLowerCase();
      const tableRows = document.querySelectorAll('.crops-table tbody tr');
      
      tableRows.forEach(row => {
        const text = row.textContent.toLowerCase();
        if (text.includes(searchTerm)) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    });
  }
  
  // Enhanced crop selection and display functionality
  const cropSelect = document.querySelector('#crop-select');
  const cropInfo = document.querySelector('#cropInfo');
  
  // Populate the crops table with data
  function populateCropTable() {
    const tableBody = document.querySelector('#crop-table tbody');
    if (tableBody) {
      tableBody.innerHTML = '';
      
      cropData.forEach(crop => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td><strong>${crop.name}</strong></td>
          <td>${crop.nitrogen}</td>
          <td>${crop.phosphorus}</td>
          <td>${crop.potassium}</td>
          <td>${crop.temperature}</td>
          <td>${crop.humidity}</td>
          <td>${crop.pH}</td>
          <td>${crop.rainfall}</td>
        `;
        tableBody.appendChild(row);
      });
    }
  }
  
  // Crop data with optimal conditions
  const cropData = [
    {
      name: "Apple",
      nitrogen: "20.80",
      phosphorus: "134.22",
      potassium: "199.89",
      temperature: "22.63",
      humidity: "92.33",
      pH: "5.93",
      rainfall: "112.65",
      description: "Apples are one of the most widely cultivated tree fruits. They require well-drained soil with moderate fertility and benefit from regular pruning to maintain productivity.",
      tips: "Ensure proper spacing between trees, implement a regular pruning schedule, and monitor for common pests like apple maggots and codling moths."
    },
    {
      name: "Banana",
      nitrogen: "100.23",
      phosphorus: "82.01",
      potassium: "50.05",
      temperature: "27.38",
      humidity: "80.36",
      pH: "5.98",
      rainfall: "104.63",
      description: "Bananas are tropical fruits that grow on large herbaceous plants. They require consistent moisture and warm temperatures to thrive.",
      tips: "Protect plants from strong winds, ensure adequate drainage, and apply mulch to retain soil moisture and suppress weeds."
    },
    {
      name: "Blackgram",
      nitrogen: "40.02",
      phosphorus: "67.47",
      potassium: "19.24",
      temperature: "29.97",
      humidity: "65.12",
      pH: "7.13",
      rainfall: "67.88",
      description: "Blackgram (Urad dal) is a pulse crop rich in protein. It's drought-resistant and can be grown in various soil types.",
      tips: "Sow seeds at the right depth, maintain proper spacing, and implement timely weed control measures for optimal yield."
    },
    {
      name: "Chickpea",
      nitrogen: "40.09",
      phosphorus: "67.79",
      potassium: "79.92",
      temperature: "18.87",
      humidity: "16.86",
      pH: "7.34",
      rainfall: "80.06",
      description: "Chickpeas are legumes that fix nitrogen in the soil. They prefer well-drained soils and moderate temperatures.",
      tips: "Avoid waterlogging, practice crop rotation, and monitor for pod borers which are common pests for chickpeas."
    },
    {
      name: "Coconut",
      nitrogen: "21.98",
      phosphorus: "16.93",
      potassium: "30.59",
      temperature: "27.41",
      humidity: "94.84",
      pH: "5.98",
      rainfall: "175.69",
      description: "Coconut palms are tropical trees that produce the versatile coconut fruit. They thrive in coastal areas with sandy soil.",
      tips: "Ensure adequate spacing between trees (7-9 meters), provide irrigation during dry periods, and apply balanced fertilizers."
    },
    {
      name: "Coffee",
      nitrogen: "101.20",
      phosphorus: "28.74",
      potassium: "29.94",
      temperature: "25.54",
      humidity: "58.87",
      pH: "6.81",
      rainfall: "158.07",
      description: "Coffee plants are woody perennials that produce the beans used to make coffee beverages. They prefer shade and high altitudes.",
      tips: "Provide shade trees for young plants, implement regular pruning, and maintain soil fertility through organic matter additions."
    },
    {
      name: "Cotton",
      nitrogen: "117.77",
      phosphorus: "46.24",
      potassium: "19.56",
      temperature: "23.99",
      humidity: "79.84",
      pH: "6.92",
      rainfall: "80.09",
      description: "Cotton is a fiber crop grown worldwide. It requires a long frost-free period and abundant sunshine.",
      tips: "Practice crop rotation to prevent pest buildup, monitor for bollworms, and ensure timely irrigation during flowering and boll formation."
    },
    {
      name: "Grapes",
      nitrogen: "23.18",
      phosphorus: "132.53",
      potassium: "200.11",
      temperature: "23.87",
      humidity: "81.87",
      pH: "6.25",
      rainfall: "69.91",
      description: "Grapes are woody vines that produce fruit clusters. They require well-drained soil and full sun exposure.",
      tips: "Implement a trellis system for support, practice regular pruning to manage growth, and monitor for powdery mildew and other fungal diseases."
    },
    {
      name: "Jute",
      nitrogen: "78.40",
      phosphorus: "46.86",
      potassium: "39.99",
      temperature: "24.96",
      humidity: "79.64",
      pH: "6.73",
      rainfall: "174.79",
      description: "Jute is a fiber crop that thrives in hot, humid conditions. It's often grown in rotation with rice.",
      tips: "Ensure proper field preparation, maintain adequate soil moisture, and harvest at the right time when plants start flowering."
    },
    {
      name: "Lentil",
      nitrogen: "18.77",
      phosphorus: "68.36",
      potassium: "19.41",
      temperature: "24.51",
      humidity: "64.80",
      pH: "6.99",
      rainfall: "45.68",
      description: "Lentils are small legumes that fix nitrogen in the soil. They're drought-tolerant and grow well in cooler conditions.",
      tips: "Sow at the right time to avoid frost damage, ensure proper weed control, and monitor for aphids and other pests."
    },
    {
      name: "Maize",
      nitrogen: "77.76",
      phosphorus: "48.44",
      potassium: "19.79",
      temperature: "22.61",
      humidity: "65.92",
      pH: "6.26",
      rainfall: "84.76",
      description: "Maize (corn) is a cereal grain that requires full sun and fertile soil. It's sensitive to frost and drought.",
      tips: "Plant in blocks rather than single rows for better pollination, ensure adequate nitrogen, and monitor for corn borers and earworms."
    },
    {
      name: "Mango",
      nitrogen: "20.07",
      phosphorus: "27.18",
      potassium: "29.92",
      temperature: "31.90",
      humidity: "50.05",
      pH: "5.77",
      rainfall: "94.99",
      description: "Mangoes are tropical fruit trees that produce sweet, juicy fruits. They require a distinct dry season for flowering.",
      tips: "Prune young trees to establish a strong framework, protect from frost, and implement fruit fly management strategies."
    },
    {
      name: "Mothbeans",
      nitrogen: "21.44",
      phosphorus: "48.01",
      potassium: "20.23",
      temperature: "28.52",
      humidity: "53.16",
      pH: "6.85",
      rainfall: "51.22",
      description: "Mothbeans are drought-resistant legumes that grow well in arid and semi-arid regions. They improve soil fertility.",
      tips: "Prepare the field properly, maintain optimal plant density, and practice timely harvesting to prevent shattering."
    },
    {
      name: "Mungbean",
      nitrogen: "20.99",
      phosphorus: "47.28",
      potassium: "19.87",
      temperature: "28.27",
      humidity: "85.95",
      pH: "6.74",
      rainfall: "48.44",
      description: "Mungbeans are small green legumes that fix nitrogen. They're fast-growing and can be used as a cover crop.",
      tips: "Ensure proper seed treatment before sowing, maintain adequate soil moisture during flowering, and harvest promptly when pods mature."
    },
    {
      name: "Muskmelon",
      nitrogen: "100.32",
      phosphorus: "17.72",
      potassium: "50.08",
      temperature: "28.66",
      humidity: "92.34",
      pH: "6.36",
      rainfall: "24.69",
      description: "Muskmelons are vining fruits that require warm temperatures and full sun. They're sensitive to frost and cold soil.",
      tips: "Use plastic mulch to warm soil and suppress weeds, provide support for vines, and ensure consistent moisture during fruit development."
    },
    {
      name: "Orange",
      nitrogen: "19.58",
      phosphorus: "16.55",
      potassium: "10.01",
      temperature: "22.77",
      humidity: "92.50",
      pH: "7.01",
      rainfall: "110.41",
      description: "Oranges are citrus fruits that grow on evergreen trees. They require good drainage and protection from strong winds.",
      tips: "Implement proper pruning techniques, ensure adequate nutrition especially micronutrients, and monitor for citrus pests like scale insects."
    },
    {
      name: "Papaya",
      nitrogen: "49.88",
      phosphorus: "59.05",
      potassium: "50.04",
      temperature: "33.72",
      humidity: "92.40",
      pH: "6.74",
      rainfall: "142.63",
      description: "Papayas are fast-growing tropical fruits that produce year-round. They're sensitive to frost and waterlogging.",
      tips: "Plant in well-drained soil, provide wind protection, and monitor for papaya ringspot virus which can severely impact production."
    },
    {
      name: "Pigeonpeas",
      nitrogen: "20.73",
      phosphorus: "67.73",
      potassium: "20.29",
      temperature: "27.74",
      humidity: "48.06",
      pH: "5.79",
      rainfall: "149.46",
      description: "Pigeonpeas are drought-resistant legumes that can grow in poor soils. They're often intercropped with cereals.",
      tips: "Practice proper spacing for intercropping systems, implement timely weed control, and monitor for pod borers and pod flies."
    },
    {
      name: "Pomegranate",
      nitrogen: "18.87",
      phosphorus: "18.75",
      potassium: "40.21",
      temperature: "21.84",
      humidity: "90.13",
      pH: "6.43",
      rainfall: "107.53",
      description: "Pomegranates are fruit-bearing shrubs that thrive in hot, dry climates. They're drought-tolerant once established.",
      tips: "Prune to maintain an open canopy structure, ensure adequate potassium for fruit development, and protect from fruit cracking during ripening."
    },
    {
      name: "Rice",
      nitrogen: "79.89",
      phosphorus: "47.58",
      potassium: "39.87",
      temperature: "23.69",
      humidity: "82.27",
      pH: "6.43",
      rainfall: "236.18",
      description: "Rice is a staple grain crop grown in flooded fields called paddies. It requires abundant water and warm temperatures.",
      tips: "Maintain proper water management, implement integrated pest management for rice pests, and ensure timely transplanting for optimal yields."
    },
    {
      name: "Watermelon",
      nitrogen: "99.77",
      phosphorus: "17.21",
      potassium: "39.61",
      temperature: "26.00",
      humidity: "85.76",
      pH: "6.47",
      rainfall: "55.71",
      description: "Watermelons are vining fruits that require warm temperatures, full sun, and plenty of space to grow.",
      tips: "Plant in well-drained soil, provide consistent moisture during vine growth and fruit development, and use mulch to suppress weeds and conserve moisture."
    }
  ];

  // Populate dropdown with crop options
  if (cropSelect) {
    cropData.forEach(crop => {
      const option = document.createElement('option');
      option.value = crop.name;
      option.textContent = crop.name;
      cropSelect.appendChild(option);
    });

    // Display crop information when selected
    cropSelect.addEventListener('change', function() {
      const selectedCrop = this.value;
      const crop = cropData.find(c => c.name === selectedCrop);
      
      if (crop && cropInfo) {
        cropInfo.innerHTML = `
          <div class="info-card">
            <div class="card-header">
              <i class="fas fa-leaf"></i>
              <h3>${crop.name} Growing Guide</h3>
            </div>
            <p class="crop-description">${crop.description}</p>
            
            <h4>Optimal Growing Conditions</h4>
            <div class="conditions-grid">
              <div class="condition-item">
                <i class="fas fa-flask"></i>
                <span>Nitrogen:</span> ${crop.nitrogen} kg/ha
              </div>
              <div class="condition-item">
                <i class="fas fa-flask"></i>
                <span>Phosphorus:</span> ${crop.phosphorus} kg/ha
              </div>
              <div class="condition-item">
                <i class="fas fa-flask"></i>
                <span>Potassium:</span> ${crop.potassium} kg/ha
              </div>
              <div class="condition-item">
                <i class="fas fa-temperature-high"></i>
                <span>Temperature:</span> ${crop.temperature}°C
              </div>
              <div class="condition-item">
                <i class="fas fa-tint"></i>
                <span>Humidity:</span> ${crop.humidity}%
              </div>
              <div class="condition-item">
                <i class="fas fa-vial"></i>
                <span>pH Level:</span> ${crop.pH}
              </div>
              <div class="condition-item">
                <i class="fas fa-cloud-rain"></i>
                <span>Rainfall:</span> ${crop.rainfall} mm
              </div>
            </div>
            
            <h4>Growing Tips</h4>
            <p class="crop-tips">${crop.tips}</p>
          </div>
        `;
      } else if (cropInfo) {
        cropInfo.innerHTML = `
          <div class="crop-placeholder">
            <i class="fas fa-seedling"></i>
            <p>Please select a crop to view detailed information</p>
          </div>
        `;
      }
    });
    
    // Trigger change event to show placeholder initially
    cropSelect.dispatchEvent(new Event('change'));
  }
  
  // Add active class to current nav item
  const currentLocation = window.location.pathname;
  const navLinks = document.querySelectorAll('.navbar a');
  
  navLinks.forEach(link => {
    const linkPath = link.getAttribute('href');
    if (currentLocation.includes('guide') && linkPath.includes('guide')) {
      link.classList.add('active');
    } else if (currentLocation.includes('explore') && linkPath.includes('explore')) {
      link.classList.add('active');
    } else if (currentLocation === '/' || currentLocation.includes('index.html')) {
      if (linkPath === 'index.html' || linkPath === './') {
        link.classList.add('active');
      }
    }
  });
  
  // Call populateCropTable when page loads
  populateCropTable();
});

// Toggle dropdown visibility
function toggleDropdown() {
  const dropdownContent = document.getElementById('dropdownContent');
  if (dropdownContent) {
    dropdownContent.classList.toggle('show');
  }
}

// Show crop information when selected from dropdown
function showCrop(cropName) {
  const cropData = [
    {
      name: "Apple",
      nitrogen: "20.80",
      phosphorus: "134.22",
      potassium: "199.89",
      temperature: "22.63",
      humidity: "92.33",
      pH: "5.93",
      rainfall: "112.65",
      description: "Apples are one of the most widely cultivated tree fruits. They require well-drained soil with moderate fertility and benefit from regular pruning to maintain productivity.",
      tips: "Ensure proper spacing between trees, implement a regular pruning schedule, and monitor for common pests like apple maggots and codling moths."
    },
    {
      name: "Banana",
      nitrogen: "100.23",
      phosphorus: "82.01",
      potassium: "50.05",
      temperature: "27.38",
      humidity: "80.36",
      pH: "5.98",
      rainfall: "104.63",
      description: "Bananas are tropical fruits that grow on large herbaceous plants. They require consistent moisture and warm temperatures to thrive.",
      tips: "Protect plants from strong winds, ensure adequate drainage, and apply mulch to retain soil moisture and suppress weeds."
    },
    {
      name: "Blackgram",
      nitrogen: "40.02",
      phosphorus: "67.47",
      potassium: "19.24",
      temperature: "29.97",
      humidity: "65.12",
      pH: "7.13",
      rainfall: "67.88",
      description: "Blackgram (Urad dal) is a pulse crop rich in protein. It's drought-resistant and can be grown in various soil types.",
      tips: "Sow seeds at the right depth, maintain proper spacing, and implement timely weed control measures for optimal yield."
    },
    {
      name: "Chickpea",
      nitrogen: "40.09",
      phosphorus: "67.79",
      potassium: "79.92",
      temperature: "18.87",
      humidity: "16.86",
      pH: "7.34",
      rainfall: "80.06",
      description: "Chickpeas are legumes that fix nitrogen in the soil. They prefer well-drained soils and moderate temperatures.",
      tips: "Avoid waterlogging, practice crop rotation, and monitor for pod borers which are common pests for chickpeas."
    },
    {
      name: "Coconut",
      nitrogen: "21.98",
      phosphorus: "16.93",
      potassium: "30.59",
      temperature: "27.41",
      humidity: "94.84",
      pH: "5.98",
      rainfall: "175.69",
      description: "Coconut palms are tropical trees that produce the versatile coconut fruit. They thrive in coastal areas with sandy soil.",
      tips: "Ensure adequate spacing between trees (7-9 meters), provide irrigation during dry periods, and apply balanced fertilizers."
    },
    {
      name: "Coffee",
      nitrogen: "101.20",
      phosphorus: "28.74",
      potassium: "29.94",
      temperature: "25.54",
      humidity: "58.87",
      pH: "6.81",
      rainfall: "158.07",
      description: "Coffee plants are woody perennials that produce the beans used to make coffee beverages. They prefer shade and high altitudes.",
      tips: "Provide shade trees for young plants, implement regular pruning, and maintain soil fertility through organic matter additions."
    },
    {
      name: "Cotton",
      nitrogen: "117.77",
      phosphorus: "46.24",
      potassium: "19.56",
      temperature: "23.99",
      humidity: "79.84",
      pH: "6.92",
      rainfall: "80.09",
      description: "Cotton is a fiber crop grown worldwide. It requires a long frost-free period and abundant sunshine.",
      tips: "Practice crop rotation to prevent pest buildup, monitor for bollworms, and ensure timely irrigation during flowering and boll formation."
    },
    {
      name: "Grapes",
      nitrogen: "23.18",
      phosphorus: "132.53",
      potassium: "200.11",
      temperature: "23.87",
      humidity: "81.87",
      pH: "6.25",
      rainfall: "69.91",
      description: "Grapes are woody vines that produce fruit clusters. They require well-drained soil and full sun exposure.",
      tips: "Implement a trellis system for support, practice regular pruning to manage growth, and monitor for powdery mildew and other fungal diseases."
    },
    {
      name: "Jute",
      nitrogen: "78.40",
      phosphorus: "46.86",
      potassium: "39.99",
      temperature: "24.96",
      humidity: "79.64",
      pH: "6.73",
      rainfall: "174.79",
      description: "Jute is a fiber crop that thrives in hot, humid conditions. It's often grown in rotation with rice.",
      tips: "Ensure proper field preparation, maintain adequate soil moisture, and harvest at the right time when plants start flowering."
    },
    {
      name: "Lentil",
      nitrogen: "18.77",
      phosphorus: "68.36",
      potassium: "19.41",
      temperature: "24.51",
      humidity: "64.80",
      pH: "6.99",
      rainfall: "45.68",
      description: "Lentils are small legumes that fix nitrogen in the soil. They're drought-tolerant and grow well in cooler conditions.",
      tips: "Sow at the right time to avoid frost damage, ensure proper weed control, and monitor for aphids and other pests."
    },
    {
      name: "Maize",
      nitrogen: "77.76",
      phosphorus: "48.44",
      potassium: "19.79",
      temperature: "22.61",
      humidity: "65.92",
      pH: "6.26",
      rainfall: "84.76",
      description: "Maize (corn) is a cereal grain that requires full sun and fertile soil. It's sensitive to frost and drought.",
      tips: "Plant in blocks rather than single rows for better pollination, ensure adequate nitrogen, and monitor for corn borers and earworms."
    },
    {
      name: "Mango",
      nitrogen: "20.07",
      phosphorus: "27.18",
      potassium: "29.92",
      temperature: "31.90",
      humidity: "50.05",
      pH: "5.77",
      rainfall: "94.99",
      description: "Mangoes are tropical fruit trees that produce sweet, juicy fruits. They require a distinct dry season for flowering.",
      tips: "Prune young trees to establish a strong framework, protect from frost, and implement fruit fly management strategies."
    },
    {
      name: "Mothbeans",
      nitrogen: "21.44",
      phosphorus: "48.01",
      potassium: "20.23",
      temperature: "28.52",
      humidity: "53.16",
      pH: "6.85",
      rainfall: "51.22",
      description: "Mothbeans are drought-resistant legumes that grow well in arid and semi-arid regions. They improve soil fertility.",
      tips: "Prepare the field properly, maintain optimal plant density, and practice timely harvesting to prevent shattering."
    },
    {
      name: "Mungbean",
      nitrogen: "20.99",
      phosphorus: "47.28",
      potassium: "19.87",
      temperature: "28.27",
      humidity: "85.95",
      pH: "6.74",
      rainfall: "48.44",
      description: "Mungbeans are small green legumes that fix nitrogen. They're fast-growing and can be used as a cover crop.",
      tips: "Ensure proper seed treatment before sowing, maintain adequate soil moisture during flowering, and harvest promptly when pods mature."
    },
    {
      name: "Muskmelon",
      nitrogen: "100.32",
      phosphorus: "17.72",
      potassium: "50.08",
      temperature: "28.66",
      humidity: "92.34",
      pH: "6.36",
      rainfall: "24.69",
      description: "Muskmelons are vining fruits that require warm temperatures and full sun. They're sensitive to frost and cold soil.",
      tips: "Use plastic mulch to warm soil and suppress weeds, provide support for vines, and ensure consistent moisture during fruit development."
    },
    {
      name: "Orange",
      nitrogen: "19.58",
      phosphorus: "16.55",
      potassium: "10.01",
      temperature: "22.77",
      humidity: "92.50",
      pH: "7.01",
      rainfall: "110.41",
      description: "Oranges are citrus fruits that grow on evergreen trees. They require good drainage and protection from strong winds.",
      tips: "Implement proper pruning techniques, ensure adequate nutrition especially micronutrients, and monitor for citrus pests like scale insects."
    },
    {
      name: "Papaya",
      nitrogen: "49.88",
      phosphorus: "59.05",
      potassium: "50.04",
      temperature: "33.72",
      humidity: "92.40",
      pH: "6.74",
      rainfall: "142.63",
      description: "Papayas are fast-growing tropical fruits that produce year-round. They're sensitive to frost and waterlogging.",
      tips: "Plant in well-drained soil, provide wind protection, and monitor for papaya ringspot virus which can severely impact production."
    },
    {
      name: "Pigeonpeas",
      nitrogen: "20.73",
      phosphorus: "67.73",
      potassium: "20.29",
      temperature: "27.74",
      humidity: "48.06",
      pH: "5.79",
      rainfall: "149.46",
      description: "Pigeonpeas are drought-resistant legumes that can grow in poor soils. They're often intercropped with cereals.",
      tips: "Practice proper spacing for intercropping systems, implement timely weed control, and monitor for pod borers and pod flies."
    },
    {
      name: "Pomegranate",
      nitrogen: "18.87",
      phosphorus: "18.75",
      potassium: "40.21",
      temperature: "21.84",
      humidity: "90.13",
      pH: "6.43",
      rainfall: "107.53",
      description: "Pomegranates are fruit-bearing shrubs that thrive in hot, dry climates. They're drought-tolerant once established.",
      tips: "Prune to maintain an open canopy structure, ensure adequate potassium for fruit development, and protect from fruit cracking during ripening."
    },
    {
      name: "Rice",
      nitrogen: "79.89",
      phosphorus: "47.58",
      potassium: "39.87",
      temperature: "23.69",
      humidity: "82.27",
      pH: "6.43",
      rainfall: "236.18",
      description: "Rice is a staple grain crop grown in flooded fields called paddies. It requires abundant water and warm temperatures.",
      tips: "Maintain proper water management, implement integrated pest management for rice pests, and ensure timely transplanting for optimal yields."
    },
    {
      name: "Watermelon",
      nitrogen: "99.77",
      phosphorus: "17.21",
      potassium: "39.61",
      temperature: "26.00",
      humidity: "85.76",
      pH: "6.47",
      rainfall: "55.71",
      description: "Watermelons are vining fruits that require warm temperatures, full sun, and plenty of space to grow.",
      tips: "Plant in well-drained soil, provide consistent moisture during vine growth and fruit development, and use mulch to suppress weeds and conserve moisture."
    }
  ];
  
  const crop = cropData.find(c => c.name.toLowerCase() === cropName.toLowerCase());
  const cropInfoContainer = document.querySelector('.crop-info-container');
  const cropDetailsSection = document.querySelector('.crop-details');
  const dropdownContent = document.getElementById('dropdownContent');
  
  // Hide dropdown
  if (dropdownContent) {
    dropdownContent.classList.remove('show');
  }
  
  // Update dropdown button text
  const dropBtn = document.querySelector('.dropbtn');
  if (dropBtn && crop) {
    dropBtn.innerHTML = `
      <i class="fas fa-seedling"></i>
      ${crop.name}
      <i class="fas fa-chevron-down"></i>
    `;
  }
  
  if (crop && cropInfoContainer && cropDetailsSection) {
    cropInfoContainer.innerHTML = `
      <div class="info-card">
        <div class="card-header">
          <i class="fas fa-leaf"></i>
          <h2>${crop.name} Growing Guide</h2>
        </div>
        <p class="crop-description">${crop.description}</p>
        
        <h3>Optimal Growing Conditions</h3>
        <div class="conditions-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
          <div class="condition-item" style="background: var(--light-gray); padding: 1.5rem; border-radius: 10px; text-align: center;">
            <i class="fas fa-flask" style="color: var(--accent-green); font-size: 2rem; margin-bottom: 1rem; display: block;"></i>
            <div><strong>Nitrogen:</strong> ${crop.nitrogen} kg/ha</div>
          </div>
          <div class="condition-item" style="background: var(--light-gray); padding: 1.5rem; border-radius: 10px; text-align: center;">
            <i class="fas fa-flask" style="color: var(--accent-green); font-size: 2rem; margin-bottom: 1rem; display: block;"></i>
            <div><strong>Phosphorus:</strong> ${crop.phosphorus} kg/ha</div>
          </div>
          <div class="condition-item" style="background: var(--light-gray); padding: 1.5rem; border-radius: 10px; text-align: center;">
            <i class="fas fa-flask" style="color: var(--accent-green); font-size: 2rem; margin-bottom: 1rem; display: block;"></i>
            <div><strong>Potassium:</strong> ${crop.potassium} kg/ha</div>
          </div>
          <div class="condition-item" style="background: var(--light-gray); padding: 1.5rem; border-radius: 10px; text-align: center;">
            <i class="fas fa-temperature-high" style="color: var(--accent-green); font-size: 2rem; margin-bottom: 1rem; display: block;"></i>
            <div><strong>Temperature:</strong> ${crop.temperature}°C</div>
          </div>
          <div class="condition-item" style="background: var(--light-gray); padding: 1.5rem; border-radius: 10px; text-align: center;">
            <i class="fas fa-tint" style="color: var(--accent-green); font-size: 2rem; margin-bottom: 1rem; display: block;"></i>
            <div><strong>Humidity:</strong> ${crop.humidity}%</div>
          </div>
          <div class="condition-item" style="background: var(--light-gray); padding: 1.5rem; border-radius: 10px; text-align: center;">
            <i class="fas fa-vial" style="color: var(--accent-green); font-size: 2rem; margin-bottom: 1rem; display: block;"></i>
            <div><strong>pH Level:</strong> ${crop.pH}</div>
          </div>
          <div class="condition-item" style="background: var(--light-gray); padding: 1.5rem; border-radius: 10px; text-align: center;">
            <i class="fas fa-cloud-rain" style="color: var(--accent-green); font-size: 2rem; margin-bottom: 1rem; display: block;"></i>
            <div><strong>Rainfall:</strong> ${crop.rainfall} mm</div>
          </div>
        </div>
        
        <h4>Growing Tips</h4>
        <p class="crop-tips">${crop.tips}</p>
      </div>
    `;
    
    // Show the crop details section
    cropDetailsSection.classList.add('show');
    
    // Scroll to crop details
    cropDetailsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
  const dropdown = document.querySelector('.dropdown');
  const dropdownContent = document.getElementById('dropdownContent');
  
  if (dropdown && dropdownContent && !dropdown.contains(event.target)) {
    dropdownContent.classList.remove('show');
  }
});
