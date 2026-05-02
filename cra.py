import argparse
import importlib.util
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent
REDA_PATH = ROOT / 'REDA-Corporate'
MODULE_PATH = REDA_PATH / 'miller_enforcement.py'


def load_module(path: Path):
    if not path.exists():
        logger.error('Miller Enforcement modules not found. Sync from REDA-Corporate.')
        return None
    spec = importlib.util.spec_from_file_location('miller_enforcement', path)
    if spec is None or spec.loader is None:
        logger.error('Failed to create import spec for %s', path)
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description='CRA enforcement entrypoint')
    parser.add_argument('--sync', action='store_true', help='sync modules from REDA-Corporate')
    parser.add_argument('--status', action='store_true', help='print status')
    args = parser.parse_args()

    if args.sync:
        module = load_module(MODULE_PATH)
        if module and hasattr(module, 'main'):
            return module.main()
        return 2

    if args.status:
        logger.info('CRA status: ready')
        return 0

    parser.print_help()
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
