Summary:	Utilites for gEDA project.
Summary(pl):	Narzêdzia dla projektu gEDA.
Name:		geda-utils
Version:	20010304
Release:	1
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/utils-%{version}.tar.gz
URL:		http://www.geda.seul.org/
BuildRequires:	libgeda-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Several utilities for the gEDA project.

%description -l pl
Narzêdzia u¿ytkowe dla projektu gEDA.

%prep
%setup  -q -n utils

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
