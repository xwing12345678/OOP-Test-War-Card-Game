from typing import Sequence,Literal

def is_non_empty_string(raw_string:str)->bool:
    striped_string = raw_string.strip()
    if not striped_string:
        return False
    return True

def in_literal_list(selection:str, literal_list:Sequence[str|Literal[None]])->bool:
    if not is_non_empty_string(selection):
        return False
    return selection in literal_list

