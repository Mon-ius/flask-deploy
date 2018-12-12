
import os

path_to_module = os.path.dirname(__file__)
# Configurations

uWSGI = os.path.join(path_to_module, "utils", "uwsgi_config.ini")
NGINX = os.path.join(path_to_module, "utils", "nginx_config.conf")
SSL = os.path.join(path_to_module, "utils", "ssl_script.sh")
SERVICE = os.path.join(path_to_module, "utils", "systemd_script.service")
DOCKER = os.path.join(path_to_module, "utils", "docker_config.run")
# uWSGI = "./"
#  = "./utils/"

#  = "./utils/"
#  = "./utils/
#  = "./utils/

# May need to change
NGINX_CONF1 = "/etc/nginx/sites-enabled/"
NGINX_CONF2 = "/etc/nginx/sites-available/"
SYSTEMD_CONF = "/etc/systemd/system/"

# SET ENV

DOMAIN = None
USR = None
CUR_LOC = None
