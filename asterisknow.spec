%define name	asterisknow
%define version	0
%define svnrel	r5210
%define release	%mkrel 0.%{svnrel}.1

Summary:	GUI for configuring Asterisk
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Servers
# svn co http://svn.digium.com/svn/asterisk-gui/branches/2.0
Source:		%{name}.%{svnrel}.tar.xz
Patch:		%{name}.mdv.patch
URL:		http://www.asterisknow.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	asterisk >= 1.6.1.0

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
%attr(0644,asterisk,asterisk)		%{_localstatedir}/lib/asterisk/scripts/rebootsystem.sh
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


%changelog
* Fri Jun 03 2011 Lonyai Gergely <aleph@mandriva.org> 0-0.r5210.1mdv2011.0
+ Revision: 682635
- svn release 5210

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0-0.r4980.3mdv2011.0
+ Revision: 616626
- the mass rebuild of 2010.0 packages

* Tue Aug 25 2009 Lonyai Gergely <aleph@mandriva.org> 0-0.r4980.2mdv2010.0
+ Revision: 420844
- rebuild
- update to svn4980

* Fri Apr 03 2009 Stefan van der Eijk <stefan@mandriva.org> 0-0.r4708.1mdv2009.1
+ Revision: 363746
- svrel 4708
- svrel 4708

* Sun Mar 01 2009 Stefan van der Eijk <stefan@mandriva.org> 0-0.r4535.1mdv2009.1
+ Revision: 346835
- svnrel 4535

* Tue Jan 27 2009 Stefan van der Eijk <stefan@mandriva.org> 0-0.r4482.1mdv2009.1
+ Revision: 334632
- svrel 4482

* Tue Jan 06 2009 Stefan van der Eijk <stefan@mandriva.org> 0-0.r4394.1mdv2009.1
+ Revision: 326162
- r4394

* Tue Dec 02 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r4260.1mdv2009.1
+ Revision: 309481
- svnrel 4260

* Tue Dec 02 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r4257.1mdv2009.1
+ Revision: 309263
- svnrel 4257

* Sat Nov 29 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r4237.1mdv2009.1
+ Revision: 308127
- svnrel 4237

* Sat Oct 25 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r4017.1mdv2009.1
+ Revision: 297080
- svnrel 4017

* Tue Oct 14 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3957.1mdv2009.1
+ Revision: 293755
- svnrel 3957

* Sat Sep 27 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3910.1mdv2009.0
+ Revision: 288899
- svnrel 3910

* Sun Sep 21 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3848.1mdv2009.0
+ Revision: 286285
- svnrel 3848

* Sun Sep 14 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3814.1mdv2009.0
+ Revision: 284648
- svnrel 3814

* Sun Sep 07 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3778.1mdv2009.0
+ Revision: 282074
- svnrel 3778

* Sun Aug 24 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3702.1mdv2009.0
+ Revision: 275449
- svnrel 3702

* Fri Aug 22 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3697.1mdv2009.0
+ Revision: 275209
- svnrel 3697

* Tue Aug 19 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3677.1mdv2009.0
+ Revision: 273868
- svnrel 3677

* Thu Aug 14 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3667.2mdv2009.0
+ Revision: 272185
- fix path to scripts

* Thu Aug 14 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3667.1mdv2009.0
+ Revision: 272058
- svnrel 3667

* Sat Aug 09 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3646.1mdv2009.0
+ Revision: 270014
- svnrel 3646

* Thu Aug 07 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3636.1mdv2009.0
+ Revision: 266992
- svn rel 3636

* Fri Jul 18 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3525.1mdv2009.0
+ Revision: 238068
- svnrel r3525

* Mon Jul 07 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3420.1mdv2009.0
+ Revision: 232326
- svn rel 3420

* Wed Jun 25 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3329.1mdv2009.0
+ Revision: 228926
- svn rel 3329

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Wed May 14 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3058.2mdv2009.0
+ Revision: 207285
- rebuild

* Tue May 13 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r3058.1mdv2009.0
+ Revision: 206800
- svnrel 3058

* Sat May 10 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r2994.2mdv2009.0
+ Revision: 205415
- rebuild due to hang in Mandriva buildsys
- r2994

* Tue May 06 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r2982.1mdv2009.0
+ Revision: 202125
- r2982

* Wed Apr 02 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r2755.1mdv2009.0
+ Revision: 191567
- svnrel 2755

* Thu Mar 13 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r2542.1mdv2008.1
+ Revision: 187429
- svn rel 2542

* Thu Mar 06 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r2486.2mdv2008.1
+ Revision: 180847
- r2486

* Thu Feb 21 2008 Olivier Blin <oblin@mandriva.com> 0-0.r2332.2mdv2008.1
+ Revision: 173605
- remove package name in summary
- remove invalid trademark characters (#37944)

* Sun Feb 17 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r2332.1mdv2008.1
+ Revision: 169834
- svnrel 2332

* Fri Feb 08 2008 Stefan van der Eijk <stefan@mandriva.org> 0-0.r2309.2mdv2008.1
+ Revision: 164181
- stuck buildbot
- add missing file
- svnrel 2309

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 15 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r1990.1mdv2008.1
+ Revision: 120354
- retry
- svn rel 1990
- fix path to Master.csv

* Fri Dec 14 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r1986mdv2008.1
+ Revision: 119906
- svnrel 1986
- fix perms on static-http dir

* Sat Dec 01 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r1878mdv2008.1
+ Revision: 114292
- svnrel 1878
- svnrel 1635

* Sun Sep 09 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r1558mdv2008.0
+ Revision: 83554
- svnrel 1558

* Tue Aug 28 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r1467mdv2008.0
+ Revision: 73272
- svnrel 1467

* Sun Aug 19 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r1390mdv2008.0
+ Revision: 67165
- add missing files
- svnrel 1390

* Mon Aug 13 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r1325mdv2008.0
+ Revision: 62646
- add missing file
- svnrel 1325

* Tue Jul 24 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r1262mdv2008.0
+ Revision: 55080
- r1262

* Mon Jul 02 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r1195mdv2008.0
+ Revision: 47005
- svnrel r1195

* Sun Jun 24 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r1165mdv2008.0
+ Revision: 43762
- svn r1165

* Sat May 26 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r988mdv2008.0
+ Revision: 31401
- add files
- svnrel r988

* Sat May 19 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r961mdv2008.0
+ Revision: 28445
- svnrel 961

* Wed May 09 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r902mdv2008.0
+ Revision: 25632
- svn rel 902

* Sun Apr 22 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r728mdv2008.0
+ Revision: 16742
- svnrel r728


* Fri Apr 06 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r612mdv2007.1
+ Revision: 150877
- svn rel 612

* Tue Apr 03 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r573mdv2007.1
+ Revision: 150264
- svn rel 573

* Sat Mar 17 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r451mdv2007.1
+ Revision: 145362
- svnrel r451

* Thu Mar 15 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r439mdv2007.1
+ Revision: 144528
- r439

* Fri Feb 16 2007 Stefan van der Eijk <stefan@mandriva.org> 0-0.r351mdv2007.1
+ Revision: 121733
- add description, summary, URL
- svnrel r351
- Import asterisknow

* Sun Feb 11 2007 Stefan van der Eijk <stefan@mandriva.org> 0.0.r331
- initial Mandriva package

