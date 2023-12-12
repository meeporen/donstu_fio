text = "фвап123 йуывфка2456" 
num = []
i = 0  
 
while i < len(text):
    s_int = ''
    while i < len(text) and '0' <= text[i] <= '9':
        s_int += text[i]
        i += 1
    i += 1
    if s_int != '':
        num.append(int(s_int))
 
print(max(num))
