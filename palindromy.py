def word_checker(txt):
    return txt == txt[::-1]

txt = "rower"
ans = word_checker(txt)

if ans: 
    print(True)
else: 
    print(False)