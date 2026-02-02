from fastapi import FastAPI, HTTPException
from app.schemas import CSVRequest, CSVResponse, Meta
from app.utils import decode_base64_csv, parse_csv

app = FastAPI(title="Base64 CSV to JSON API")

@app.post("/csv-to-json", response_model=CSVResponse)
def csv_to_json(payload: CSVRequest):
    try:
        csv_text = decode_base64_csv(payload.file_base64)
        data, columns = parse_csv(csv_text)

        if not data:
            raise ValueError("CSV contains no rows")

        return {
            "status": "success",
            "meta": {
                "rows": len(data),
                "columns": columns
            },
            "data": data
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))