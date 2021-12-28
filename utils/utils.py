# -*- coding: utf-8 -*-

from typing import List
import subprocess
from csskp.settings import PUBLIC_URL, BASE_DIR
from urllib.parse import urlparse


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
