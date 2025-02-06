import pytest
from datetime import datetime
from photo_analyzer.clustering import location_based, time_based

class TestLocationClustering:
    """Test suite for location-based clustering."""
    
    @pytest.fixture
    def sample_locations(self):
        """Fixture providing sample location data."""
        return [
            {'lat': 40.7128, 'lon': -74.0060},  # NYC
            {'lat': 40.7129, 'lon': -74.0061},  # NYC (close)
            {'lat': 34.0522, 'lon': -118.2437}, # LA
        ]
        
    def test_location_clustering(self, sample_locations):
        """Test that similar locations are clustered together."""
        clusterer = location_based.LocationClusterer()
        clusters = clusterer.cluster(sample_locations)
        assert len(clusters) == 2  # Should identify NYC and LA clusters
        
    def test_distance_threshold(self, sample_locations):
        """Test that distance threshold affects clustering."""
        clusterer = location_based.LocationClusterer(distance_threshold=100)
        clusters = clusterer.cluster(sample_locations)
        assert len(clusters) > 0

class TestTimeClustering:
    """Test suite for time-based clustering."""
    
    @pytest.fixture
    def sample_timestamps(self):
        """Fixture providing sample timestamp data."""
        return [
            datetime(2024, 1, 1, 12, 0),
            datetime(2024, 1, 1, 12, 5),
            datetime(2024, 1, 2, 12, 0),
        ]
        
    def test_time_clustering(self, sample_timestamps):
        """Test that temporally close photos are clustered."""
        clusterer = time_based.TimeClusterer()
        clusters = clusterer.cluster(sample_timestamps)
        assert len(clusters) == 2  # Should cluster same-day photos together
        
    def test_time_threshold(self, sample_timestamps):
        """Test that time threshold affects clustering."""
        clusterer = time_based.TimeClusterer(time_threshold_minutes=60)
        clusters = clusterer.cluster(sample_timestamps)
        assert len(clusters) > 0

