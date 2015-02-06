# Logwatch
##### Monitor multiple log files simultaneously in a single terminal window

The web servers where I work split the Apache logs into multiple files, so I made this little utility to allow me to see all of the activity on the server I'm working on in a single screen.  A number of file types (e.g. access, error) are listed in the config.json file, along with which colour each of the types will be echoed to screen.

The following are prerequisites to use this:
 - Python (written and tested on 2, but should work on 3 as well)
 - Colorama module for Python ([link](https://github.com/tartley/colorama))

To install logwatch, simple put the `logwatch.py` file wherever you want (preferable somewhere in your path) and the one or many config files somewhere as well.  Then just run the script with the full path to the config file as the only parameter:
```
logwatch.py /etc/logwatch/nginx.json
```

I have a few minor features I want to add to this in the near future, so do check back in a while.