Name:           WIPP_Nagios_Plugins
Version:        0.0.2
Release:        1%{?dist}
Summary:        nagios plugins that were not installed from standard repositories

License:        Other
##Source0:        %{name}-%{version}.tar.gz 
Source0:        WIPP_Nagios_Plugins-0.0.2.tar.gz

BuildArch: noarch

##BuildRequires:  
Requires:       bash perl nagios-plugins ethtool

%description	
nagios plugins that were not installed from standard repositories
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




%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $RPM_BUILD_ROOT/usr/lib64/nagios/plugins
install -m 0755 * $RPM_BUILD_ROOT/usr/lib64/nagios/plugins/
##[ -d  /usr/lib64/nagios/plugins_test ] || mkdir -p  /usr/lib64/nagios/plugins_test
##cp * /usr/lib64/nagios/plugins_test/

%clean

rm -rf $RPM_BUILD_ROOT

%files

##%doc
/usr/lib64/nagios/plugins/*


%changelog
* Thu Jul  4 2024 Alexey Konvisher <akonvisher@gmail.com> 
- First version being packaged.
