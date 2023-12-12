text = "стоит строй на улице"
list_text = list(text)
res_text = ''
count = 0
for i in range(0,len(list_text)):
    if list_text[i] == 'с':
        list_text[i] = ''
       
for i in range(0, len(text)):
    if text[i] == 'с':
        count +=1
for i in list_text:
    res_text += i
print(res_text,count)


        

        
