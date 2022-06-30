from charms.reactive import when, when_not, set_flag
from charmhelpers.core.hookenv import status_set
import charms.apt

@when_not("apt.installed.apache")
def install_apache_apt():
    charms.apt.queue_install(["apache2"])
    set_flag("apt.installed.apache")


@when("apt.installed.apache")
@when_not("apache.ready")
def install_apache():
    status_set("blocked", "apache installed, waiting.")
    # Config here
    set_flag("apache.ready")

@when_not("apache.ready")
@when_not("apt.installed.apache")
def waiting_for_apache():
    status_set("maintenance", "waiting for apt apache installation")


@when("apache.ready")
def apache_start():
    status_set("active", "")

