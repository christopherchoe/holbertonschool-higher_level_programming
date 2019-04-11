#!/bin/bash
# display methods server will accept
curl -sI "$1" | grep Allow | sed 's/Allow: //g'
