Name: ea-php72-php-imagick
Version: 3.4.4
Summary: Provides a wrapper to the ImageMagick library.
Release: 1%{?dist}
License: PHP
Group: Programming/Languages
URL: http://pecl.php.net/package/imagick
Source0: https://github.com/Imagick/imagick/archive/3.4.4.tar.gz
Source1: imagick.ini

BuildRequires: ImageMagick-devel
BuildRequires: ea-php72 ea-php72-php-cli ea-php72-php-devel
Requires: ea-php72

%description
Imagick is a native php extension to create and modify images using the ImageMagick API.
This extension requires ImageMagick version 6.2.4+ and PHP 5.1.3+.

IMPORTANT: Version 2.x API is not compatible with earlier versions.

%prep
%setup -q -n imagick-%{version}

%build
scl enable ea-php72 phpize
scl enable ea-php72 ./configure
make

%install
scl enable ea-php72 'make install INSTALL_ROOT=%{buildroot}'
install -m 755 -d $RPM_BUILD_ROOT/opt/cpanel/ea-php72/root/etc/php.d/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/opt/cpanel/ea-php72/root/etc/php.d/

%clean
%{__rm} -rf %{buildroot}

%files
/opt/cpanel/ea-php72/root/usr/lib64/php/modules/imagick.so
/opt/cpanel/ea-php72/root/etc/php.d/imagick.ini
/opt/cpanel/ea-php72/root/usr/include/php/ext/imagick/

%changelog
* Tue May 28 2019 Ricky Grassmuck <r.grassmuck@cpanel.net> - 1.0.0
- Initial spec file creation.
