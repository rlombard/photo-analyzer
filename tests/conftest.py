import pytest
from pathlib import Path

@pytest.fixture
def test_image():
    """Fixture providing a test image path for testing purposes.
    
    Returns:
        Path: Path object pointing to a test image file
    """
    return Path("tests/data/test_image.jpg")

