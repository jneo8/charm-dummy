import charms.apt
import charms.reactive as reactive
import charms_openstack.charm as charm
import charm.openstack.dummy as dummy


@reactive.when_not("charm.installed")
def install_pkgs():
    dummy.install()
    reactive.set_state("charm.installed")
