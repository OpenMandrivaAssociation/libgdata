%define major 6
%define libname %mklibname gdata %major
%define develname %mklibname -d gdata

Name:           libgdata
Version:        0.5.0
Release:        %mkrel 1
Summary:        Library for the GData protocol

Group:          System/Libraries
License:        LGPLv2+
URL:            http://live.gnome.org/libgdata
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  libsoup-devel 
BuildRequires:  dbus-glib-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool

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
Requires: %name-i18n >= %version

%description -n %{libname}
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.


%package -n %develname
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:	%name-devel = %version-%release

%description -n %develname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang gdata

%clean
rm -rf $RPM_BUILD_ROOT

%check
# Only the general test can be run without network access
cd gdata/tests
LD_LIBRARY_PATH=../.libs/ ./general

%if %mdvver < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files i18n -f gdata.lang

%files -n %libname
%defattr(-,root,root,-)
%doc COPYING.LIB NEWS README AUTHORS
%{_libdir}/libgdata.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/gdata/

