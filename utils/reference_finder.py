import logging
import subprocess
import re
import sys

log = logging.getLogger(sys.modules[__name__].__name__)

FLAG_REGEX = "(?:get_value|getValue|getValueAsync|GetValue|GetValueAsync|GetValueForUser)(?:.*?\s*?)?\((?:.*?\s*?)(?:[\"'])(?P<flag>.+?)(?:[\"'])"


class ReferenceFinder:
    def __init__(self,
                 path):
        self._path = path

    def find_references(self):
        try:
            log.info("Searching for ConfigCat setting references.")
            args = ["ag", "-s", "-o", FLAG_REGEX, self._path]
            result = subprocess.check_output(args)

            matches = re.findall(FLAG_REGEX, result.decode("utf-8"))
            log.info("%s references found.", len(matches))
            flags = []
            for match in matches:
                flags.append(match.strip())

            distinct = set(flags)
            log.debug("Distinct setting reference keys: %s", distinct)
            return distinct
        except subprocess.CalledProcessError:
            log.warning("No feature flag references found!")
            return set()
