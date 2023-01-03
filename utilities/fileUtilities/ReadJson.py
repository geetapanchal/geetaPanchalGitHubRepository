import pytest


class ReadJson:

    def readJson(fileName):
        # read menu json
        with open(fileName) as f:
            read_data = f.read()
        f.closed

        return read_data
