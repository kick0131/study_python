import basic.logutil.check_propagate as logutil


def calltop():
    logger = logutil.getlogger_top()
    logger.error(f'{__name__} Root-Top 1st call')


def callsub1():
    logger = logutil.getlogger_topsub1()
    logger.error(f'{__name__} Root-Sub1 1st call')


def callsub2():
    logger = logutil.getlogger_topsub2()
    logger.error(f'{__name__} Root-Top-Sub2 1st call')
