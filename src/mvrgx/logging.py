import sys

import loguru
from loguru import logger

logger.remove()

def enable_logging(target_logger: 'loguru.Logger', stdout_level: str = 'INFO') -> int:
    """Adds handlers (after clearing previous ones) to the given `loguru` logger and returns their `int` identifiers.

    :param target_logger: `loguru.Logger` to add handles to.
    :param stdout_level: What level to set the `stdout` stream's handler to. Defaults to "INFO".
    :param output_dir: Specify what directory log files should be stored in for this logger.
        Defaults to the value of `squaremap_combine.project.LOGS_DIR`.

    :returns: stdout handler ID
    :rtype: int
    """
    target_logger.remove()

    target_logger.level('WARNING', color='<yellow>')
    target_logger.level('ERROR', color='<red>')

    stdout_handler = target_logger.add(
        sys.stdout,
        colorize=True,
        format="<level>{level}: {message}</level>", level=stdout_level,
        diagnose=False
    )

    return stdout_handler
