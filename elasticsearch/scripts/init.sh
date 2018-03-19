#!/usr/bin/env bash
curl -XPUT 'http://localhost:9200/test_index?pretty' -H "Content-Type: application/json" -d "@/utils/data/create-index.json"
curl -XPOST 'http://localhost:9200/test_index/_bulk?pretty' -H "Content-Type: application/json" --data-binary "@/utils/data/bulk-insert.json"