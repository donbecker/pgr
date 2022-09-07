from cmd import Cmd
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as printft
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
import requests
import json
import time

# requests a password from API
def requestpw(payload):
    url = 'https://passwordinator.herokuapp.com'
    try:
        response = requests.get(url, params=payload)
        if str(response.status_code) == '200':
            resjson = response.json()
            response = resjson['data']
            iserror = False
        else:
            response = "API returned non-200 code"
            iserror = True
    except: 
        response = "Error calling api"
        iserror = True
    return response, iserror

def formpayload(input):
    inp = input.strip()
    inpsplit = inp.split('--')
    payload = {}
    for inparg in inpsplit:
        if inparg.startswith('len'):
            # add to payload
            payload['len'] = inparg.split(' ')[1]

        elif inparg.startswith('caps'):
            # add to payload
            payload['caps'] = 'true'

        elif inparg.startswith('num'):
            # add to payload
            payload['num'] = 'true'

        elif inparg.startswith('char'):
            # add to payload
            payload['char'] = 'true'

    #print("Split: " + str(inpsplit))
    #print("Payload: ")
    #for k, v in payload.items():
    #    print(k, v)

    return payload

# main CLI prompt loop
class PromptLoop(Cmd):
    prompt = 'pgr>'
    intro = "Password Generator Retriever v1.0.0"

    # handles getpw ('get password') command
    def do_getpw(self, inp):
        #printft('You typed ' + inp)
        payload = formpayload(inp)
        req, reterror = requestpw(payload)
        if not reterror:
            print("Password returned: " + req)
        else: 
            print("Error retrieving password, please try again")
        return False   

    def do_getbatch(self, inp):
        #printft('You typed ' + inp)

        if not inp.isdigit():
            print("Error: count for batch must be positive integer")
            return False
        else: 
            pwlist = []
            for c in range(int(inp)):
                 payload = formpayload('')
                 req, reterror = requestpw(payload)
                 if not reterror:
                     print("Password returned: " + req)
                     pwlist.append(req)
                     time.sleep(3)
                 else: 
                     print("Error retrieving password, please try again")
            print("Password Batch: ")
            for pw in pwlist:
                print(pw)
            return False 

    # handles exiting CLI prompt loop
    def do_exit(self, inp):
        printft('exiting....')
        # true here means exit
        return True

if __name__ == '__main__':
    PromptLoop().cmdloop()