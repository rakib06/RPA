## Creating environment 
```cmd
pip install virtualenv
virtualenv venv
```
## Activate isolation 
(cmd as administrator) powershell Set-ExecutionPolicy RemoteSigned
.\venv\Scripts\activate
## to save the required packages 
pip freeze > .\requirements.txt 

## install required packages 
pip install -r .\requirements.txt

# Execution Policy 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

```python
def basic_limit_visible(driver, logging):
    try:
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located(
                (By.XPATH, "/html/body/table[3]/tbody/tr/td[3]/form/table[1]/tbody/tr[2]/td[2]"))
        )
        return True

    except Exception as e:
        logging.warning('_From-> basic_limit_visible()_ :' + str(e))
        return False
```
