
def snakecase(s):
    result = ""
    for ch in s:
        if ch.isupper():
            result += f"_{ch.lower()}"
        else:
            result += ch
    return result
    
s = "getHTTPResponse"
print(snakecase(s))