import usage.elasticsearchUsage.elasticsample as ElasticSample
import usage.elasticsearchUsage.dsl as dsl


if __name__ == '__main__':
    host = 'localhost'
    port = 9200
    es = ElasticSample.EsClass.init_es(host, port)

    dsl.dslsample(es, 'amazon')

