Summary:	Heimdal implementation of Kerberos V5 system
Summary(pl):	Implementacja Heimdal systemu Kerberos V5
Name:		heimdal
Version:	0.1g
Release:	2
Source0:	%{name}-%{version}.tar.gz
Source3:	heimdal.init
Source4:	inetd.conf.secure
Source5:	heimdal.logrotate
Source6:	heimdal.sysconfig
Patch0:		heimdal-paths.patch
Patch1:		heimdal-0.1g-recvfrom.patch
Group:		Networking
Group(pl):	Sieciowe
Copyright:	Free
BuildRoot:	/tmp/%{name}-%{version}-root
Conflicts:	krb5-lib
Requires:	rc-scripts

%description
Heimdal is a free implementation of Kerberos 5. The goals are to:
   * have an implementation that can be freely used by anyone
   * be protocol compatible with existing implementations and, if not in
     conflict, with RFC 1510 (and any future updated RFC)
   * be reasonably compatible with the M.I.T Kerberos V5 API
   * have support for Kerberos V5 over GSS-API (RFC1964)
   * include the most important and useful application programs (rsh,
     telnet, popper, etc.)
   * include enough backwards compatibility with Kerberos V4
   * IPv6 support

%description -l pl
Heimdal jest darmow± implementacj± Kerberosa 5. G³ówne zalety to:
   * implementacja, która mo¿e byæ u¿ywana przez ka¿dego
   * kompatybilno¶æ na poziomie protoko³u z istniej±cymi implementacjami
   * racjonalna kompatybilno¶æ z M.I.T Kerberos V5 API
   * wsparcie dla Kerberosa 5 poprzez GSS-API (RFC1964)
   * zawiera wiêkszo¶æ istotnych i u¿ytecznych aplikacji (rsh,
     telnet, popper, etc.)
   * zawiera wystarczaj±c± kompatybilno¶æ z Kerberos V4
   * wsparcie dla IPv6

%package	clients 
Summary:	Kerberos programs for use on workstations
Summary(pl):	Oprogramowanie klienckie dla stacji roboczej kerberosa
Group:		Networking
Group(pl):	Sieciowe
Requires:	%{name}-lib = %{version}

%description clients
Kerberos 5 Clients.

%description -l pl clients
Oprogramowanie klienckie do korzystania z us³ug systemu Kerberos 5.

%package	daemons
Summary:	Kerberos daemons programs for use on servers
Summary(pl):	Serwery popularnych us³ug, autoryzuj±ce przy pomocy kerberosa.
Group:		Networking
Group(pl):	Sieciowe
Requires:	%{name}-lib = %{version}

%description daemons
Kerberos Daemons.

%description -l pl daemons
Daemony korzystaj±ce z systemu Kerberos do autoryzacji dostêpu.

%package	server
Summary:	Kerberos Server 
Summary(pl):	Serwer Kerberosa
Group:		Networking
Group(pl):	Sieciowe
Requires:	%{name}-lib = %{version}

%description server
Master KDC.

%description -l pl server
G³ówne centrum dystrybucji kluczy (KDC).

%package	lib
Summary:	Kerberos shared libraries
Summary(pl):	Biblioteki dzielone dla kerberosa
Group:		Libraries
Group(pl):	Biblioteki
Prereq:		/usr/sbin/fix-info-dir

%description lib
Libraries for Kerberos V5 Server and Client

%description -l pl lib
Biblioteki dynamiczne dla systemu kerberos.

%package	devel
Summary:	Header files for Kerberos libraries and documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do bibliotek Kerberosa
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name}-lib = %{version}

%description devel
Header files for Kerberos libraries and development documentation

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do bibliotek Kerberosa

%package	static
Summary:	Static Kerberos libraries
Summary(pl):	Biblioteki statyczne Kerberosa
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name}-lib = %{version}

%description static
Sattic Kerberos libraries.

%description -l pl static
Biblioteki statyczne Kerberosa.

#%package	pam
#Summary:	PAM - Kerberos 5 module
#Summary(pl):	PAM - Kerberos 5 modu³
#Requires:	pam >= 0.66
#Group:		Libraries
#Group:		Libraries
#Requires:	%{name}-lib = %{version}
#
#%description pam
#This is a PAM - Kerberos 5 module for PLD Linux.
#It supports authentication, session, and password modules. 
#
#%description -l pl pam
#W pakiecie znajduje siê modu³ PAM wspomagaj±cy autoryzacjê przez
#Kerberosa V5. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%define _prefix		/usr/heimdal
%define _mandir		/usr/share/man
%define _infodir	/usr/share/info

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--libexecdir=%{_sbindir} \
	--enable-shared \
	--enable-static \
	--enable-new-des3-code \
	--with-readline \
	--with-x \
	--localstatedir=/var %{_target_platform}

# --enable-netinfo - czo to takiego ?
# mo¿na u¿ywaæ albo krb5.conf albo netinfo
# 
#       --enable-osfc2 \
#    setluid(epw->ufld->fd_uid);
#    if(getluid() != epw->ufld->fd_uid) {
# setluid() && getluid() - sk±d to

make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/rc.d/init.d,var/heimdal}
install -d $RPM_BUILD_ROOT/etc/{heimdal,sysconfig,profile.d,logrotate.d}

make install DESTDIR=$RPM_BUILD_ROOT
install appl/su/.libs/su $RPM_BUILD_ROOT%{_bindir}/ksu
install krb5.conf        $RPM_BUILD_ROOT/etc/heimdal

install %{SOURCE5}			$RPM_BUILD_ROOT/etc/logrotate.d/heimdal
install %{SOURCE3}			$RPM_BUILD_ROOT/etc/rc.d/init.d/heimdal
install %{SOURCE6}			$RPM_BUILD_ROOT/etc/sysconfig/heimdal
#install %{SOURCE7}	%{SOURCE8}	$RPM_BUILD_ROOT/etc/profile.d

strip $RPM_BUILD_ROOT{%{_bindir}/*,%{_sbindir}/*} || :
strip --strip-debug $RPM_BUILD_ROOT%{_libdir}/*.so.*

touch $RPM_BUILD_ROOT/etc/heimdal/krb5.keytab
touch $RPM_BUILD_ROOT/var/heimdal/kadmind.acl

gzip -9fn $RPM_BUILD_ROOT{%{_mandir}/man[1358]/*,%{_infodir}/*} \
	doc/* NEWS TODO 

chmod a+rw $RPM_BUILD_ROOT%{_bindir}/otp

%clean
rm -rf $RPM_BUILD_ROOT

%post lib
if [ "$1" = "0" ]; then
        /etc/rc.d/init.d/heimdal stop >&2
        /sbin/chkconfig --del heimdal >&2
fi
/sbin/ldconfig
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1


%preun lib
if [ "$1" = "0" ]; then
        /etc/rc.d/init.d/heimdal stop >&2
        /sbin/chkconfig --del heimdal >&2
fi

%postun lib -p /sbin/ldconfig
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files server
%defattr(644,root,root,755)
%doc NEWS.gz TODO.gz

%attr(754,root,root) /etc/rc.d/init.d/heimdal
%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) /etc/sysconfig/*

%attr(700,root,root) %dir /var/heimdal
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) /var/heimdal/*

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

%{_mandir}/man8/hprop.8.gz
%{_mandir}/man8/hpropd.8.gz
%{_mandir}/man8/kdc.8.gz
%{_mandir}/man8/ktutil.8.gz
%{_mandir}/man8/kstash.8.gz
%{_mandir}/man8/kpasswdd.8.gz

%files clients
%defattr(644,root,root,755)
#%attr(755,root,root) /etc/profile.d/kerberos.* 

%attr(755,root,root) %{_bindir}/compile_et
%attr(755,root,root) %{_bindir}/des
%attr(755,root,root) %{_bindir}/ftp
%attr(755,root,root) %{_bindir}/kauth
%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kgetcred
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/kx
%attr(755,root,root) %{_bindir}/pfrom
%attr(755,root,root) %{_bindir}/rsh
%attr(755,root,root) %{_bindir}/rxtelnet
%attr(755,root,root) %{_bindir}/rxterm
%attr(755,root,root) %{_bindir}/string2key
%attr(755,root,root) %{_bindir}/telnet
%attr(755,root,root) %{_bindir}/tenletxr
%attr(755,root,root) %{_bindir}/otpprint
%attr(000,root,root) %{_bindir}/otp
%attr(4711,root,root) %{_bindir}/ksu

%{_mandir}/man1/kdestroy.1.gz
%{_mandir}/man1/kgetcred.1.gz
%{_mandir}/man1/kinit.1.gz
%{_mandir}/man1/klist.1.gz
%{_mandir}/man1/kpasswd.1.gz

%files daemons
%defattr(644,root,root,755)

%attr(755,root,root) %{_sbindir}/ftpd
%attr(755,root,root) %{_sbindir}/telnetd
%attr(755,root,root) %{_sbindir}/rshd
%attr(755,root,root) %{_sbindir}/popper

%files lib
%defattr(644,root,root,755)
%attr(644,root,root) %{_infodir}/heimdal.info.gz

%dir /etc/heimdal
%config(noreplace) %verify(not size mtime md5) /etc/heimdal/krb5.conf
%attr(400,root,root) %ghost /etc/heimdal/krb5.keytab

%attr(755,root,root) %{_libdir}/*.so.*
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_bindir}/login

%{_mandir}/man5/krb5.conf.5.gz

%files devel
%defattr(644,root,root,755)

%{_includedir}/*

%files static
%defattr(644,root,root,755)

%{_libdir}/*.a

#%files pam
#%defattr(644,root,root,755)
#%doc ../pam_krb5-1.0-1/README.gz

#%attr(755,root,root) /lib/security/pam_krb5.so
