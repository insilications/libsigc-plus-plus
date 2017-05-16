Name     : libsigc++
Version  : 2.10.0
Release  : 4
URL      : http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.10/libsigc++-2.10.0.tar.xz
Source0  : http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.10/libsigc++-2.10.0.tar.xz
Summary  : Typesafe signal and callback system for C++
Group    : Development/Tools
License  : LGPL-2.1
Requires: libsigc++-lib

%description
libsigc++ -- The Typesafe Callback Framework for C++
General information:
libsigc++ implements a typesafe callback system for standard C++. It
allows you to define signals and to connect those signals to any
callback function, either global or a member function, regardless of
whether it is static or virtual.

%package dev
Summary: dev components for the libsigc++ package.
Group: Development
Requires: libsigc++-lib
Requires: libsigc++-doc
Provides: libsigc++-devel

%description dev
dev components for the libsigc++ package.

%package doc
Summary: doc components for the libsigc++ package.
Group: Documentation

%description doc
doc components for the libsigc++ package.

%package lib
Summary: lib components for the libsigc++ package.
Group: Libraries

%description lib
lib components for the libsigc++ package.


%prep
%setup -q -n libsigc++-2.10.0

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files doc
%defattr(-,root,root,-)
/usr/share/doc/libsigc++-2.0/*
/usr/share/devhelp/books/libsigc++-2.0/libsigc++-2.0.devhelp2

%files dev
%defattr(-,root,root,-)
/usr/include/sigc++-2.0/*
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc
/usr/lib64/sigc++-2.0/include/sigc++config.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
