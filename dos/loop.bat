SET COUNTER=1

:loop

SET /A COUNTER=COUNTER+1

ECHO %COUNTER%

nc -v -z idockbbevpngw1.bloomberg.com 4443

nc -v -z idockbbevpngw2.bloomberg.com 4443

goto loop
