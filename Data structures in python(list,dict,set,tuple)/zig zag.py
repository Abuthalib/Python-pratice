def convert( s, numRows):
    if numRows == 1:
        return s
    string = ""
    step = (numRows - 1) * 2
    down = 0
    for i in range(numRows):
        if i < len(s):
            string += s[i]
        j = i
        while j < len(s):
            j += step
            if step and j < len(s):
                string += s[j]
            j += down
            if down and j < len(s):
                string += s[j]

        step -= 2
        down += 2
    return string


s = "PAYPALISHIRING"

print(convert(s,4))
