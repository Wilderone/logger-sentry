import logging
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename='access.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)


class OnlyInfoFliter:
    def filter(self, logRecord):
        return logRecord.levelno == logging.INFO


handler.addFilter(OnlyInfoFliter())
LOG.addHandler(handler)
