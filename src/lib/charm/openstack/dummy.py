import collections
import socket
import subprocess

import charmhelpers.core.hookenv as hookenv
import charms_openstack.charm
import charms_openstack.ip as os_ip



class DummyCharm(charms_openstack.charm.HAOpenStackCharm):

    # Internal name of charm
    service_name = name = 'dummy'

    # First release supported
    release = 'mitaka'

    # List of packages to install for this charm
    packages = ['congress-server', 'congress-common', 'python-antlr3', 'python-pymysql', 'python-apt']

    api_ports = {
        'congress-server': {
            os_ip.PUBLIC: 1789,
            os_ip.ADMIN: 1789,
            os_ip.INTERNAL: 1789,
        }
    }

    service_type = 'congress'
    default_service = 'congress-server'
    services = ['haproxy', 'congress-server']

    # Note that the hsm interface is optional - defined in config.yaml
    required_relations = ['shared-db', 'amqp', 'identity-service']

    restart_map = {

        '/etc/congress/congress.conf': services,
    }

    ha_resources = ['vips', 'haproxy']

    release_pkg = 'dummy-common'

    package_codenames = {
        'dummy-common': collections.OrderedDict([
            ('2', 'mitaka'),
            ('3', 'newton'),
            ('4', 'ocata'),
        ]),
    }


    sync_cmd = ['congress-db-manage', '--config-file', '/etc/congress/congress.conf', 'upgrade', 'head']

    def get_amqp_credentials(self):
        return ('congress', 'congress')

    def get_database_setup(self):
        return [{
            'database': 'congress',
            'username': 'congress',
            'hostname': hookenv.unit_private_ip() },]
