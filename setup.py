from setuptools import setup, find_packages

setup(
    name='RadEx',
    version='1.0.0',
    author='Farida Mohsen',
    author_email='faridamhsen91@gmail.com',
    description='Nonlinear Radon-based Transform for Medical Image Feature Extraction',
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
    ],
    python_requires='>=3.8',
)
