# Manual Debugging
Activate virtual env for python
```
source venv/bin/activate
cd rpi_styra/services
python main.py
```

# remove services
sudo rm /etc/systemd/system/request.service
sudo rm /etc/systemd/system/backlight.service
sudo rm /etc/systemd/system/energenie.service