from usage.elasticsearchUsage.elasticsample import EsClass
from elasticsearch_dsl import Search, A

# サンプル
query = {
    "size": 0,
    "query": {
        "range": {
            "@timestamp": {
                "gte": "2020-08-01T00:00:00+09:00",
                "lte": "2020-08-01T23:59:59+09:00",
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


class EsClassDsl(EsClass):
    def __init__(self, host, port):
        super().__init__(host, port)

    def dslsample(self, index):
        '''
        queryをelasticsearch_dslに書き換えたサンプル
        '''

        # 検索部分（Searchオブジェクト）
        s = Search(using=self.es, index=index) \
            .filter('range',
                    **{'createdAt': {
                        'gte': '2020-07-01T00:00:00+09:00',
                        'lt': '2020-08-01T23:59:59+09:00',
                        'format': 'date_time_no_millis'
                    }}) \
            .extra(size=0)
        print(f'XXX : {s.to_dict()}')

        # 集計部分（Aggregationオブジェクト）
        aggs_port = A("terms", field="port", size=20)

        # Aggregation オブジェクトを Search オブジェクトに紐付ける
        s.aggs.bucket("port-count", aggs_port)

        result = s.execute()

        # 結果抽出(Attrlist型)
        res_bucket = result.aggregations['port-count'].buckets
        for item in res_bucket:
            print(f'port_count : {item}')
