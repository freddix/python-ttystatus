Summary:	Python library for showing progress reporting
Name:		python-ttystatus
Version:	0.19
Release:	1
License:	GPL v3
Group:		Libraries/Python
Source0:	http://code.liw.fi/debian/pool/main/p/python-ttystatus/%{name}_%{version}.orig.tar.gz
# Source0-md5:	93638e9d92810c6b1d217ce045a26469
URL:		http://liw.fi/cliapp/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ttystatus is a Python library for showing progress reporting
and status updates on terminals.

%prep
%setup -qn ttystatus-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/ttystatus
%{py_sitescriptdir}/ttystatus/*.py[co]

