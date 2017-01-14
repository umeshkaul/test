import dns.resolver
myResolver = dns.resolver.Resolver() #create a new instance named 'myResolver'
myAnswers = myResolver.query("www.bloomberg.com", "A") #Lookup the 'A' record(s) for google.com
for rdata in myAnswers: #for each response
    print rdata #print the data