import re
import dns.resolver
import socket
import smtplib
import quickemailverification

# Get A EmailValidation API And Get Started Working With it
# Implement It
# API 4823f2be33cee613ba4b73c8f2ac11fd2011074710ba63f14685907c1172

class EmailValidator:
        
    def Valid(self,emailToVerify):
         

            # Syntax Check 
        self.match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailToVerify)

        if self.match == None:
            return 
            
        
        self.client = quickemailverification.Client('4823f2be33cee613ba4b73c8f2ac11fd2011074710ba63f14685907c1172')
        self.quickemailverification = self.client.quickemailverification()

            # PRODUCTION MODE
        self.response = self.quickemailverification.verify(emailToVerify)

            # SANDBOX MODE
        #self.response = self.quickemailverification.sandbox('')
                   
        
        if(self.response.body["result"] == 'valid'):
            return True
        elif (self.response.body["result"] == 'invalid'):
            return False

                                    
if __name__ == '__main__':
    valid = EmailValidator()
    valid.Valid('saugatjarif@gmail.com')
