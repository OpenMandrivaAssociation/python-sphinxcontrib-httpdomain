# Created by pyp2rpm-3.3.5
%global pypi_name sphinxcontrib-httpdomain

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        1
Summary:        Sphinx domain for documenting HTTP APIs
Group:          Development/Python
License:        BSD
URL:            https://github.com/sphinx-contrib/httpdomain
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
sphinxcontrib.httpdomain This contrib extension, sphinxcontrib.httpdomain,
provides a Sphinx domain for describing HTTP APIs.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_httpdomain-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/sphinxcontrib_httpdomain-%{version}-py%{python3_version}-nspkg.pth
