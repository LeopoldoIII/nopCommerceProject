# enviroment setup 
    
create your venv

    python3 -m venv venv 

source your venv 

    source venv/bin/activate

install modules 

    pip3 install -r requirements.txt

# Run the project 

    pytest -s -v testCases/test_login.py --browser chrome
