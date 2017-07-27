#!/usr/bin/env bash
# START AMBARI AGENTS !!!
# Run commands from guest
curl -H "X-Requested-By: ambari" -X POST -u admin:admin http://node1:8080/api/v1/blueprints/bigdata-hdp -d @blueprint.json

curl -H "X-Requested-By: ambari" -X POST -u admin:admin http://node1:8080/api/v1/clusters/bigdata-hdp -d @hostmap.json