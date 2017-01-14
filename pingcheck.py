import subprocess
from subprocess import Popen
#p1 = subprocess.Popen(['ping','-c 2', 'bbe.bloomberg.com'], stdout=subprocess.PIPE)
p1=subprocess.Popen(['fping','-C5','-q', 'bbvpnweb.bloomberg.com'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#output = p1.communicate()[0]
##proc = Popen(["ping","www.google.com"])
#proc.wait()
#print p1.returncode()
result = p1.communicate()[1]
output = result.split()
#print output
#print output[2] , output[3] , output[4]
print('ping latency for {}\n {} ms\n {} ms\n {} ms\n {} ms\n'.format(output[0] ,output[2] , output[3] , output[4], output[5]))


