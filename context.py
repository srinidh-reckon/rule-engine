import rule_engine

# comic book
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
# Create a rule to match a literal first name and apply a regex to the email
rule = rule_engine.Rule(
    'issue > 1',context=context
    
)

rule1 = rule_engine.Rule(
    'first_name.length > 5 or age < 25'
    
)

# Check if the rule matches the JSON data
data1 = {
    'first_name': 'Luke walker',
    'last_name': 'Skywalker',
    'email': 'luke@rebels.org',
    'age': 25,
    'title': 'Harry Potter',
    'released': '01-02-2002',
    'publisher': 'JK Rowling',
    'issue' : 0
}
data2 = {
    'first_name': 'Luke',
    'last_name': 'Vader',
    'email': 'dvader@rebels.org',
    'age': 1,
    'title': 'Harry Potter 1',
    'released': '07-07-2002',
    'publisher': 'JK Rowling uehfuh',
    'issue' : 5
}

match1 = rule.matches(data1)
match2 = rule.matches(data2)

# match11 = rule1.matches(data1)
# match21 = rule1.matches(data2)

print(match1)  # True
print(match2)  # False
# engine = rule_engine.engine()
# engine.matches(rule1)
