%define name	asterisknow
%define version	0
%define svnrel	r988
%define release	%mkrel 0.%{svnrel}

Summary:	AsteriskNOW. GUI for configuring Asterisk®
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Servers
# svn co http://svn.digium.com/svn/asterisk-gui/branches/asterisknow/
Source:		%{name}.%{svnrel}.tar.bz2
Patch0:		%{name}.mdv.patch
URL:		http://www.asterisknow.org/
BuildRequires:	zaptel-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	asterisk >= 1.4.0-3

%description
Asterisk® in minutes. The most popular open source PBX software,
Asterisk®, can now be easily configured with a graphical interface.
AsteriskNOW. Mandriva Linux distribution that includes Asterisk®,
the Asterisk GUI, and all other software needed for an Asterisk® system.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%configure
%make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p %{buildroot}/sbin
%makeinstall

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README
%attr(0755,asterisk,asterisk)	%dir	%{_localstatedir}/asterisk/scripts
%attr(0644,asterisk,asterisk)		%{_localstatedir}/asterisk/scripts/graphs.sh
%attr(0644,asterisk,asterisk)		%{_localstatedir}/asterisk/scripts/gui_sysinfo
%attr(0644,asterisk,asterisk)		%{_localstatedir}/asterisk/scripts/listfiles
%attr(0755,asterisk,asterisk)	%dir	%{_localstatedir}/asterisk/static-http/config
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/*.html
%attr(0755,asterisk,asterisk)	%dir	%{_localstatedir}/asterisk/static-http/config/bkps
%attr(0755,root,root)		%dir	%{_localstatedir}/asterisk/static-http/config/graphs
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/graphs/graph_cpu.svgz
%attr(0755,root,root)		%dir	%{_localstatedir}/asterisk/static-http/config/images
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/images/*.gif
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/images/*.ico
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/images/*.jpg
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/images/*.png
%attr(0755,root,root)		%dir	%{_localstatedir}/asterisk/static-http/config/scripts
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/scripts/*.js
%attr(0755,root,root)		%dir	%{_localstatedir}/asterisk/static-http/config/setup
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/setup/*.html
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/setup/digiumlogo.gif
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/setup/setup.css
%attr(0755,root,root)		%dir	%{_localstatedir}/asterisk/static-http/config/stylesheets
%attr(0644,root,root)			%{_localstatedir}/asterisk/static-http/config/stylesheets/*.css
%attr(0644,asterisk,asterisk)	%config(noreplace)	%{_sysconfdir}/asterisk/gui_custommenus.conf

/sbin/zapscan
/sbin/zapscan.bin
%{_sbindir}/zapscan
%{_sbindir}/zapscan.bin
