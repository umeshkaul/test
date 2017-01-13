#!/bin/sh
set -x
inl=`eval echo 'inline $1'`
#echo "ssh -t tg "'""$inl""'"" 
#cat cmd.sh
exec ssh -t tg "'""$inl""'"
