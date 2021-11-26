import pprint
from opensearchpy import OpenSearch, helpers
from elasticsearch_dsl import Search, A
from elasticsearch import (RequestsHttpConnection, Elasticsearch)

query_agg = {
    "size": 0,
    "query": {
        "range": {
            "@timestamp": {
                "gte": "2020-10-01T00:00:00+09:00",
                "lte": "2020-10-01T23:59:59+09:00",
                "format": "date_time_no_millis"
            }
        }
    },
    "aggs": {
        "port-count": {
            "terms": {
                "field": "destination.port"
            }
        }
    }
}

query_match_all = {
    "query": {"match_all": {}}
}


class ElasticsearchSampler():
    """Elasticsearchサンプルクラス
    """

    def __init__(self):
        host = 'localhost'
        port = 9200
        auth = ('admin', 'admin')
        certs = 'cert/root-ca.pem'

        # Elasticsearchインタンスの作成
        self.es = OpenSearch(
            hosts=[{'host': host, 'port': port}],
            http_auth=auth,
            use_ssl=True,
            verify_certs=True,
            ca_certs=certs,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )

    def __del__(self):
        # ElasticsearchインスタンスのCLOSE
        self.es.close()
        print("close elasticsearch instance--------------------------")

    def search(self, idx: str, query: str):

        result = self.es.search(index=idx, body=query)

        print(f'{type(result)}')
        print('--[search]-------------------------------------------')
        pprint.pprint(result, sort_dicts=False)

    def dslusage(self, index):
        # 検索部分（Searchオブジェクト）
        s = Search(using=self.es, index=index)
        s = s.filter('range',
                     **{'@timestamp': {
                        'gte': '2020-10-01T00:00:00+09:00',
                        'lte': '2020-10-01T23:59:59+09:00',
                        'format': 'date_time_no_millis'
                        }})
        s = s.extra(size=0)

        # 集計部分（Aggregationオブジェクト）
        aggs_port = A("terms", field="destination.port", size=20)

        # Aggregation オブジェクトを Search オブジェクトに紐付ける
        s.aggs.bucket("port-count", aggs_port)

        result = s.execute()

        # 結果抽出(Attrlist型)
        res_bucket = result.aggregations['port-count'].buckets
        print(f'==res_bucket : {res_bucket}')
        for item in res_bucket:
            print(f'port_count : {item}')


def main():

    es = ElasticsearchSampler()

    # 動作確認
    # es.search("customer", query_match_all)

    # 通常の集計クエリ
    es.search("customer", query_agg)

    # elasticsearch_dslを使用した集計クエリ
    es.dslusage('customer')


if __name__ == '__main__':
    main()
