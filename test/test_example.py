import os
import shutil

from src.BingImageCreator import ImageGen


def test_save_images():
    # create a temporary output directory for testing purposes
    test_output_dir = "test_output"
    os.mkdir(test_output_dir)
    # download a test image
    test_image_url = "https://picsum.photos/200"
    gen = ImageGen(auth_cookie="")
    gen.save_images([test_image_url], test_output_dir)
    gen.save_images([test_image_url], test_output_dir, file_name="test_image")
    # check if the image was downloaded and saved correctly
    assert os.path.exists(os.path.join(test_output_dir, "test_image_0.jpeg"))
    assert os.path.exists(os.path.join(test_output_dir, "0.jpeg"))
    # remove the temporary output directory
    shutil.rmtree(test_output_dir)
