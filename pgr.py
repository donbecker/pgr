from cmd import Cmd
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as printft
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
import requests

def requestpw(payload):
    url = 'https://passwordinator.herokuapp.com'
    try:
        response = requests.get(url, params=payload)
        #print("Status code: " + str(response.status_code))
        #print("Json returned: " + str(response.json()))
        if str(response.status_code) == '200':
            response = str(response.json())
        else:
            response = "API returned non-200 code"
    except: 
        response = "Error calling api"
    return response

class PromptLoop(Cmd):
    prompt = 'pgr>'
    intro = "Password Generator Retriever v1.0.0"

    def do_getpw(self, inp):
        printft('TODO: implement getting password....')
        payload = {
            'len': 5
        }
        req = requestpw(payload)
        print("API returned: " + req)
        return False   

    def do_exit(self, inp):
        printft('exiting....')
        # true here means exit
        return True

if __name__ == '__main__':
    PromptLoop().cmdloop()