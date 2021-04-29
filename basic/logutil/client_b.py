import basic.logutil.check_propagate as logutil


def calltop():
    logger = logutil.getlogger_top()
    logger.debug(f'{__name__} Root-Top 2nd call')


def callsub1():
    logger = logutil.getlogger_topsub1()
    logger.debug(f'{__name__} Root-Sub1 2nd call')


def callsub2():
    logger = logutil.getlogger_topsub2()
    logger.debug(f'{__name__} Root-Top-Sub2 2nd call')
