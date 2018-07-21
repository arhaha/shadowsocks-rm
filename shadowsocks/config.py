import logging

#Config
MYSQL_HOST = '202.5.18.182'
MYSQL_PORT = 3306
MYSQL_USER = 'sspanel'
MYSQL_PASS = 'p@ssw0Rd'
MYSQL_DB = 'sspanel'

# Pro node 1 true , others false
PRO_NODE = 0

MANAGE_PASS = 'passwd'
#if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
#make sure this port is idle
MANAGE_PORT = 6666
#BIND IP
#if you want bind ipv4 and ipv6 '[::]'
#if you want bind all of ipv4 if '0.0.0.0'
#if you want bind all of if only '4.4.4.4'
SS_BIND_IP = '0.0.0.0'
SS_METHOD = 'chacha20-ietf-poly1305'

# Firewall Settings
# -----------------
# These settings are to prevent user from abusing your service
SS_FIREWALL_ENABLED = True
# Mode = whitelist or blacklist
SS_FIREWALL_MODE = 'blacklist'
# Member ports should be INTEGERS
# Only Ban these target ports (for blacklist mode)
SS_BAN_PORTS = [22, 23, 25]
# Only Allow these target ports (for whitelist mode)
SS_ALLOW_PORTS = [53, 80, 443, 8080, 8081]
# Trusted users (all target ports will be not be blocked for these users)
SS_FIREWALL_TRUSTED = [443]
# Banned Target IP List
SS_FORBIDDEN_IP = []

#LOG CONFIG
LOG_ENABLE = False
SS_VERBOSE = False
LOG_LEVEL = logging.DEBUG
LOG_FILE = '/var/log/shadowsocks.log'
