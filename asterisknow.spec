%define name	asterisknow
%define version	0
%define svnrel	r4708
%define release	%mkrel 0.%{svnrel}.1

Summary:	GUI for configuring Asterisk
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Servers
# svn co http://svn.digium.com/svn/asterisk-gui/branches/2.0
Source:		%{name}.%{svnrel}.tar.bz2
Patch:		%{name}.mdv.patch
URL:		http://www.asterisknow.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	asterisk >= 1.4.0-3

%description
Asterisk in minutes. The most popular open source PBX software,
Asterisk, can now be easily configured with a graphical interface.
AsteriskNOW. Mandriva Linux distribution that includes Asterisk,
the Asterisk GUI, and all other software needed for an Asterisk system.

%prep
%setup -q -n 2.0
%patch -p0

%build
%configure
%make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"
%makeinstall
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/lib/asterisk/sounds/record

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README
%attr(0755,asterisk,asterisk)	%dir	%{_localstatedir}/lib/asterisk/gui_backups
%attr(0755,asterisk,asterisk)	%dir	%{_localstatedir}/lib/asterisk/scripts
%attr(0644,asterisk,asterisk)		%{_localstatedir}/lib/asterisk/scripts/dldsoundpack
%attr(0755,asterisk,asterisk)		%{_localstatedir}/lib/asterisk/scripts/detectdahdi.sh
%attr(0644,asterisk,asterisk)		%{_localstatedir}/lib/asterisk/scripts/editmisdn.sh
%attr(0644,asterisk,asterisk)		%{_localstatedir}/lib/asterisk/scripts/editzap.sh
%attr(0644,asterisk,asterisk)		%{_localstatedir}/lib/asterisk/scripts/listfiles
%attr(0644,asterisk,asterisk)		%{_localstatedir}/lib/asterisk/scripts/mastercsvexists
%attr(0644,asterisk,asterisk)		%{_localstatedir}/lib/asterisk/scripts/registerg729.sh
%attr(0644,asterisk,asterisk)		%{_localstatedir}/lib/asterisk/scripts/restorebackup
%attr(0644,asterisk,asterisk)		%{_localstatedir}/lib/asterisk/scripts/takebackup
%attr(0755,asterisk,asterisk)	%dir	%{_localstatedir}/lib/asterisk/sounds/record
%attr(0755,asterisk,asterisk)	%dir	%{_localstatedir}/lib/asterisk/static-http/config
%attr(0644,root,root)			%{_localstatedir}/lib/asterisk/static-http/config/*.html
%attr(0755,root,root)		%dir	%{_localstatedir}/lib/asterisk/static-http/config/images
%attr(0644,root,root)			%{_localstatedir}/lib/asterisk/static-http/config/images/*.gif
%attr(0644,root,root)			%{_localstatedir}/lib/asterisk/static-http/config/images/*.ico
%attr(0644,root,root)			%{_localstatedir}/lib/asterisk/static-http/config/images/*.jpg
%attr(0644,root,root)			%{_localstatedir}/lib/asterisk/static-http/config/images/*.png
%attr(0755,root,root)		%dir	%{_localstatedir}/lib/asterisk/static-http/config/js
%attr(0644,root,root)			%{_localstatedir}/lib/asterisk/static-http/config/js/*.js
%attr(0755,asterisk,asterisk)	%dir	%{_localstatedir}/lib/asterisk/static-http/config/private
%attr(0755,asterisk,asterisk)	%dir	%{_localstatedir}/lib/asterisk/static-http/config/private/bkps
%attr(0755,root,root)		%dir	%{_localstatedir}/lib/asterisk/static-http/config/stylesheets
%attr(0644,root,root)			%{_localstatedir}/lib/asterisk/static-http/config/stylesheets/*.css
%attr(0644,root,root)			%{_localstatedir}/lib/asterisk/static-http/index.html
