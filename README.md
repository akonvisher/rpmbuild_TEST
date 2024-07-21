This is the nagios plugins that were not installed from standard repositories
________________________________________________________________________________
check_ethtool:
Check Linux media settings using ethtool
anders@fupp.net, 2007-09-19
_________________________________________________________________________________
check_mcelog:
Monitoring plugin to check for hardware errors logged by mcelog
_________________________________________________________________________________
check_systemd:
Based on https://lzone.de/blog/Nagios-Check-for-Systemd-Failed-Units
_________________________________________________________________________________
check_user_implementation:
 Version: MPL 2.0
Check if a specified user exists and that he has the correct userId and groupId.

 author: Daniel Werdermann / dwerdermann@web.de
 projectsite: https://github.com/echocat/nagios-plugin-check_userimplementation
 veriosn: 1.3
 date: 2012-12-30 14:21:44Z
_________________________________________________________________________________
check_writable:
Checks is the folder writable or is reliable writable
_________________________________________________________________________________

to create SOURCE archive:
tar cf SOURCES/WIPP_Nagios_Plugins-0.0.2.tar.gz BUILD/WIPP_Nagios_Plugins-0.0.2

to build RPM:
rpmbuild -bb SPECS/WIPP_Nagios_Plugins.spec
or
rpmbuild -bb SPECS/WIPP_Nagios_Plugins_for_wipp-www.spec #For wipp-www server
