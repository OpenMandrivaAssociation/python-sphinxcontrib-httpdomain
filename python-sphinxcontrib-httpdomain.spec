%define module sphinxcontrib-httpdomain
%define oname sphinxcontrib_httpdomain

Name:		python-sphinxcontrib-httpdomain
Version:	2.0.0
Release:	1
Summary:	Sphinx domain for documenting HTTP APIs
Group:		Development/Python
License:	BSD-2-Clause
URL:		https://sphinxcontrib-httpdomain.readthedocs.io
Source0:	https://github.com/sphinx-contrib/httpdomain/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(uv-build)
BuildRequires:	python%{pyver}dist(wheel)

%description
sphinxcontrib.httpdomain This contrib extension, sphinxcontrib.httpdomain,
provides a Sphinx domain for describing HTTP APIs.

%files
%doc README.rst
%{python_sitelib}/sphinxcontrib
%{python_sitelib}/%{oname}-%{version}.dist-info
