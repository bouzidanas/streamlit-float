from setuptools import setup, find_packages

setup(
    name='streamlit-float',
    version='0.1.0',
    author='Anas Bouzid',
    author_email='anasbouzid@gmail.com',
    description='A simple module for fixing the vertical position of Streamlit containers relative to viewport instead of page',
    url="https://github.com/bouzidanas/streamlit.io/tree/dev/streamlit-float",
    packages=find_packages(),
    classifiers=[],
    python_requires='>=3.6',
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)