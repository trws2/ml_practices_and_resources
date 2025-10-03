import re
import string
import json
from typing import List, Dict, Any

def remove_punc(s: str) -> str:
    pattern = r'[%s]' % re.escape(string.punctuation)
    return re.sub(pattern, "", s)

def write_jsonl(input_list: List[Dict[str, Any]], output_filepath) -> None:
    output_list = [json.dumps(x) + "\n" for x in input_list]
    with open(output_filepath, 'w') as f:
        f.writelines(output_list)

if __name__ == "__main__":
    print(remove_punc("This is a test! I finished it."))
    write_jsonl([{"text":"test1", "attr": 1, "metadata": {"id": 3, "v": 4}}, {"text":"test2", "attr": 2, "metadata": {"id": 5, "v": 6}}], "./test_out.jsonl")
