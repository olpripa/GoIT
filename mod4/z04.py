def get_grade(key):
    ects_bal = {"F": 1,
                "FX": 2,
                "E": 3,
                "D": 3,
                "C": 4,
                "B": 5,
                "A": 5}
    return ects_bal.get(key)

def get_description(key):
    ects_p = {"F": "Unsatisfactorily",
              "FX": "Unsatisfactorily",
              "E": "Enough",
              "D": "Satisfactorily",
              "C": "Good",
              "B": "Very good",
              "A": "Perfectly"}
    return ects_p.get(key)

print(get_grade("B"))
print(get_description("B"))
