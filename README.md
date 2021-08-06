## HW3 - WAD VNIT 2021
## Installation
Install Flask in Window

1. `Set-ExecutionPolicy Unrestricted - Scope Process`

2. `venv\Scripts\activate`

3. `pip install Flask`

Install dependencies

```sh
pip install -r requirements.txt
```
## Run
```sh 
python index.py
```
Add page that will change subset of images according to the GET parameter

```sh
http://localhost:5000/img/get/'<number>'
```