%define upstream_name    Crypt-RC4
%define upstream_version 2.02
Name:		perl-%{upstream_name}
Version:	2.02
Release:	2

Summary:	Crypt-RC4 module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Crypt-RC4
Source0:	https://cpan.metacpan.org/authors/id/S/SI/SIFUKURT/Crypt-RC4-2.02.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides a simple implementation of the RC4 algorithm.

%prep
%setup -q -n Crypt-RC4-2.02

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test || :

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Crypt/RC4.pm
%{_mandir}/*/*


