#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Dir
%define	pnam	Purge
Summary:	Dir::Purge - purge directories to a given number of files
Summary(pl):	Dir::Purge - czyszczenie katalogu do podanej liczby plików
Name:		perl-Dir-Purge
Version:	1.0
Release:	3
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6321bb4373f3aef6f8c4484dee7d692d
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::Path)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dir::Purge implements functions to reduce the number of files in a
directory according to a strategy. It currently provides one strategy:
removal of files by age.

%description -l pl
Modu³ Dir::Purge jest implementacj± funkcji zmniejszaj±cej liczbê
plików w katalogu zgodnie ze strategi±. Aktualnie obs³uguje jedn±
strategiê: usuwanie plików w zale¿no¶ci od ich wieku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%dir %{perl_vendorlib}/Dir
%{perl_vendorlib}/Dir/*.pm
%{_mandir}/man3/*
