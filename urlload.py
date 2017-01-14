import os , socket, time, urllib, urlparse
dns_ips = [] 

for line in file('/etc/resolv.conf', 'r'): 
	columns = line.split()
	if columns[0] == 'nameserver':
		print 'dns server {}'.format(columns[1])
#if columns[0] == 'nameserver': 
#	dns_ips.extend(columns[1:]) 

#print dns_ips 

URL = 'http://bbvpnweb.bloomberg.com'

print '\nResolving the url : ', URL 

urlinfo = urlparse.urlparse(URL)

start = time.time()
ip = socket.gethostbyname( urlinfo.netloc )
print ('\nip address {}'.format(ip))
dns_tm = time.time()-start
print '\ntime to resolve dns :\t\t{:.3f} seconds'.format( dns_tm )

start = time.time()
_data = urllib.urlopen(URL).read()
load_tm = time.time()-start
print 'time to load url :\t\t{:.3f} seconds'.format( load_tm )
#print 'url load without DNS :\t\t{:.3f} seconds'.format( load_tm-dns_tm )