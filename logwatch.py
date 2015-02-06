#!/usr/bin/python

import json, threading, colorama, time, sys, os

class LogWatchConfig:
    
    _config = {}

    def __init__(self, config_file):
        try:
            with open(config_file) as cf:
                self._config = json.load(cf)
        except IOError as e:
            raise Exception('Unable to load global config: '+config_file)
        except ValueError as e:
            raise Exception('Unable to parse global config: '+config_file)

    def getValue(self, key):
        levels = key.split('::')
        config = self._config
        for i in levels:
            if i in config:
                config = config[i]
            else:
                return None
        return config

class LogWatch:

    _time_to_go = False

    def __init__(self):
        try:
            if len(sys.argv) == 1:
                raise Exception('Config file not specified')
            config = LogWatchConfig(sys.argv[1])
        except Exception as e:
            sys.exit('ERROR - '+str(e))
        colours = config.getValue('colours')
        files = config.getValue('files')
        colorama.init()
        for filetype in files:
            for filename in files[filetype]:
                if files[filetype][filename]:
                    t = threading.Thread(target=self.thread, args=(filename, colours[filetype]))
                    t.start()
        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            self._time_to_go = True

    def fastPrint(self, text):
        sys.stdout.write(text)
        sys.stdout.flush()

    def monitorFile(self, fp, offset=2):
        fp.seek(0,offset)
        while not self._time_to_go:
            line = fp.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

    def thread(self, filename, colour):
        offset = 2
        while not os.path.isfile(filename):
            time.sleep(0.5)
            offset = 0
            if self._time_to_go:
                return
        fp = open(filename)
        for line in self.monitorFile(fp, offset):
            self.fastPrint(getattr(colorama.Fore, colour)+line+colorama.Fore.RESET)


if __name__ == "__main__":
    lw = LogWatch()
