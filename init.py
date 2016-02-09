#!/usr/bin/env python

import os
import subprocess
import sys
import yaml

# read config.yml
fname = "/portus/config/config.yml"
stream = open(fname, 'r')
data = yaml.load(stream)

# place environment variables in config.yml data
data['email']['from'] = os.getenv('EMAIL_FROM', 'portus@example.com')
data['email']['name'] = os.getenv('EMAIL_NAME', 'Portus')
data['email']['reply_to'] = os.getenv('EMAIL_REPLY_TO', 'no-reply@example.com')

data['ldap']['enabled'] = os.getenv('LDAP_ENABLED', 'false')
data['ldap']['hostname'] = os.getenv('LDAP_HOSTNAME', 'ldap.example.com')
data['ldap']['port'] = os.getenv('LDAP_PORT', '389')
data['ldap']['method'] = os.getenv('LDAP_METHOD', 'plain')
data['ldap']['base'] = os.getenv('LDAP_BASE', 'cn=users,cn=accounts,dc=example,dc=com')
data['ldap']['filter'] = os.getenv('LDAP_FILTER', '&(memberOf=cn=group,cn=groups,cn=accounts,dc=example,dc=com)')
data['ldap']['uid'] = os.getenv('LDAP_UID', 'uid')
data['ldap']['authentication']['enabled'] = os.getenv('LDAP_AUTHENTICATION_ENABLED', 'false')
data['ldap']['authentication']['bind_dn'] = os.getenv('LDAP_AUTHENTICATION_BIND_DN', 'uid=portus,cn=sysaccounts,cn=etc,dc=example,dc=com')
data['ldap']['authentication']['password'] = os.getenv('LDAP_AUTHENTICATION_PASSWORD', 'password')
data['ldap']['guess_email']['enabled'] = os.getenv('LDAP_GUESS_EMAIL_ENABLED', 'false')
data['ldap']['guess_email']['attr'] = os.getenv('LDAP_GUESS_EMAIL_ATTR', 'mail')

data['machine_fqdn']['value'] = os.getenv('MACHINE_FQDN', 'portus.example.com')

# write config.yml
with open(fname, 'w') as yaml_file:
   yaml_file.write(yaml.dump(data, default_flow_style=False))

# now lets run
ret_val = subprocess.call(sys.argv[1:])
sys.exit(ret_val)
