#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : stevedore
Version  : 1.30.1
Release  : 48
URL      : http://tarballs.openstack.org/stevedore/stevedore-1.30.1.tar.gz
Source0  : http://tarballs.openstack.org/stevedore/stevedore-1.30.1.tar.gz
Source99 : http://tarballs.openstack.org/stevedore/stevedore-1.30.1.tar.gz.asc
Summary  : Manage dynamic plugins for Python applications
Group    : Development/Tools
License  : Apache-2.0
Requires: stevedore-license = %{version}-%{release}
Requires: stevedore-python = %{version}-%{release}
Requires: stevedore-python3 = %{version}-%{release}
Requires: pbr
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
===========================================================
stevedore -- Manage dynamic plugins for Python applications
===========================================================

%package license
Summary: license components for the stevedore package.
Group: Default

%description license
license components for the stevedore package.


%package python
Summary: python components for the stevedore package.
Group: Default
Requires: stevedore-python3 = %{version}-%{release}

%description python
python components for the stevedore package.


%package python3
Summary: python3 components for the stevedore package.
Group: Default
Requires: python3-core

%description python3
python3 components for the stevedore package.


%prep
%setup -q -n stevedore-1.30.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551397691
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/stevedore
cp LICENSE %{buildroot}/usr/share/package-licenses/stevedore/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/stevedore/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
