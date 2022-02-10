Name:          robottelo-mock-service
Version:       0.0.4
Release:       1%{?dist}
Summary:       Simple mock service for katello-tracer testing in robottelo
License:       GPLv3+
URL:           https://github.com/ogajduse/robottelo-mock-service
Source0:       %{name}-%{version}.tar.gz

%if 0%{?rhel} < 8
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%{?systemd_requires}
%endif
BuildRequires: gcc
BuildRequires: make

%{?systemd_requires}

%description
This package provides simple mock service that serves for katello-tracer testing
in robottelo.

%prep
%setup -q

%build
%set_build_flags
%make_build

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}/%{_unitdir}
install -m 0644 %{name}.service %{buildroot}/%{_unitdir}/%{name}.service

mkdir -p --mode=0700 $RPM_BUILD_ROOT/%{_var}/log/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%license LICENSE

%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%attr(-,root,-) %dir %{_var}/log/%{name}

%changelog
* Thu Feb 10 2022 Ondřej Gajdušek <ogajduse@redhat.com> 0.0.4-1
- Change source in spec (ogajduse@redhat.com)

* Thu Feb 10 2022 Ondřej Gajdušek <ogajduse@redhat.com> 0.0.3-1
- new package built with tito

* Wed Feb 09 2022 Ondřej Gajdušek <ogajduse@redhat.com> - 0.0.2-1
- Bump version to 0.0.2

* Tue Feb 08 2022 Ondřej Gajdušek <ogajduse@redhat.com> - 0.0.1-1
- Initial release

