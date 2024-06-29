import argparse
import logging


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="basic argparse and logging setup")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase log level")
    return parser.parse_args()


def setup_logging(verbosity) -> logging.Logger:
    format = "%(levelname)s: %(message)s"
    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity >= 2:
        level = logging.DEBUG
    logging.basicConfig(level=level, format=format)
    return logging.getLogger(__name__)


def main():
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")


if __name__ == "__main__":
    args = parse_args()
    logger = setup_logging(args.verbose)
    main()
