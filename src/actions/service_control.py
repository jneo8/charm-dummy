#!/usr/bin/env python3
import sys
import os

# Disgusting hack to enable charmhelpers usage in actions.
# The other option is to hard copy-paste charmhelpers int "lib/"
# or "hooks/"
sys.path.append('../.venv/lib/python3.8/site-packages/')

from charmhelpers.core.services import service_stop, service_restart
from charmhelpers.core.hookenv import (
    function_fail,
    log,
    INFO,

)


def restart():
    """Implementation of "restart" and "start" actions."""
    service_restart("apache2")


def stop():
    """Implementation of "stop" action."""
    service_stop("apache2")


ACTIONS = {
    "start": restart,
    "restart": restart,
    "stop": stop,
}


def main(args):
    action_name = os.path.basename(args.pop(0))
    try:
        action = ACTIONS[action_name]
    except KeyError:
        s = "Action {} undefined".format(action_name)
        function_fail(s)
        return
    else:
        try:
            log("Running action '{}'.".format(action_name), INFO)
            action()
        except Exception as exc:
            function_fail("Action {} failed: {}".format(action_name, str(exc)))


if __name__ == '__main__':
    main(sys.argv)