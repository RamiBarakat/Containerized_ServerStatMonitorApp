import unittest
import mock
import logging
import readstats

class TestReadStats(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.INFO)

    def tearDown(self):
        pass


    def test_get_system_statse(self):
        cpu_usage, memory_usage, disk_usage = readstats.get_system_stats()

        self.assertGreaterEqual(cpu_usage, 0.0)
        self.assertLessEqual(cpu_usage, 100.0)

        self.assertGreaterEqual(memory_usage, 0.0)
        self.assertLessEqual(memory_usage, 100.0)

        self.assertGreaterEqual(disk_usage, 0.0)
        self.assertLessEqual(disk_usage, 100.0)


    @mock.patch('mysql.connector.connect')
    def test_connect_to_database(self, mock_connect):
        mock_connection = mock.MagicMock()
        mock_connect.return_value = mock_connection

        conn = readstats.connect_to_database()

        self.assertEqual(conn, mock_connection)

        
    @mock.patch('mysql.connector.connect')
    def test_insert_data_into_table(self, mock_connect):
        conn = mock.MagicMock()
        cursor = mock.MagicMock()
        mock_connect.return_value = conn
        conn.cursor.return_value = cursor

        readstats.insert_data_into_table(conn, "cpu", 50.0)

        cursor.execute.assert_called_once_with("INSERT INTO cpu (value) VALUES (%s)", (50.0,))
        conn.commit.assert_called_once()
        cursor.close.assert_called_once()

   
if __name__ == '__main__':
    unittest.main()
