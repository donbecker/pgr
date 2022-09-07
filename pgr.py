from cmd import Cmd
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as printft
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
import requests
import json

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

class PromptLoop(Cmd):
    prompt = 'pgr>'
    intro = "Password Generator Retriever v1.0.0"

    def do_getpw(self, inp):
        printft('TODO: implement getting password....')
        payload = {
            'len': 5
        }
        req, reterror = requestpw(payload)
        if not reterror:
            print("Password returned: " + req)
        else: 
            print("Error retrieving password, please try again")
        return False   

    def do_exit(self, inp):
        printft('exiting....')
        # true here means exit
        return True

if __name__ == '__main__':
    PromptLoop().cmdloop()