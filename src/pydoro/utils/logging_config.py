import logging

level = logging.DEBUG


def setup_logger():
    # create logger
    logger = logging.getLogger("project")
    logger.setLevel(level)

    # create console handler and set level to debug
    consoleHdlr = logging.StreamHandler()
    consoleHdlr.setLevel(level)

    # create formatter
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    # add formatter to ch
    consoleHdlr.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(consoleHdlr)
