from elasticsearch import Elasticsearch

es_client = Elasticsearch([{'host': 'es'}])

search_query = {
    "query": {
        "match": {
            "content_text": "therefore"
        }
    }
}

if __name__ == "__main__":
    res = es_client.search(index="test_index",
                           doc_type='content', body=search_query)
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print(hit["_source"])
