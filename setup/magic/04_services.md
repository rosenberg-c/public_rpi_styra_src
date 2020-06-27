# Setup virtual environment
Run this from the home of pi user
`cd $HOME` or just `cd` to get to the home directory

Run this to create an env and then activate said env and then install necessary third party libs
```
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install RPi.GPIO
pip install flask-cors

```

# Setup services
Run the contents of the files
-->
request - /services/requests/systemd/01_ln.sh
request - /services/requests/systemd/02_install.sh

baklight - /services/backlight/systemd/ln.sh
baklight - /services/backlight/systemd/install.sh
<--