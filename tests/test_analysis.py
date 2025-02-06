import pytest
from photo_analyzer.analysis import scene, object_detection, blip

class TestSceneAnalysis:
    """Test suite for scene analysis functionality."""
    
    def test_scene_detection(self, test_image):
        """Test that scene detection returns expected categories."""
        detector = scene.SceneDetector()
        results = detector.analyze(test_image)
        assert isinstance(results, list)
        assert len(results) > 0
        assert all(isinstance(x, str) for x in results)
        
    def test_invalid_image_path(self):
        """Test handling of invalid image paths."""
        detector = scene.SceneDetector()
        with pytest.raises(FileNotFoundError):
            detector.analyze("nonexistent.jpg")

class TestObjectDetection:
    """Test suite for object detection functionality."""
    
    def test_object_detection(self, test_image):
        """Test that object detection returns valid results."""
        detector = object_detection.ObjectDetector()
        results = detector.detect(test_image)
        assert isinstance(results, list)
        assert all(isinstance(x, dict) for x in results)
        
    def test_confidence_threshold(self, test_image):
        """Test that confidence threshold filters results properly."""
        detector = object_detection.ObjectDetector(confidence_threshold=0.9)
        results = detector.detect(test_image)
        assert all(x['confidence'] >= 0.9 for x in results)

class TestBlipAnalysis:
    """Test suite for BLIP image captioning."""
    
    def test_image_captioning(self, test_image):
        """Test that image captioning generates valid descriptions."""
        captioner = blip.BlipCaptioner()
        caption = captioner.generate_caption(test_image)
        assert isinstance(caption, str)
        assert len(caption) > 0

