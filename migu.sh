#!/usr/bin/env bash 
#咪咕账号1
echo '------------------sign------------------'
curl -H "Cookie: ${MIGUCOOKIE1}" -X POST 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-sign/sign'
echo ''
echo '---------------check sign---------------'
curl -H "Cookie: ${MIGUCOOKIE1}" -X POST 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-sign/checkSign'

#咪咕账号2
echo '------------------sign------------------'
curl -H "Cookie: ${MIGUCOOKIE2}" -X POST 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-sign/sign'
echo ''
echo '---------------check sign---------------'
curl -H "Cookie: ${MIGUCOOKIE2}" -X POST 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-sign/checkSign'

#咪咕账号3
echo '------------------sign------------------'
curl -H "Cookie: ${MIGUCOOKIE3}" -X POST 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-sign/sign'
echo ''
echo '---------------check sign---------------'
curl -H "Cookie: ${MIGUCOOKIE3}" -X POST 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-sign/checkSign'

#咪咕账号4
echo '------------------sign------------------'
curl -H "Cookie: ${MIGUCOOKIE4}" -X POST 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-sign/sign'
echo ''
echo '---------------check sign---------------'
curl -H "Cookie: ${MIGUCOOKIE4}" -X POST 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-sign/checkSign'

