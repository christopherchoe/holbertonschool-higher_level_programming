#!/bin/bash
# sends url request and displays size of body
curl -s -w %{size_download} -o /dev/null
