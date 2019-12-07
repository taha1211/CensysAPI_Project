import csv
import censys.certificates


with open('outputFile.csv', mode='w') as output_file:
    output = csv.writer(output_file, delimiter=',', quotechar='.', quoting=csv.QUOTE_MINIMAL)
    #this validates my ability to be able to access the Censys API
    c = censys.certificates.CensysCertificates(api_id="XXX", api_secret="XXX")



    #These are the fields we want to hold on to -- In order to print them to our csv
    fields = ["parsed.fingerprint_sha256" ,"parsed.validity.start", "parsed.validity.end"]
    
    #Go ahead and make the header -- For organization
    output.writerow(['SHA-256 Fingerprint', 'Valid Start Date', 'Valid End Date'])

    #Use the censys search function as loop to look for "parsed:names: censys.io" AND "tags.raw: trusted" (trusted tag)
    for cert in c.search("""(parsed.names: censys.io) AND tags.raw: "trusted" """, fields=fields):
   
        #Now go ahead and print your row with the relevant information
        #SHA-256 Fingerprint, Valid Start, Valid End
        output.writerow([cert["parsed.fingerprint_sha256"],cert["parsed.validity.start"],cert["parsed.validity.end"]])
    
    
#End of script

