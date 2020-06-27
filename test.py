import fitz
import re
import json
doc = fitz.open("THE.pdf")
l = []
skips = ['Solutions of Assignment (Set-2)','The Living World','Aakash Educational Services Pvt. Ltd. - Regd. Office : Aakash Tower, 8, Pusa Road, New Delhi-110005 Ph.011-47623456','Objective Type Questions','Solutions','Chapter 1']
questions = {}
options = {}
answers = {}
otpscount = 0
for page in doc:
    l= l + page.getText().split("\n")
d =False
opts = []
for i in range(len(l)):
    if l[i] == 'SECTION - D':
        d = True
    if l[i] in skips or l[i].startswith("SECTION"):
        pass
    elif re.search("\d\.",l[i]):
        if d:
            q = []
            q.append(l[i+1])
            q.append(l[i+2])
            questions[len(questions)+1] = q
            i+=2
        else:
            questions[len(questions)+1] = l[i+1]
            i+=1
    elif re.search("\(\d\)\s[a-z]*",l[i]):
        if l[i].split()[0][1] == '4':
            opts.append(l[i])
            options[otpscount] = opts
            otpscount +=1
            opts = []
        else:    
            opts.append(l[i])
    elif l[i].startswith("Sol. "):
        answers[len(answers)+1] = l[i+1]
        i+=1
data ={}
data['questions'] = questions
data['Multiple choice options'] = options
data['answer'] = answers


with open('data.json', 'a') as f:
    json.dump(data,  f,  indent=2)