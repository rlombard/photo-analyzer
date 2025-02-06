import pytest
from photo_analyzer.immich_api import client, uploader

class TestImmichClient:
    """Test suite for Immich API client."""
    
    @pytest.fixture
    def mock_client(self):
        """Fixture providing a mock Immich client."""
        return client.ImmichClient(
            base_url="http://localhost:3001",
            api_key="test_key"
        )
        
    def test_client_initialization(self, mock_client):
        """Test client initialization with config."""
        assert mock_client.base_url == "http://localhost:3001"
        assert mock_client.api_key == "test_key"
        
    def test_authentication_headers(self, mock_client):
        """Test that authentication headers are properly set."""
        headers = mock_client.get_headers()
        assert 'x-api-key' in headers
        assert headers['x-api-key'] == "test_key"

class TestImmichUploader:
    """Test suite for Immich uploader functionality."""
    
    @pytest.fixture
    def mock_uploader(self, mock_client):
        """Fixture providing a mock uploader instance."""
        return uploader.ImmichUploader(client=mock_client)
        
    def test_upload_photo(self, mock_uploader, test_image):
        """Test photo upload functionality."""
        result = mock_uploader.upload(test_image)
        assert result is not None
        
    def test_upload_batch(self, mock_uploader, test_image):
        """Test batch upload functionality."""
        images = [test_image] * 3
        results = mock_uploader.upload_batch(images)
        assert len(results) == 3

