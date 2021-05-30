"""
 if
 if - else
 elif (def: else if)
 switch: doesn't exit

 Logic operators: and, or, in
 Comparators: ==, >, >=, <, <=
"""
def evaluation(score):
    assessment = "pass"
    if score < 5:
        assessment = "fail"
    return assessment

exam = float(input("What did you get in your exam?"))
print(evaluation(exam))

"""

"""