#!/bin/sh

echo $1;
eval $1
ECHO_TEXT="Echo this";
ECHO_CMD="echo ${ECHO_TEXT} | awk -F' ' '{print \$1}'";
echo $ECHO_CMD;

result=`${ECHO_CMD}`;
echo $result;

result=`eval $ECHO_CMD`;
echo $result;

#result=`echo ${ECHO_TEXT} | awk -F' ' '{print \$1}'`;
#echo $result;
