Name:           dolibarr
Version:        13.0.4
Release:        1%{?dist}
Summary:        Dolibarr ERP & CRM is a modern software package to manage your organization's activity (contacts, suppliers, invoices, orders, stocks, agenda…).
License:        AGPLv3+
Group:          Networking/CRM
URL:            https://www.dolibarr.org/
Source0:        https://github.com/Dolibarr/dolibarr/archive/%{version}.tar.gz


BuildArch:      noarch

%description 
Dolibarr ERP & CRM is a modern software package to manage your organization's activity (contacts, suppliers, invoic  es, orders, stocks, agenda…).

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
cp -r %{name}-%{version}/%{name}-%{version}/* %{buildroot}%{_datadir}/%{name}


%files
%{_datadir}/%{name}
%dir %attr(0750,apache,apache) %{_datadir}/%{name}/documents
%dir %attr(0750,apache,apache) %{_datadir}/%{name}/htdocs/custom
%post
%postun

%changelog
* Tue Aug 10 2021  stephane de Labrusse <stephdl@de-labrusse.fr>
- Bump to 13.0.4

* Fri Jul 02 2021  stephane de Labrusse <stephdl@de-labrusse.fr>
- Bump to 13.0.3

* Thu Apr 21 2021 stephane de Labrusse <stephdl@de-labrusse.fr>
- Upstream upgrade to 13.0.2

* Thu Jan 14 2021 stephane de Labrusse <stephdl@de-labrusse.fr>
- Upstream upgrade to 12.0.4

* Thu Nov 05 2020 stephane de labrusse <stephdl@de-labrusse.fr> 12.0.3
- Upstream update 

* Tue Aug 04 2020 stephane de labrusse <stephdl@de-labrusse.fr> 12.0.1
- Upstream update 

* Sun Apr 19 2020 stephane de labrusse <stephdl@de-labrusse.fr> 
- chmod/chown apache:apache custom folder

* Mon Apr 06 2020 stephane de labrusse <stephdl@de-labrusse.fr> 11.0.0
- first release
