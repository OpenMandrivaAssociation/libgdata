%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	0.0
%define major	22
%define libname %mklibname gdata %{major}
%define devname %mklibname -d gdata
%define girname %mklibname gdata-gir %{api}

Summary:	Library for the GData protocol
Name:		libgdata
Version:	0.18.1
Release:	7
Group:		System/Libraries
License:	LGPLv2+
Url:		http://live.gnome.org/libgdata
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdata/%{url_ver}/%{name}-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/libgdata/-/merge_requests/47
# Build against gcr 4
Patch0:         47.patch

BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:  libtool
BuildRequires:  rootcerts
BuildRequires:	meson
BuildRequires:	vala
BuildRequires:	uhttpmock-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gcr-4)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gio-2.0) >= 2.17.3
BuildRequires:	pkgconfig(glib-2.0) >= 2.19.0
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
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
%autosetup -p1

%build
%meson -Dinstalled_tests=false
%meson_build

%install
%meson_install

%find_lang gdata

%files i18n -f gdata.lang

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}{,.*}

%files -n %{devname}
#doc #{_datadir}/gtk-doc/html/gdata/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/GData-%{api}.gir
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi

%files -n %{girname}
%{_libdir}/girepository-1.0/GData-%{api}.typelib

