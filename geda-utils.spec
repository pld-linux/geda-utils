# 1Revision: 1.22 $, $Date: 2008-12-21 15:27:24 $
Summary:	Utilites for gEDA project
Summary(pl.UTF-8):	Narzędzia dla projektu gEDA
Name:		geda-utils
Version:	1.4.2
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/release/v1.4/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	641db62f76de101ced936b7c1a9c8dda
URL:		http://www.geda.seul.org/
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	libgeda-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
Requires:	libgeda >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Several utilities for the gEDA project.

%description -l pl.UTF-8
Narzędzia użytkowe dla projektu gEDA.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README docs/README.*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gEDA/system-gschlasrc
%{_docdir}/geda-doc/readmes/README*
