# TODO
#        file /usr/lib64/libgssapi.la from install of libgssapi-devel-0.9-1.amd64 conflicts with file from package heimdal-devel-0.7.2-4.amd64
#        file /usr/lib64/libgssapi.so from install of libgssapi-devel-0.9-1.amd64 conflicts with file from package heimdal-devel-0.7.2-4.amd64
#
# Conditional build:
%bcond_without	x11	# without X11-based utilities
#
Summary:	Heimdal implementation of Kerberos V5 system
Summary(pl):	Implementacja Heimdal systemu Kerberos V5
Name:		heimdal
Version:	0.7.2
Release:	5
License:	Free
Group:		Networking
Source0:	ftp://ftp.pdc.kth.se/pub/heimdal/src/%{name}-%{version}.tar.gz
# Source0-md5:	c937580d6f8b11bf7f0e540530e1dc18
Source1:	%{name}.init
Source2:	%{name}.logrotate
Source3:	%{name}.sysconfig
Source4:	%{name}-krb5.conf
Source5:	%{name}-ftpd.inetd
Source6:	%{name}-rshd.inetd
Source7:	%{name}-telnetd.inetd
Source8:	%{name}-kadmind.inetd
Source9:	%{name}-kpasswdd.init
Source10:	%{name}-kpasswdd.sysconfig
Patch0:		%{name}-paths.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-am_man_fixes.patch
Patch3:		%{name}-amfix.patch
Patch4:		%{name}-dbpaths.patch
Patch5:		%{name}-system-comm_err.patch
Patch6:		%{name}-acfixes.patch
Patch7:		%{name}-no-editline.patch
Patch8:		%{name}-gcc4.patch
Patch9:		%{name}-db4.patch
Patch10:	%{name}-libadd.patch
Patch11:	ftp://ftp.pdc.kth.se/pub/heimdal/src/%{name}-0.7.2-setuid-patch.txt
URL:		http://www.pdc.kth.se/heimdal/
%{?with_x11:BuildRequires:	XFree86-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	flex
BuildRequires:	libcom_err-devel >= 1.34-5
BuildRequires:	libtool
BuildRequires:	mawk
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	texinfo
Requires:	%{name}-libs = %{version}-%{release}
Conflicts:	krb5-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_sbindir}
%define		_localstatedir	/var/lib/%{name}
%define		_sysconfdir	/etc/%{name}

%description
Heimdal is a free implementation of Kerberos 5. The goals are to:
- have an implementation that can be freely used by anyone
- be protocol compatible with existing implementations and, if not in
  conflict, with RFC 1510 (and any future updated RFC)
- be reasonably compatible with the M.I.T Kerberos V5 API
- have support for Kerberos V5 over GSS-API (RFC1964)
- include the most important and useful application programs (rsh,
  telnet, popper, etc.)
- include enough backwards compatibility with Kerberos V4
- IPv6 support

%description -l pl
Heimdal jest darmow± implementacj± Kerberosa 5. G³ówne zalety to:
- implementacja, która mo¿e byæ u¿ywana przez ka¿dego
- kompatybilno¶æ na poziomie protoko³u z istniej±cymi implementacjami
- racjonalna kompatybilno¶æ z M.I.T Kerberos V5 API
- wsparcie dla Kerberosa 5 poprzez GSS-API (RFC1964)
- zawiera wiêkszo¶æ istotnych i u¿ytecznych aplikacji (rsh, telnet,
  popper, etc.)
- zawiera wystarczaj±c± kompatybilno¶æ z Kerberos V4
- wsparcie dla IPv6

%package server
Summary:	Kerberos Server
Summary(pl):	Serwer Kerberosa
Group:		Networking
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	rc-scripts

%description server
Master KDC.

%description server -l pl
G³ówne centrum dystrybucji kluczy (KDC).

%package libs
Summary:	Heimdal shared libraries
Summary(pl):	Biblioteki wspó³dzielone dla heimdal
Group:		Libraries
Requires(post,postun):	/sbin/ldconfig

%description libs
Package contains shared libraries required by several of the other
heimdal packages.

%description libs -l pl
Pakiet zawiera biblioteki wspó³dzielone dla heimdal.

%package login
Summary:	login is used when signing onto a system
Summary(pl):	Narzêdzie do logowania w systemie
Group:		Applications/Networking
Requires:	%{name}-libs = %{version}-%{release}
#Provides:	login
#Obsoletes:	login

%description login
login is used when signing onto a system. It can also be used to
switch from one user to another at any time (most modern shells have
support for this feature built into them, however). This package
contain kerberized version login program.

%description login -l pl
login jest u¿ywany przy logowaniu do systemu. Mo¿e byæ tak¿e u¿yty do
prze³±czenia z jednego u¿ytkownika na innego w dowolnej chwili
(wiêkszo¶æ wspó³czesnych shelli ma wbudowan± obs³ugê tego). Ten pakiet
zawiera skerberyzowan± wersjê programu login.

%package ftp
Summary:	The standard UNIX FTP (file transfer protocol) client
Summary(pl):	Klient protoko³u FTP
Group:		Applications/Networking
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	ftp
Conflicts:	heimdal-clients

%description ftp
The FTP package provides the standard UNIX command-line FTP client
with kerberos authentication support. FTP is the file transfer
protocol, which is a widely used Internet protocol for transferring
files and for archiving files.

%description ftp -l pl
Ten pakiet dostarcza standardowego klienta FTP z wbudowan± obs³ug±
kerberosa. FTP jest protoko³em do przesy³ania plików szeroko
rozpowszechnionym w Internecie.

%package rsh
Summary:	Clients for remote access commands (rsh, rlogin, rcp)
Summary(pl):	Klient zdalnego dostêpu (rsh, rlogin, rcp)
Group:		Applications/Networking
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	rsh
Conflicts:	heimdal-clients

%description rsh
The rsh package contains a set of programs which allow users to run
commands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp). All three of these commands
use rhosts style authentication. This package contains the clients
needed for all of these services.

%description rsh -l pl
Ten pakiet zawiera zestaw narzêdzi pozwalaj±cych na wykonywanie
poleceñ na zdalnych maszynach, logowanie na inne maszyny oraz
kopiowanie plików pomiêdzy maszynami (rsh, rlogin, rcp).

%package telnet
Summary:	Client for the telnet remote login
Summary(pl):	Klient us³ugi telnet
Group:		Applications/Networking
Requires:	%{name}-libs = %{version}-%{release}
Provides:	telnet
Obsoletes:	telnet
Conflicts:	heimdal-clients

%description telnet
Telnet is a popular protocol for remote logins across the Internet.
This package provides a command line telnet client.

%description telnet -l pl
Telnet jest popularnym protoko³em zdalnego logowania. Ten pakiet
zawiera klienta tej us³ugi.

%package ftpd
Summary:	The standard UNIX FTP (file transfer protocol) server
Summary(pl):	Serwer FTP
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	ftpd

%description ftpd
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

%description ftpd -l pl
FTP jest protoko³em transmisji plików szeroko rozpowszechnionym w
Internecie.

%package rshd
Summary:	Server for remote access commands (rsh, rlogin, rcp)
Summary(pl):	Serwer zdalnego dostêpu (rsh, rlogin, rcp)
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	rshd

%description rshd
The rsh package contains a set of programs which allow users to run
commmands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp). All three of these commands
use rhosts style authentication. This package contains servers needed
for all of these services.

%description rshd -l pl
Ten pakiet zawiera zestaw serwerów pozwalaj±cych na wykonywanie
poleceñ na zdalnych maszynach, logowanie na inne maszyny oraz
kopiowanie plików pomiêdzy maszynami (rsh, rlogin, rcp).

%package telnetd
Summary:	Server for the telnet remote login
Summary(pl):	Serwer protoko³u telnet
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	telnetd

%description telnetd
Telnet is a popular protocol for remote logins across the Internet.
This package provides a telnet daemon which allows remote logins into
the machine it is running on.

%description telnetd -l pl
Telnet jest popularnym protoko³em zdalnego logowania. Ten pakiet
zawiera serwer pozwalaj±cy na zdalne logowanie siê klientów na maszynê
na której dzia³a.

%package daemons
Summary:	Kerberos daemons programs for use on servers
Summary(pl):	Serwery popularnych us³ug, autoryzuj±ce przy pomocy kerberosa
Group:		Networking
Requires:	%{name}-libs = %{version}-%{release}

%description daemons
Kerberos Daemons.

%description daemons -l pl
Demony korzystaj±ce z systemu Kerberos do autoryzacji dostêpu.

%package devel
Summary:	Header files for heimdal
Summary(pl):	Pliki nag³ówkowe i dokumentacja do bibliotek heimdal
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	db-devel
Requires:	libcom_err-devel >= 1.34-5
Requires:	openssl-devel

%description devel
contains files needed to compile and link software using the kerberos
libraries.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do bibliotek heimdal.

%package static
Summary:	Static heimdal libraries
Summary(pl):	Biblioteki statyczne heimdal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Satatic heimdal libraries.

%description static -l pl
Biblioteki statyczne heimdal.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
rm -f acinclude.m4
%{__libtoolize}
%{__aclocal} -I cf
%{__autoconf}
%{__automake}
# glibc glob() has no support to GLOB_QUOTE and GLOB_LIMIT/GLOB_MAXPATH
# rename internal libroken glob/globfree
export CPPFLAGS="-Dglob=heimdal_glob -Dglobfree=heimdal_globfree"
%configure \
	--enable-shared \
	--enable-static \
	--enable-new-des3-code \
	--with-openldap=/usr \
	--with-readline=/usr \
		--with%{!?with_x11:out}-x \
	--with-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_localstatedir},%{_sysconfdir}} \
	$RPM_BUILD_ROOT/etc/{sysconfig/rc-inetd,logrotate.d,rc.d/init.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

libtool --mode=install install appl/su/su $RPM_BUILD_ROOT%{_bindir}/ksu
install appl/su/su.1  $RPM_BUILD_ROOT%{_mandir}/man1/ksu.1

install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/krb5.conf

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/%{name}

install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/rshd
install %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/kadmind

install %{SOURCE9} $RPM_BUILD_ROOT/etc/rc.d/init.d/kpasswdd
install %{SOURCE10} $RPM_BUILD_ROOT/etc/sysconfig/kpasswdd

# other implementation exists in e2fsprogs (conflict with e2fsprogs-devel)
rm -rf $RPM_BUILD_ROOT{%{_libdir}/libss.so,%{_includedir}/ss}
# this is created because glibc's <glob.h> has no GLOB_LIMIT and GLOB_QUOTE
rm -f $RPM_BUILD_ROOT%{_includedir}/glob.h

touch $RPM_BUILD_ROOT{%{_sysconfdir}/krb5.keytab,%{_localstatedir}/kadmind.acl}

%clean
rm -rf $RPM_BUILD_ROOT

%post server
/sbin/chkconfig --add heimdal
%service heimdal restart "heimdal daemon"

/sbin/chkconfig --add kpasswdd
%service kpasswdd restart "heimdal password changing daemon"

%service -q rc-inetd reload

%preun server
if [ "$1" = "0" ]; then
	%service heimdal stop
	/sbin/chkconfig --del heimdal

	%service kpasswdd stop
	/sbin/chkconfig --del kpasswdd

	%service -q rc-inetd reload
fi

%post ftpd
%service -q rc-inetd reload

%postun ftpd
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
fi

%post rshd
%service -q rc-inetd reload

%postun rshd
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
fi

%post telnetd
%service -q rc-inetd reload

%postun telnetd
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
fi

%post libs
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun libs
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afslog
%attr(755,root,root) %{_bindir}/kauth
%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kf
%attr(755,root,root) %{_bindir}/kgetcred
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/pagsh
%attr(755,root,root) %{_bindir}/pfrom
%attr(755,root,root) %{_bindir}/string2key
%attr(755,root,root) %{_bindir}/otpprint
%attr(755,root,root) %{_bindir}/verify_krb5_conf
%attr(755,root,root) %{_sbindir}/ktutil
%if %{with x11}
%attr(755,root,root) %{_bindir}/kx
%attr(755,root,root) %{_bindir}/tenletxr
%attr(755,root,root) %{_bindir}/xnlock
%attr(755,root,root) %{_bindir}/rxtelnet
%attr(755,root,root) %{_bindir}/rxterm
%endif

%attr(4755,root,root) %{_bindir}/otp
%attr(4755,root,root) %{_bindir}/ksu

%{_mandir}/man1/afslog.1*
%{_mandir}/man1/kdestroy.1*
%{_mandir}/man1/kf.1*
%{_mandir}/man1/kgetcred.1*
%{_mandir}/man1/kinit.1*
%{_mandir}/man1/klist.1*
%{_mandir}/man1/kpasswd.1*
%{_mandir}/man1/ksu.1*
%{_mandir}/man1/otp.1*
%{_mandir}/man1/otpprint.1*
%{_mandir}/man1/pagsh.1*
%{_mandir}/man1/pfrom.1*
%{_mandir}/man8/ktutil.8*
%{_mandir}/man8/string2key.8*
%{_mandir}/man8/verify_krb5_conf.8*

%if %{with x11}
%{_mandir}/man1/kx.1*
%{_mandir}/man1/tenletxr.1*
%{_mandir}/man1/xnlock.1*
%{_mandir}/man1/rxtelnet.1*
%{_mandir}/man1/rxterm.1*
%endif

%files server
%defattr(644,root,root,755)
%doc NEWS TODO

%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(754,root,root) /etc/rc.d/init.d/kpasswdd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/heimdal
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/kpasswdd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/kadmind

%attr(700,root,root) %dir %{_localstatedir}
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/*

%attr(755,root,root) %{_sbindir}/dump_log
%attr(755,root,root) %{_sbindir}/kadmin
%attr(755,root,root) %{_sbindir}/kfd
%attr(755,root,root) %{_sbindir}/kstash
%attr(755,root,root) %{_sbindir}/replay_log
%attr(755,root,root) %{_sbindir}/hprop
%attr(755,root,root) %{_sbindir}/hpropd
%attr(755,root,root) %{_sbindir}/ipropd-master
%attr(755,root,root) %{_sbindir}/ipropd-slave
%attr(755,root,root) %{_sbindir}/kadmind
%attr(755,root,root) %{_sbindir}/kdc
%attr(755,root,root) %{_sbindir}/kpasswdd
%attr(755,root,root) %{_sbindir}/push
%attr(755,root,root) %{_sbindir}/truncate_log
%{?with_x11:%attr(755,root,root) %{_sbindir}/kxd}

%{_mandir}/man8/iprop.8*
%{_mandir}/man8/hprop.8*
%{_mandir}/man8/hpropd.8*
%{_mandir}/man8/kadmin.8*
%{_mandir}/man8/kadmind.8*
%{_mandir}/man8/kdc.8*
%{_mandir}/man8/kfd.8*
%{_mandir}/man8/kpasswdd.8*
%{_mandir}/man8/kstash.8*
%{?with_x11:%{_mandir}/man8/kxd.8*}
%{_mandir}/man8/push.8*

%files libs
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/krb5.conf
%attr(400,root,root) %ghost %{_sysconfdir}/krb5.keytab
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%{_infodir}/heimdal.info*
%{_mandir}/man5/krb5.conf.5*
%{_mandir}/man8/kerberos.8*

%files login
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/login
%{_mandir}/man1/login.1*
# conflicts with shadow
#%{_mandir}/man5/login.access.5*

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%{_mandir}/man1/ftp.1*

%files rsh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rsh
%attr(755,root,root) %{_bindir}/rcp
%{_mandir}/man1/rsh.1*

%files telnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/telnet
%{_mandir}/man1/telnet.1*

%files ftpd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/ftpd
%attr(755,root,root) %{_sbindir}/ftpd
%{_mandir}/man5/ftpusers.5*
%{_mandir}/man8/ftpd.8*

%files rshd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/rshd
%attr(755,root,root) %{_sbindir}/rshd
%{_mandir}/man8/rshd.8*

%files telnetd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/telnetd
%attr(755,root,root) %{_sbindir}/telnetd
%{_mandir}/man8/telnetd.8*

%files daemons
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/popper
%{_mandir}/man8/popper.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krb5-config
# conflicts with e2fsprogs
#%attr(755,root,root) %{_bindir}/mk_cmds
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man1/krb5-config.1*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
