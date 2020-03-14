# Setup virtual environment
Run this from the home of pi user
`cd $HOME` or just `cd` to get to the home directory

Run this to create an env and then activate said env and then install necessary third party libs
```
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install RPi.GPIO
```

# Setup services
Run the contents of the files
```
request - rpi_styra/services/requests/systemd/01_ln.sh
request - rpi_styra/services/requests/systemd/02_install.sh

energenie - rpi_styra/services/energenie/systemd/01_ln.sh
energenie - rpi_styra/services/energenie/systemd/02_install.sh

```