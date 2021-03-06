Summary:	MySQL backup hook for Bacula
Name:		bacula-backup-mysql
Version:	0.8
Release:	2
License:	GPL v2
Group:		Applications/Databases
Source0:	https://github.com/glensc/bacula-backup-mysql/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e9bf019ba75f2d7db5ec215eb7668632
Patch0:		default-mysqldump.patch
URL:		https://github.com/glensc/bacula-backup-mysql
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	bacula-common
Requires:	perl-DBD-mysql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/bacula

%description
Bacula - It comes by night and sucks the vital essence from your
computers.

This package contains MySQL backup hook.

%prep
%setup -q
%patch0 -p1

%build
pod2man README.pod -o bacula-backup-mysql.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir},%{_mandir}/man1}
install -p %{name}.pl $RPM_BUILD_ROOT%{_sbindir}/%{name}
cp -p backup-mysql.conf $RPM_BUILD_ROOT%{_sysconfdir}
cp -p bacula-backup-mysql.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/backup-mysql.conf
%attr(755,root,root) %{_sbindir}/bacula-backup-mysql
%{_mandir}/man1/bacula-backup-mysql.1*
