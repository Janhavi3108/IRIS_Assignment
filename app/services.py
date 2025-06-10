import os
import pandas as pd
import math

EXCEL_PATH = os.path.join(os.path.dirname(__file__), "../Data/capbudg.xlsx")
SHEET_NAME = "CapBudgWS"

# Hardcoded logical table definitions: (start_row, end_row)
table_definitions = {
    "Initial Investment": (2, 8),
    "Working Capital": (11, 13),
    "Growth Rates": (17, 17),
    "Fixed Expenses": (18, 18),
    "Salvage Value": (31, 33),
    "Operating Cashflows": (35, 39)
}

def get_table_names():
    return list(table_definitions.keys())

def get_table_details(table_name: str):
    try:
        start, end = table_definitions[table_name]
        df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME, engine='openpyxl')
        table_df = df.iloc[start:end + 1]
        row_names = table_df.iloc[:, 0].dropna().astype(str).tolist()
        return row_names
    except Exception as e:
        raise Exception(f"Error reading table details: {str(e)}")

def get_row_sum(table_name: str, row_name: str):
    try:
        start, end = table_definitions[table_name]
        df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME, engine='openpyxl')
        table_df = df.iloc[start:end + 1]

        # Debugging output
        print("Available rows:", table_df.iloc[:, 0].tolist())
        print("Looking for row:", row_name.strip())

        target_row = table_df[table_df.iloc[:, 0].astype(str).str.strip() == row_name.strip()]

        if target_row.empty:
            raise Exception(f"Row '{row_name}' not found in table '{table_name}'.")

        row_data = target_row.iloc[0, 1:]  # Exclude first column (row name)
        cleaned = []
        for val in row_data:
            if isinstance(val, str) and "%" in val:
                try:
                    cleaned.append(float(val.replace("%", "").strip()))  # treat 10% as 10
                except:
                    cleaned.append(None)
            else:
                try:
                    cleaned.append(float(val))
                except:
                    cleaned.append(None)

        result = sum(filter(lambda x: x is not None and not math.isnan(x), cleaned))

        return round(result, 4)

    except Exception as e:
        raise Exception(f"Error calculating row sum: {str(e)}")