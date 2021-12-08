# -*- coding: utf-8 -*-

from csskp.settings import PUBLIC_URL
from urllib.parse import urlparse


def can_redirect(url: str) -> bool:
    """
    Check if a redirect is authorised.
    """
    o = urlparse(url)
    return o.netloc in PUBLIC_URL
