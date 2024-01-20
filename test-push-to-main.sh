#!/bin/bash

docker build -t test --target test . && docker run -d -e TEST_COUNT=10 test


CONTAINERS_ID=$(docker ps -q)
RUNING_CONTAINER_COUNT=$(docker ps -q | wc -l)

while [ $RUNING_CONTAINER_COUNT -ne 0 ]
do
	EXIT_STATUS=$(docker inspect $CONTAINERS_ID -f '{{.State.ExitCode}}')
	RUNING_CONTAINER_COUNT=$(docker ps -q | wc -l)
	if [ $EXIT_STATUS -ne 0 ]
	then
		echo "TEST FAILED"
		exit 1
	fi
	sleep 1
done

echo "TEST PASS"
exit 0
