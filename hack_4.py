"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    if len(result) == 0: 
        return result
    return result[:-1] + result[-1].upper()