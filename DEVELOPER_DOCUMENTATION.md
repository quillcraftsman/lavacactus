# Developer Documentation

## Install

After you create a "Fork"

    git clone https://github.com/<your github username>/lavacactus

Virtual environment recommended

Install dependencies

    pip install -r requirements.txt
    pip install -r test_requirements.txt

## Run tests

You can use on of the way (run in the project folder):
* `nose2`
* `make test`
* `make alltests`

## Work with package

Install

    make install

Uninstall 

    make uninstall

Reinstall

    make reinstall

If you change something in the package code you can run `make reinstall` and test your project after that.
Maybe there is a better way to change the package code, but I don't find it yet :)

    