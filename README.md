# RadEx-Transform
Nonlinear Radon-based Transform

# RadEx Transform: Adaptive Nonlinear Radon-based Feature Extraction

## Overview
RadEx is a Python package implementing an adaptive, nonlinear Radon transform designed for advanced feature extraction in medical imaging applications, including chest X-ray and retinal image analysis.

## Installation
Clone the repository and install the package locally:

```bash
git clone https://github.com/your-username/RadEx-Transform.git
cd RadEx-Transform
pip install .


## Requirements
Python 3.8+

numpy

Pillow

matplotlib

pandas

To install dependencies manually:
pip install -r requirements.txt

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


## Citation
If you use RadEx in your work, please cite:
Farida Mohsen, et al., 
"Introducing Radex: Adaptive Parameterized Feature Extraction from Medical Images", 
CGI, 2024.

## License
This project is licensed under the MIT License.


License
MIT

