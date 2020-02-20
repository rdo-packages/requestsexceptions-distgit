# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}}
%global pypi_name requestsexceptions

%global common_desc \
This is a simple library to find the correct path to exceptions in the \
requests library regardless of whether they are bundled.

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Import exceptions from potentially bundled packages in requests

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n python%{pyver}-%{pypi_name}
Summary:        Import exceptions from potentially bundled packages in requests
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools

%description -n python%{pyver}-%{pypi_name}
%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{upstream_version}

%build
%{pyver_build}

%install
%{pyver_install}

%files -n python%{pyver}-%{pypi_name}
%doc README.rst
%license LICENSE
%{pyver_sitelib}/%{pypi_name}
%{pyver_sitelib}/*.egg-info

%changelog
