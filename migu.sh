#!/usr/bin/env bash 
#咪咕账号1
echo '------------------sign 1------------------'
curl -H "Cookie: ${MIGUCOOKIE1}" -H "Content-Type: application/json; charset=UTF-8" -X POST -d '{}' 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-activity-custom/sign/sendAward'
echo ''
#咪咕账号2
echo '------------------sign 2------------------'
curl -H "Cookie: ${MIGUCOOKIE2}" -H "Content-Type: application/json; charset=UTF-8" -X POST -d '{}' 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-activity-custom/sign/sendAward'
echo ''
#咪咕账号3
echo '------------------sign 3------------------'
curl -H "Cookie: ${MIGUCOOKIE3}" -H "Content-Type: application/json; charset=UTF-8" -X POST -d '{}' 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-activity-custom/sign/sendAward'
echo ''
#咪咕账号4
echo '------------------sign 4------------------'
curl -H "Cookie: ${MIGUCOOKIE4}" -H "Content-Type: application/json; charset=UTF-8" -X POST -d '{}' 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-activity-custom/sign/sendAward'
echo ''
#咪咕账号5
echo '------------------sign 5------------------'
curl -H "Cookie: ${MIGUCOOKIE5}" -H "Content-Type: application/json; charset=UTF-8" -X POST -d '{}' 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-activity-custom/sign/sendAward'
echo ''
#咪咕账号6
echo '------------------sign 6------------------'
curl -H "Cookie: ${MIGUCOOKIE6}" -H "Content-Type: application/json; charset=UTF-8" -X POST -d '{}' 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-activity-custom/sign/sendAward'
echo ''
#咪咕账号6
echo '------------------sign 7------------------'
curl -H "Cookie: ${MIGUCOOKIE7}" -H "Content-Type: application/json; charset=UTF-8" -X POST -d '{}' 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-activity-custom/sign/sendAward'
echo ''
