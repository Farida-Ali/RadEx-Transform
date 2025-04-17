import unittest
from radex.radex import generate_radex_image
from PIL import Image

class TestRadEx(unittest.TestCase):
    
    def test_output_type(self):
        image_path = 'examples/test1.png'
        result = generate_radex_image(image_path)
        self.assertIsInstance(result, Image.Image)

    def test_output_size(self):
        image_path = 'examples/sample_image.png'
        result = generate_radex_image(image_path, resize_dim=(512, 512))
        self.assertEqual(result.size, (512, 512))

if __name__ == '__main__':
    unittest.main()
