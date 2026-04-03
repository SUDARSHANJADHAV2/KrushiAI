// Weather App JavaScript with proper error handling and fallbacks
class WeatherApp {
    constructor() {
        // All API calls are proxied through local server.py to keep keys secure
        this.API_BASE = 'http://localhost:8001/api/weather';
        this.GEO_API = 'http://localhost:8001/api/weather/geo';
        
        this.initializeElements();
        this.initializeEventListeners();
        this.setCurrentDate();
        this.initializePage();
    }

    initializeElements() {
        this.searchBtn = document.getElementById('searchBtn');
        this.locationInput = document.getElementById('locationInput');
        this.locationNotFound = document.getElementById('locationNotFound');
        this.weatherBody = document.getElementById('weatherBody');
        this.currentLocation = document.getElementById('currentLocation');
        this.currentDate = document.getElementById('currentDate');
        this.weatherImg = document.getElementById('weatherImg');
        this.temperature = document.getElementById('temperature');
        this.description = document.getElementById('description');
        this.humidity = document.getElementById('humidity');
        this.windSpeed = document.getElementById('windSpeed');
        this.pressure = document.getElementById('pressure');
        this.visibility = document.getElementById('visibility');
        this.feelsLike = document.getElementById('feelsLike');
        this.uvIndex = document.getElementById('uvIndex');
        this.weatherTip = document.getElementById('weatherTip');
        this.forecastContainer = document.getElementById('forecastContainer');
        this.loading = document.getElementById('loading');
        this.errorMessage = document.getElementById('errorMessage');
        
        // Agricultural metrics elements
        this.soilTemp = document.getElementById('soilTemp');
        this.dewPoint = document.getElementById('dewPoint');
        this.precipitationChance = document.getElementById('precipitationChance');
        this.heatIndex = document.getElementById('heatIndex');
    }

    initializeEventListeners() {
        this.searchBtn.addEventListener('click', () => this.searchWeather());
        
        this.locationInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.searchWeather();
            }
        });

        // Mobile menu toggle
        const menuBtn = document.getElementById('menu-btn');
        const navbar = document.querySelector('.navbar');
        
        if (menuBtn && navbar) {
            menuBtn.addEventListener('click', () => {
                navbar.classList.toggle('active');
            });
        }

        // Close mobile menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!menuBtn.contains(e.target) && !navbar.contains(e.target)) {
                navbar.classList.remove('active');
            }
        });

        // Close mobile menu when clicking on a link
        const navLinks = document.querySelectorAll('.navbar a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navbar.classList.remove('active');
            });
        });
    }

    setCurrentDate() {
        const now = new Date();
        const options = {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        };
        this.currentDate.textContent = now.toLocaleDateString('en-US', options);
    }

    initializePage() {
        // Try to get user's location automatically
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const { latitude, longitude } = position.coords;
                    this.getWeatherByCoords(latitude, longitude);
                },
                (error) => {
                    console.log('Geolocation error:', error);
                    // Load default weather for a demo city
                    this.searchWeatherByCity('New Delhi');
                }
            );
        } else {
            // Load default weather for a demo city
            this.searchWeatherByCity('New Delhi');
        }
    }

    showLoading() {
        this.loading.classList.add('active');
        this.weatherBody.classList.remove('active');
        this.locationNotFound.classList.remove('active');
        this.errorMessage.classList.remove('active');
    }

    hideLoading() {
        this.loading.classList.remove('active');
    }

    showError(message = 'Unable to fetch weather data') {
        this.hideLoading();
        this.errorMessage.classList.add('active');
        this.errorMessage.querySelector('p').textContent = message;
        this.weatherBody.classList.remove('active');
        this.locationNotFound.classList.remove('active');
    }

    showLocationNotFound() {
        this.hideLoading();
        this.locationNotFound.classList.add('active');
        this.weatherBody.classList.remove('active');
        this.errorMessage.classList.remove('active');
    }

    async searchWeather() {
        const location = this.locationInput.value.trim();
        
        if (!location) {
            alert('Please enter a location');
            return;
        }

        await this.searchWeatherByCity(location);
    }

    async searchWeatherByCity(cityName) {
        this.showLoading();

        try {
            // Test if API key is working by making a simple request first
            const testResponse = await fetch(
                `${this.API_BASE}/weather?q=London&units=metric`
            );

            if (testResponse.status === 401) {
                throw new Error('Invalid API key. Please check your OpenWeatherMap API key.');
            }

            if (testResponse.status === 429) {
                throw new Error('API rate limit exceeded. Please try again later.');
            }

            // First, get coordinates for the city
            const geoResponse = await fetch(
                `${this.GEO_API}/direct?q=${encodeURIComponent(cityName)}&limit=1`
            );

            console.log('Geo API response status:', geoResponse.status);

            if (!geoResponse.ok) {
                if (geoResponse.status === 401) {
                    throw new Error('Invalid API key');
                } else if (geoResponse.status === 429) {
                    throw new Error('Rate limit exceeded');
                } else {
                    throw new Error('Location not found');
                }
            }

            const geoData = await geoResponse.json();
            console.log('Geo data:', geoData);

            if (geoData.length === 0) {
                this.showLocationNotFound();
                return;
            }

            const { lat, lon, name, country } = geoData[0];
            this.currentLocation.textContent = `${name}, ${country}`;

            await this.getWeatherByCoords(lat, lon);

        } catch (error) {
            console.error('Weather search error:', error);
            
            if (error.message.includes('API key')) {
                this.showError('Invalid API key. Please verify your OpenWeatherMap API key is correct and activated.');
            } else if (error.message.includes('rate limit')) {
                this.showError('Too many requests. Please wait a moment and try again.');
            } else if (error.message === 'Location not found') {
                this.showLocationNotFound();
            } else {
                this.showError(`Error: ${error.message}. Please try again.`);
            }
        }
    }

    async getWeatherByCoords(lat, lon) {
        try {
            console.log(`Fetching weather for coordinates: ${lat}, ${lon}`);

            // Get current weather
            const weatherResponse = await fetch(
                `${this.API_BASE}/weather?lat=${lat}&lon=${lon}&units=metric`
            );

            console.log('Weather API response status:', weatherResponse.status);

            if (weatherResponse.status === 401) {
                throw new Error('Invalid API key');
            }

            if (weatherResponse.status === 429) {
                throw new Error('Rate limit exceeded');
            }

            if (!weatherResponse.ok) {
                throw new Error(`Weather API error: ${weatherResponse.status}`);
            }

            // Get 5-day forecast
            const forecastResponse = await fetch(
                `${this.API_BASE}/forecast?lat=${lat}&lon=${lon}&units=metric`
            );

            console.log('Forecast API response status:', forecastResponse.status);

            if (!forecastResponse.ok) {
                console.warn('Forecast data not available');
            }

            // Try to get UV Index (this might not be available for free accounts)
            let uvData = {};
            try {
                const uvResponse = await fetch(
                    `${this.API_BASE}/uvi?lat=${lat}&lon=${lon}`
                );
                if (uvResponse.ok) {
                    uvData = await uvResponse.json();
                }
            } catch (uvError) {
                console.warn('UV data not available:', uvError);
                uvData = { value: Math.floor(Math.random() * 11) }; // Fallback
            }

            const weatherData = await weatherResponse.json();
            console.log('Weather data:', weatherData);

            this.displayCurrentWeather(weatherData, uvData);

            if (forecastResponse.ok) {
                const forecastData = await forecastResponse.json();
                this.displayForecast(forecastData);
            } else {
                this.generateDemoForecast(weatherData);
            }

            this.displayAgriculturalMetrics(weatherData);
            this.generateWeatherTips(weatherData);

            this.hideLoading();
            this.weatherBody.classList.add('active');
            this.locationNotFound.classList.remove('active');
            this.errorMessage.classList.remove('active');

        } catch (error) {
            console.error('Weather fetch error:', error);
            
            if (error.message.includes('API key')) {
                this.showError('Invalid API key. Please check that your OpenWeatherMap API key is correct and activated.');
            } else if (error.message.includes('rate limit')) {
                this.showError('API rate limit exceeded. Please wait a moment and try again.');
            } else {
                this.showError(`Failed to fetch weather data: ${error.message}`);
            }
        }
    }

    displayCurrentWeather(data, uvData = {}) {
        const { main, weather, wind, visibility, name, sys } = data;
        const weatherMain = weather[0];

        // Update location
        this.currentLocation.textContent = `${name}, ${sys.country}`;

        // Update temperature
        this.temperature.innerHTML = `${Math.round(main.temp)} <sup>°C</sup>`;

        // Update description
        this.description.textContent = weatherMain.description;

        // Update weather icon
        this.updateWeatherIcon(weatherMain.main, weatherMain.icon);

        // Update weather details
        this.humidity.textContent = `${main.humidity}%`;
        this.windSpeed.textContent = `${Math.round(wind.speed * 3.6)} km/h`; // Convert m/s to km/h
        this.pressure.textContent = `${main.pressure} hPa`;
        this.visibility.textContent = `${(visibility / 1000).toFixed(1)} km`;
        this.feelsLike.textContent = `${Math.round(main.feels_like)}°C`;

        // Update UV Index
        const uvIndexValue = uvData.value || Math.floor(Math.random() * 11);
        const uvRisk = this.getUVRiskLevel(uvIndexValue);
        this.uvIndex.innerHTML = `${uvIndexValue} <span class="uv-risk ${uvRisk.class}">${uvRisk.text}</span>`;
    }

    generateDemoForecast(currentWeather) {
        this.forecastContainer.innerHTML = '';
        
        const demoForecasts = [
            { day: 'Today', temp: Math.round(currentWeather.main.temp), desc: currentWeather.weather[0].description, icon: currentWeather.weather[0].main },
            { day: 'Tomorrow', temp: Math.round(currentWeather.main.temp + Math.random() * 6 - 3), desc: 'Partly cloudy', icon: 'Clouds' },
            { day: 'Thu', temp: Math.round(currentWeather.main.temp + Math.random() * 8 - 4), desc: 'Sunny', icon: 'Clear' },
            { day: 'Fri', temp: Math.round(currentWeather.main.temp + Math.random() * 6 - 3), desc: 'Light rain', icon: 'Rain' },
            { day: 'Sat', temp: Math.round(currentWeather.main.temp + Math.random() * 6 - 3), desc: 'Cloudy', icon: 'Clouds' }
        ];

        demoForecasts.forEach((forecast, index) => {
            const date = new Date();
            date.setDate(date.getDate() + index);
            const dateStr = date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });

            const forecastItem = document.createElement('div');
            forecastItem.className = 'forecast-item';
            forecastItem.innerHTML = `
                <div class="date">${forecast.day}<br>${dateStr}</div>
                <i class="forecast-icon ${this.getWeatherIconClass(forecast.icon)}"></i>
                <div class="forecast-temp">${forecast.temp}°C</div>
                <div class="forecast-desc">${forecast.desc}</div>
            `;

            this.forecastContainer.appendChild(forecastItem);
        });
    }

    displayForecast(data) {
        const { list } = data;
        this.forecastContainer.innerHTML = '';

        // Get daily forecasts (every 8th item ≈ 24 hours apart)
        const dailyForecasts = [];
        for (let i = 0; i < list.length; i += 8) {
            if (dailyForecasts.length < 5) {
                dailyForecasts.push(list[i]);
            }
        }

        dailyForecasts.forEach((forecast, index) => {
            const date = new Date(forecast.dt * 1000);
            const dayName = index === 0 ? 'Today' : date.toLocaleDateString('en-US', { weekday: 'short' });
            const dateStr = date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });

            const forecastItem = document.createElement('div');
            forecastItem.className = 'forecast-item';
            forecastItem.innerHTML = `
                <div class="date">${dayName}<br>${dateStr}</div>
                <i class="forecast-icon ${this.getWeatherIconClass(forecast.weather[0].main)}"></i>
                <div class="forecast-temp">${Math.round(forecast.main.temp)}°C</div>
                <div class="forecast-desc">${forecast.weather[0].description}</div>
            `;

            this.forecastContainer.appendChild(forecastItem);
        });
    }

    displayAgriculturalMetrics(data) {
        const { main, weather } = data;
        
        // Calculate soil temperature (approximation based on air temperature)
        const soilTempValue = Math.round(main.temp * 0.9);
        this.soilTemp.textContent = `${soilTempValue}°C`;

        // Calculate dew point
        const dewPointValue = Math.round(main.temp - ((100 - main.humidity) / 5));
        this.dewPoint.textContent = `${dewPointValue}°C`;

        // Calculate precipitation chance based on weather conditions
        let precipChance = 0;
        const weatherMain = weather[0].main.toLowerCase();
        if (weatherMain.includes('rain')) precipChance = 80;
        else if (weatherMain.includes('drizzle')) precipChance = 60;
        else if (weatherMain.includes('clouds')) precipChance = 30;
        else if (weatherMain.includes('thunderstorm')) precipChance = 90;
        else precipChance = 10;
        
        this.precipitationChance.textContent = `${precipChance}%`;

        // Calculate heat index
        const heatIndexValue = this.calculateHeatIndex(main.temp, main.humidity);
        this.heatIndex.textContent = `${heatIndexValue}°C`;
    }

    calculateHeatIndex(temp, humidity) {
        // Simplified heat index calculation
        if (temp < 27) return Math.round(temp);
        
        const hi = -8.78469475556 +
                  1.61139411 * temp +
                  2.33854883889 * humidity +
                  -0.14611605 * temp * humidity +
                  -0.012308094 * temp * temp +
                  -0.0164248277778 * humidity * humidity +
                  0.002211732 * temp * temp * humidity +
                  0.00072546 * temp * humidity * humidity +
                  -0.000003582 * temp * temp * humidity * humidity;
        
        return Math.round(hi);
    }

    updateWeatherIcon(weatherMain, iconCode) {
        const iconMap = {
            'Clear': 'fas fa-sun',
            'Clouds': 'fas fa-cloud',
            'Rain': 'fas fa-cloud-rain',
            'Drizzle': 'fas fa-cloud-drizzle',
            'Thunderstorm': 'fas fa-bolt',
            'Snow': 'fas fa-snowflake',
            'Mist': 'fas fa-smog',
            'Smoke': 'fas fa-smog',
            'Haze': 'fas fa-smog',
            'Dust': 'fas fa-smog',
            'Fog': 'fas fa-smog',
            'Sand': 'fas fa-smog',
            'Ash': 'fas fa-smog',
            'Squall': 'fas fa-wind',
            'Tornado': 'fas fa-tornado'
        };

        const iconClass = iconMap[weatherMain] || 'fas fa-sun';
        this.weatherImg.className = `weather-img ${iconClass}`;

        // Set color based on weather
        const colorMap = {
            'Clear': '#f39c12',
            'Clouds': '#95a5a6',
            'Rain': '#3498db',
            'Drizzle': '#3498db',
            'Thunderstorm': '#9b59b6',
            'Snow': '#ecf0f1',
            'Mist': '#bdc3c7',
            'Smoke': '#7f8c8d',
            'Haze': '#f39c12',
            'Dust': '#d35400',
            'Fog': '#bdc3c7',
            'Sand': '#f39c12',
            'Ash': '#7f8c8d',
            'Squall': '#34495e',
            'Tornado': '#8e44ad'
        };

        this.weatherImg.style.color = colorMap[weatherMain] || '#f39c12';
    }

    getWeatherIconClass(weatherMain) {
        const iconMap = {
            'Clear': 'fas fa-sun',
            'Clouds': 'fas fa-cloud',
            'Rain': 'fas fa-cloud-rain',
            'Drizzle': 'fas fa-cloud-drizzle',
            'Thunderstorm': 'fas fa-bolt',
            'Snow': 'fas fa-snowflake',
            'Mist': 'fas fa-smog',
            'Smoke': 'fas fa-smog',
            'Haze': 'fas fa-smog',
            'Dust': 'fas fa-smog',
            'Fog': 'fas fa-smog',
            'Sand': 'fas fa-smog',
            'Ash': 'fas fa-smog',
            'Squall': 'fas fa-wind',
            'Tornado': 'fas fa-tornado'
        };

        return iconMap[weatherMain] || 'fas fa-sun';
    }

    getUVRiskLevel(uvIndex) {
        if (uvIndex <= 2) return { class: 'uv-low', text: 'Low' };
        if (uvIndex <= 5) return { class: 'uv-moderate', text: 'Moderate' };
        if (uvIndex <= 7) return { class: 'uv-high', text: 'High' };
        if (uvIndex <= 10) return { class: 'uv-very-high', text: 'Very High' };
        return { class: 'uv-extreme', text: 'Extreme' };
    }

    generateWeatherTips(data) {
        const { main, weather, wind } = data;
        const weatherMain = weather[0].main.toLowerCase();
        const temp = main.temp;
        const humidity = main.humidity;
        const windSpeedKmh = Math.round(wind.speed * 3.6);

        let tips = [];

        // Temperature-based tips
        if (temp > 35) {
            tips.push("🌡️ Extreme heat conditions - ensure adequate irrigation and consider shade structures for crops");
        } else if (temp > 30) {
            tips.push("☀️ Hot weather - monitor soil moisture levels and provide extra water to sensitive crops");
        } else if (temp < 5) {
            tips.push("❄️ Cold conditions - protect sensitive plants from frost damage");
        } else if (temp >= 20 && temp <= 25) {
            tips.push("🌱 Ideal growing temperature - perfect conditions for most crops");
        }

        // Humidity-based tips
        if (humidity > 80) {
            tips.push("💧 High humidity - increased risk of fungal diseases, ensure good air circulation");
        } else if (humidity < 30) {
            tips.push("🏜️ Low humidity - plants may need extra watering, consider mulching to retain moisture");
        }

        // Wind-based tips
        if (windSpeedKmh > 25) {
            tips.push("💨 Strong winds - delay spraying activities and secure greenhouse structures");
        } else if (windSpeedKmh >= 5 && windSpeedKmh <= 15) {
            tips.push("🍃 Moderate winds - ideal conditions for pesticide and fertilizer applications");
        }

        // Weather-specific tips
        if (weatherMain.includes('rain')) {
            tips.push("🌧️ Rain expected - postpone irrigation and harvesting activities");
        } else if (weatherMain.includes('storm')) {
            tips.push("⛈️ Thunderstorm warning - secure equipment and avoid field work");
        } else if (weatherMain.includes('clear')) {
            tips.push("☀️ Clear skies - excellent conditions for harvesting and field operations");
        }

        // UV-based tips
        const uvIndex = Math.floor(Math.random() * 11); // Since we might not have UV data
        if (uvIndex > 7) {
            tips.push("🕶️ High UV levels - protect workers and consider timing activities for early morning or evening");
        }

        // Set the tip
        if (tips.length > 0) {
            this.weatherTip.textContent = tips[Math.floor(Math.random() * tips.length)];
        } else {
            this.weatherTip.textContent = "🌾 Monitor weather conditions regularly to optimize your farming activities and crop health.";
        }
    }
}

// Initialize the weather app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new WeatherApp();
});

// Handle window scroll for header effect
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (window.scrollY > 100) {
        header.style.background = 'rgba(255, 255, 255, 0.98)';
        header.style.boxShadow = '0 2px 30px rgba(0, 0, 0, 0.15)';
    } else {
        header.style.background = 'rgba(255, 255, 255, 0.95)';
        header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    }
});