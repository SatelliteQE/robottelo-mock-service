Name:          robottelo-mock-service
Version:       0.0.1
Release:       1%{?dist}
Summary:       Simple mock service for katello-tracer testing in robottelo
License:       GPLv3+
URL:           https://github.com/ogajduse/robottelo-mock-service
Source0:       %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: systemd-rpm-macros

%{?systemd_requires}
Requires:      bash

BuildArch:     noarch

%description
This package provides simple mock service that serves for katello-tracer testing
in robottelo.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_unitdir}
install -m 0644 %{name}.service %{buildroot}/%{_unitdir}/%{name}.service

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name}.sh %{buildroot}/%{_bindir}/%{name}.sh

mkdir -p --mode=0700 $RPM_BUILD_ROOT/%{_var}/log/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%license LICENSE

%{_bindir}/%{name}.sh
%{_unitdir}/%{name}.service
%attr(-,root,-) %dir %{_var}/log/%{name}

%changelog
* Tue Feb 08 2022 Ondřej Gajdušek <ogajduse@redhat.com> - 0.0.1-1
- Initial release

