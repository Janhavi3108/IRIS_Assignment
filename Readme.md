# IRIS Assignment - FastAPI Excel Processor

This project is a solution for the assignment from IRIS Business Services Limited. It demonstrates how to build a FastAPI application that:

- Parses data from an Excel sheet (capbudg.xlsx)
- Exposes RESTful API endpoints to list tables, row details, and compute row sums

## Tech Stack
- Python 3.9+
- FastAPI
- Pandas
- Uvicorn
- OpenPyXL

## Project Structure

```
IRIS_Assignment/
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI app runner
│   ├── routes.py           # Endpoint definitions
│   └── services.py         # Business logic
├── Data/
│   └── capbudg.xlsx        # Input Excel sheet
└── requirements.txt        # Python dependencies
```

## How to Run Locally

### 1. Clone the repository
```
git clone https://github.com/Janhavi3108/IRIS_Assignment.git
cd IRIS_Assignment
```

### 2. Create virtual environment & install dependencies
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Start the server
```
uvicorn app.main:app --reload --port 9090
```

### 4. Access Swagger UI:

- URL: http://localhost:9090/docs

## API Endpoints

### 1. GET /list_tables
- Returns a list of logical table names extracted from the Excel sheet.
```
{
  "tables": [
    "Initial Investment",
    "Working Capital",
    "Growth Rates",
    "Fixed Expenses",
    "Salvage Value",
    "Operating Cashflows"
  ]
}
```
### 2. GET /get_table_details?table_name= Initial Investment
- Returns the row names (first column values) for a selected table.
```
{
  "table_name": " Initial Investment",
  "row_names": ["Tax Credit (if any )="]
}
```
### 3. GET /row_sum?table_name= Initial Investment &row_name= Tax Credit (if any )=
- Returns the sum of all numeric values in the specified row.
```
{
  "table_name": " Initial Investment",
  "row_name": " Tax Credit (if any )= ",
  "sum": 0.4
}
```
- Percentage-typed cells (like 10%) are treated as 0.10 in Excel and will be summed accordingly.

## Potential Improvements
- Add schema validation using `pydantic` to ensure the uploaded file has expected columns, datatypes, and no critical nulls before processing.

## Missed Edge Cases
- Data Type Mismatch
   - A column like price contains "10k" or "Not Available" instead of numbers.
   - Summarization or calculations will fail or return incorrect results.
   - Fix: Cast and validate columns, and skip/report rows with type mismatches.

## Postman Collection
Included as a JSON file: Postman_Collection.json

Import this into Postman to test all endpoints with localhost:9090 as base URL.

## Technical Notes

- This app supports only `.xlsx` files.
- `.xls` files are not supported due to compatibility issues with modern libraries (`pandas` dropped default support for `.xls` via `xlrd`).
- Users are encouraged to convert older Excel files to `.xlsx` before uploading.

## Author
- Submitted by: Janhavi Panvekar
- For: IRIS Business Services Ltd

