from elasticsearch import Elasticsearch
import pprint


def essample(query):
    es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])
    es.info()
    result = es.search(index='amazon', body=query)
    pprint.pprint(f'{result}')
    es.close()


if __name__ == '__main__':
    query = {
        'query': {
            'match_all': {}
        }
    }
    essample(query)
