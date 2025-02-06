import pytest
from photo_analyzer.database import connection, queries

class TestDatabaseConnection:
    """Test suite for database connection handling."""
    
    @pytest.fixture
    def db_connection(self):
        """Fixture providing a test database connection."""
        conn = connection.create_connection(":memory:")
        yield conn
        conn.close()
        
    def test_connection_creation(self):
        """Test database connection creation."""
        conn = connection.create_connection(":memory:")
        assert conn is not None
        conn.close()
        
    def test_schema_creation(self, db_connection):
        """Test database schema creation."""
        connection.create_schema(db_connection)
        cursor = db_connection.cursor()
        # Verify tables exist
        tables = cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
        assert len(tables) > 0

class TestDatabaseQueries:
    """Test suite for database queries."""
    
    def test_insert_photo(self, db_connection):
        """Test photo insertion into database."""
        photo_data = {
            'path': 'test.jpg',
            'timestamp': '2024-01-01 12:00:00'
        }
        queries.insert_photo(db_connection, photo_data)
        result = queries.get_photo(db_connection, photo_data['path'])
        assert result is not None
        
    def test_update_photo(self, db_connection):
        """Test photo update in database."""
        photo_data = {
            'path': 'test.jpg',
            'timestamp': '2024-01-01 12:00:00'
        }
        queries.insert_photo(db_connection, photo_data)
        updated_data = {'caption': 'Test caption'}
        queries.update_photo(db_connection, photo_data['path'], updated_data)
        result = queries.get_photo(db_connection, photo_data['path'])
        assert result['caption'] == updated_data['caption']

