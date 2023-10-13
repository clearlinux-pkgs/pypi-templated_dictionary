#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-templated_dictionary
Version  : 1.2
Release  : 17
URL      : https://files.pythonhosted.org/packages/16/32/5e9726056345a1943d250ac51d2c17476f965495554d058c9dd308d790fa/templated-dictionary-1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/16/32/5e9726056345a1943d250ac51d2c17476f965495554d058c9dd308d790fa/templated-dictionary-1.2.tar.gz
Summary  : Dictionary with Jinja2 expansion
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pypi-templated_dictionary-license = %{version}-%{release}
Requires: pypi-templated_dictionary-python = %{version}-%{release}
Requires: pypi-templated_dictionary-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jinja2)

%description
# templated-dictionary
This module provides dictionary where every item is evaluated as a Jinja2 expression.

%package license
Summary: license components for the pypi-templated_dictionary package.
Group: Default

%description license
license components for the pypi-templated_dictionary package.


%package python
Summary: python components for the pypi-templated_dictionary package.
Group: Default
Requires: pypi-templated_dictionary-python3 = %{version}-%{release}

%description python
python components for the pypi-templated_dictionary package.


%package python3
Summary: python3 components for the pypi-templated_dictionary package.
Group: Default
Requires: python3-core
Provides: pypi(templated_dictionary)
Requires: pypi(jinja2)

%description python3
python3 components for the pypi-templated_dictionary package.


%prep
%setup -q -n templated-dictionary-1.2
cd %{_builddir}/templated-dictionary-1.2
pushd ..
cp -a templated-dictionary-1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670884831
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-templated_dictionary
cp %{_builddir}/templated-dictionary-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-templated_dictionary/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-templated_dictionary/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
