# -*- coding: utf-8 -*-

from typing import Dict
import sys
import requests
from urllib.parse import urljoin
from django.core.management.base import BaseCommand
from survey.models import (
    Recommendations,
    # SurveyCompany
)

CY_DB_URL = "https://api.db.cy.lu/"


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

        subparser_signin = subparsers.add_parser("signin")
        subparser_login = subparsers.add_parser("login")
        # subparser_refresh = subparsers.add_parser("refresh")
        subparser_sync = subparsers.add_parser("sync")

        subparser_signin.add_argument("company", type=str, help="Company name.")
        subparser_signin.add_argument("department", type=str, help="Deparrtment name.")
        subparser_signin.add_argument("email", type=str, help="Email.")

        subparser_login.add_argument("email", type=str, help="Email.")
        subparser_login.add_argument("password", type=str, help="Password.")

        subparser_sync.add_argument("object", type=str, help="Objects to sync.")

    def handle(self, *args, **options):
        # self.stdout.write(','.join(options))
        # headers = {"Content-Type": "application/json", "accept": "application/json"}

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
                print(r.status_code)
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
            print(elem)
            Recommendations.objects.get_or_create(name=elem["name"])
