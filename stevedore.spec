#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : stevedore
Version  : 1.8.0
Release  : 14
URL      : http://tarballs.openstack.org/stevedore/stevedore-1.8.0.tar.gz
Source0  : http://tarballs.openstack.org/stevedore/stevedore-1.8.0.tar.gz
Summary  : Manage dynamic plugins for Python applications
Group    : Development/Tools
License  : Apache-2.0
Requires: stevedore-python
BuildRequires : Jinja2
BuildRequires : Pillow
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : funcsigs-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mox3-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
===========================================================
stevedore -- Manage dynamic plugins for Python applications
===========================================================

%package python
Summary: python components for the stevedore package.
Group: Default
Requires: six-python

%description python
python components for the stevedore package.


%prep
%setup -q -n stevedore-1.8.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
