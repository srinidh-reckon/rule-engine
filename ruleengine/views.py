from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import rule_engine
from rule_engine import Rule

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")



def index(request):
    # Create an instance of the rule engine
    

    # Create a rule to match a literal first name and apply a regex to the email
    rule = rule_engine.Rule(
        'first_name.length > 5 and age > 16'
        
    )
    print(rule)
    # Create a rule with dyanmic functionality and it can acheived using f strings
    i = 10
    rule1 = rule_engine.Rule(
        f'first_name.length > 5 and age < {i}'
    
    )

    # Check if the rule matches the JSON data
    data1 = {
        'first_name': 'Luke walker',
        'last_name': 'Skywalker',
        'email': 'luke@rebels.org',
        'age': 25
    }
    data2 = {
        'first_name': 'Luke',
        'last_name': 'Vader',
        'email': 'dvader@rebels.org',
        'age': 1
    }

    match1 = rule.matches(data1)
    match2 = rule.matches(data2)

    match11 = rule1.matches(data1)
    match21 = rule1.matches(data2)

    print(match1)  # True
    print(match2)  # False
    # engine = rule_engine.engine()
    # engine.matches(rule1)
    
    print(match21)
    # Access the results
    results = [match1,match2]
    rules = [rule,rule1]
    output = [{rule : match1},{rule1: match2}]
    return render(request, 'test.html', {'output' : output})


