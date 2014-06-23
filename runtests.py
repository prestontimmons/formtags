#!/usr/bin/env python

from os.path import dirname, abspath
import sys

from django.conf import settings


if not settings.configured:
    settings_dict = dict(
        INSTALLED_APPS=["formtags"],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            },
        },
    )

    settings.configure(**settings_dict)


def runtests(test_labels):
    sys.path.insert(0, dirname(abspath(__file__)))

    from django.test.runner import DiscoverRunner
    failures = DiscoverRunner(
        verbosity=1,
    ).run_tests(test_labels)
    sys.exit(failures)


if __name__ == "__main__":
    labels = sys.argv[1:] or [
        "formtags",
    ]

    runtests(labels)