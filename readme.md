## Creating environment 
pip install virtualenv
virtualenv venv
## Activate isolation 
(cmd as administrator) powershell Set-ExecutionPolicy RemoteSigned
.\venv\Scripts\activate
## to save the required packages 
pip freeze > .\requirements.txt 

## install required packages 
pip install -r .\requirements.txt
