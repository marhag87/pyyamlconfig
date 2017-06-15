%define    shortname pyyamlconfig

Name:      python3-%{shortname}
Version:   0.2.1
Release:   1%{?dist}
Summary:   Load configuration file in yaml format

Group:     Development/Libraries
License:   WTFPL
URL:       https://github.com/marhag87/pyyamlconfig
Source0:   https://github.com/marhag87/%{shortname}/archive/v%{version}.tar.gz#/%{shortname}-%{version}.tar.gz

BuildArch: noarch

Requires:  python3-PyYAML

%description
Load configuration file in yaml format

%prep
%setup -q -n "%{shortname}"

%build
%py3_build

%install
%py3_install

%files
/usr/lib/python3.5/site-packages/%{shortname}/*
/usr/lib/python3.5/site-packages/%{shortname}-%{version}-py3.5.egg-info/*

%changelog
* Thu Jun 15 2017 Martin Hagstrom <marhag87@gmail.com> 0.2.1-1
- Initial release
