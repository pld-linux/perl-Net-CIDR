#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	CIDR
Summary:	Net::CIDR - manipulate IPv4/IPv6 netblocks in CIDR notation
Summary(pl.UTF-8):	Net::CIDR - przetwarzanie bloków sieci IPv4/IPv6 w notacji CIDR
Name:		perl-Net-CIDR
Version:	0.19
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	08bf7e5d5eb07bef562e2f38423eb62c
URL:		http://search.cpan.org/dist/Net-CIDR/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::CIDR package contains functions that manipulate lists of IP
netblocks expressed in CIDR notation. The Net::CIDR functions handle
both IPv4 and IPv6 addresses.

%description -l pl.UTF-8
Pakiet Net::CIDR zawiera funkcje przetwarzające listy bloków sieci IP
zapisanych w notacji CIDR. Funkcje Net::CIDR obsługują adresy IPv4 i
IPv6.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Net/*.pm
%{_mandir}/man3/*
