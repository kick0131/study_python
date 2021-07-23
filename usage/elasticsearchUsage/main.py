import usage.elasticsearchUsage.dsl as dsl


if __name__ == '__main__':
    host = 'localhost'
    port = 9200
    index = 'porttest'

    es = dsl.EsClassDsl(host, port)
    es.change_es(host=host, port=port)
    es.dslsample(index)
