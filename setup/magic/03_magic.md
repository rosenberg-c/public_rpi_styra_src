
# Setup git cred
```
git config --global credential.helper "cache --timeout=3600"
```

--->
# Setup basic magic-mirror
git clone https://github.com/rosenberg-c/rpi_styra.git


# Run the contents over ssh
`/mirrors/magic_clock/01_name.sh`
`/mirrors/magic_clock/02_modules.sh`

# Run the content of ln.sh
`/mirrors/ln.sh`

<---

pm2 start magic_clock.sh
pm2 save
