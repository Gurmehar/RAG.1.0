import json
from pathlib import Path
DATA_SET_PATH=Path("evaluation/qa_dataset.jsonl")

def test_data_set_file_exists():
    assert DATA_SET_PATH.exists(), f"Data set file does not exist at {DATA_SET_PATH}"

def test_data_set_file_is_valid_jsonl():
    with DATA_SET_PATH.open(encoding="utf-8") as f:
        for line_number,line in enumerate(f,start=1):
            if(line.strip()): # skip line is empty
                try:
                    json.loads(line)
                except json.JSONDecodeError as e:
                    raise AssertionError(f"Line {line_number} in data set file is not valid JSON: {e}")
            