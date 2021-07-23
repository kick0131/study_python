import usage.elasticsearchUsage.elasticsample as ElasticSample
import usage.elasticsearchUsage.dsl as dsl


if __name__ == '__main__':
    host = 'localhost'
    port = 9200
    index = 'porttest'

    es = ElasticSample.EsClass()
    # es.change_es(host=host, port=port)
    # es = es.get_es()

    dsl.dslsample(es, index)
