import subprocess
from typing import List
from urllib.parse import urlparse

from csskp.settings import BASE_DIR
from csskp.settings import PUBLIC_URL


def can_redirect(url: str) -> bool:
    """
    Check if a redirect is authorised.
    """
    o = urlparse(url)
    return o.netloc in PUBLIC_URL


def exec_cmd(cmd: str) -> str:
    """Execute a command in a sub process and wait for the result."""
    bash_string = r"""#!/bin/bash
    set -e
    {}
    """.format(
        cmd
    )
    result = subprocess.check_output(
        bash_string, shell=True, executable="/bin/bash", text=True, cwd=BASE_DIR
    )
    return result.strip()


def exec_cmd_no_wait(cmd: List) -> None:
    """Execute a command in a sub process."""
    subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=BASE_DIR)
