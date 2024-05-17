# The following code installs the required depencies to run the tests on your system.
# This setup is for mac users only. If you are using windows or linux, please install the dependencies manually as mentioned in readme file

#echo "Cleaning python"
#brew uninstall python > /dev/null 2>&1

#brew uninstall pyenv-virtualenv > /dev/null 2>&1
#brew uninstall pyenv > /dev/null 2>&1
#rm -rf /Users/$USER/.pyenv

echo "Installing the dependencies"
brew install python
brew install git
pip install selenium
pip install webdriver_manager
pip install -U pytest
pip install pytest-html
pip install requests

pip install requests
echo "Installed the required dependencies"
