# -*- coding: utf-8 -*-

from typing import Dict
import sys
import requests
from urllib.parse import urljoin
from django.core.management.base import BaseCommand
from csskp.settings import CY_DB_URL
from survey.models import (
    Recommendations,
    # SurveyCompany
)


class Command(BaseCommand):
    help = "Command to access the Cybersecurity Luxembourg database"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.user_agent = f'Fit4CyberSecurity - Python {".".join(map(str, sys.version_info[:2]))}'
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(metavar="subcommand", dest="subcommand")

        subparser_signin = subparsers.add_parser("signin", help="Create an account to the service.")
        subparser_login = subparsers.add_parser("login", help="Authenticate to the service.")
        # subparser_refresh = subparsers.add_parser("refresh", help="Refresh a token.")
        subparser_sync = subparsers.add_parser("sync", help="Synchronize local data with the service.")

        subparser_signin.add_argument("--company", type=str, help="Company name.")
        subparser_signin.add_argument("--department", type=str, help="Deparrtment name.")
        subparser_signin.add_argument("--email", type=str, help="Email.")

        subparser_login.add_argument("--email", type=str, help="Email.")
        subparser_login.add_argument("--password", type=str, help="Password.")

        subparser_sync.add_argument("object", type=str, help="Objects to sync.")

    def handle(self, *args, **options):
        match options["subcommand"]:
            case "signin":
                self.stdout.write("Signin")
                data = {
                    "company": options["company"],
                    "department": options["department"],
                    "email": options["email"]
                }
                url = urljoin(CY_DB_URL, "account/create_account")
                r = requests.post(
                    url,
                    json=data,
                    headers=self.headers
                )
                print(url)
                print(r.status_code)
                print(r.text)
                if r.status_code == 422:
                    self.stdout.write("Error: An account already exists with this email address")
            case "login":
                self.stdout.write("Login")
                data = {
                    "email": options["email"],
                    "password": options["password"]
                }
                url = urljoin(CY_DB_URL, "account/login")
                r = requests.post(url + "login", json=data)
            case "refresh":
                self.stdout.write("Refresh")
            case "sync":
                self.sync(self.headers, options)
            case _:
                pass

    @staticmethod
    def sync(headers: Dict[str, str], options: Dict[str, str]):
        """Retrieve objects from the Cybersecurity Ecosystem database and update the
        local database."""
        objects = {
            "company": "company/get_companies",
            "address": "address/get_all_adresses"
        }
        assert options["object"] in objects, "object type not handled: {}".format(
            options["object"]
        )
        headers.update({"access_token_cookie": "<TOKEN>"})
        url = urljoin(CY_DB_URL, objects[options["object"]])
        r = requests.get(url, headers=headers)
        assert r.status_code == 200, "error returned from server: {}".format(r.text)

        data = r.json()
        for elem in data["objects"]:
            Recommendations.objects.get_or_create(name=elem["name"])
