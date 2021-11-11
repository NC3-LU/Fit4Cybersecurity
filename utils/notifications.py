#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Fit4Cybersecurity
# Copyright (C) 2021 SECURITYMADEIN.LU
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


from django.template.loader import render_to_string

from csskp.settings import CONFIG
from utils import emails


def send_report(email_address):
    """
    Send a survey report to an email address.
    """
    plaintext_email_from_parsed_template = render_to_string(
        "emails/send_report.txt",
        {
            "user": email_address,
        },
    )
    emails.send(
        to=email_address,
        subject="[{}] Your report".format(CONFIG["tool_name"]),
        plaintext=plaintext_email_from_parsed_template,
    )
