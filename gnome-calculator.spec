%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		gnome-calculator
Version:	3.34.0
Release:	1
Summary:	GNOME Desktop calculator
Group:		Graphical desktop/GNOME
License:	GPLv2+
URL:		https://wiki.gnome.org/Calculator
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
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

