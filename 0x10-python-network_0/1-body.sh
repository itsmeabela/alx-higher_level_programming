#!/bin/bash
# script that takes in a URL, sends GET and displays body of response
curl -sLX GET "$1"
