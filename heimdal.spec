Summary:	Heimdal implementation of Kerberos V5 system
Summary(pl):	Implementacja Heimdal systemu Kerberos V5
Name:		heimdal
Version:	0.2t
Release:	1
Copyright:	Free
Group:		Networking
Group(pl):	Sieciowe
Source0:	ftp://ftp.pdc.kth.se/pub/heimdal/src/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}.logrotate
Source3:	%{name}.sysconfig
Source4:	%{name}-krb5.conf
Source5:	%{name}-ftpd.inetd
Source6:	%{name}-rshd.inetd
Source7:	%{name}-telnetd.inetd
Source8:	%{name}-kadmind.inetd
Patch0:		heimdal-paths.patch
URL:		http://www.pdc.kth.se/heimdal/
BuildRequires:	flex
BuildRequires:	mawk
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	krb5-lib
Requires:	rc-scripts

%define		_libexecdir	%{_sbindir}
%define		_localstatedir	/var/%{name}
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
Group(pl):	Sieciowe
Requires:	%{name}-libs = %{version}

%description server
Master KDC.

%description -l pl server
G³ówne centrum dystrybucji kluczy (KDC).

%package libs
Summary:	Heimdal shared libraries
Summary(pl):	Biblioteki dzielone dla heimdal
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki

%description libs
Package contains shared libraries required by several of the other
heimdal packages.

%description -l pl libs
Pakiet zawiera biblioteki wspó³dzielone dla heimdal.

%package login
Summary:	login is used when signing onto a system
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Requires:	%{name}-libs = %{version}
Provides:	login
Obsoletes:	login

%description login
login is used when signing onto a system. It can also be used to
switch from one user to another at any time (most modern shells have
support for this feature built into them, however). This package
contain kerberized version login program.

%package ftp
Summary:	The standard UNIX FTP (file transfer protocol) client
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Requires:	%{name}-libs = %{version}

%description ftp
The ftp package provides the standard UNIX command-line FTP client
with kerberos authentication support. FTP is the file transfer
protocol, which is a widely used Internet protocol for transferring
files and for archiving files.

%package rsh
Summary:	Clients for remote access commands (rsh, rlogin, rcp)
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Requires:	%{name}-libs = %{version}
Obsoletes:	rsh

%description rsh
The rsh package contains a set of programs which allow users to run
commmands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp). All three of these commands
use rhosts style authentication. This package contains the clients
needed for all of these services.

%package telnet
Summary:	Client for the telnet remote login
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Requires:	%{name}-libs = %{version}
Obsoletes:	telnet

%description telnet
Telnet is a popular protocol for remote logins across the Internet.
This package provides a command line telnet client.

%package ftpd
Summary:	The standard UNIX FTP (file transfer protocol) server
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		rc-inetd >= 0.8.1
Requires:	%{name}-libs = %{version}
Obsoletes:	ftpd

%description ftpd
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

%package rshd
Summary:	Server for remote access commands (rsh, rlogin, rcp)
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		rc-inetd >= 0.8.1
Requires:	%{name}-libs = %{version}
Obsoletes:	rshd

%description rshd
The rsh package contains a set of programs which allow users to run
commmands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp). All three of these commands
use rhosts style authentication. This package contains servers needed
for all of these services.

%package telnetd
Summary:	Server for the telnet remote login
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		rc-inetd >= 0.8.1
Requires:	%{name}-libs = %{version}
Obsoletes:	telnetd

%description telnetd
Telnet is a popular protocol for remote logins across the Internet.
This package provides a telnet daemon which allows remote logins into
the machine it is running on.

%package clients
Summary:	Kerberos programs for use on workstations
Summary(pl):	Oprogramowanie klienckie dla stacji roboczej kerberosa
Group:		Networking
Group(pl):	Sieciowe
Requires:	%{name}-libs = %{version}

%description clients
Kerberos 5 Clients.

%description -l pl clients
Oprogramowanie klienckie do korzystania z us³ug systemu Kerberos 5.

%package daemons
Summary:	Kerberos daemons programs for use on servers
Summary(pl):	Serwery popularnych us³ug, autoryzuj±ce przy pomocy kerberosa
Group:		Networking
Group(pl):	Sieciowe
Requires:	%{name}-libs = %{version}

%description daemons
Kerberos Daemons.

%description -l pl daemons
Daemony korzystaj±ce z systemu Kerberos do autoryzacji dostêpu.

%package devel
Summary:	Header files for heimdal
Summary(pl):	Pliki nag³ówkowe i dokumentacja do bibliotek heimdal
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name}-libs = %{version}

%description devel
contains files needed to compile and link software using the kerberos
libraries.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do bibliotek heimdal.

%package static
Summary:	Static heimdal libraries
Summary(pl):	Biblioteki statyczne heimdal
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name}-libs = %{version}

%description static
Satatic heimdal libraries.

%description -l pl static
Biblioteki statyczne heimdal.

%prep
%setup -q
%patch0 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-shared \
	--enable-static \
	--enable-new-des3-code \
	--with-readline \
	--with-x \
	--with-ipv6

# --enable-netinfo - czo to takiego ?
# mo¿na u¿ywaæ albo krb5.conf albo netinfo
# 
#       --enable-osfc2 \
#    setluid(epw->ufld->fd_uid);
#    if(getluid() != epw->ufld->fd_uid) {
# setluid() && getluid() - sk±d to

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_localstatedir},%{_sysconfdir}} \
	$RPM_BUILD_ROOT/etc/{sysconfig/rc-inetd,logrotate.d,rc.d/init.d}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install appl/su/.libs/su $RPM_BUILD_ROOT%{_bindir}/ksu
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/krb5.conf

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/%{name}

install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/rshd
install %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/kadmind

rm -rf $RPM_BUILD_ROOT%{_libdir}/libcom_err.*

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/*.so.*

chmod +r $RPM_BUILD_ROOT%{_bindir}/otp   # qrde dlaczego to ma chmod 0

touch $RPM_BUILD_ROOT{%{_sysconfdir}/krb5.keytab,%{_localstatedir}/kadmind.acl}

gzip -9nf $RPM_BUILD_ROOT{%{_mandir}/man[1358]/*,%{_infodir}/*} \
	NEWS TODO 

%post server
/sbin/chkconfig --add heimdal
if [ -f /var/lock/sybsys/heimdal ]; then
	/etc/rc.d/init.d/heimdal restart >&2
else
	echo "Run \"/etc/rc.d/init.d/heimdal start\" to start heimdal daemon."
fi

if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%preun server
if [ "$1" = 0 ]; then
	if [ -f /var/lock/sybsys/heimadal ]; then
		/etc/rc.d/init.d/heimdal stop >&2
	fi
	/sbin/chkconfig --del heimdal
fi

if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi
	    
%post ftpd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun ftpd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%post rshd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun rshd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%post telnetd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun telnetd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%post libs
/sbin/ldconfig
[ -x %{_sbindir}/fix-info-dir ] && %{_sbindir}/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun libs 
/sbin/ldconfig
[ -x %{_sbindir}/fix-info-dir ] && %{_sbindir}/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files server
%defattr(644,root,root,755)
%doc NEWS.gz TODO.gz

%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) /etc/sysconfig/heimdal
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/kadmind

%attr(700,root,root) %dir %{_localstatedir}
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_localstatedir}/*

%attr(755,root,root) %{_sbindir}/dump_log
%attr(755,root,root) %{_sbindir}/kadmin
%attr(755,root,root) %{_sbindir}/kstash
%attr(755,root,root) %{_sbindir}/ktutil
%attr(755,root,root) %{_sbindir}/replay_log
%attr(755,root,root) %{_sbindir}/hprop
%attr(755,root,root) %{_sbindir}/hpropd
%attr(755,root,root) %{_sbindir}/ipropd-master
%attr(755,root,root) %{_sbindir}/ipropd-slave
%attr(755,root,root) %{_sbindir}/kadmind
%attr(755,root,root) %{_sbindir}/kdc
%attr(755,root,root) %{_sbindir}/kxd 
%attr(755,root,root) %{_sbindir}/kpasswdd

%{_mandir}/man8/hprop.8*
%{_mandir}/man8/hpropd.8*
%{_mandir}/man8/kdc.8*
%{_mandir}/man8/ktutil.8*
%{_mandir}/man8/kstash.8*
%{_mandir}/man8/kpasswdd.8*

%files libs
%defattr(644,root,root,755)

%dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/krb5.conf
%attr(400,root,root) %ghost %{_sysconfdir}/krb5.keytab

%attr(755,root,root) %{_libdir}/lib*.so.*.*

%{_infodir}/heimdal.info*
%{_mandir}/man5/krb5.conf.5*

%files login
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/login

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%{_mandir}/man1/ftp.1*

%files rsh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rsh

%files telnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/telnet
%{_mandir}/man1/telnet.1*

%files ftpd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/ftpd
%attr(755,root,root) %{_sbindir}/ftpd
%{_mandir}/man5/ftpusers.5*
%{_mandir}/man8/ftpd.8*

%files rshd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/rshd
%attr(755,root,root) %{_sbindir}/rshd

%files telnetd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/telnetd
%attr(755,root,root) %{_sbindir}/telnetd
%{_mandir}/man8/telnetd.8*

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/compile_et
%attr(755,root,root) %{_bindir}/des
%attr(755,root,root) %{_bindir}/kauth
%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kgetcred
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/kx
%attr(755,root,root) %{_bindir}/pfrom
%attr(755,root,root) %{_bindir}/rxtelnet
%attr(755,root,root) %{_bindir}/rxterm
%attr(755,root,root) %{_bindir}/string2key
%attr(755,root,root) %{_bindir}/tenletxr
%attr(755,root,root) %{_bindir}/otpprint
%attr(755,root,root) %{_bindir}/verify_krb5_conf
%attr(755,root,root) %{_bindir}/xnlock

%attr(4755,root,root) %{_bindir}/otp
%attr(4755,root,root) %{_bindir}/ksu

%{_mandir}/man1/kdestroy.1*
%{_mandir}/man1/kgetcred.1*
%{_mandir}/man1/kinit.1*
%{_mandir}/man1/klist.1*
%{_mandir}/man1/kpasswd.1*

%files daemons
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/popper

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
