# Python Testing, P11
## Installation
clone the repo 
```sh
git clone https://github.com/raltheo/Python_Testing.git
cd Python_Testing
```
create new virtual environnement
```sh
py -m venv venv
or
python -m venv venv
or
python3 -m venv venv
```
activate 
```sh
venv\Scripts\activate.bat (on windows cmd)
venv\Scripts\activate.ps1 (on windows powershell)
source venv/bin/activate (on linux/mac)
```
install requirements
```sh
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```
(for exit from virtual environnement)
```sh
deactivate
```
* * *
## Usage
### run server
```sh
export FLASK_APP=server.py
flask run
```
Running on http://127.0.0.1:5000/

## Tests

### Running pytest

```sh
pytest tests/unknow_email_404/test.py
# pytest <file>
```

### Coverage
```sh
coverage run -m pytest tests/integration/integration.py
coverage report -m
```

* * *
