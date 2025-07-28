import pytest
import pandas as pd
from pathlib import Path
import sys
import os

# Add parent directory to path to import consolidator
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.consolidator import ExcelConsolidator


class TestExcelConsolidator:
    def setup_method(self):
        self.consolidator = ExcelConsolidator()

    def test_consolidator_initialization(self):
        """Test that ExcelConsolidator initializes correctly"""
        assert self.consolidator.input_file is None
        assert self.consolidator.output_file is None

    def test_find_header_row(self):
        """Test header row detection"""
        # Create a test dataframe with headers in row 2
        test_data = [
            ["", "", "", ""],
            ["", "", "", ""],
            ["Fecha", "Asiento", "Cuenta", "Importe"],
            ["2020-01-01", "001", "123", "100.00"],
        ]
        df = pd.DataFrame(test_data)

        header_row = self.consolidator.find_header_row(df)
        assert header_row == 2

    def test_find_header_row_not_found(self):
        """Test header row detection when headers are not found"""
        test_data = [
            ["", "", "", ""],
            ["Data", "Number", "Account", "Amount"],
            ["2020-01-01", "001", "123", "100.00"],
        ]
        df = pd.DataFrame(test_data)

        header_row = self.consolidator.find_header_row(df)
        assert header_row is None

    def test_find_header_row_case_insensitive(self):
        """Test header row detection works with different cases"""
        test_data = [
            ["FECHA", "ASIENTO", "CUENTA", "IMPORTE"],
            ["2020-01-01", "001", "123", "100.00"],
        ]
        df = pd.DataFrame(test_data)

        header_row = self.consolidator.find_header_row(df)
        assert header_row == 0

    def test_find_header_row_partial_match(self):
        """Test header row detection with partial matches"""
        test_data = [
            ["Fecha inicio", "Núm. Asiento", "Cuenta", "Importe"],
            ["2020-01-01", "001", "123", "100.00"],
        ]
        df = pd.DataFrame(test_data)

        header_row = self.consolidator.find_header_row(df)
        assert header_row == 0