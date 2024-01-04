%global glib2_version 2.69.1

Name:    libsoup3
Version: 3.4.4
Release: 1
Summary: Soup, an HTTP library implementation
License: LGPLv2+
URL:     https://wiki.gnome.org/Projects/libsoup
Source0: %{name}-%{version}.tar.xz

BuildRequires: gettext
BuildRequires: glib-networking
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libnghttp2)
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(sqlite3)

Recommends: glib-networking >= %{glib2_version}

%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.

libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it), but the SOAP parts were removed
long ago.

%package devel
Summary: Header files for the Soup library
Requires: %{name} = %{version}-%{release}

%description devel
Libsoup is an HTTP library implementation in C. This package allows
you to develop applications that use the libsoup library.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson \
  -Dautobahn=disabled \
  -Dbrotli=disabled \
  -Ddocs=disabled \
  -Dgssapi=disabled \
  -Dntlm=disabled \
  -Dpkcs11_tests=disabled \
  -Dsysprof=disabled \
  -Dvapi=disabled
%meson_build

%install
%meson_install
install -m 644 -D tests/libsoup.supp %{buildroot}%{_datadir}/libsoup-3.0/libsoup.supp

%find_lang libsoup-3.0

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f libsoup-3.0.lang
%license COPYING
%doc README NEWS AUTHORS
%{_libdir}/libsoup-3.0.so.0*
%{_libdir}/girepository-1.0/Soup-3.0.typelib

%files devel
%{_includedir}/libsoup-3.0
%{_libdir}/libsoup-3.0.so
%{_libdir}/pkgconfig/libsoup-3.0.pc
%dir %{_datadir}/libsoup-3.0
%{_datadir}/libsoup-3.0/libsoup.supp
%{_datadir}/gir-1.0/Soup-3.0.gir
