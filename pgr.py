from cmd import Cmd
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as printft
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
import requests
import json

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
        ##inpsplit = inp.split('--')
        ##print("Split: " + str(inpsplit))
        ###inp = inp.strip()
        ###print("Split: " + str(inp.split('--')))
        ####dsplit = dict(x.split("=") for x in inp.split('--'))
        ####print("Split: " + str(dsplit))
    payload = {
    'len': 5
    }
    # payload = input
    return payload

# main CLI prompt loop
class PromptLoop(Cmd):
    prompt = 'pgr>'
    intro = "Password Generator Retriever v1.0.0"

    # handles getpw ('get password') command
    def do_getpw(self, inp):
        printft('You typed ' + inp)
        payload = formpayload(inp)
        req, reterror = requestpw(payload)
        if not reterror:
            print("Password returned: " + req)
        else: 
            print("Error retrieving password, please try again")
        return False   

    # handles exiting CLI prompt loop
    def do_exit(self, inp):
        printft('exiting....')
        # true here means exit
        return True

if __name__ == '__main__':
    PromptLoop().cmdloop()