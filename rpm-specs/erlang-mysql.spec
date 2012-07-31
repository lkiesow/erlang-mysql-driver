Name:          erlang-mysql-driver
Version:       20120731
Release:       1%{?dist}
Summary:       Erlang MySQL Driver
Group:         System Environment/Libraries
License:       BSD
URL:           https://github.com/dizzyd/erlang-mysql-driver
Source0:       %{name}-%{version}-%{release}.tar.gz

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: erlang


%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}


%description
This MySQL driver for Erlang is based on the Yxa driver obtained from Process
One (at https://support.process-one.net/doc/display/CONTRIBS/Yxa). It includes
several new features such as prepared statements, transactions, binary queries,
type-converted query results, more efficient logging and a new connection
pooling mechanism.


%prep
%setup -q -n %{name}
iconv -f ISO-8859-1 -t utf-8 COPYING.txt > COPYING-utf8.txt

%build
%__make clean all

%install
rm -rf $RPM_BUILD_ROOT
%__install -dm 755 %{buildroot}%{_libdir}/erlang/lib/mysql
%__install -dm 755 %{buildroot}%{_libdir}/erlang/lib/mysql/src
%__install -dm 755 %{buildroot}%{_libdir}/erlang/lib/mysql/ebin
%__install -dm 755 %{buildroot}%{_libdir}/erlang/lib/mysql/include
%__install -m  644 ebin/*    %{buildroot}%{_libdir}/erlang/lib/mysql/ebin/
%__install -m  644 src/*     %{buildroot}%{_libdir}/erlang/lib/mysql/src/
%__install -m  644 include/* %{buildroot}%{_libdir}/erlang/lib/mysql/include/


%clean
[ -d "%{buildroot}" -a "%{buildroot}" != "" ] && %__rm -rf "%{buildroot}"

%post

%postun

%files
%defattr(-,root,root,-)
%doc README.txt COPYING-utf8.txt
%{_libdir}/erlang/lib/mysql

%changelog
* Tue Jul 31 2012 <lkiesow@uos.de> - 20120731-1
- Initial spec file for erlang-mysql-driver
