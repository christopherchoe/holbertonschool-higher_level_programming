#!/bin/bash
# sends POST request with variables
curl -s "$1" -X POST -d 'email=hr@holbertonschool.com' -d 'subject=I will always be here for PLD'
