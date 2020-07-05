from loggingHelper import createDeveloplogger

# ロガー
logger = createDeveloplogger(__name__, 'log/debug.log')


def genSample():
    """ジェネレータのサンプル
    """

    # 式をカッコでくくればgenerator
    it = (len(x) for x in open('log/debug.log'))
    logger.debug(type(it))

    logger.debug(next(it))
    logger.debug(next(it))

    # generatorからさらにgeneratorを作る。平方根の計算。
    roots = ((x, x**0.5) for x in it)
    logger.debug(next(roots))


if __name__ == '__main__':
    logger.info('開始(info)')
    genSample()
