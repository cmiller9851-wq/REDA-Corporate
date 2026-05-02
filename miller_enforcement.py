import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info('Miller Enforcement module loaded')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
