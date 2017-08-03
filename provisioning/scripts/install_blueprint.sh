#!/usr/bin/env bash
# START AMBARI AGENTS !!!
# Run commands from guest

#register
curl -H "X-Requested-By: ambari" -X POST -u admin:admin http://node1:8080/api/v1/blueprints/bigdata-hdp -d @blueprint.json

#install
curl -H "X-Requested-By: ambari" -X POST -u admin:admin http://node1:8080/api/v1/clusters/bigdata-hdp -d @hostmap.json

#retrieve
curl -H "X-Requested-By: ambari" -X GET -u admin:admin http://node1:8080/api/v1/clusters/bigdata-hdp?format=blueprint