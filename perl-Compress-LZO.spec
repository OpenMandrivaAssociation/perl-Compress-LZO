%define real_name Compress-LZO

Summary:	Compress-LZO module for perl 
Name:		perl-%{real_name}
Version:	1.08
Release:	%mkrel 7
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
# seems a hack, but since we don't have liblzo1-devel...
Patch:		Compress-LZO-1.08-lzo2.patch
BuildRequires:	perl-devel
BuildRequires:	liblzo2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LZO is a portable lossless data compression library written in ANSI C. It
offers pretty fast compression and *very* fast decompression. Decompression
requires no memory. Perl-LZO provides LZO bindings for Perl, i.e. you can
access the LZO library from your Perl scripts thereby compressing ordinary Perl
strings.

%prep
%setup -q -n %{real_name}-%{version} 
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

