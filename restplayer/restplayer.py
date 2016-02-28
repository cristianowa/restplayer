#!/usr/bin/env python
import argparse
import sys
import ConfigParser
from commands import getstatusoutput as cmd
import os
import inspect

NETWORK = "Network"
DIRECTORIES = "Directories"
IP = "Ip"
PORT = "Port"
DIRECTORY = "Directory"
DEFAULT_CFG_FILE = os.path.join(os.path.expanduser("~") + ".restplayerrc")
DEBUG = "Debug"
default_config = """[program:restplayer]
command=COMMANDLINE
user=USER
autostart=true
autorestart=true
stderr_logfile=/var/log/restplayer.err.log
stdout_logfile=/var/log/restplayer.out.log"""
supervisor_file = "/etc/supervisor/conf.d/restplayer.conf"

class UserConfig:
    def __init__(self):
        self.ip = "0.0.0.0"
        self.port = 5000
        self.debug = False
        self.userConfigFile = os.path.join(os.path.expanduser("~"), ".restplayerrc")
        self.directory = os.path.join(os.path.expanduser("~"), ".restplayer")

    def read(self):
        if not os.path.exists(self.userConfigFile):
            return
        cfg = ConfigParser.ConfigParser()
        cfg.read(self.userConfigFile)
        self.ip = cfg.get(NETWORK, IP)
        self.port = int(cfg.get(NETWORK, PORT))
        self.debug = bool(cfg.get(NETWORK, DEBUG))
        self.directory = cfg.get(DIRECTORIES, DIRECTORY)

    def write(self):
        cfg = ConfigParser.ConfigParser()
        cfg.add_section(NETWORK)
        cfg.set(NETWORK, IP, self.ip)
        cfg.set(NETWORK, PORT, self.port)
        cfg.set(NETWORK, DEBUG, self.debug)
        cfg.add_section(DIRECTORIES)
        cfg.set(DIRECTORIES, DIRECTORY, self.directory)
        with open(self.userConfigFile, "w") as f:
            cfg.write(f)


userConfig = UserConfig()
import getpass


def first_run(userCfg):
    x = raw_input("Would you like to install supervisor and supervisor entry ? (y/N) ")
    psw = getpass.getpass()
    if x.lower() == "y":
        sts, ret = cmd("echo " + psw + " | sudo -S apt-get install supervisor")
        if sts != 0:
            print "Error installing supervisor - aborting"
            print "[" + ret + "]"
            return
        cmd("echo " + psw + " | sudo -S touch /etc/supervisor/conf.d/restplayer.conf")
        cmd("echo " + psw + " | sudo -S chown " + getpass.getuser() + " /etc/supervisor/conf.d/restplayer.conf")
        with open("/etc/supervisor/conf.d/restplayer.conf", "w") as f:
            cfg = default_config
            current_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
            cfg = cfg.replace("COMMANDLINE", current_path)
            cfg = cfg.replace("USER", getpass.getuser())
            f.write(cfg)
    userConfig.write()
    cmd("supervisorctl reload")
    cmd("supervisorctl restart restplayer")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-p", "-port", help="Port to listen", type=int, dest="port", default=userConfig.port)
    parser.add_argument("--bind", help="IP to bind to", dest="bind", default=userConfig.ip)
    parser.add_argument("--debug", help="Enable debug mode on server", dest="debug", action="store_true",
                        default=userConfig.debug)
    parser.add_argument("--dry-run", help="Only validates arguments", dest="dryrun", action="store_true")
    parser.add_argument("--first-run", help="Configuration walkthrough", dest="first", action="store_true")
    parser.add_argument("--daemon", help="Fork and stay at background", dest="daemon", action="store_true")
    parser.add_argument("--config-file", help="Use different config file", dest="cfg", default=None)
    args = parser.parse_args()

    if args.dryrun:
        sys.exit(0)
    if args.cfg is not None:
        userConfig.read(args.cfg)
    userConfig.ip = args.bind
    userConfig.port = args.port
    userConfig.debug = bool(args.debug)
    import config

    config.base_dir = userConfig.directory
    if args.first:
        first_run(userConfig)
        sys.exit(0)
    from webservice import app

    app.run(debug=args.debug, host=args.bind, port=args.port)
