Summary:	Run maintenance tasks outside the OS
Name:		maintboot
Version:	0.1.0
Release:	0.1
License:	GPL v3
Group:		Applications/System
Source0:	https://pypi.python.org/packages/source/m/maintboot/%{name}-%{version}.tar.gz
# Source0-md5:	c70a7743f2654274494d6a5c261a55f1
URL:		https://github.com/g2p/maintboot
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
maintboot runs commands outside of the current OS, with exclusive
access to the system and hardware.

This can be useful to run maintenance tasks, like repartitioning, in a
controlled environment.

Maintboot builds an appliance on the fly from a list of packages
(using supermin). It then loads the appliance with kexec, bypassing
the bios, and runs the maintenance ...

%prep
%setup -q

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# egg has no value for executable
rm $RPM_BUILD_ROOT%{py3_sitescriptdir}/maintboot-%{version}-py*.egg-info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/maintboot
