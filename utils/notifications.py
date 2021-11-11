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


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from csskp.settings import CONFIG
# from utils import emails


def send_report(email_address, pdf_data):
    """
    Send a survey report to an email address.
    """
    subject = "[{}] Your report".format(CONFIG["tool_name"])
    from_email = " "
    to = email_address
    text_content = render_to_string(
        "emails/send_report.txt",
        {
            "user": email_address,
        },
    )
    html_content = ""
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.attach('report.pdf', pdf_data, 'application/pdf')
    msg.send()
