from basic.mylogging_helper import createDeveloplogger

# ロガー
logger = createDeveloplogger(__name__, 'log/debug.log')


class Base:
    def __init__(self, **kwargs):
        # コンストラクタで渡された内容を後から使えるように保持
        self.cluster_arn = (
            kwargs['cluster_arn'] if 'cluster_arn' in kwargs else None)
        self.secret_arn = (
            kwargs['secret_arn'] if 'secret_arn' in kwargs else None)
        self.database = kwargs['database'] if 'database' in kwargs else None

    def __repr__(self):
        return (
            f'{__class__.__name__}'
            f'(cluster_arn={self.cluster_arn},'
            f'secret_arn={self.secret_arn},'
            f'database={self.database})'
        )


class MainClass(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return (
            f'{__class__.__name__}'
            f'(cluster_arn={self.cluster_arn},'
            f'secret_arn={self.secret_arn},'
            f'database={self.database})'
        )

    @classmethod
    def builder(cls, cluster, secret, database):
        return cls(
            cluster_arn=cluster,
            secret_arn=secret,
            database=database
        )


if __name__ == '__main__':
    logger.info('開始(info)')
    target = MainClass(
        cluster_arn='A',
        secret_arn='B',
        database='C',
    )
    logger.info(f'{target}')

    target2 = MainClass.builder('A', 'B', 'C')
    logger.info(f'{target2}')
