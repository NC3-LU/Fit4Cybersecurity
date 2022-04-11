import os
import subprocess

from django.core.management.commands import makemessages


def templatize(path):
    keywords = ["label", "tooltip", "service_category", "section"]
    custom_regex = ""
    for keyword in keywords:
        custom_regex = (
            custom_regex + 's/"' + keyword + '": "(.*)"/"' + keyword + '": _("\\1")/g;'
        )

    return subprocess.check_output(
        ["sed", "-E", str.format(custom_regex), path]
    ).decode()


class BuildFile(makemessages.BuildFile):
    def preprocess(self):
        if not self.is_templatized:
            return

        file_ext = os.path.splitext(self.translatable.file)[1]
        if file_ext == ".json":
            content = templatize(self.path)
            with open(self.work_path, "w", encoding="utf-8") as fp:
                fp.write(content)
            return

        super().preprocess()


class Command(makemessages.Command):
    build_file_class = BuildFile
