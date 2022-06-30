import collections
import socket
import subprocess
import charms_openstack.ip as os_ip
import charms_openstack.charm as charm



class DummyCharm(charm.OpenStackCharm):

    release = "yoga"

    # Internal name of charm
    service_name = name = "dummy"

    # List of packages to install for this charm
    packages = [
        "python3-pip", "python3-virtualenv"
    ]

    api_ports = {
        "dummy-api": {
            os_ip.PUBLIC: 8080,
            os_ip.ADMIN: 8080,
            os_ip.INTERNAL: 8080,
        }
    }



def install():
    DummyCharm.singleton.install()
