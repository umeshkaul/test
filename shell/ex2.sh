#!/bin/sh

#echo $1;

result=`eval echo $1`
#echo $result;
inl=`eval echo 'inline $1'`
result2=`eval echo ssh -t tg '$inl'`
echo $result2
echo echo ssh -t tg "'""$inl""'"
