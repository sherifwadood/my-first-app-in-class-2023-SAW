
# my-first-app-in-class-2023-SAW

## Setup

Create and activate a virtual environment:
```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```

Install packages:

'''sh
pip install -r requirements.txt
''
##Usage


Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Create a ".env" file and past ein the following contents:

'''sh

ALPHAVANTAGE_API_KEY="_____"
'''
## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

'''sh
python app/unemployment.py
'''

#API KEY


Send an example email:

'''sh
python app/email_service.py
'''


python -m app.unemployment

## Testing

Run tests:

```sh
pytest
```