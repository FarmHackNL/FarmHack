#!/bin/bash
# file: main.sh
# Created by: Gert Sterenborg: gert@sterenborg.nu


## open the crop-r api key
if [ ! -f api-key.txt ]; 
then
	echo "------ERROR!------"
    echo "api-key.txt not found!"
    echo "Create file with CROPRAPIKEY=xxxx"
    echo "Where xxxx= the sessionid cookie"
    exit 1
else
	source api-key.txt
	# echo $CROPRAPIKEY
fi

# create folder if not exists
mkdir -p tmp

## open python script which handles downloading the data and transform it.
python fetch-and-transform.py $CROPRAPIKEY
