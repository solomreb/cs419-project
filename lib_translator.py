#!/usr/bin/env python

import json


class Translator:
    def __init__(self, locale="en"):
        language_file = "locale_{0}.json".format(locale)
        self.dictionary = json.load(open(language_file))

    def get_text(self, text):
        return u"{0}".format(self.dictionary[text])
