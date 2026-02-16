# KrushiAI Deployment Guide

## 🚀 Streamlit Cloud Deployment

This guide will help you successfully deploy your KrushiAI plant disease detection app to Streamlit Cloud.

## 🔧 Pre-Deployment Checklist

### 1. Run Health Check
Before deploying, always run the health check script:

```bash
python health_check.py
```

This will verify all dependencies and files are correct.

### 2. Test Locally
Test the Streamlit app locally:

```bash
python test_streamlit.py
```

Or manually run:

```bash
streamlit run main.py
```

### 3. Verify Files
Ensure these critical files are present:
- ✅ `main.py` (main application)
- ✅ `utils.py` (utility functions)
- ✅ `disease_info.py` (disease database)
- ✅ `requirements.txt` (dependencies)
- ✅ `trained_plant_disease_model.keras` (AI model)
- ✅ `training_hist.json` (training history)
- ✅ `.streamlit/config.toml` (Streamlit config)

## 🛠 Fixed Issues

### Problem 1: Connection Refused (Port 8501)
**Solution**: Simplified Streamlit configuration
- Removed custom port settings
- Set `headless = true`
- Reduced logging level to `warning`

### Problem 2: Import Errors
**Solution**: Added comprehensive error handling
- Import errors are caught and displayed clearly
- Fallback mechanisms for missing modules
- Better debugging information

### Problem 3: Model Loading Failures
**Solution**: Enhanced model loading
- File existence checks before loading
- File size validation
- Detailed error messages with troubleshooting tips

### Problem 4: TensorFlow Compatibility
**Solution**: Updated requirements.txt
- Fixed exact version numbers
- Added missing `scikit-learn`
- Synchronized with Streamlit Cloud environment

## 📋 Deployment Steps

### 1. Push to GitHub
```bash
git add .
git commit -m "Fix deployment issues - add error handling and debugging"
git push origin main
```

### 2. Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect your GitHub repository
3. Set deployment settings:
   - **Main file**: `main.py`
   - **Python version**: 3.11 (recommended)
   - **Branch**: `main`

### 3. Monitor Deployment
Watch the deployment logs for:
- ✅ Dependencies installation
- ✅ Model file loading
- ✅ App startup
- ✅ Health check passing

## 🐛 Troubleshooting Common Issues

### Issue: "Model file not found"
**Cause**: The `.keras` model file wasn't uploaded to GitHub
**Solution**: 
1. Check if the file is in `.gitignore`
2. Use Git LFS for large files:
   ```bash
   git lfs track "*.keras"
   git add .gitattributes
   git add trained_plant_disease_model.keras
   git commit -m "Add model file with Git LFS"
   git push
   ```

### Issue: "Import errors"
**Cause**: Missing dependencies or version conflicts
**Solution**: 
1. Verify `requirements.txt` has all packages
2. Use exact version numbers (not ranges)
3. Test locally first

### Issue: "TensorFlow not loading"
**Cause**: Version incompatibility with Python 3.13
**Solution**: 
1. Set Python version to 3.11 in Streamlit Cloud
2. Update TensorFlow to compatible version

### Issue: "Memory issues"
**Cause**: Large model file or memory-intensive operations
**Solution**: 
1. Use model caching (`@st.cache_resource`)
2. Optimize image preprocessing
3. Consider model quantization

### Issue: "Slow startup"
**Cause**: Large dependencies and model loading
**Solution**: 
1. This is normal for first deployment
2. Subsequent starts will be faster due to caching
3. Consider using lighter model if needed

## 🔍 Debugging Tools

### 1. Health Check Script
```bash
python health_check.py
```
Checks all dependencies and files.

### 2. Local Testing
```bash
python test_streamlit.py
```
Tests app startup and basic functionality.

### 3. Streamlit Cloud Logs
Monitor the deployment logs in Streamlit Cloud dashboard for detailed error information.

### 4. Built-in Error Handling
The app now includes comprehensive error handling that shows:
- Import errors with solutions
- Model loading issues with troubleshooting
- File missing errors with file lists
- System information for debugging

## 🎯 Performance Optimization

### 1. Caching
- Model loading is cached with `@st.cache_resource`
- Image processing results can be cached
- Disease information is cached

### 2. Memory Management
- Models are loaded once and reused
- Images are processed in batches
- Temporary files are cleaned up

### 3. User Experience
- Loading spinners for long operations
- Progress bars for processing
- Clear error messages with solutions

## 🔐 Security Considerations

### 1. File Upload Security
- File type validation
- File size limits (200MB max)
- Temporary file cleanup

### 2. Model Security
- Model file integrity checks
- Safe model loading practices
- Error handling without exposing internals

## 📚 Resources

- [Streamlit Cloud Documentation](https://docs.streamlit.io/streamlit-cloud)
- [Git LFS Guide](https://git-lfs.github.io/)
- [TensorFlow Compatibility Guide](https://www.tensorflow.org/install)

## 💡 Tips for Success

1. **Always test locally first** before deploying
2. **Use exact version numbers** in requirements.txt
3. **Monitor deployment logs** carefully
4. **Keep model files under 100MB** when possible
5. **Use Git LFS for large files**
6. **Test with different image types** after deployment

## 🆘 Getting Help

If you continue to face issues:

1. Check the health check output
2. Review Streamlit Cloud deployment logs
3. Test locally with the exact same environment
4. Check GitHub repository for missing files
5. Verify all dependencies are correctly specified

---

**Last Updated**: September 2025  
**Tested With**: Python 3.11, Streamlit 1.49.1, TensorFlow 2.20.0