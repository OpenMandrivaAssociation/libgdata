%define major 7
%define libname %mklibname gdata %major
%define develname %mklibname -d gdata
%define girname %mklibname gdata-gir 0.0

Name:		libgdata
Version:	0.10.1
Release:	1
Summary:	Library for the GData protocol
Group:		System/Libraries
License:	LGPLv2+
URL:		http://live.gnome.org/libgdata
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

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

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{girname}
Group:		System/Libraries
Summary:	GObject Introspection interface library for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains libraries and header files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang gdata

# remove unpackaged files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files i18n -f gdata.lang

%files -n %{libname}
%doc NEWS README AUTHORS
%{_libdir}/libgdata.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GData-0.0.typelib

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/gdata/
%{_datadir}/gir-1.0/GData-0.0.gir

