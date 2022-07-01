from charms.reactive import when, when_any, when_not, set_flag
from charmhelpers.core.hookenv import (
    status_set,
    open_port,
    close_port,
    opened_ports,
    config,
    log,
)
from charmhelpers.core.services import service_restart
from charmhelpers.core.templating import render
import charms.apt


@when_not("apt.installed.apache")
def install_apache_apt():
    charms.apt.queue_install(["apache2"])
    set_flag("apt.installed.apache")


@when("apt.installed.apache")
@when_not("apache.ready")
def configure_apache():
    status_set("maintenance", "apache installed, waiting.")
    reconfigure_vhost()
    set_flag("apache.ready")


@when_any("config.changed.port", "config.changed.host")
def reconfigure_vhost():
    new_port = config("port")
    new_host = config("host")
    log("Reconfiguring apache vhost. Port: %s; Host: %s" % (new_port, new_host))
    context = {
        "port": new_port,
        "bind_address": new_host,
    }
    render("vhost.j2", "/etc/apache2/sites-available/000-default.conf",
           context=context)

    # close previously opened ports
    for port_spec in opened_ports():
        log("Closing port %s" % port_spec)
        port, protocol = port_spec.split("/")
        close_port(port, protocol.upper())
    # Set new port as opened
    log("Opening port %s" % new_port)
    open_port(str(new_port))
    service_restart("apache2")


@when("apache.ready")
def apache_start():
    status_set("active", "Unit is ready")

