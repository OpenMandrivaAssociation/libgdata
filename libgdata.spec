%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major 13
%define gir_major 0.0
%define libname %mklibname gdata %{major}
%define develname %mklibname -d gdata
%define girname %mklibname gdata-gir %{gir_major}

Summary:	Library for the GData protocol
Name:		libgdata
Version:	0.13.2
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://live.gnome.org/libgdata
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdata/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:         libgdata-0.13.0-CVE-2012-1177.diff
BuildRequires:  autoconf automake libtool
BuildRequires:  rootcerts
Requires:       rootcerts
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gcr-base-3)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(oauth) >= 0.9.4

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
#apply_patches
%patch0 -p0 -b .CVE-2012-1177

%build
%configure2_5x \
    --disable-static \
    --with-ca-certs=/etc/pki/tls/certs/ca-bundle.crt

%make

%install
%makeinstall_std
%find_lang gdata

# remove unpackaged files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files i18n -f gdata.lang

%files -n %{libname}
%doc NEWS README AUTHORS
%{_libdir}/libgdata.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GData-%{gir_major}.typelib

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/gdata/
%{_datadir}/gir-1.0/GData-0.0.gir


%changelog
* Tue Oct 16 2012 Arkady L. Shane <ashejn@rosalab.ru> 0.13.2-1
- update to 0.13.2

* Wed Jul 25 2012 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-3
+ Revision: 810996
- fix CVE-2012-1177

* Wed Apr 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.12.0-2
+ Revision: 793380
- rebuild for typelib

* Wed Apr 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.12.0-1
+ Revision: 793296
- new version 0.12.0

* Wed Apr 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.10.2-2
+ Revision: 790294
- rebuild for rpmlib(distepoch)

* Mon Mar 12 2012 Götz Waschk <waschk@mandriva.org> 0.10.2-1
+ Revision: 784393
- update build deps
- fix linking
- new version

* Sat Nov 19 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.10.1-1
+ Revision: 731765
- fix major
- adjusted BRs
- new version 0.10.1
- split out gir pkg
- removed mkrel BuildRoot
- remove defattr
- removed old ldconfig scriptlets
- removed clean & check sections
- removed .la files
- cleaned up spec
- shortened lib * devel pkg descriptions
- converted BRs to pkgconfig provides

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-3
+ Revision: 662368
- mass rebuild

* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 0.6.6-2
+ Revision: 650927
- rebuild for updated libsoup libtool archive

* Sat Dec 11 2010 Götz Waschk <waschk@mandriva.org> 0.6.6-1mdv2011.0
+ Revision: 620587
- update to new version 0.6.6

* Thu Sep 30 2010 Götz Waschk <waschk@mandriva.org> 0.6.5-1mdv2011.0
+ Revision: 582187
- update to new version 0.6.5

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 0.6.4-5mdv2011.0
+ Revision: 577924
- rebuild for new g-i

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.6.4-4mdv2011.0
+ Revision: 568187
- disable check
- rebuild for new libproxy

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 0.6.4-2mdv2011.0
+ Revision: 563853
- rebuild for new gobject-introspection

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 0.6.4-1mdv2010.1
+ Revision: 528949
- update to new version 0.6.4

* Sat Mar 20 2010 Götz Waschk <waschk@mandriva.org> 0.6.3-1mdv2010.1
+ Revision: 525397
- update to new version 0.6.3

* Sun Feb 21 2010 Götz Waschk <waschk@mandriva.org> 0.6.2-1mdv2010.1
+ Revision: 509183
- update to new version 0.6.2

* Tue Feb 16 2010 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 506430
- update to new version 0.6.1

* Sun Feb 14 2010 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 505966
- new version
- new major
- add gobject-introspection support

* Mon Nov 23 2009 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2010.1
+ Revision: 469214
- update to new version 0.5.1

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2010.0
+ Revision: 447296
- new version
- new major

* Mon Jul 20 2009 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2010.0
+ Revision: 398208
- new version
- new major

* Mon May 25 2009 Götz Waschk <waschk@mandriva.org> 0.3.0-1mdv2010.0
+ Revision: 379551
- fix build deps
- new version
- new major
- fix check

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 0.2.0-2mdv2010.0
+ Revision: 374639
- fix devel provides

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdv2010.0
+ Revision: 374526
- import libgdata

