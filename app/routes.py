from fastapi import APIRouter, Query, HTTPException
from app.services import get_table_names, get_table_details, get_row_sum

router = APIRouter()

@router.get("/list_tables")
def list_tables():
    return {"tables": get_table_names()}

@router.get("/get_table_details")
def get_table_details_endpoint(table_name: str = Query(...)):
    try:
        rows = get_table_details(table_name)
        return {"table_name": table_name, "row_names": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/row_sum")
def row_sum_endpoint(
    table_name: str = Query(...),
    row_name: str = Query(...)
):
    try:
        row_sum = get_row_sum(table_name, row_name)
        return {"table_name": table_name, "row_name": row_name, "sum": row_sum}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
