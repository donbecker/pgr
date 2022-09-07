# PGR: Password Generator Retriever

## Summary
This project is an interactive Python CLI application, which retrieves passwords generated from a public API. 

DISCLAIMER #1: this is a proof of concept, and any passwords should not actually be used as passwords, for any purpose. 

DISCLAIMER #2: this project uses a publicly available API, not created by the author. Be kind to free, public resources. 


## Overview
This project uses prompt_toolkit to place the user in an interactive CLI prompt. Users can interact with the app via the `getpw` and `getbatch` commands, and can exit with the `exit` command. 

In addition to the three commands above, there are two functions. `formpayload` handles parsing the user arguments in the `getpw` function while `requestpw` handles the actual request to the API service. 


## Usage

Start the interctive prompt by running the Python file with no arguments: `.\pgr.py`

There are two available functions: 

### getpw
`getpw` uses optional arguments supplied by the user to retrieve a password from the API service.
Supported arguments: 
- `--len x`: the length of the password to generate, denoted by "x"
- `--caps`: a flag to include capital letters
- `--char`: a flag to include special characters
- `--num`: a flag to include numbers

Example Usage:

This will generate a 4 character long password, including the possibility of capitalized characters: 

`pgr> getpw --len 4 --caps`


### getbatch
`getbatch` uses a user supplied count value to retrieve a batch list of passwords from the API service. 
Note that this call is rate limited to one API call every two seconds. 
Supported arguments:
- `x`: the number of passwords to generate for the batch. 

Example Usage: 

This will generate a batch list of five passwords: 

`pgr> getbatch 5`

## Future Improvements
The following areas could be improved: 
- Add unit testing
- Add mock for API / testing without API
- Extend `getbatch` to permit the optional arguments supported by `getpw`
- Extend `getbatch` to allow a user specified rate limit
- Add a retry mechanism to the API call
- Add a uniform debugging flag/output for all code
- Choose a naming standard 