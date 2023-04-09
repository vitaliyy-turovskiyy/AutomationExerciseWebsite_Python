# AutomationExerciseWebsite_Python
_____
### **In this project, the test suite for the [site](https://www.automationexercise.com/)** was automated. The tests were written in Python. Integrated allure report with deployment to GitHub pages. Slack notifications are also installed. 

## Getting started
___
### *Prerequisites* :
- Node.js 14 or above. You can download it [here](https://nodejs.org/en/download/)
- Python. You can download it [here](https://www.python.org/downloads/)

### *Installation* :  
1. Clone the repo :file_folder: using:  
```sh 
git clone git@github.com:vitaliyy-turovskiyy/AutomationExerciseWebsite_Python.git
```
2. Install our packages using :
```sh
pip install pipenv
```
3. To use the allure reporter you need to install it :
```sh
pipenv install allure-pytest
```
### *Usage* :
To run the test from the terminal just type :
```sh
   pytest
   ```
To run tests in headed mode add :
```sh
   --headed
   ```
Running tests in parallel :
```sh
    pytest -n 2 --browser chromium
   ```
### *Generate and open allure report* :
```sh
   pytest --alluredir=./reports --clean-alluredir
   allure serve reports - to open report 
   ```
____
### The test report implemented through GitHub pages can be seen [here](https://vitaliyy-turovskiyy.github.io/AutomationExerciseWebsite_Python/) 

