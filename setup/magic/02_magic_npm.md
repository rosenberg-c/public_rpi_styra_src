# Setup -pi

## update npm
```
sudo apt-get install npm -y &&
sudo npm install -g npm -y &&

sudo npm i npm@latest -g

```
Some warning may occur, but is not a concern

# Install Magic Mirror

https://docs.magicmirror.builders/getting-started/installation.html

curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs

git clone https://github.com/MichMich/MagicMirror
cd MagicMirror/
npm install
cp config/config.js.sample config/config.js
npm run start
npm run server


# install pm2

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
