%global pypi_name requestsexceptions

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        2%{?dist}
Summary:        Import exceptions from potentially bundled packages in requests

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a simple library to find the correct path to exceptions in the
requests library regardless of whether they are bundled.

%package -n python2-%{pypi_name}
Summary:        Import exceptions from potentially bundled packages in requests
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python-pbr

%description -n python2-%{pypi_name}
This is a simple library to find the correct path to exceptions in the
requests library regardless of whether they are bundled.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build

%install
%py2_install

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/*.egg-info

%changelog
* Mon Nov 23 2015 jpena <jpena@redhat.com> - 1.1.1-2
- Used macros for prep, build and install
* Tue Nov 17 2015 jpena <jpena@redhat.com> - 1.1.1-1
- Initial package.
