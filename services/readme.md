python3 -m venv venv
source venv/bin/activate

pip install flask
pip install RPi.GPIO

pip install Flask-Cors




# First time you must use
git submodule update --init --recursive
git submodule update --recursive --remote

# After that you can update submodules with this
git pull --recurse-submodules
