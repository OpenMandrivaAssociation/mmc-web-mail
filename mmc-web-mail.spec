%define _requires_exceptions pear(graph\\|pear(includes\\|pear(modules
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	Postfix/Mail module for the MMC web interface
Name:		mmc-web-mail
Version:	2.3.2
Release:	%mkrel 3
License:	GPL
Group:		System/Servers
URL:		https://mds.mandriva.org/
Source0:	%{name}-%{version}.tar.gz
Patch0:		mmc-web-mail-Makefile_fix.diff
Requires:	postfix
Requires:	mmc-web-base >= 2.3.2
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mandriva Management Console web interface designed by Linbox.

This is the Mail module.

%prep

%setup -q -n %{name}-%{version}
for i in `find . -type d -name .svn`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%patch0 -p0

%build

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang mail

%clean
rm -rf %{buildroot}

%files -f mail.lang
%defattr(-,root,root,0755)
%doc Changelog
%dir %{_datadir}/mmc/modules/mail
%{_datadir}/mmc/modules/mail/graph
%{_datadir}/mmc/modules/mail/includes
%dir %{_datadir}/mmc/modules/mail/locale
%dir %{_datadir}/mmc/modules/mail/locale/*/
%dir %{_datadir}/mmc/modules/mail/locale/*/LC_MESSAGES
%{_datadir}/mmc/modules/mail/mail
%{_datadir}/mmc/modules/mail/infoPackage.inc.php
