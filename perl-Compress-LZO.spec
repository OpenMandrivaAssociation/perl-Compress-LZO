%define upstream_name    Compress-LZO
%define upstream_version 1.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Compress-LZO module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
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
