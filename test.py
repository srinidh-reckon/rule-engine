import rule_engine

# Create a rule to match a literal first name and apply a regex to the email
rule = rule_engine.Rule(
    'first_name.length > 5 and age > 16'
    
)

rule1 = rule_engine.Rule(
    'first_name.length > 5 or age < 25'
    
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
