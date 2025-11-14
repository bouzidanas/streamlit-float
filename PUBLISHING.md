# Publishing to PyPI

This guide explains how to publish new versions of `streamlit-float` to PyPI.

## Quick Publishing Steps

1. **Setup Authentication**: Create API token at https://pypi.org/manage/account/token/
2. **Add token to `.env` file**:
   ```bash
   export PYPI_API=your_api_token_here
   ```
3. **Load environment variables**:
   ```bash
   source .env
   ```
4. **Remove old build files**:
   ```bash
   rm -rf dist/ build/ streamlit_float.egg-info/
   ```
5. **Update version in `setup.py`**:
   ```python
   version="0.4.1",  # Increment this
   ```
6. **Build distribution files**:
   ```bash
   python setup.py sdist bdist_wheel
   ```
7. **Upload to PyPI**:
   ```bash
   twine upload --username __token__ --password $PYPI_API dist/*
   ```

## Prerequisites

1. **PyPI Account**: Make sure you have an account at https://pypi.org/
2. **API Token**: Create an API token at https://pypi.org/manage/account/token/
   - Go to PyPI account settings
   - Create a new API token
   - Scope it to the `streamlit-float` project (recommended) or your entire account
   - Copy the token (starts with `pypi-`)

## Setup

### 1. Install Required Tools
```bash
pip install twine build
```

### 2. Configure Authentication

**Option A: Environment Variables (Recommended)**
Create/update `.env` file in the project root:
```bash
export PYPI_API=your_api_token_here
```

Then load it:
```bash
source .env
```

**Option B: Create ~/.pypirc**
```ini
[distutils]
index-servers = pypi

[pypi]
username = __token__
password = your_api_token_here
```

## Publishing Process

### 1. Update Version
Update the version number in `setup.py`:
```python
setup(
    name="streamlit-float",
    version="0.4.1",  # Update this
    # ...
)
```

### 2. Clean Previous Builds
```bash
rm -rf dist/ build/ *.egg-info/
```

### 3. Build Distribution Files
```bash
python setup.py sdist bdist_wheel
```

This creates files in the `dist/` directory:
- `streamlit_float-X.X.X.tar.gz` (source distribution)
- `streamlit_float-X.X.X-py3-none-any.whl` (wheel distribution)

### 4. Test Upload (Optional)
Test on TestPyPI first:
```bash
twine upload --repository testpypi dist/*
```

### 5. Upload to PyPI
```bash
# If using environment variables:
twine upload --username __token__ --password $PYPI_API dist/*

# If using ~/.pypirc:
twine upload dist/*

# If entering credentials manually:
twine upload --username __token__ dist/*
# (will prompt for password - enter your API token)
```

### 6. Verify Upload
- Check the package page: https://pypi.org/project/streamlit-float/
- Test installation: `pip install streamlit-float==X.X.X`

## Common Issues and Solutions

### Authentication Errors
**Error**: `HTTPError: 403 Forbidden` or `Invalid or non-existent authentication information`

**Solutions**:
- Make sure your API token is correct and not expired
- Use `__token__` as username (literally, not your PyPI username)
- Ensure the token has the right scope (project or account)

### Wrong Command Syntax
**Error**: `unrecognized arguments` or `Missing section from ~/.pypirc`

**Wrong**:
```bash
twine upload --repository https://upload.pypi.org/legacy/ streamlit-float
```

**Correct**:
```bash
twine upload dist/*
# OR
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

### File Not Found
**Error**: Files not found or no distributions found

**Solution**: Make sure you're uploading from `dist/*` not the package name:
```bash
# Wrong
twine upload streamlit-float

# Correct  
twine upload dist/*
```

### Version Already Exists
**Error**: `File already exists`

**Solutions**:
- Increment the version number in `setup.py`
- Use `--skip-existing` flag (not recommended for production)

## Environment Variables Format

Make sure your `.env` file uses the correct format:

**Wrong**:
```bash
PYPI_API = pypi-your-token-here
```

**Correct**:
```bash
export PYPI_API=pypi-your-token-here
```

## Security Notes

- **Never commit `.env` files** - they contain sensitive API tokens
- Add `.env` to your `.gitignore` file
- Rotate API tokens regularly
- Use project-scoped tokens when possible
- Consider using CI/CD for automated publishing

## Quick Reference

Complete publishing workflow:
```bash
# 1. Update version in setup.py
# 2. Clean and build
rm -rf dist/ build/ *.egg-info/
python setup.py sdist bdist_wheel

# 3. Load credentials
source .env

# 4. Upload
twine upload --username __token__ --password $PYPI_API dist/*

# 5. Verify at https://pypi.org/project/streamlit-float/
```

## Troubleshooting

If you encounter issues:
1. Use `--verbose` flag with twine for detailed error information
2. Check that all required files are in `dist/` directory
3. Verify your API token is correct and has proper permissions
4. Ensure version number in `setup.py` is incremented from the last release