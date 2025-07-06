"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    palabra = "fooziman"
    palabra = palabra.upper()
    palabra = palabra.replace('O', '0')
    palabra = palabra.replace('I', '1')
    palabra = palabra.replace('A', '@')
    return list(palabra)