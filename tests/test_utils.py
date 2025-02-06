import pytest
from photo_analyzer.utils import image, file_ops

class TestImageUtils:
    """Test suite for image utility functions."""
    
    def test_image_loading(self, test_image):
        """Test image loading functionality."""
        img = image.load_image(test_image)
        assert img is not None
        
    def test_image_resizing(self, test_image):
        """Test image resizing functionality."""
        img = image.load_image(test_image)
        resized = image.resize_image(img, (224, 224))
        assert resized.size == (224, 224)

class TestFileOperations:
    """Test suite for file operation utilities."""
    
    def test_file_extension_check(self):
        """Test file extension validation."""
        assert file_ops.is_valid_image("test.jpg")
        assert file_ops.is_valid_image("test.jpeg")
        assert file_ops.is_valid_image("test.png")
        assert not file_ops.is_valid_image("test.txt")
        
    def test_file_path_normalization(self):
        """Test path normalization functionality."""
        path = file_ops.normalize_path("folder/../test.jpg")
        assert str(path) == "test.jpg"

