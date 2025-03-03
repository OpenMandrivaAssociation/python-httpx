%define pypi_name httpx

Name:       python-%{pypi_name}
Version:    0.28.1
Release:    1
Summary:    The next generation HTTP client
Group:      Development/Python
License:    BSD
URL:        https://pypi.org/project/httpx
Source0:    https://files.pythonhosted.org/packages/source/h/httpx/httpx-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(hatchling)
BuildSystem:  python

%description
HTTPX is a fully featured HTTP client for Python 3, which provides sync and
async APIs, and support for both HTTP/1.1 and HTTP/2.

%files
%{_bindir}/httpx
