from radex.radex import generate_radex_image
import matplotlib.pyplot as plt

# Provide the path to your image clearly
image_path = 'examples/test.png'


# Generate RadEx transformed image
radex_img = generate_radex_image(image_path)

# Display the transformed image
plt.imshow(radex_img, cmap='gray')
plt.title("RadEx Transformed Image")
plt.axis('off')
plt.savefig('radex_example_output.png')  # save image
plt.show()
