from elasticsearch_dsl import Search, A

query = {
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


def dslsample(es, index):
    '''
    queryをelasticsearch_dslに書き換えたサンプル
    '''

    # 検索部分（Searchオブジェクト）
    search = Search(using=es, index=index) \
        .filter('range',
                **{'@timestamp': {
                    'gte': '2020-10-01T00:00:00+09:00',
                    'lt': '2020-10-01T23:59:59+09:00',
                    'format': 'date_time_no_millis'
                }}) \
        .extra(size=0)

    # 集計部分（Aggregationオブジェクト）
    aggs_port = A("terms", field="destination.port", size=20)

    # Aggregation オブジェクトを Search オブジェクトに紐付ける
    search.aggs.bucket("port-count", aggs_port)

    result = search.execute()

    # 結果抽出(Attrlist型)
    res_bucket = result.aggregations['port-count'].buckets
    for item in res_bucket:
        print(f'port_count : {item}')


