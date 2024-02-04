__author__ = "Cedric Watzl"


import logging
from pydoro.pomodoro_timer import PomodoroTimer
from pydoro.utils.logging_config import setup_logger

logger = logging.getLogger(__name__)


def test_logger() -> None:
    setup_logger()

    logger.error("Error")
    logger.warn("Warn")
    logger.debug("Debug")
    logger.info("Info")

    pass
