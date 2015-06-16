# -- coding: utf-8 --

__author__ = 'tdgunes'

SUPERVISOR_CONF = u"""
; Sample supervisor config file.
;
; For more information on the config file, please see:
; http://supervisord.org/configuration.html
;
; Notes:
;  - Shell expansion ("~" or "$HOME") is not supported.  Environment
;    variables can be expanded using this syntax: "%(ENV_HOME)s".
;  - Comments must have a leading space: "a=b ;comment" not "a=b;comment".

[unix_http_server]
file=/tmp/supervisor.sock   ; (the path to the socket file)
;chmod=0700                 ; socket file mode (default 0700)
;chown=nobody:nogroup       ; socket file uid:gid owner
;username=user              ; (default is no username (open server))
;password=123               ; (default is no password (open server))

[inet_http_server]         ; inet (TCP) server disabled by default
port=*:3000        ; (ip_address:port specifier, *:port for all iface)
;username=user              ; (default is no username (open server))
;password=123               ; (default is no password (open server))

[supervisord]
logfile=/tmp/supervisord.log ; (main log file;default $CWD/supervisord.log)
logfile_maxbytes=50MB        ; (max main logfile bytes b4 rotation;default 50MB)
logfile_backups=10           ; (num of main logfile rotation backups;default 10)
loglevel=info                ; (log level;default info; others: debug,warn,trace)
pidfile=/tmp/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
nodaemon=false               ; (start in foreground if true;default false)
minfds=1024                  ; (min. avail startup file descriptors;default 1024)
minprocs=200                 ; (min. avail process descriptors;default 200)
;umask=022                   ; (process file creation umask;default 022)
;user=chrism                 ; (default is current user, required if root)
;identifier=supervisor       ; (supervisord identifier, default is 'supervisor')
;directory=/tmp              ; (default is not to cd during start)
;nocleanup=true              ; (don't clean up tempfiles at start;default false)
;childlogdir=/tmp            ; ('AUTO' child log dir, default $TEMP)
;environment=KEY="value"     ; (key value pairs to add to environment)
;strip_ansi=false            ; (strip ansi escape codes in logs; def. false)

; the below section must remain in the config file for RPC
; (supervisorctl/web interface) to work, additional interfaces may be
; added by defining them in separate rpcinterface: sections
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket
;serverurl=http://127.0.0.1:3000 ; use an http:// url to specify an inet socket
;username=chris              ; should be same as http_username if set
;password=123                ; should be same as http_password if set
;prompt=mysupervisor         ; cmd line prompt (default "supervisor")
;history_file=~/.sc_history  ; use readline history if available

; The below sample program section shows all possible program subsection values,
; create one or more 'real' program: sections to be able to control them under
; supervisor.

;[program:theprogramname]
;command=/bin/cat              ; the program (relative uses PATH, can take args)
;process_name=%(program_name)s ; process_name expr (default %(program_name)s)
;numprocs=1                    ; number of processes copies to start (def 1)
;directory=/tmp                ; directory to cwd to before exec (def no cwd)
;umask=022                     ; umask for process (default None)
;priority=999                  ; the relative start priority (default 999)
;autostart=true                ; start at supervisord start (default: true)
;autorestart=unexpected        ; whether/when to restart (default: unexpected)
;startsecs=1                   ; number of secs prog must stay running (def. 1)
;startretries=3                ; max # of serial start failures (default 3)
;exitcodes=0,2                 ; 'expected' exit codes for process (default 0,2)
;stopsignal=QUIT               ; signal used to kill process (default TERM)
;stopwaitsecs=10               ; max num secs to wait b4 SIGKILL (default 10)
;stopasgroup=false             ; send stop signal to the UNIX process group (default false)
;killasgroup=false             ; SIGKILL the UNIX process group (def false)
;user=chrism                   ; setuid to this UNIX account to run the program
;redirect_stderr=true          ; redirect proc stderr to stdout (default false)
;stdout_logfile=/a/path        ; stdout log path, NONE for none; default AUTO
;stdout_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stdout_logfile_backups=10     ; # of stdout logfile backups (default 10)
;stdout_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
;stdout_events_enabled=false   ; emit events on stdout writes (default false)
;stderr_logfile=/a/path        ; stderr log path, NONE for none; default AUTO
;stderr_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stderr_logfile_backups=10     ; # of stderr logfile backups (default 10)
;stderr_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
;stderr_events_enabled=false   ; emit events on stderr writes (default false)
;environment=A="1",B="2"       ; process environment additions (def no adds)
;serverurl=AUTO                ; override serverurl computation (childutils)

; The below sample eventlistener section shows all possible
; eventlistener subsection values, create one or more 'real'
; eventlistener: sections to be able to handle event notifications
; sent by supervisor.

;[eventlistener:theeventlistenername]
;command=/bin/eventlistener    ; the program (relative uses PATH, can take args)
;process_name=%(program_name)s ; process_name expr (default %(program_name)s)
;numprocs=1                    ; number of processes copies to start (def 1)
;events=EVENT                  ; event notif. types to subscribe to (req'd)
;buffer_size=10                ; event buffer queue size (default 10)
;directory=/tmp                ; directory to cwd to before exec (def no cwd)
;umask=022                     ; umask for process (default None)
;priority=-1                   ; the relative start priority (default -1)
;autostart=true                ; start at supervisord start (default: true)
;autorestart=unexpected        ; whether/when to restart (default: unexpected)
;startsecs=1                   ; number of secs prog must stay running (def. 1)
;startretries=3                ; max # of serial start failures (default 3)
;exitcodes=0,2                 ; 'expected' exit codes for process (default 0,2)
;stopsignal=QUIT               ; signal used to kill process (default TERM)
;stopwaitsecs=10               ; max num secs to wait b4 SIGKILL (default 10)
;stopasgroup=false             ; send stop signal to the UNIX process group (default false)
;killasgroup=false             ; SIGKILL the UNIX process group (def false)
;user=chrism                   ; setuid to this UNIX account to run the program
;redirect_stderr=true          ; redirect proc stderr to stdout (default false)
;stdout_logfile=/a/path        ; stdout log path, NONE for none; default AUTO
;stdout_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stdout_logfile_backups=10     ; # of stdout logfile backups (default 10)
;stdout_events_enabled=false   ; emit events on stdout writes (default false)
;stderr_logfile=/a/path        ; stderr log path, NONE for none; default AUTO
;stderr_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stderr_logfile_backups        ; # of stderr logfile backups (default 10)
;stderr_events_enabled=false   ; emit events on stderr writes (default false)
;environment=A="1",B="2"       ; process environment additions
;serverurl=AUTO                ; override serverurl computation (childutils)

; The below sample group section shows all possible group values,
; create one or more 'real' group: sections to create "heterogeneous"
; process groups.

;[group:thegroupname]
;programs=progname1,progname2  ; each refers to 'x' in [program:x] definitions
;priority=999                  ; the relative start priority (default 999)

; The [include] section can just contain the "files" setting.  This
; setting can list multiple files (separated by whitespace or
; newlines).  It can also contain wildcards.  The filenames are
; interpreted as relative to this file.  Included files *cannot*
; include files themselves.

;[include]
;files = relative/directory/*.ini

"""
import requests
import os
import shutil, json, random, time

ROUTER_URL = "http://127.0.0.1:8080"
AREAS_URL = "{0}/api/areas/".format(ROUTER_URL)


def print_execute(command):
    print(u"> " + command)
    os.system(command.encode('utf-8'))


def print_wait(text):
    raw_input(text + " ")


def ensure_clean_dir(directory):
    try:
        shutil.rmtree(directory)
    except OSError:
        pass
    if not os.path.exists(directory):
        os.makedirs(directory)


print_wait("Ensuring a clean 'servers' directory...")
ensure_clean_dir("servers")
print_wait("Fetching areas from router(127.0.0.1:8080)...")
areas = requests.get(AREAS_URL).json()

print_wait("Going inside 'servers' directory")
os.chdir("servers")

SUPERVISOR_PROGRAMS = u""
PORT_NUMBER = 8001


def add_program(name):
    global SUPERVISOR_PROGRAMS, PORT_NUMBER
    program = u"""
[program:{0}]
command=python \"{0}/manage.py\" runserver 0.0.0.0:{1}
redirect_stderr=true
autostart=true
stopasgroup=true
    """.format(name, PORT_NUMBER)
    SUPERVISOR_PROGRAMS = SUPERVISOR_PROGRAMS + "\n" + program
    PORT_NUMBER += 1


for area in areas:
    short_name = (''.join(e for e in area["name"] if e.isalnum())).lower()
    print(u"Initializing {0} server's files...".format(area["name"]))
    print_execute("git clone https://github.com/tdgunes/polserver.git")
    os.rename("polserver", short_name)
    print("Generating the initial database")
    print_execute(u"python \"{0}/manage.py\" migrate".format(short_name))
    add_program(short_name)
    print("Setting address to the router")
    area["url"] = "http://127.0.0.1:{0}".format(PORT_NUMBER - 1)
    headers = {'Content-type': 'application/json'}
    print("Add default super user to the server")
    print_execute(u"python \"{0}/manage.py\" add_default_super_user".format(short_name))
    # Add new url to server
    r = requests.put("http://127.0.0.1:8080/api/areas/{0}/".format(area["id"]), data=json.dumps(area), headers=headers)



print("Writing supervisor configuration and helper starter files")
with open("supervisord.conf", "w") as f:
    str = SUPERVISOR_CONF + SUPERVISOR_PROGRAMS
    f.write(str.encode('utf8'))

with open("start.sh", "w") as f:
    f.write("supervisord -c supervisord.conf\n")

with open("stop.sh", "w") as f:
    f.write("supervisorctl -c supervisord.conf shutdown\n")

print("Starting the supervisor silently")
# print_execute("supervisorctl -c supervisord.conf shutdown")
print_execute("supervisord -c supervisord.conf")
print("For shutdown write: supervisorctl -c ./servers/supervisord.conf shutdown ")
print("Setting up new servers:(waiting {0} seconds)".format(len(areas)*2))

example_policies = [
    "Devices with photographing capabilities are not allowed.",
    "Devices with speakers must turn off their devices.",
    "Devices must turn off wireless communication capabilities.",
    "Bluetooth is not allowed.",
    "WiFi connections are not allowed.",
    "Maximum allowed volume is %20.",
    "Devices shall play only jazz songs.",
    "Vibrate mode is not allowed. "
]
time.sleep(len(areas)*2)
for area in areas:
    print(u"Setting up server named as {0}".format(area["name"]))
    headers = {'Content-type': 'application/json'}
    payload = {'key':"name", "value": area["name"]}
    print requests.post("{0}/api/settings/".format(area["url"]), data=json.dumps(payload), headers=headers).text
    payload = {'key': "url", "value": area["url"]}
    print requests.post("{0}/api/settings/".format(area["url"]), data=json.dumps(payload), headers=headers).text
    payload = {'key': "id", "value": area["id"]}
    print requests.post("{0}/api/settings/".format(area["url"]), data=json.dumps(payload), headers=headers).text
    payload = {'key': "router", "value": ROUTER_URL}
    print requests.post("{0}/api/settings/".format(area["url"]), data=json.dumps(payload), headers=headers).text
    payload = {'text': random.choice(example_policies), "author": 1}
    print requests.post("{0}/api/policies/".format(area["url"]), data=json.dumps(payload), headers=headers).text

print("In total {0} servers are up and running for testing.".format(len(areas)))
print("Bye!")