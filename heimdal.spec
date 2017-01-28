#
# Conditional build:
%bcond_without	x11			# X11-based utilities
%bcond_without	ldap			# LDAP plugin
%bcond_without	sqlite			# Sqlite3 support
%bcond_with	openssl			# use OpenSSL instead of internal hcrypto
%bcond_with	expose_internals	# install internal KCM headers

Summary:	Heimdal implementation of Kerberos V5 system
Summary(pl.UTF-8):	Implementacja Heimdal systemu Kerberos V5
# see dev-7.3 WIP branch for newer version
Name:		heimdal
Version:	7.1.0
Release:	0.1
License:	Free
Group:		Networking
Source0:	https://github.com/heimdal/heimdal/releases/download/heimdal-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bbeedb8eae6f81b12cbbaada4faaeb47
Source1:	%{name}.init
Source2:	%{name}-kpasswdd.init
Source3:	%{name}-ipropd.init
Source4:	%{name}-kcm.init
Source5:	%{name}.sysconfig
Source6:	%{name}-kcm.sysconfig
Source7:	%{name}-krb5.conf
Source8:	%{name}-ftpd.inetd
Source9:	%{name}-rshd.inetd
Source10:	%{name}-telnetd.inetd
Source11:	%{name}-kadmind.inetd
#Patch0:		%{name}-paths.patch
Patch0:		%{name}-hdb-ldap.patch
Patch1:		%{name}-am_man_fixes.patch
Patch2:		%{name}-amfix.patch
Patch3:		%{name}-dbpaths.patch
Patch4:		%{name}-db4.patch
Patch5:		%{name}-libadd.patch
Patch6:		%{name}-signal.patch
Patch7:		%{name}-make.patch
Patch8:		%{name}-info.patch
Patch9:		%{name}-sbindir.patch
Patch10:	%{name}-ntlm-digest.patch
Patch11:	%{name}-krb5config-nosysdirs.patch
Patch12:	%{name}-tinfo.patch
Patch13:	%{name}-missing-exports.patch
#Patch14:	%{name}-texinfo.patch
URL:		http://www.h5l.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.10.3
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	flex
BuildRequires:	libcap-ng-devel >= 0.4.0
BuildRequires:	libcom_err-devel >= 1.41.11
BuildRequires:	libtool >= 2:2.2
BuildRequires:	mawk
BuildRequires:	ncurses-devel >= 5.1
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_openssl:BuildRequires:	openssl-devel >= 0.9.7d}
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.268
%{?with_sqlite:BuildRequires:	sqlite3-devel}
BuildRequires:	texinfo
%{?with_x11:BuildRequires:	xorg-lib-libICE-devel}
%{?with_x11:BuildRequires:	xorg-lib-libSM-devel}
%{?with_x11:BuildRequires:	xorg-lib-libX11-devel}
%{?with_x11:BuildRequires:	xorg-lib-libXau-devel}
%{?with_x11:BuildRequires:	xorg-lib-libXt-devel}
Requires:	%{name}-libs-common = %{version}-%{release}
Provides:	kerberos5-client
Obsoletes:	kerberos5-client
Conflicts:	krb5-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib/%{name}
%define		schemadir	/usr/share/openldap/schema

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

%description -l pl.UTF-8
Heimdal jest darmową implementacją Kerberosa 5. Główne zalety to:
- implementacja, która może być używana przez każdego
- kompatybilność na poziomie protokołu z istniejącymi implementacjami
- racjonalna kompatybilność z M.I.T Kerberos V5 API
- wsparcie dla Kerberosa 5 poprzez GSS-API (RFC1964)
- zawiera większość istotnych i użytecznych aplikacji (rsh, telnet,
  popper, etc.)
- zawiera wystarczającą kompatybilność z Kerberos V4
- wsparcie dla IPv6

%package common
Summary:	Heimdal essential config files and documentation
Summary(pl.UTF-8):	Niezbędne pliki konfiguracyjne i dokumentacja dla Heimdala
Group:		Networking

%description common
Package contains essential configs and documentation required by
Heimdal packages.

%description common -l pl.UTF-8
Pakiet zawiera niezbędne pliki konfiguracyjne i dokumentację dla
Heimdala.

%package libs
Summary:	Heimdal shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone dla Heimdala
Group:		Libraries
Requires:	libcom_err >= 1.41.11

%description libs
This package contains shared libraries required by several of the
other Heimdal packages.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki współdzielone wymagane przez kilka
innych pakietów składowych Heimdala.

%package libs-common
Summary:	Common libraries used by Heimdal programs
Summary(pl.UTF-8):	Wspólne biblioteki używane przez programy z Heimdala
Group:		Libraries
Requires:	%{name}-common = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

%description libs-common
Common libraries used by Heimdal programs.

%description libs-common -l pl.UTF-8
Wspólne biblioteki używane przez programy z projektu Heimdal.

%package libs-server
Summary:	Libraries used by Heimdal KDC server
Summary(pl.UTF-8):	Biblioteki używane przez serwer Heimdal KDC
Group:		Libraries
Requires:	%{name}-libs-common = %{version}-%{release}

%description libs-server
This package contains shared libraries required to run Heimdal KDC
server.

%description libs-server -l pl.UTF-8
Ten pakiet zawiera biblioteki współdzielone używane potrzebne dla
serwera KDC z projektu Heimdal.

%package devel
Summary:	Header files for Heimdal
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do bibliotek Heimdal
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-libs-common = %{version}-%{release}
Requires:	%{name}-libs-server = %{version}-%{release}
Requires:	db-devel
Requires:	libcom_err-devel >= 1.41.11
%{?with_openssl:Requires:	openssl-devel}
%{?with-sqlite:Requires:	sqlite3-devel}
Conflicts:	krb5-devel
Conflicts:	libgssglue-devel

%description devel
This package contains files needed to compile and link software using
the Heimdal libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe do kompilowania programów przy użyciu bibliotek
Heimdal.

%package static
Summary:	Static Heimdal libraries
Summary(pl.UTF-8):	Biblioteki statyczne Heimdal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Satatic Heimdal libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Heimdal.

%package ldap
Summary:	LDAP HDB plugin
Summary(pl.UTF-8):	Wtyczka HDB LDAP
Group:		Libraries
Requires:	%{name}-libs-common = %{version}-%{release}

%description ldap
LDAP HDB plugin.

%description ldap -l pl.UTF-8
Wtyczka HDB LDAP.

%package -n openldap-schema-heimdal
Summary:	Heimdal Kerberos LDAP schema
Summary(pl.UTF-8):	Schemat LDAP Kerberosa Heimdal
Group:		Networking/Daemons
Requires(post,postun):	sed >= 4.0
Requires:	openldap-servers
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n openldap-schema-heimdal
This package contains Heimdal Kerberos LDAP schema for openldap.

%description -n openldap-schema-heimdal -l pl.UTF-8
Ten pakiet zawiera schemat LDAP Kerberosa Heimdal dla openldap-a.

%package server
Summary:	Kerberos Server
Summary(pl.UTF-8):	Serwer Kerberosa
Group:		Networking
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs-server = %{version}-%{release}
Requires:	rc-scripts
Provides:	kerberos5-server
# probably not a good idea
#Obsoletes:	kerberos5-server
Conflicts:	krb5-server

%description server
Master KDC.

%description server -l pl.UTF-8
Główne centrum dystrybucji kluczy (KDC).

%package kcm
Summary:	KCM - credencial cache daemon for Kerberos tickets
Summary(pl.UTF-8):	KCM - demon zapamiętujący dane uwierzytelniające dla biletów Kerberosa
Group:		Daemons
Requires:	%{name}-libs-common = %{version}-%{release}

%description kcm
KCM is a credencial cache daemon for Kerberos tickets.

%description kcm -l pl.UTF-8
KCM to demon zapamiętujący dane uwierzytelniające dla biletów
Kerberosa.

%package login
Summary:	login is used when signing onto a system
Summary(pl.UTF-8):	Narzędzie do logowania w systemie
Group:		Applications/Networking
Requires:	%{name}-libs-common = %{version}-%{release}
Provides:	kerberos5-login
Obsoletes:	kerberos5-login
Conflicts:	shadow < 1:4.0.16

%description login
login is used when signing onto a system. It can also be used to
switch from one user to another at any time (most modern shells have
support for this feature built into them, however). This package
contain kerberized version login program.

%description login -l pl.UTF-8
login jest używany przy logowaniu do systemu. Może być także użyty do
przełączenia z jednego użytkownika na innego w dowolnej chwili
(większość współczesnych shelli ma wbudowaną obsługę tego). Ten pakiet
zawiera skerberyzowaną wersję programu login.

%package ftp
Summary:	The standard UNIX FTP (file transfer protocol) client
Summary(pl.UTF-8):	Klient protokołu FTP
Group:		Applications/Networking
Requires:	%{name}-libs-common = %{version}-%{release}
Provides:	kerberos5-ftp
Obsoletes:	ftp
Obsoletes:	kerberos5-ftp
Conflicts:	heimdal-clients
Conflicts:	krb5-ftp

%description ftp
The FTP package provides the standard UNIX command-line FTP client
with Kerberos authentication support. FTP is the file transfer
protocol, which is a widely used Internet protocol for transferring
files and for archiving files.

%description ftp -l pl.UTF-8
Ten pakiet dostarcza standardowego klienta FTP z wbudowaną obsługą
Kerberosa. FTP jest protokołem do przesyłania plików szeroko
rozpowszechnionym w Internecie.

%package rsh
Summary:	Clients for remote access commands (rsh, rlogin, rcp)
Summary(pl.UTF-8):	Klient zdalnego dostępu (rsh, rlogin, rcp)
Group:		Applications/Networking
Requires:	%{name}-libs-common = %{version}-%{release}
Provides:	kerberos5-rsh
Obsoletes:	kerberos5-rsh
Obsoletes:	rsh
Conflicts:	heimdal-clients
Conflicts:	krb5-rsh

%description rsh
The rsh package contains a set of programs which allow users to run
commands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp). All three of these commands
use rhosts style authentication. This package contains the clients
needed for all of these services.

%description rsh -l pl.UTF-8
Ten pakiet zawiera zestaw narzędzi pozwalających na wykonywanie
poleceń na zdalnych maszynach, logowanie na inne maszyny oraz
kopiowanie plików pomiędzy maszynami (rsh, rlogin, rcp).

%package telnet
Summary:	Client for the telnet remote login
Summary(pl.UTF-8):	Klient usługi telnet
Group:		Applications/Networking
Requires:	%{name}-libs-common = %{version}-%{release}
Provides:	kerberos5-telnet
Obsoletes:	kerberos5-telnet
Obsoletes:	telnet
Conflicts:	heimdal-clients
Conflicts:	krb5-telnet

%description telnet
Telnet is a popular protocol for remote logins across the Internet.
This package provides a command line telnet client.

%description telnet -l pl.UTF-8
Telnet jest popularnym protokołem zdalnego logowania. Ten pakiet
zawiera klienta tej usługi.

%package ftpd
Summary:	The standard UNIX FTP (file transfer protocol) server
Summary(pl.UTF-8):	Serwer FTP
Group:		Networking/Daemons
Requires:	%{name}-libs-common = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Provides:	kerberos5-ftpd
Obsoletes:	ftpd
Obsoletes:	kerberos5-ftpd
Conflicts:	krb5-ftpd

%description ftpd
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

%description ftpd -l pl.UTF-8
FTP jest protokołem transmisji plików szeroko rozpowszechnionym w
Internecie.

%package rshd
Summary:	Server for remote access commands (rsh, rlogin, rcp)
Summary(pl.UTF-8):	Serwer zdalnego dostępu (rsh, rlogin, rcp)
Group:		Networking/Daemons
Requires:	%{name}-libs-common = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Provides:	kerberos5-rshd
Obsoletes:	kerberos5-rshd
Obsoletes:	rshd
Conflicts:	krb5-rshd

%description rshd
The rsh package contains a set of programs which allow users to run
commmands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp). All three of these commands
use rhosts style authentication. This package contains servers needed
for all of these services.

%description rshd -l pl.UTF-8
Ten pakiet zawiera zestaw serwerów pozwalających na wykonywanie
poleceń na zdalnych maszynach, logowanie na inne maszyny oraz
kopiowanie plików pomiędzy maszynami (rsh, rlogin, rcp).

%package telnetd
Summary:	Server for the telnet remote login
Summary(pl.UTF-8):	Serwer protokołu telnet
Group:		Networking/Daemons
Requires:	%{name}-libs-common = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Provides:	kerberos5-telnetd
Obsoletes:	kerberos5-telnetd
Obsoletes:	telnetd
Conflicts:	krb5-telnetd

%description telnetd
Telnet is a popular protocol for remote logins across the Internet.
This package provides a telnet daemon which allows remote logins into
the machine it is running on.

%description telnetd -l pl.UTF-8
Telnet jest popularnym protokołem zdalnego logowania. Ten pakiet
zawiera serwer pozwalający na zdalne logowanie się klientów na maszynę
na której działa.

%package daemons
Summary:	Kerberos daemons programs for use on servers
Summary(pl.UTF-8):	Serwery popularnych usług, autoryzujące przy pomocy Kerberosa
Group:		Networking
Requires:	%{name}-libs-common = %{version}-%{release}

%description daemons
Kerberos Daemons.

%description daemons -l pl.UTF-8
Demony korzystające z systemu Kerberos do autoryzacji dostępu.

%define	specflags	-pthread

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1 outdated?
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
#%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%{__rm} acinclude.m4
# cf/{libtool,lt*}.m4

%build
install -d our-ld
ln -s %{_bindir}/ld.bfd our-ld/ld
export PATH=$(pwd)/our-ld:$PATH

%{__libtoolize}
%{__aclocal} -I cf
%{__autoconf}
%{__automake}
cd lib/libedit
%{__aclocal}
%{__autoconf}
%{__automake}
cd ../..
%configure \
%if %{with ldap}
	--enable-hdb-openldap-module \
	--with-openldap=/usr \
%endif
	--with%{!?with_openssl:out}-openssl \
	--enable-kcm \
	--enable-pthread-support \
	--enable-shared \
	--disable-silent-rules \
	--enable-static \
	--with-hdbdir=%{_localstatedir} \
	--with-ipv6 \
	--with-readline=/usr \
	%{?with_sqlite:--with-sqlite3=/usr} \
	--without-hesiod \
	--with%{!?with_x11:out}-x

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_localstatedir},%{_sysconfdir},%{schemadir},/sbin,/%{_lib}} \
	$RPM_BUILD_ROOT/etc/{sysconfig/rc-inetd,rc.d/init.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p lib/hdb/hdb.schema $RPM_BUILD_ROOT%{schemadir}

%{__mv} $RPM_BUILD_ROOT%{_sbindir}/kcm $RPM_BUILD_ROOT/sbin/kcm

%{__mv} $RPM_BUILD_ROOT%{_bindir}/su $RPM_BUILD_ROOT%{_bindir}/ksu
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/su.1 $RPM_BUILD_ROOT%{_mandir}/man1/ksu.1

install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install -p %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/kpasswdd
install -p %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/ipropd
install -p %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/kcm
cp -p %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
cp -p %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/kcm

cp -p %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/krb5.conf

%if 0
cp -p %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
cp -p %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/rshd
cp -p %{SOURCE10} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd
%endif
cp -p %{SOURCE11} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/kadmind

for l in $RPM_BUILD_ROOT%{_libdir}/lib{asn1,gssapi,heimbase,heimntlm,hx509,kafs,krb5,roken,wind}.so %{!?with_openssl:libhcrypto.so}; do
	lib=`basename $l`
	%{__mv} $RPM_BUILD_ROOT%{_libdir}/$lib.* $RPM_BUILD_ROOT/%{_lib}
	ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/$lib.*.*) $RPM_BUILD_ROOT%{_libdir}/$lib
done

%if %{with expose_internals}
# install definitions of KCM internal data structures to get KCM support in nfs-utils
install -d $RPM_BUILD_ROOT%{_includedir}/kcm
_mutexdef=$(cat << EOF | %{__cc} -E -I./include - | sed 's/_HEIMDAL_MUTEX \(.*\)/\1/p; d'
#include "config.h"
#include "heim_threads.h"
_HEIMDAL_MUTEX HEIMDAL_MUTEX
EOF)
%{__sed} -e '/#include <kcm-protos.h>/d' \
	-e '/#include "headers.h"/d' \
	-e '/kcm_service/N; /kcm_service/d;' \
	-e 's/<kcm\.h>/<kcm\/kcm.h>/' \
	-e "s/HEIMDAL_MUTEX/$_mutexdef/g" kcm/kcm_locl.h >$RPM_BUILD_ROOT%{_includedir}/kcm/kcm_locl.h
install -p lib/krb5/kcm.h $RPM_BUILD_ROOT%{_includedir}/kcm
%endif

# just a test plugin
%{__rm} $RPM_BUILD_ROOT%{_libdir}/windc.*
%if %{with ldap}
# not needed for plugin
%{__rm} $RPM_BUILD_ROOT%{_libdir}/hdb_ldap.{la,a}
%endif
# resolve heimdal-libs/krb5-libs conflict
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man5/{krb5.conf.5,krb5.conf.5h}

touch $RPM_BUILD_ROOT{%{_sysconfdir}/krb5.keytab,%{_localstatedir}/kadmind.acl}

%clean
rm -rf $RPM_BUILD_ROOT

%post server
/sbin/chkconfig --add heimdal
%service heimdal restart "heimdal KDC daemon"
/sbin/chkconfig --add kpasswdd
%service kpasswdd restart "heimdal password changing daemon"
/sbin/chkconfig --add ipropd
%service ipropd restart "heimdal propagation daemons"
%service -q rc-inetd reload

%preun server
if [ "$1" = "0" ]; then
	%service ipropd stop
	/sbin/chkconfig --del ipropd
	%service kpasswdd stop
	/sbin/chkconfig --del kpasswdd
	%service heimdal stop
	/sbin/chkconfig --del heimdal
	%service -q rc-inetd reload
fi

%post kcm
/sbin/chkconfig --add kcm
%service -n kcm restart
# Add note to service -n restart
echo "WARNING: it will clear all credentials and tickets kept in kcm!" >&2

%preun kcm
if [ "$1" = "0" ]; then
	%service kcm stop
	/sbin/chkconfig --del kcm
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

%post common
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun common
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
%post   libs-common -p /sbin/ldconfig
%postun libs-common -p /sbin/ldconfig
%post   libs-server -p /sbin/ldconfig
%postun libs-server -p /sbin/ldconfig

%post -n openldap-schema-heimdal
%openldap_schema_register %{schemadir}/hdb.schema
%service -q ldap restart

%postun -n openldap-schema-heimdal
if [ "$1" = "0" ]; then
	%openldap_schema_unregister %{schemadir}/hdb.schema
	%service -q ldap restart
fi

%triggerpostun libs -- heimdal-libs < 1.2.1-6
if [ -f /etc/heimdal/krb5.conf.rpmsave ]; then
	mv /etc/krb5.conf{,.rpmnew}
	mv -f /etc/heimdal/krb5.conf.rpmsave /etc/krb5.conf
fi
if [ -f /etc/heimdal/krb5.keytab.rpmsave ]; then
	mv /etc/krb5.keytab{,.rpmnew}
	mv -f /etc/heimdal/krb5.keytab.rpmsave /etc/krb5.keytab
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/afslog
%attr(755,root,root) %{_bindir}/bsearch
%attr(755,root,root) %{_bindir}/gsstool
%attr(755,root,root) %{_bindir}/heimtools
%attr(755,root,root) %{_bindir}/hxtool
%attr(755,root,root) %{_bindir}/idn-lookup
%attr(755,root,root) %{_bindir}/kadmin
#%attr(755,root,root) %{_bindir}/kcc
%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kf
%attr(755,root,root) %{_bindir}/kgetcred
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/kswitch
%attr(755,root,root) %{_bindir}/ktutil
%attr(755,root,root) %{_bindir}/otpprint
%attr(755,root,root) %{_bindir}/pagsh
#%attr(755,root,root) %{_bindir}/pfrom
%attr(755,root,root) %{_bindir}/string2key
%attr(755,root,root) %{_bindir}/verify_krb5_conf
%attr(755,root,root) %{_sbindir}/kdigest
%attr(755,root,root) %{_sbindir}/kimpersonate
#%attr(755,root,root) %{_sbindir}/push
%if %{with x11}
#%attr(755,root,root) %{_bindir}/kx
#%attr(755,root,root) %{_bindir}/rxtelnet
#%attr(755,root,root) %{_bindir}/rxterm
#%attr(755,root,root) %{_bindir}/tenletxr
#%attr(755,root,root) %{_bindir}/xnlock
%endif
%attr(4755,root,root) %{_bindir}/otp
%attr(4755,root,root) %{_bindir}/ksu
%{_mandir}/man1/afslog.1*
%{_mandir}/man1/bsearch.1*
%{_mandir}/man1/kadmin.1*
%{_mandir}/man1/kdestroy.1*
%{_mandir}/man1/kf.1*
%{_mandir}/man1/kgetcred.1*
%{_mandir}/man1/kinit.1*
%{_mandir}/man1/klist.1*
%{_mandir}/man1/kpasswd.1*
%{_mandir}/man1/ksu.1*
%{_mandir}/man1/kswitch.1*
%{_mandir}/man1/ktutil.1*
%{_mandir}/man1/otp.1*
%{_mandir}/man1/otpprint.1*
%{_mandir}/man1/pagsh.1*
#%{_mandir}/man1/pfrom.1*
%if %{with x11}
#%{_mandir}/man1/kx.1*
#%{_mandir}/man1/rxtelnet.1*
#%{_mandir}/man1/rxterm.1*
#%{_mandir}/man1/tenletxr.1*
#%{_mandir}/man1/xnlock.1*
%endif
%{_mandir}/man8/kdigest.8*
%{_mandir}/man8/kimpersonate.8*
#%{_mandir}/man8/push.8*
%{_mandir}/man8/string2key.8*
%{_mandir}/man8/verify_krb5_conf.8*

%files common
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/krb5.conf
%attr(400,root,root) %ghost %{_sysconfdir}/krb5.keytab
%{_infodir}/heimdal.info*
%{_infodir}/hx509.info*
%{_mandir}/man5/krb5.conf.5*
%{_mandir}/man5/mech.5*
%{_mandir}/man8/kerberos.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libasn1.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libasn1.so.8
%attr(755,root,root) /%{_lib}/libgssapi.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libgssapi.so.3
%attr(755,root,root) /%{_lib}/libheimbase.so.*.*.*
%if %{without openssl}
%attr(755,root,root) /%{_lib}/libhcrypto.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libhcrypto.so.4
%endif
%attr(755,root,root) %ghost /%{_lib}/libheimbase.so.1
%attr(755,root,root) /%{_lib}/libheimntlm.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libheimntlm.so.0
%attr(755,root,root) /%{_lib}/libhx509.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libhx509.so.5
%attr(755,root,root) /%{_lib}/libkafs.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libkafs.so.0
%attr(755,root,root) /%{_lib}/libkrb5.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libkrb5.so.26
%attr(755,root,root) /%{_lib}/libroken.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libroken.so.18
%attr(755,root,root) /%{_lib}/libwind.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libwind.so.0

%files libs-common
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhdb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdb.so.9
%attr(755,root,root) %{_libdir}/libkadm5clnt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkadm5clnt.so.7
%attr(755,root,root) %{_libdir}/libkadm5srv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkadm5srv.so.8
%attr(755,root,root) %{_libdir}/libotp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libotp.so.0
%attr(755,root,root) %{_libdir}/libsl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsl.so.0
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/asn1_compile
%attr(755,root,root) %{_libdir}/%{name}/asn1_print
%attr(755,root,root) %{_libdir}/%{name}/slc

%files libs-server
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdc.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krb5-config
%attr(755,root,root) %{_libdir}/libasn1.so
%attr(755,root,root) %{_libdir}/libgssapi.so
%{!?with_openssl:%{_libdir}/libhcrypto.so}
%attr(755,root,root) %{_libdir}/libhdb.so
%attr(755,root,root) %{_libdir}/libheimbase.so
%attr(755,root,root) %{_libdir}/libheimntlm.so
%attr(755,root,root) %{_libdir}/libhx509.so
%attr(755,root,root) %{_libdir}/libkadm5clnt.so
%attr(755,root,root) %{_libdir}/libkadm5srv.so
%attr(755,root,root) %{_libdir}/libkafs.so
%attr(755,root,root) %{_libdir}/libkdc.so
%attr(755,root,root) %{_libdir}/libkrb5.so
%attr(755,root,root) %{_libdir}/libotp.so
%attr(755,root,root) %{_libdir}/libroken.so
%attr(755,root,root) %{_libdir}/libsl.so
%attr(755,root,root) %{_libdir}/libwind.so
%{_libdir}/libasn1.la
%{_libdir}/libgssapi.la
%{!?with_openssl:%{_libdir}/libhcrypto.la}
%{_libdir}/libhdb.la
%{_libdir}/libheimbase.la
%{_libdir}/libheimntlm.la
%{_libdir}/libhx509.la
%{_libdir}/libkadm5clnt.la
%{_libdir}/libkadm5srv.la
%{_libdir}/libkafs.la
%{_libdir}/libkdc.la
%{_libdir}/libkrb5.la
%{_libdir}/libotp.la
%{_libdir}/libroken.la
%{_libdir}/libsl.la
%{_libdir}/libwind.la
%{_includedir}/*.h
%{_includedir}/gssapi
%{!?with_openssl:%{_includedir}/hcrypto}
%{_includedir}/kadm5
%{?with_expose_internals:%{_includedir}/kcm}
%{_includedir}/krb5
%{_includedir}/roken
%{_pkgconfigdir}/heimdal-gssapi.pc
%{_pkgconfigdir}/heimdal-kadm-client.pc
%{_pkgconfigdir}/heimdal-kadm-server.pc
%{_pkgconfigdir}/heimdal-krb5.pc
%{_pkgconfigdir}/kadm-client.pc
%{_pkgconfigdir}/kadm-server.pc
%{_pkgconfigdir}/kafs.pc
%{_pkgconfigdir}/krb5.pc
%{_pkgconfigdir}/krb5-gssapi.pc
%{_mandir}/man1/krb5-config.1*
%{_mandir}/man3/DES_*.3*
%{_mandir}/man3/DH_*.3*
%{_mandir}/man3/EVP_*.3*
%{_mandir}/man3/HDB.3*
%{_mandir}/man3/OSSL_CIPHER_ALGORITHM.3*
%{_mandir}/man3/OpenSSL_add_all_algorithms*.3*
%{_mandir}/man3/PKCS5_PBKDF2_HMAC.3*
%{_mandir}/man3/PKCS5_PBKDF2_HMAC_SHA1.3*
%{_mandir}/man3/RAND_*.3*
%{_mandir}/man3/RSA_*.3*
%{_mandir}/man3/WINCNG_CIPHER_ALGORITHM.3*
%{_mandir}/man3/WINCNG_CIPHER_ALGORITHM_UNAVAILABLE.3*
%{_mandir}/man3/data.3*
%{_mandir}/man3/ecalloc.3*
%{_mandir}/man3/getarg.3*
%{_mandir}/man3/gss_*.3*
%{_mandir}/man3/gssapi*.3*
%{_mandir}/man3/hcrypto_*.3*
%{_mandir}/man3/hdb_*.3*
%{_mandir}/man3/heim_ntlm_*.3*
%{_mandir}/man3/heimbase.3*
%{_mandir}/man3/hx509*.3*
%{_mandir}/man3/internal_v_smechname.3*
%{_mandir}/man3/kadm5_pwcheck.3*
%{_mandir}/man3/kafs.3*
%{_mandir}/man3/krb5*.3*
%{_mandir}/man3/length.3*
%{_mandir}/man3/ntlm*.3*
%{_mandir}/man3/page_*.3*
%{_mandir}/man3/parse_time.3*
%{_mandir}/man3/rtbl.3*
%{_mandir}/man3/wind*.3*
%{_mandir}/man7/krb5-plugin.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libasn1.a
%{_libdir}/libgssapi.a
%{!?with_openssl:%{_libdir}/libhcrypto.a}
%{_libdir}/libhdb.a
%{_libdir}/libheimbase.a
%{_libdir}/libheimntlm.a
%{_libdir}/libhx509.a
%{_libdir}/libkadm5clnt.a
%{_libdir}/libkadm5srv.a
%{_libdir}/libkafs.a
%{_libdir}/libkdc.a
%{_libdir}/libkrb5.a
%{_libdir}/libotp.a
%{_libdir}/libroken.a
%{_libdir}/libsl.a
%{_libdir}/libwind.a

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/hdb_ldap.so

%files -n openldap-schema-heimdal
%defattr(644,root,root,755)
%{schemadir}/hdb.schema
%endif

%files kcm
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/kcm
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/kcm
%attr(755,root,root) /sbin/kcm
%{_mandir}/man8/kcm.8*

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/digest-service
%attr(755,root,root) %{_sbindir}/hprop
%attr(755,root,root) %{_sbindir}/hpropd
%attr(755,root,root) %{_sbindir}/ipropd-master
%attr(755,root,root) %{_sbindir}/ipropd-slave
%attr(755,root,root) %{_sbindir}/iprop-log
%attr(755,root,root) %{_sbindir}/kadmind
%attr(755,root,root) %{_sbindir}/kdc
%attr(755,root,root) %{_sbindir}/kfd
%attr(755,root,root) %{_sbindir}/kpasswdd
%attr(755,root,root) %{_sbindir}/kstash
#%{?with_x11:%attr(755,root,root) %{_sbindir}/kxd}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(754,root,root) /etc/rc.d/init.d/kpasswdd
%attr(754,root,root) /etc/rc.d/init.d/ipropd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/heimdal
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/kadmind
%attr(700,root,root) %dir %{_localstatedir}
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/*
%{_mandir}/man8/hprop.8*
%{_mandir}/man8/hpropd.8*
%{_mandir}/man8/iprop.8*
%{_mandir}/man8/iprop-log.8*
%{_mandir}/man8/kadmind.8*
%{_mandir}/man8/kdc.8*
%{_mandir}/man8/kfd.8*
%{_mandir}/man8/kpasswdd.8*
%{_mandir}/man8/kstash.8*
#%{?with_x11:%{_mandir}/man8/kxd.8*}

%if 0
%files login
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/login
%{_mandir}/man1/login.1*
%{_mandir}/man5/login.access.5*

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%{_mandir}/man1/ftp.1*

%files rsh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rcp
%attr(755,root,root) %{_bindir}/rsh
%{_mandir}/man1/rcp.1*
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
%endif
