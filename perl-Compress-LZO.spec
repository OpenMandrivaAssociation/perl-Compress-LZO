%define upstream_name    Compress-LZO
%define upstream_version 1.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:	Compress-LZO module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Compress/%{upstream_name}-%{upstream_version}.tar.bz2
# seems a hack, but since we don't have liblzo1-devel...
Patch:		Compress-LZO-1.08-lzo2.patch

BuildRequires:	perl-devel
BuildRequires:	liblzo2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
LZO is a portable lossless data compression library written in ANSI C. It
offers pretty fast compression and *very* fast decompression. Decompression
requires no memory. Perl-LZO provides LZO bindings for Perl, i.e. you can
access the LZO library from your Perl scripts thereby compressing ordinary Perl
strings.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING INSTALL NEWS README
%{perl_vendorlib}/*/Compress/LZO.pm
%{perl_vendorlib}/*/auto/Compress/LZO
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.80.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.80.0-3
+ Revision: 680836
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-2mdv2011.0
+ Revision: 555697
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 403025
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.08-7mdv2009.0
+ Revision: 256041
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.08-5mdv2008.1
+ Revision: 151463
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-4mdv2008.0
+ Revision: 86185
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.08-3mdv2007.0
- rebuild

* Mon Jul 18 2005 Oden Eriksson <oeriksson@mandriva.com> 1.08-2mdk
- fix deps

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.08-1mdk
- initial Mandriva package

