#!/bin/bash
# sends GET request and display response with header variable sent
curl -s "$1" -X GET -H 'X-HolbertonSchool-User-Id: 98'
