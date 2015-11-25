%if 0%{?fedora}
%global with_python3 1
%endif


%global pypi_name requestsexceptions

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
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

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Import exceptions from potentially bundled packages in requests
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr

%description -n python3-%{pypi_name}
This is a simple library to find the correct path to exceptions in the
requests library regardless of whether they are bundled.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/*.egg-info
%endif

%changelog
