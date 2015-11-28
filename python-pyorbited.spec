
%define		module pyorbited

Summary:	A Python client for the orbited (Orbit Event Daemon)
Summary(pl.UTF-8):	Pythonowy klient demona zdarzeń orbited (Orbit Event Daemon)
Name:		python-%{module}
Version:	0.1.1
Release:	4
License:	MIT
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pyorbited/%{module}-%{version}.zip
# Source0-md5:	50779977e358601a7a19719fc9ace3a5
Patch0:		%{name}-orbited03.patch
URL:		http://brbx.com/orbited/index.html
BuildRequires:	libevent-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
%pyrequires_eq	python-libs
Suggests:	orbited
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python client for the orbited (Orbit Event Daemon), a COMET server.
Includes three implementations: pyevent, twisted, basic sockets.

%description -l pl.UTF-8
Pythonowy klient demona zdarzeń orbited (Orbit Event Daemon), serwera
COMET. Zawiera trzy implementacje: pyevent, twisted i opartą na
zwykłych gniazdach.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/pyorbited
%{py_sitescriptdir}/pyorbited-*.egg-info
