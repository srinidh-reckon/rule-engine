import rule_engine
from rule_engine import Rule

import time
from datetime import date
# making sure the type is fixed
def type_resolver(name):
    if name == 'title':
        return rule_engine.DataType.STRING
    elif name == 'publisher':
        return rule_engine.DataType.STRING
    elif name == 'issue':
        return rule_engine.DataType.FLOAT
    elif name == 'released':
        return rule_engine.DataType.DATETIME
    # if the name is none of those, raise a SymbolResolutionError
    raise rule_engine.errors.SymbolResolutionError(name)

context = rule_engine.Context(type_resolver=type_resolver)
# Create a rule for using context types
rule = rule_engine.Rule(
    'issue > 1',context=context
    
)

# Create a rule with dyanmic functionality and it can acheived using f strings
i = 4 
attr = 'volume_number'

rule1 = rule_engine.Rule(
    f'{attr}.length > {i}'
    
)

rule2 = rule_engine.Rule(
    't_no_articles ==  null' 
)

rule3 = rule_engine.Rule(
    'publication_month >= 1 and publication_month <= 12'
)

# rule4 = rule_engine.Rule(
#     'publication_year == datetime.year'
# )

# rule_5 = rule_engine.Rule(
#     ''
# )

# Check if the rule matches the JSON data
data1 = {
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
data2 = {
    'first_name': 'Luke jeffery',
    'last_name': 'Vader',
    'email': 'dvader@rebels.org',
    'age': 1,
    'title': 'Harry Potter 1',
    'released': '07-07-2002',
    'publisher': 'JK Rowling uehfuh',
    'issue' : 5,
    'volume_number' : 'nejnjkenkf'
}

# match1 = rule.matches(data1)
# match2 = rule.matches(data2)

match11 = rule2.matches(data1) # Checks for firstname length > 5 and the age < 10
match21 = rule1.matches(data2)

print(match11)  # False
print(match21)  # True

def rulescript(data):
    a = rule.matches(data)
    b = rule1.matches(data)
    c = rule2.matches(data)
    d = rule3.matches(data)

    return [a,b,c,d]