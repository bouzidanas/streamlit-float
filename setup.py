from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "PROJECT.md").read_text()

setup(
    name='streamlit-float',
    version='0.3.2',
    author='Anas Bouzid',
    author_email='anasbouzid@gmail.com',
    description='Fix Streamlit containers relative to viewport instead of page',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/bouzidanas/streamlit-float",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)