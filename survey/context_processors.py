import os
import subprocess
from csskp.settings import BASE_DIR
from survey.globals import FIT4TOOL_NAME


def get_version(request):
    version = (
        os.environ.get("PKGVER")
        or subprocess.run(
            ["git", "-C", BASE_DIR, "describe", "--tags"], stdout=subprocess.PIPE
        )
        .stdout.decode()
        .strip()
    )
    version = version.split("-")
    if len(version) == 1:
        app_version = version[0]
        version_url = (
            "https://github.com/CASES-LU/Fit4Cybersecurity/releases/tag/{}".format(
                version[0]
            )
        )
    else:
        app_version = "{} - {}".format(version[0], version[2][1:])
        version_url = "https://github.com/CASES-LU/Fit4Cybersecurity/commits/{}".format(
            version[2][1:]
        )
    return {"app_version": app_version, "version_url": version_url}

def get_fit4tool_name(request):
    return {"fit4tool_name" : FIT4TOOL_NAME}
