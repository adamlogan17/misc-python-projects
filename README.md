- [misc-python-projects](#misc-python-projects)
  - [How do I get set up?](#how-do-i-get-set-up)
    - [Windows Machine](#windows-machine)

# misc-python-projects

Contains miscellaneous python projects. Some of these projects are still a work in progress. They are simply small scripts that do not justify their own repository.

## How do I get set up?

### Windows Machine

1. Replace ```fileName``` with the name of the script you are trying to run and then execute the following commands:

   ```console
   python -m venv venv
   venv\scripts\activate
   pip install -r requirements.txt
   python fileName.py
   ```

2. To exit the virtual environment use the command ```deactivate```

Alternatively it is possible to install the dependencies by using the requirements.txt included within this folder (example command below)

```console
pip install -r requirements.txt
```
