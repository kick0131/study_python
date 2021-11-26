import pprint
from opensearchpy import OpenSearch, helpers

"""
    OpenSearchは予めDockerなどで立ち上げておく
    docker pull opensearchproject/opensearch:1.1.0
    docker run -d --rm --name opensearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" opensearchproject/opensearch:1.1.0

    dotを含むフィールドの扱いについて
    https://www.elastic.co/guide/en/elasticsearch/reference/7.3/dot-expand-processor.html

    "ip.checksum": "0x000021e5"
    ↓
    "ip" : {
        "checksum" : "0x000021e5"
    }
    と解釈される

    その為、"ip.checksum.status": "2"といった、『ドットが2つあるデータ』は登録できない
    - ip.checksumがtext型であり、オブジェクト(ネスト)型ではない為
    - ip.checksum.status単独の登録も、親オブジェクト(ip.checksum)が存在しないので登録不可

    公式
    https://elasticsearch-py.readthedocs.io/en/master/helpers.html#elasticsearch.helpers.bulk


"""


# クエリを指定して検索
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
        "hira-port": {
            "terms": {
                "field": "destination.port"
            }
        }
    }
}

query_match_all = {
    "query": {"match_all": {}}
}


def gendata(index: str):
    """バルク登録用ジェネリクス
    """
    # 登録内容(list<dict>)
    students = [
        {
            "name": "Jiro",
            "age": 25,
            "email": "jiro@example.com",
            "addr": {
                "country": "japan"
            }
        },
        {
            "name": "Saburo",
            "age": 20,
            "email": "saburo@example.com",
            "addr": {
                "country": "united states"
            }
        }
        # OK
        # { "iif":"eth2","destination":{"geo":{"continent_name":"Asia","region_iso_code":"JP-13","city_name":"Tokyo","country_iso_code":"JP","region_name":"Tokyo","location":{"lon":139.7532,"lat":35.6882}},"port":"443","ip":"18.178.22.21"},"customerCode":"YSK","msgId":"1796.230913","tenantCode":"b","source":{"port":"51843","ip":"172.16.1.190"},"type":"APG","wanMac":"08:00:37:CA:6A:A6","act":"Pass","ecs":{"version":"1.6.0"},"apg":{"app":"Yahoo.com","gid":"0","bid":"6","aid":"3181","url":"ups.analytics.yahoo.com","sid":"8803181060001"},"lanMac":"20:C6:EB:65:93:3B","@timestamp":"2020-10-01T05:05:08.000Z","proto":"6"}
    ]

    for student in students:
        yield {
            "_op_type": "create",
            "_index": index,
            "_source": student
        }


def gendata2(index: str):
    """_op_type省略した場合の動作

        省略時はcreateとして動作、インデックスが無ければインデックス作成も行われる
    """
    mywords = ['foo', 'bar', 'baz']
    for word in mywords:
        yield {
            "_index": index,
            "word": word,
        }


def gendata3(index: str):
    """_id指定パターン

        _id重複時は上書き動作
        _idを指定しない場合はランダムな値が払い出されるので、基本ランダムで問題なし
    """
    ids = ['mywords_01', 'mywords_02', 'mywords_03']
    mywords = ['adam', 'bob', 'carry']
    for id, word in zip(ids, mywords):
        yield {
            "_id": id,
            "_index": index,
            "word": word,
        }


def bulklist(index: str):
    # bulkに渡すリスト
    actions = []
    docs = [
        {'zipcode': '100-0013', 'address': 'Kasumiga-seki'},
        {'zipcode': '60601-0001', 'address': 'Chicago'},
    ]

    for doc in docs:
        actions.append(
            {'_index': index, '_type': 'zip-code', '_source': doc})
    return actions


class ElasticsearchSampler():
    """Elasticsearchサンプルクラス
    """

    def __init__(self):
        host = 'localhost'
        port = 9200
        auth = ('admin', 'admin')
        # certs = 'esnode.pem'

        # Elasticsearchインタンスの作成
        self.es = OpenSearch(
            hosts=[{'host': host, 'port': port}],
            http_auth=auth,
            use_ssl=True,
            verify_certs=False,
            # ca_certs=certs,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )

    def __del__(self):
        self.es.close()
        print("close elasticsearch instance--------------------------")

    def search(self, idx: str, query: str):
        """検索
        """
        result = self.es.search(index=idx, body=query)
        print('--[search]-------------------------------------------')
        pprint.pprint(result, sort_dicts=False)

    def bulk(self, index: str):
        """バルクインサート
        """

        try:
            # iterableなオブジェクトであればよいので以下どちらも可能
            # - ジェネレータで渡す
            success, failed = helpers.bulk(self.es, gendata3(index))
            # - list型で渡す
            # success, failed = helpers.bulk(self.es, bulklist())
        # except opensearchpy.ElasticsearchException as e:
        #     pprint.pprint(e)
        except Exception as e:
            pprint.pprint(e)
            return

        print('--[bulk  ]-------------------------------------------')
        pprint.pprint(success)
        pprint.pprint(failed)

    def delete_by_query(self, idx: str, query: str):
        """条件指定の削除
        """
        result = self.es.delete_by_query(index=idx, body=query)

        print(f'{type(result)}')
        print('--[delete_by_query]----------------------------------')
        pprint.pprint(result, sort_dicts=False)


def main():

    es = ElasticsearchSampler()
    target_index = 'mywords'

    # 一括登録
    # es.bulk(target_index)

    # 削除
    # es.delete_by_query(target_index, query_match_all)

    # 検索
    es.search(target_index, query_match_all)
    # es.search("*", query_match_all)


if __name__ == '__main__':
    main()
