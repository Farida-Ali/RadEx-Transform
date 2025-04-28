# 🧠 RadEx Transform: Nonlinear Radon-based Transformation

## Overview
RadEx is a Python package implementing an adaptive, nonlinear Radon transform designed for advanced feature extraction from medical imaging applications, such as chest X-ray and retinal image analysis.

## Installation
Clone the repository and install the package locally:

```bash
git clone https://github.com/Farida-Ali/RadEx-Transform.git
cd RadEx-Transform
pip install .

## Requirements
Python 3.8+
numpy
Pillow
matplotlib
pandas


## Usage Example
from radex.radex import generate_radex_image
import matplotlib.pyplot as plt

# Load and transform image
image_path = 'examples/test.png'
radex_img = generate_radex_image(image_path)

# Display transformed image
plt.imshow(radex_img, cmap='gray')
plt.title("radex_example_output")
plt.axis('off')
plt.show()


## License
MIT License.


