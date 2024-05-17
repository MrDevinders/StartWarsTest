Star Wars Demo Tests

This repository contains web and api tests for star wars demo website cloned from "https://github.com/MindfulMichaelJames/star-wars/tree/main"

Tests folder structure:

testCases - contains web tests in 3 files "test_SortTitle_AssertLastMovie.py" "test_ViewMovie_CheckPlanet.py" "test_ViewMovie_CheckSpecies.py"

testCasesAPI - contains API tests into 1 file "test_API.py"

The automation tests have been done in python using selenium and pytest framework.

Run:

Clone this repository and make sure you have the following dependencies installed on your machine:

Python 3.11.6

Pip3 24.0

Selenium 4.20.0 -> Pip3 install selenium

pyTest 8.2.0 -> Pip3 install -U pytest

pytest-html 4.1.1 -> pip install pytest-html

webdriver-manager 4.0.1 -> Pip3 install webdriver_manager


requests 2.31.0 -> pip install requests

After the installation, please run the following command from the terminal window:

Go to /star-wars-assignment/


For web tests:

pytest -v -m web

For api tests:

pytest -v -m api
