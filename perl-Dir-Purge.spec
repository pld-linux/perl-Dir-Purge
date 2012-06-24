#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Dir
%define	pnam	Purge
Summary:	Dir::Purge - Purge directories to a given number of files.
#Summary(pl):	
Name:		perl-Dir-Purge
Version:	1.0
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(File::Path)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dir::Purge implements functions to reduce the number of files in a
directory according to a strategy. It currently provides one strategy:
removal of files by age.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%dir %{perl_sitelib}/Dir
%{perl_sitelib}/Dir/*.pm
%{_mandir}/man3/*
