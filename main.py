import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main():
    """Parse the args and if all is good, summon Prime to do the computation."""
    logger.debug('Inside main()')
    print('All the work should be done in here')


if __name__ == '__main__':
    print('TODO: all the things')
    main()

