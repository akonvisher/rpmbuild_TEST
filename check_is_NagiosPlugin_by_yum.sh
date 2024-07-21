#!/bin/bash
for plugin in $(ls /usr/lib64/nagios/plugins/) 
do 
	yum provides  /usr/lib64/nagios/plugins/$plugin 2>/dev/null| grep -q Filename || echo "$plugin has not been installed from yum" 
done

