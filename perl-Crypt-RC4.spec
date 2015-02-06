%define upstream_name    Crypt-RC4
%define upstream_version 2.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Crypt-RC4 module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides a simple implementation of the RC4 algorithm.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Crypt/RC4.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.20.0-2mdv2011.0
+ Revision: 680865
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.20.0-1mdv2011.0
+ Revision: 403037
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.02-3mdv2009.0
+ Revision: 256336
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.02-1mdv2008.1
+ Revision: 136699
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 2.02-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.02-1mdk
- initial Mandriva package

