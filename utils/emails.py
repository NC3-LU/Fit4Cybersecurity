#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Fit4Cybersecurity
# Copyright (C) SECURITYMADEIN.LU
#
# For more information: https://github.com/CASES-LU/Fit4Cybersecurity
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import smtplib
from email.mime.nonmultipart import MIMENonMultipart
from email import charset

from csskp.settings import MAIL_DEFAULT_SENDER, MAIL_USERNAME, MAIL_PASSWORD, MAIL_SERVER

# from mosp.decorators import async_maker

logger = logging.getLogger(__name__)


def send_smtp(to="", subject="", plaintext="", html=""):
    """
    Send an email.
    """
    # Create message container
    msg = MIMENonMultipart("text", "plain", charset="utf-8")
    # Construct a new charset which uses Quoted Printables (base64 is default)
    cs = charset.Charset('utf-8')
    cs.body_encoding = charset.QP
    msg["Subject"] = subject
    msg["From"] = MAIL_DEFAULT_SENDER
    msg["To"] = to

    msg.set_payload(plaintext, charset=cs)

    try:
        s = smtplib.SMTP(MAIL_SERVER)
        if MAIL_USERNAME is not None:
            s.login(MAIL_USERNAME, MAIL_PASSWORD)
    except ConnectionRefusedError:
        print("Problem when sending email.")
    except Exception:
        logger.exception("send_smtp raised:")
    else:
        try:
            s.sendmail(
                MAIL_DEFAULT_SENDER,
                msg["To"],
                msg.as_bytes().decode(encoding="UTF-8"),
            )
            s.quit()
        except Exception:
            pass
