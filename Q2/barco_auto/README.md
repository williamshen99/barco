

## Supported Browsers

* Chrome
* Others - TBD


## Supported OS

* Mac
* Others - TBD


-------------------------------

## How To Use

P.S. the webdriver in /webdriver folder is for version 101.0.4951.64,
please help to replace with a correct webdriver it if your browser is not this version

* download this repo
* open terminal
* go to folder /amazon_login
* run the command below to create and activate environment:
```bash
python3 -m venv tutorial-env
source tutorial-env/bin/activate
```

* run the command below to install all required packages:
```bash
python setup.py develop
```

* run the command below to start test:
```bash
pytest tests
```

* you will see the test result in the terminal
* you also can go to /amazon_login/report to see the report: report.html
