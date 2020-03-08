# Setup -pi

## update npm
```
sudo apt-get install npm -y &&
sudo npm install -g npm -y &&

sudo npm i npm@latest -g

```
Some warning may occur, but is not a concern

# Install Magic Mirror

```
url="https://raw.githubusercontent.com/MichMich/MagicMirror/master/installers/raspberry.sh"
bash -c "$(curl -sL $url)"

```
# install pm2
Sometimes pm2 dont install correctly when running magic mirror install.
Run this if you get pm2 missing error
you can test by running command `pm2 list`

info  - `https://stackoverflow.com/questions/52979927/npm-warn-checkpermissions-missing-write-access-to-usr-local-lib-node-modules`

`nano .bashrc` 
add to end
```
npm set prefix ~/.npm
PATH="$HOME/.npm/bin:$PATH"
PATH="./node_modules/.bin:$PATH"
```

---

then 

`npm install pm2 -g`

---

run `pm2 startup`, this will generate a command,
copy and paste that command 
