%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	0.0
%define major	22
%define libname %mklibname gdata %{major}
%define devname %mklibname -d gdata
%define girname %mklibname gdata-gir %{api}

Summary:	Library for the GData protocol
Name:		libgdata
Version:	0.17.4
Release:	4
Group:		System/Libraries
License:	LGPLv2+
Url:		http://live.gnome.org/libgdata
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdata/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:  libtool
BuildRequires:  rootcerts
BuildRequires:	uhttpmock-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gcr-base-3)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(oauth) >= 0.9.4
Requires:       rootcerts

%description
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

%package i18n
Summary:	Library for the GData protocol - translations
Group:		System/Internationalization

%description i18n
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

%package -n %{libname}
Summary:	Library for the GData protocol
Group:		System/Libraries
Suggests:	%{name}-i18n

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{girname}
Group:		System/Libraries
Summary:	GObject Introspection interface library for %{name}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure \
	--disable-static \
	--with-ca-certs=/etc/pki/tls/certs/ca-bundle.crt

%make

%install
%makeinstall_std
%find_lang gdata

%files i18n -f gdata.lang

%files -n %{libname}
%{_libdir}/libgdata.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GData-%{api}.typelib

%files -n %{devname}
%doc NEWS README AUTHORS
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/gdata/
%{_datadir}/gir-1.0/GData-%{api}.gir

