from typing import Any

def is_int(raw_variable:Any)->bool:
    if not (isinstance (raw_variable,int) and not isinstance(raw_variable,bool)):
        return False
    return True

def is_positive_int(integer:int)->bool:
    if not is_int(integer):
        return False
    if not integer > 0:
        return False
    return True

def int_in_list(number:int,number_list:list[int]):
    if not is_int(number):
        return False
    return number in number_list
    