from elasticsearch import Elasticsearch
import json
import pprint


class esclass:

    def __init__(self):
        self.es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
        infodata = self.es.info()
        print('-- print es.info() ----------------------------')
        pprint.pprint(infodata, indent=2)

    def __del__(self):
        self.es.close()

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

    es = esclass()
    for item in (query, query2):
        result = es.search(item)
        print('-- print es.search() ----------------------------')
        print(json.dumps(result, indent=2))
        result = es.count(item)
        print('-- print es.count() ----------------------------')
        print(json.dumps(result, indent=2))
