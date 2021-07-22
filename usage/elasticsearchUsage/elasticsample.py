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
            self.es.close()
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
            self.es.close()
            self.es = Elasticsearch(
                hosts=[{'host': host, 'port': port}],
                timeout=timeout,
                max_retry=max_retry,
                retry_on_timeout=True
            )

    def search(self, query: str):
        return self.es.search(index='amazon', body=query)

    def count(self, query: str):
        return self.es.count(index='amazon', body=query)


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

    es = EsClass()
    for item in (query, query2):
        result = es.search(item)
        print('-- print es.search() ----------------------------')
        print(json.dumps(result, indent=2))
        result = es.count(item)
        print('-- print es.count() ----------------------------')
        print(json.dumps(result, indent=2))
