from elasticsearch import Elasticsearch
import json
import pprint


class EsClass:
    def __init__(self, host: str, port: int):
        self.es = Elasticsearch(hosts=[{'host': host, 'port': port}])
        infodata = self.es.info()
        print('-- print es.info() ----------------------------')
        pprint.pprint(infodata, indent=2)

    def __del__(self):
        self.es.close()
        pass

    def change_es(
            self, host: str, port: int, timeout: int = 10, max_retry: int = 0,
            http_auth: bool = False,
            user: str = None, pwd: str = None, certs: str = None):
        """接続先を変更

        Args:
            host (str): Elasticsearchホスト
            port (int): 接続先ポート
            timeout (int, optional): タイムアウト秒. Defaults to 10.
            max_retry (int, optional): リトライ数. Defaults to 0.
            http_auth (bool, optional): HTTP認証の利用有無. Defaults to False.
            user (str, optional): HTTP認証時のID. Defaults to None.
            pwd (str, optional): HTTP認証時のパスワード. Defaults to None.
            certs (str, optional): SSL利用時の秘密鍵ファイルパス. Defaults to None.
        """
        if http_auth:
            self.es = Elasticsearch(
                hosts=[{'host': host, 'port': port}],
                http_auth=(user, pwd),
                verify_certs=True,
                ca_certs=certs,
                timeout=timeout,
                max_retry=max_retry,
                retry_on_timeout=True,
                scheme="https",
                port=30001
            )
        else:
            self.es = Elasticsearch(
                hosts=[{'host': host, 'port': port}],
                timeout=timeout,
                max_retry=max_retry,
                retry_on_timeout=True
            )

    def search(self, index: str, query: str):
        return self.es.search(index=index, body=query)

    def count(self, index: str, query: str):
        return self.es.count(index=index, body=query)


if __name__ == '__main__':
    # 全検索
    query = {
        'query': {
            'match_all': {}
        }
    }
    # フィールド検索
    query2 = {
        'query': {
            'exists': {
                'field': 'founder'
            }
        }
    }
    # 時間範囲、createdAtの部分は@timestampがよく使われるが
    # date型であれば別のフィールドでも指定可能
    query3 = {
        'query': {
            'range': {
                "createdAt": {
                    "gte": "2020-07-01T00:00:00+09:00",
                    "lt": "2020-08-02T23:59:59+09:00",
                    "format": "date_time_no_millis"
                }
            }
        }
    }
    # 時間範囲で対象を絞って集計
    query4 = {
        'query': {
            'range': {
                "createdAt": {
                    "gte": "2020-07-01T00:00:00+09:00",
                    "lt": "2020-08-02T23:59:59+09:00",
                    "format": "date_time_no_millis"
                }
            }
        },
        "aggs": {
            "port-count": {
                "terms": {
                    "field": "port"
                }
            }
        }
    }

    host = 'localhost'
    port = 9200
    es = EsClass(host, port)
    # for index, item in [("amazon", query), ("porttest", query3)]:
    for index, item in [("porttest", query4)]:
        result = es.search(index, item)
        print(
            f'-- print es.search() index:{index} ----------------------------')
        print(json.dumps(result, indent=2))
        # result = es.count(index, item)
        # print(json.dumps(result, indent=2))
