from setuptools import setup, find_packages

setup(
    name='streamlit-float',
    version='0.2.5',
    author='Anas Bouzid',
    author_email='anasbouzid@gmail.com',
    description='Fix Streamlit containers relative to viewport instead of page',
    long_description="A simple module for fixing the vertical position of Streamlit containers relative to viewport instead of page",
    long_description_content_type="text/plain",
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