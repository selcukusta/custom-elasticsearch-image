FROM docker.elastic.co/elasticsearch/elasticsearch:6.2.2

RUN useradd -r -g elasticsearch 1000

ADD ./scripts/init.sh /utils/init.sh
ADD ./json-files/create-index.json /utils/data/create-index.json
ADD ./json-files/bulk-insert.json /utils/data/bulk-insert.json
ADD ./scripts/wait-for-it.sh /utils/wait-for-it.sh

USER elasticsearch

RUN bin/elasticsearch -E "cluster.name=TestCluster" -E "xpack.security.enabled=false" -p /tmp/epid & /bin/bash /utils/wait-for-it.sh -t 0 localhost:9200 -- /utils/init.sh; kill $(cat /tmp/epid) && wait $(cat /tmp/epid); exit 0;