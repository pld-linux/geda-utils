Summary:	Utilites for gEDA project
Summary(pl):	Narzêdzia dla projektu gEDA
Name:		geda-utils
Version:	20050313
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fbdc7676027a6547f54308b88851395d
URL:		http://www.geda.seul.org/
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	libgeda-devel >= %{version}
BuildRequires:	pkgconfig
Requires:	libgeda >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Several utilities for the gEDA project.

%description -l pl
Narzêdzia u¿ytkowe dla projektu gEDA.

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
