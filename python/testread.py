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
    def test_check_num(self, mock_connect):
        conn = mock.MagicMock()
        cursor = mock.MagicMock()
        mock_connect.return_value = conn
        conn.cursor.return_value = cursor

        tables = ['cpu', 'mem', 'disk']
        for table in tables:
            cursor.fetchone.return_value = (25,)
            cursor.execute.reset_mock()

        readstats.check_num(conn, *tables)

        expected_calls = [mock.call(f"DELETE FROM {table_name} ORDER BY id LIMIT 1;") for table_name in tables]
        cursor.execute.assert_has_calls(expected_calls, any_order=True)
        

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

        readstats.insert_data_into_table(conn, "cpu", 50.0, "12:00:00")

        cursor.execute.assert_called_once_with("INSERT INTO cpu (time,value) VALUES (%s, %s)", ("12:00:00",50.0))

   
if __name__ == '__main__':
    unittest.main()
