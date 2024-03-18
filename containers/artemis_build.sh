#!/bin/sh
echo "$0" "$1" "$2" "$3" "$4" "$5" "$ANDY_HOME"
whoami
cd "$ANDY_HOME"
pwd
echo $PATH
cd activemq-artemis
git fetch --all
git checkout "$GIT_TAG"
git pull origin "$GIT_TAG"
VERSION=$(mvn -q \
    -Dexec.executable=echo \
    -Dexec.args='${project.version}' \
    --non-recursive \
    exec:exec)
mvn clean install -Pdev -DskipTests
cp -R artemis-distribution/target/apache-artemis-"$VERSION"-bin /home/ataylor/output