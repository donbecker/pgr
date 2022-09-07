from cmd import Cmd
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as printft
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
import requests

class PromptLoop(Cmd):
    prompt = 'pgr>'
    intro = "Password Generator Retriever v1.0.0"

    def do_getpw(self, inp):
        printft('TODO: implement getting password....')
        req = requests.get('https://passwordinator.herokuapp.com')
        print("Status code: " + str(req.status_code))
        print("Json returned: " + str(req.json()))
        return False   

    def do_exit(self, inp):
        printft('exiting....')
        # true here means exit
        return True

if __name__ == '__main__':
    PromptLoop().cmdloop()