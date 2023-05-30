from django.shortcuts import render
from ruleengine.rules import *
# Create your views here.
from django.http import HttpResponse
import rule_engine
from rule_engine import Rule

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")



def index(request):
    # Create an instance of the rule engine
    

    # Create a rule to match a literal first name and apply a regex to the email
   


    # Check if the rule matches the JSON data
    
    data3 = {
    'first_name': 'Luke walker',
    'last_name': 'Skywalker',
    'email': 'luke@rebels.org',
    'age': 25,
    'title': 'Harry Potter',
    'released': '01-02-2002',
    'publisher': 'JK Rowling',
    'issue' : 0,
    't_no_articles': None,
    'volume_number': 'ejwhfje',
    'publication_month' : 10,
    'publication_year': '01-01-2023'
    }
    
    res = rulescript(data3)
   
    
    print(res)
    # Access the results
    results = res
    
    output = [{rule1 : res[1]},{rule2: res[2]}]
    return render(request, 'test.html', {'output' : output})


