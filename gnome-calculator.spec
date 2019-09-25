%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

%global major   0
%define api             1
%global libname         %mklibname gcalc %{api} %{major}
%global develname         %mklibname -d gcalc

Name:		gnome-calculator
Version:	3.34.0
Release:	1
Summary:	GNOME Desktop calculator
Group:		Graphical desktop/GNOME
License:	GPLv2+
URL:		https://wiki.gnome.org/Calculator
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-4)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	libmpc-devel
BuildRequires:  gmp-devel
BuildRequires:	meson
BuildRequires:	vala
BuildRequires:  vala-tools
BuildRequires:  pkgconfig(vapigen)
Provides:	gcalctool = %{version}
Obsoletes:	gcalctool <= 6.6.2
Requires:       %libname = %version

%description
Calculator is an application that solves mathematical equations and is
suitable as a default application in a Desktop environment.

What Calculator is:
- A tool for calculating mathematical equations.
- Uses standard mathematical notation where possible.
- Easy enough to use for simple maths.
- Powerful enough for mid-level mathematics.
- Fast to load and responsive to input.
- Appropriately sized to fit into standard screen resolutions.
- Fully accessible.
- Well documented.
- Integrated into the GNOME Desktop.

What Calculator is not:
- It does not emulate any existing calculator interfaces, hardware or software.
- It is not a power-tool for professional mathematicians.
- It is not a programming language.

%package -n %libname
Summary:  Libraries for %{name}
Group:    System/Libraries
	 
%description -n %libname
This package contains the shared libraries for %name.

%package        -n %develname
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    -n %develname
The %{name}-devel package contains libraries and header files for developing applications that use %{name}.

%prep
%setup -q
%apply_patches

%build
%meson -Ddocs=true
%meson_build

%install
%meson_install


%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING NEWS
%{_bindir}/gcalccmd
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Calculator.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Calculator-search-provider.ini
%{_datadir}/metainfo/org.gnome.Calculator.appdata.xml
%{_datadir}/icons/hicolor/*
#{_libdir}/%{name}
%doc %{_mandir}/man1/%{name}.1.*
%doc %{_mandir}/man1/gcalccmd.1*
/usr/libexec/%{name}-search-provider

%files -n %libname
%{_libdir}/libgcalc-%{api}.so.%{major}*

%files -n %develname
%{_includedir}/gcalc-1/gcalc/gcalc.h
%{_libdir}/libgcalc-1.so
%{_libdir}/pkgconfig/gcalc-1.pc
%{_datadir}/gir-1.0/GCalc-1.gir
%{_datadir}/vala/vapi/gcalc-1.deps
%{_datadir}/vala/vapi/gcalc-1.vapi

