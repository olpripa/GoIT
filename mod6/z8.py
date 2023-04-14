list_students = [{"name": "Kovalchuk Oleksiy", "specialty": 301, "math": 175, "lang": 180, "eng": 155,},
                 {"name": "Ivanchuk Boryslav", "specialty": 101, "math": 135, "lang": 150, "eng": 165,},
                 {"name": "Karpenko Oleksandr", "specialty": 201,   "math": 155, "lang": 175, "eng": 185,},]


def save_applicant_data(source, output):
    st = ''
    for i in source:
        st += ','.join(map(str, list(i.values()))) + "\n"
    
    with open(output,'w') as fh:
            fh.write(st)
    print('Дані записані у файл')

save_applicant_data(list_students, 'test_st.txt')