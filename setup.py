from setuptools import setup, find_packages

setup(
    name='RadEx',
    version='1.0.0',
    author='Farida Mohsen',
    author_email='your.email@domain.com',  # replace with your actual email
    description='A Python package for  Nonlinear Radon-based Transform',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/RadEx-Transform',  # Replace with your actual GitHub URL
    packages=find_packages(),
    install_requires=[
        'numpy',
        'Pillow',
        'matplotlib',
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Image Processing'
    ],
    python_requires='>=3.8',
)
