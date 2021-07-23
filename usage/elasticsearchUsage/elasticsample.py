from elasticsearch import Elasticsearch
import json
import pprint


class EsClass:
    host = 'localhost'
    port = 9200

    def __init__(self):
        self.es = Elasticsearch(hosts=[{'host': self.host, 'port': self.port}])
        infodata = self.es.info()
        print('-- print es.info() ----------------------------')
        pprint.pprint(infodata, indent=2)

    def __del__(self):
        self.es.close()
        pass

    def get_es(self):
        return self.es

    def change_es(
            self, host, port, timeout=10, max_retry=0, http_auth=False,
            user=None, pwd=None, certs=None):
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
    query = {
        'query': {
            'match_all': {}
        }
    }
    query2 = {
        'query': {
            'exists': {
                'field': 'founder'
            }
        }
    }
    # createdAtの部分は@timestampがよく使われる
    query3 = {
        'query': {
            'range': {
                "createdAt": {
                    "gte": "2020-07-01T00:00:00+09:00",
                    "lte": "2020-08-02T23:59:59+09:00",
                    "format": "date_time_no_millis"
                }
            }
        }
    }

    es = EsClass()
    # for index, item in [("amazon", query), ("porttest", query3)]:
    for index, item in [("porttest", query3)]:
        result = es.search(index, item)
        print(
            f'-- print es.search() index:{index} ----------------------------')
        print(json.dumps(result, indent=2))
        # result = es.count(index, item)
        # print(
        #     f'-- print es.count() index:{index} ----------------------------')
        # print(json.dumps(result, indent=2))
