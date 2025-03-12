studentinfo = { 'stu1' :
               {'name' : ['Aadhya'],
                'class' : ['A'],
                'subject_integration' : ['maths, history, chemistry, physics, english']
                },
                'stu2' : 
                {'name' : ['Sarah'], 
                 'class' : ['E'], 
                 'subject_integration' : ['maths, integrated humanities, biology, chemistry, english']
                 }, 
                'stu3' : 
                {'name' : ['Siddhi'], 
                 'class' : ['B'], 
                 'subject_integration' : ['integrated humanities, biology, chemistry, physics, english']
                 }, 
                }
result = {}

for i,j in studentinfo.items():
    if j not in result.values():
        result[i] = j
print(result)