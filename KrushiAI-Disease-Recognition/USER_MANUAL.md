# 📖 KrushiAI User Manual

## Table of Contents
1. [Getting Started](#getting-started)
2. [Navigation Guide](#navigation-guide)
3. [Disease Detection](#disease-detection)
4. [Understanding Results](#understanding-results)
5. [Disease Database](#disease-database)
6. [Analytics Dashboard](#analytics-dashboard)
7. [Tips and Best Practices](#tips-and-best-practices)
8. [Troubleshooting](#troubleshooting)
9. [FAQ](#frequently-asked-questions)

## Getting Started

### System Requirements
- **Web Browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Internet Connection**: Required for web-based deployment
- **Image Formats**: JPG, JPEG, PNG
- **Image Size**: Minimum 224x224 pixels recommended

### Accessing KrushiAI
1. Open your web browser
2. Navigate to the application URL (e.g., `http://localhost:8501` for local deployment)
3. Wait for the application to load

### First Time Use
1. **Welcome Screen**: You'll see the KrushiAI home page with feature overview
2. **Navigation**: Use the horizontal menu bar to navigate between different sections
3. **Upload Test**: Try the sample images to familiarize yourself with the system

## Navigation Guide

### Main Navigation Menu
The application features a horizontal navigation menu with five main sections:

#### 🏠 Home
- **Purpose**: Overview of KrushiAI features and capabilities
- **Content**: 
  - Welcome message and project description
  - Key features highlight
  - Disease severity statistics
  - Quick start guide

#### 🔬 Disease Detection
- **Purpose**: Main functionality for analyzing plant images
- **Content**:
  - Image upload interface
  - Analysis controls
  - Results display
  - Sample images for testing

#### 📊 Analytics
- **Purpose**: Model performance metrics and training insights
- **Content**:
  - Model accuracy statistics
  - Training history charts
  - Performance analysis
  - Technical metrics

#### 📚 Disease Database
- **Purpose**: Comprehensive disease information repository
- **Content**:
  - Searchable disease catalog
  - Filter options (plant type, severity)
  - Detailed disease information
  - Treatment and prevention guides

#### ℹ️ About
- **Purpose**: Project information and technical details
- **Content**:
  - Project overview
  - Technology stack
  - Usage guidelines
  - Support information

## Disease Detection

### Step-by-Step Process

#### Step 1: Image Upload
1. Navigate to the **🔬 Disease Detection** page
2. Click on the file upload area or drag and drop your image
3. Select an image file (JPG, JPEG, or PNG format)
4. Wait for the image to upload and display

#### Step 2: Image Analysis
1. Once your image is uploaded, it will be displayed on the screen
2. Click the **🔍 Analyze Image** button
3. The system will show a loading indicator with "🧠 AI is analyzing your image..."
4. Wait 2-3 seconds for processing to complete

#### Step 3: View Results
The results will be displayed in several sections:
- **Primary Prediction**: Main disease identification with confidence score
- **Disease Information**: Detailed information about the identified condition
- **Treatment Recommendations**: Specific treatment steps
- **Prevention Methods**: Preventive measures for future protection

### Sample Images
If you don't have a plant image available:
1. Scroll down to the **Sample Images** section
2. Select from available test images using the dropdown
3. Click **🔍 Analyze Sample Image** to see how the system works

## Understanding Results

### Prediction Results

#### Confidence Score
- **Range**: 0-100%
- **Interpretation**:
  - 90-100%: Very high confidence (🎯)
  - 80-89%: High confidence (✅)
  - 70-79%: Moderate confidence (👍)
  - 60-69%: Low confidence (⚠️)
  - Below 60%: Very low confidence (🤔)

#### Confidence Messages
The system provides user-friendly confidence messages:
- **🎯 Very confident**: Highly reliable prediction
- **✅ Quite confident**: Reliable with minor uncertainty
- **👍 Moderately confident**: Generally reliable
- **⚠️ Low confidence**: Consider retaking photo
- **🤔 Very low confidence**: Recommend better image quality

### Disease Information

#### Basic Information
- **Disease Name**: Common name of the disease
- **Plant**: Affected plant species
- **Scientific Name**: Scientific/botanical name
- **Severity Level**: Critical, High, Medium, Low, or None
- **Description**: Overview of the disease

#### Symptoms
Detailed list of visual symptoms to help verify the diagnosis:
- Physical appearance changes
- Color variations
- Texture modifications
- Growth abnormalities

#### Treatment Recommendations
Step-by-step treatment guidance:
- Immediate actions required
- Fungicide/pesticide applications
- Cultural practices
- Follow-up care

#### Prevention Methods
Proactive measures to prevent disease occurrence:
- Environmental management
- Plant care practices
- Early detection strategies
- Resistant variety recommendations

### Advanced Analysis

#### Top 5 Predictions
- Shows alternative possibilities with confidence percentages
- Helps understand uncertainty in predictions
- Useful when primary confidence is low

#### Image Analysis Metrics
- **Image Size**: Pixel dimensions of uploaded image
- **Brightness**: Average brightness level (0-255)
- **Contrast**: Image contrast measurement
- **Edge Density**: Measure of detail/texture in image

#### Feature Analysis Chart
- Radar chart showing normalized image features
- Helps understand image quality factors
- Useful for troubleshooting poor predictions

## Disease Database

### Search and Filter Options

#### Plant Type Filter
1. Use the dropdown to select specific plant types
2. Options include: Apple, Tomato, Potato, Corn, etc.
3. Select "All" to view all diseases

#### Severity Filter
1. Filter diseases by severity level:
   - Critical: Immediate action required
   - High: Serious threat to crop
   - Medium: Moderate impact
   - Low: Minor issues
   - None: Healthy plants

#### Search Function
1. Use the search box to find specific diseases
2. Type partial disease names for quick results
3. Search is case-insensitive

### Disease Information Cards
Each disease is displayed in a card format showing:
- Disease name and plant type
- Severity level with color coding
- Brief description
- "View Details" expandable section

### Pagination
- Displays 12 diseases per page
- Use page selector to navigate through results
- Page counter shows current position

## Analytics Dashboard

### Model Performance Metrics

#### Key Statistics
- **🎯 Accuracy**: Current validation accuracy percentage
- **📊 Loss**: Model loss value (lower is better)
- **🔄 Epochs**: Number of training iterations completed
- **🏆 Best**: Best validation accuracy achieved during training

#### Training History Charts
- **Model Accuracy**: Training vs validation accuracy over time
- **Model Loss**: Training vs validation loss progression
- Interactive charts with hover details

#### Performance Analysis
- Automated analysis of model performance
- Recommendations for improvement
- Overfitting detection
- Generalization assessment

## Tips and Best Practices

### Image Quality Guidelines

#### ✅ Best Practices
- **High Resolution**: Use images with minimum 224x224 pixels
- **Good Lighting**: Natural daylight provides best results
- **Clear Focus**: Ensure affected areas are in sharp focus
- **Close-up Views**: Focus on diseased plant parts (leaves, fruits, stems)
- **Multiple Angles**: Take photos from different angles if symptoms are unclear
- **Clean Background**: Remove distracting background elements
- **Stable Camera**: Avoid blurry or shaky images

#### ❌ Avoid These Issues
- Low resolution or pixelated images
- Poor lighting conditions (too dark or overexposed)
- Blurry or out-of-focus images
- Heavy image filters or processing
- Images with mostly healthy plant parts
- Extreme close-ups where disease context is lost
- Images with multiple overlapping diseases

### Interpreting Results

#### High Confidence Predictions (>80%)
- Generally reliable for decision making
- Proceed with recommended treatments
- Monitor plant response to treatment

#### Moderate Confidence Predictions (60-80%)
- Consider as preliminary diagnosis
- Look for additional symptoms
- Consult with agricultural experts if critical
- Consider taking additional photos

#### Low Confidence Predictions (<60%)
- Retake photos with better quality
- Try different angles or lighting
- Consider multiple disease possibilities
- Seek expert consultation for critical crops

### When to Seek Expert Help
- Consistent low confidence predictions
- Critical or high-severity disease detections
- Unusual or rare symptoms not matching database
- Multiple simultaneous disease symptoms
- Commercial crop management decisions
- Pesticide application planning

## Troubleshooting

### Common Issues and Solutions

#### Image Upload Problems
**Issue**: Cannot upload image
- **Solution**: Check file format (use JPG, JPEG, or PNG)
- **Solution**: Ensure file size is under 200MB
- **Solution**: Try refreshing the browser page

#### Slow Analysis
**Issue**: Analysis takes too long
- **Solution**: Check internet connection
- **Solution**: Try smaller image file
- **Solution**: Refresh page and try again

#### Poor Prediction Accuracy
**Issue**: Consistently low confidence scores
- **Solution**: Improve image quality (lighting, focus)
- **Solution**: Focus on affected plant parts
- **Solution**: Try different camera angles
- **Solution**: Use sample images to verify system is working

#### Browser Compatibility
**Issue**: Application not displaying correctly
- **Solution**: Update to latest browser version
- **Solution**: Clear browser cache and cookies
- **Solution**: Try different browser (Chrome recommended)

#### Model Loading Errors
**Issue**: Error messages about model loading
- **Solution**: Check internet connection
- **Solution**: Refresh the page
- **Solution**: Contact support if persistent

### Getting Help

#### Self-Service Options
1. **User Manual**: This comprehensive guide
2. **Sample Images**: Test with provided samples
3. **FAQ Section**: Common questions and answers
4. **About Page**: Technical specifications and limitations

#### Contact Support
- **Email**: support@krushiai.com
- **GitHub Issues**: Report bugs and feature requests
- **Documentation**: Additional technical resources

## Frequently Asked Questions

### General Questions

**Q: Is KrushiAI free to use?**
A: Yes, KrushiAI is open-source and free to use for agricultural purposes.

**Q: How accurate is the disease detection?**
A: The system achieves 96.5% validation accuracy on test data, but real-world performance may vary based on image quality and conditions.

**Q: Can I use KrushiAI offline?**
A: Currently, KrushiAI requires an internet connection. Offline capability is planned for future versions.

### Technical Questions

**Q: What plants are supported?**
A: KrushiAI supports 15+ crop types including apple, tomato, potato, corn, grape, and others. See the complete list in the Disease Database.

**Q: How many diseases can it identify?**
A: The current model can identify 38 different plant diseases plus healthy plant conditions.

**Q: What image formats are supported?**
A: JPG, JPEG, and PNG formats are supported. Other formats may not work properly.

**Q: Why do I get low confidence scores?**
A: Low confidence usually indicates poor image quality, unusual disease symptoms, or conditions not well-represented in training data.

### Usage Questions

**Q: Can I analyze multiple images at once?**
A: Currently, the system analyzes one image at a time. Batch processing is planned for future updates.

**Q: How should I interpret confidence scores?**
A: Scores above 80% are generally reliable. Scores below 60% suggest retaking the photo or seeking expert consultation.

**Q: Are the treatment recommendations safe to follow?**
A: The recommendations are general guidelines. Always consult agricultural experts before applying pesticides or making critical crop management decisions.

**Q: Can I save or export the results?**
A: Currently, results are displayed on-screen only. Export functionality is planned for future versions.

### Privacy Questions

**Q: Are my uploaded images stored?**
A: Images are processed temporarily and not permanently stored by the system.

**Q: Is my data shared with third parties?**
A: No, KrushiAI does not share user data or images with third parties.

---

**Need more help?** Contact our support team at support@krushiai.com or visit our documentation at docs.krushiai.com.