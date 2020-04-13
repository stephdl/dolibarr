Name:           dolibarr
Version:        11.0.3
Release:        1%{?dist}
Summary:        Simple, modern & fast web-based email client.
License:        AGPLv3+
Group:          Networking/CRM
URL:            https://www.dolibarr.org/
Source0:        https://github.com/Dolibarr/dolibarr/archive/%{version}.tar.gz


BuildArch:      noarch

%description
RoundCube Webmail is a browser-based multilingual IMAP client
with an application-like user interface. It provides full
functionality you expect from an e-mail client, including MIME
support, address book, folder manipulation, message searching
and spell checking. RoundCube Webmail is written in PHP and 
requires a database: MySQL, PostgreSQL and SQLite are known to
work. The user interface is fully skinnable using XHTML and
CSS 2.

%prep
mkdir %{name}-%{version}
cd %{name}-%{version}
tar xzvf %{SOURCE0}

%build
# Nothing to do!!

%install

# Temp directory
mkdir -p %{buildroot}/usr/share/%{name}/documents


install -d -m 755 %{buildroot}%{_datadir}/%{version}.tar.gz
cp -r %{name}-%{version}/* %{buildroot}%{_datadir}/%{name}


%files
%{_datadir}/%{name}
%dir %attr(0750,apache,apache) %{_datadir}/%{name}/documents
%post
%postun

%changelog
* Mon Apr 06 2020 stephane de labrusse <stephdl@de-labrusse.fr> 1.4.3-el7
- first release
