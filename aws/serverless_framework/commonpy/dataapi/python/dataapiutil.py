import json
import boto3
import botocore
import loginit


class DataApiUtil:
    def __init__(self, **kwargs):
        self._logger = loginit.uselogger(__name__)
        self.cluster_arn = kwargs['cluster_arn'] if 'cluster_arn' in kwargs else None
        self.secret_arn = kwargs['secret_arn'] if 'secret_arn' in kwargs else None
        self.database = kwargs['database'] if 'database' in kwargs else None

    def __repr__(self):
        return f'{self.__class__.__name__}'

    @classmethod
    def builder(cls, cluster_arn, secret_arn, database):
        return cls(cluster_arn, secret_arn, database)

    def select(self, query: str):

        rdsData = boto3.client('rds-data')
        self.logger.info(f'{boto3.__version__}')

        self.logger.info(f'query:{query}')
        if query is None:
            return None

        # DataAPI実行
        try:
            rdsResponse = rdsData.execute_statement(
                resourceArn=self.cluster_arn,
                secretArn=self.secret_arn,
                database=self.database,
                sql=query
            )
            self.logger.info(f'res:{rdsResponse}')
        except botocore.exceptions.ClientError as e:
            self.logger.error(f'exception:{e}')
            raise e

        # レコード情報があればレスポンスボディに設定して返却
        body = rdsResponse['records'] if 'records' in rdsResponse else 'Empty'
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response


@loginit.InsertFuncLog
def hello(message, **kwargs):
    return f'{message}'


if __name__ == '__main__':
    client = DataApiUtil()
    client.logger.info(f'{client}')
    hello('world', logger=client.logger)
