import unittest
from datetime import datetime
from io import StringIO
from unittest.mock import patch
from log_parser_batch import parse_line, validate_datetime, filter_connections, print_connections

class TestLogParser(unittest.TestCase):
    def test_parse_line(self):
        line = "1565733435250 Sukayna Maryhannah"
        timestamp, source, destination = parse_line(line)
        self.assertEqual(timestamp, 1565733435250)
        self.assertEqual(source, "Sukayna")
        self.assertEqual(destination, "Maryhannah")

    def test_validate_datetime_valid(self):
        valid_datetime = "2023-08-24 12:00:00"
        self.assertIsNone(validate_datetime(valid_datetime))

    def test_validate_datetime_invalid(self):
        invalid_datetime = "2023-08-24T12:00:00"
        with self.assertRaises(ValueError):
            validate_datetime(invalid_datetime)

    def test_filter_connections(self):
        connections = [
            (datetime(2023, 8, 24, 10, 0, 0), "Source1", "Target"),
            (datetime(2023, 8, 24, 11, 0, 0), "Source2", "Target"),
            (datetime(2023, 8, 24, 12, 0, 0), "Source3", "OtherTarget"),
        ]
        init_time = datetime(2023, 8, 24, 10, 30, 0)
        end_time = datetime(2023, 8, 24, 11, 30, 0)
        target_hostname = "Target"
        filtered_connections = filter_connections(connections, init_time, end_time, target_hostname)
        self.assertEqual(len(filtered_connections), 1)
        self.assertEqual(filtered_connections[0][1], "Source2")

    @patch("sys.stdout", new_callable=StringIO)
    def test_print_connections(self, mock_stdout):
        connections = [
            (datetime(2023, 8, 24, 10, 0, 0), "Source1"),
            (datetime(2023, 8, 24, 11, 0, 0), "Source2"),
        ]
        init_time = datetime(2023, 8, 24, 10, 0, 0)
        end_time = datetime(2023, 8, 24, 11, 30, 0)
        target_hostname = "Target"
        print_connections(connections, init_time, end_time, target_hostname)
        expected_output = (
            "Printing connections TO the host Target in the period from 2023-08-24 10:00:00 to 2023-08-24 11:30:00\n"
            "Timestamp            From Host           \n"
            "========================================\n"
            "2023-08-24 10:00:00  Source1             \n"
            "2023-08-24 11:00:00  Source2             \n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
