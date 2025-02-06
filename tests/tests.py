import pytest
from unittest.mock import patch, MagicMock
from PIL import Image

from analysis.blip import analyze_caption
from analysis.scene import analyze_scene
from analysis.object import analyze_object
from database.connection import get_connection, release_connection
from immich_api.client import fetch_images
from immich_api.uploader import upload_metadata
from utils.geocode import reverse_geocode
from utils.helpers import format_album_name

@pytest.fixture(scope="module")
def test_image():
    """Fixture to provide a test image"""
    return Image.new("RGB", (100, 100), "white")  # Mocked blank image

@patch("analysis.blip.processor")
@patch("analysis.blip.model")
def test_blip_captioning(mock_model, mock_processor, test_image):
    """ Test BLIP captioning with a mocked model """
    mock_processor.return_value = MagicMock()
    mock_model.generate.return_value = [[1234]]  # Mock token ID
    mock_processor.batch_decode.return_value = ["Mocked Caption"]

    caption = analyze_caption(test_image)
    assert caption == "Mocked Caption"

@patch("analysis.scene.feature_extractor")
@patch("analysis.scene.model")
def test_scene_classification(mock_model, mock_feature_extractor, test_image):
    """ Test scene classification with a mocked model """
    mock_feature_extractor.return_value = MagicMock()
    mock_model.return_value.logits.argmax.return_value = 1
    mock_model.config.id2label = {1: "Mocked Scene"}

    scene = analyze_scene(test_image)
    assert scene == "Mocked Scene"

@patch("analysis.object.feature_extractor")
@patch("analysis.object.model")
def test_object_detection(mock_model, mock_feature_extractor, test_image):
    """ Test object detection with a mocked model """
    mock_feature_extractor.return_value = MagicMock()
    mock_model.return_value.logits.argmax.return_value = 2
    mock_model.config.id2label = {2: "Mocked Object"}

    detected_object = analyze_object(test_image)
    assert detected_object == "Mocked Object"

@patch("database.connection.get_connection")
def test_database_connection(mock_get_connection):
    """ Test database connection handling """
    mock_conn = MagicMock()
    mock_get_connection.return_value = mock_conn
    conn = get_connection()
    assert conn is not None
    release_connection(conn)

@patch("immich_api.client.requests.get")
def test_fetch_images(mock_requests_get):
    """ Test fetching images from Immich API """
    mock_requests_get.return_value.json.return_value = [{"id": "123", "name": "Test Image"}]
    images = fetch_images()
    assert len(images) == 1
    assert images[0]["id"] == "123"

@patch("immich_api.uploader.requests.post")
def test_upload_metadata(mock_requests_post):
    """ Test uploading metadata to Immich API """
    mock_requests_post.return_value.status_code = 200
    response = upload_metadata("123", {"tags": ["Test"]})
    assert response == 200

@patch("utils.geocode.requests.get")
def test_reverse_geocode(mock_requests_get):
    """ Test reverse geocoding API """
    mock_requests_get.return_value.json.return_value = {"address": {"city": "Test City", "country": "Test Country"}}
    location = reverse_geocode(0.0, 0.0)
    assert location == "Test City, Test Country"

@patch("utils.helpers.logger")
def test_format_album_name(mock_logger):
    """ Test album name formatting """
    formatted_name = format_album_name("Test@Album#Name!")
    assert formatted_name == "Test_Album_Name_"