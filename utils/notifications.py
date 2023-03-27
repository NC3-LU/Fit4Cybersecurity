#! /usr/bin/env python
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from csskp.settings import CUSTOM
from csskp.settings import OPERATOR_CONTACT
from utils.decorators import async_maker


@async_maker
def send_report(email_address: str, pdf_data: bytes) -> None:
    """
    Send a survey report to an email address.
    """
    subject = "[{}] Your report".format(CUSTOM["tool_name"])
    from_email = OPERATOR_CONTACT["contact_email"]
    to = email_address
    text_content = render_to_string(
        "emails/send_report.txt",
        {
            "tool_name": CUSTOM["tool_name"],
        },
    )
    html_content = render_to_string(
        "emails/send_report.html",
        {
            "tool_name": CUSTOM["tool_name"],
        },
    )
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.attach("report.pdf", pdf_data, "application/pdf")
    msg.send()
