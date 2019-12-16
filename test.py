import quickemailverification

client = quickemailverification.Client('4823f2be33cee613ba4b73c8f2ac11fd2011074710ba63f14685907c1172')
quickemailverification = client.quickemailverification()

# PRODUCTION MODE
#response = quickemailverification.verify('saugatjarif@gmail.com')

# SANDBOX MODE
response = quickemailverification.sandbox('saugatjarif@gmail.com')

print(response.body) # The response is in the body attribute
