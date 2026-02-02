import base64
import csv
import io

def decode_base64_csv(base64_string: str):
    # Decode base64 → bytes
    decoded_bytes = base64.b64decode(base64_string)

    # Bytes → string
    csv_text = decoded_bytes.decode("utf-8")

    return csv_text


def parse_csv(csv_text: str):
    reader = csv.DictReader(io.StringIO(csv_text))

    data = [row for row in reader]
    columns = reader.fieldnames or []

    return data, columns