# Excel A3 Format Consolidator

This application consolidates Excel files in A3 format by extracting all rows with "Fecha" and "Asiento" data and combining them into a master sheet.

## Features

- GUI interface for easy file selection
- Processes all sheets in the Excel file
- Preserves original sheets in the output file
- Creates a "master" sheet with all consolidated data
- Adds sheet origin tracking for each row

## Requirements

- Python 3.7+
- pandas
- openpyxl
- tkinter (usually included with Python)

## Usage

### Windows
1. Double-click `run_excel_consolidator.bat` to start the application
2. Click "Browse Input File" to select your A3 format Excel file
3. Click "Browse Output File" to choose where to save the consolidated file
4. Click "Process Files" to consolidate the data

### Manual Installation
```bash
pip install pandas openpyxl
python excel_consolidator.py
```

## How it Works

1. The application reads each sheet in the input Excel file
2. Identifies the header row containing "Fecha" and "Asiento" columns
3. Extracts all rows that have values in both Fecha and Asiento columns
4. Combines all valid rows from all sheets into a master sheet
5. Creates an output file with:
   - All original sheets (preserved as-is)
   - A new "master" sheet with consolidated data
   - Sheet origin tracking for each consolidated row

## A3 Format Support

The application automatically detects the A3 format structure where:
- Header information is at the top of each sheet
- The actual data table starts after several header rows
- Column headers include "Fecha" and "Asiento"
- Data rows contain accounting entries with dates and entry numbers

## File Structure

- `excel_consolidator.py` - Main GUI application
- `test_consolidator.py` - Command-line testing version
- `requirements.txt` - Python dependencies
- `run_excel_consolidator.bat` - Windows batch file for easy execution