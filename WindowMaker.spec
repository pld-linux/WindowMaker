Summary:     NeXT-alike window manager
Summary(fr): Gestionnaire de fenêtres avec le look NeXT
Name:        WindowMaker
Version:     0.19.3
Release:     1
Group:       X11/Window Managers
Copyright:   GPL
Vendor:      Dan Pascu <dan@services.iiruc.ro>
URL:         http://www.windowmaker.org
Source:      ftp://ftp.windowmaker.org/pub/beta/srcs/%{name}-%{version}.tar.bz2
Patch0:      WindowMaker-autoconf.patc
Patch1:      WindowMaker-fix_po.patch
Prereq:      /lib/cpp
BuildRoot:   /tmp/%{name}-%{version}-root

%description
WindowMaker is a window manager designed to emulate the look and feel of
part of the NEXTSTEP(tm) GUI. It's supposed to be fast, relatively small,
feature rich and easy to configure, with a simple and elegant appearance
borrowed from NEXTSTEP(tm).

%description -l fr
WindowMaker est un "Window Manager" conçu pour émuler l'apparence et la
sensation de l'interface graphique NeXTSTEP(tm). Il est suposé être rapide,
relativement petit, facile a configurer, extremement complet et avec
l'apparence simple et élégante empruntée a NeXTSTEP(tm).

%package devel
Summary:     WindowMaker libraries
Summary(fr): Librairies de WindowMaker
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
This package contains libraries for building WindowMaker-enhanced
applications.

%description devel -l fr
Ce paquet contient des librairies pour faire des applications mise en valeur
par WindowMaker.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

autoconf

%build
echo "b" | CFLAGS=$RPM_OPT_FLAGS LDFLAGS="-s" ./configure \
		--prefix=/usr/X11R6 \
		--includedir=/usr/include/X11 \
		--with-nlsdir=/usr/share/locale \
		--enable-sound --with-gnome \
		--enable-superfluous \
		--enable-newstyle \
		--disable-debug
make


%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT/usr/{include/X11,X11R6/share/pixmaps}

make	install-strip \
	prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	exec_prefix=$RPM_BUILD_ROOT/usr/X11R6 \
	nlsdir=$RPM_BUILD_ROOT/usr/share/locale \
	includedir=$RPM_BUILD_ROOT/usr/X11R6/include

%clean
rm -r $RPM_BUILD_ROOT

%files
%attr(644, root, root, 755)
%doc AUTHORS BUGFORM BUGS ChangeLog FAQ NEWS README TODO util/bughint
%attr(755, root, root) /usr/X11R6/bin/*
/usr/X11R6/share/*

%dir /usr/X11R6/GNUstep
%dir /usr/X11R6/GNUstep/Apps
%dir /usr/X11R6/GNUstep/Apps/WPrefs.app
%attr(755, root, root) /usr/X11R6/GNUstep/Apps/WPrefs.app/WPrefs
/usr/X11R6/GNUstep/Apps/WPrefs.app/tiff
/usr/X11R6/GNUstep/Apps/WPrefs.app/xpm
/usr/X11R6/GNUstep/Apps/WPrefs.app/WPrefs.tiff
/usr/X11R6/GNUstep/Apps/WPrefs.app/WPrefs.xpm

%lang(cs) /usr/share/locale/cs/LC_MESSAGES/*
%lang(de) /usr/share/locale/de/LC_MESSAGES/*
%lang(el) /usr/share/locale/el/LC_MESSAGES/*
%lang(es) /usr/share/locale/es/LC_MESSAGES/*
%lang(fi) /usr/share/locale/fi/LC_MESSAGES/*
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/*
%lang(gl) /usr/share/locale/gl/LC_MESSAGES/*
%lang(hr) /usr/share/locale/hr/LC_MESSAGES/*
%lang(it) /usr/share/locale/it/LC_MESSAGES/*
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/*
%lang(nl) /usr/share/locale/nl/LC_MESSAGES/*
%lang(no) /usr/share/locale/no/LC_MESSAGES/*
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/*
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/*
%lang(ru) /usr/share/locale/ru/LC_MESSAGES/*
%lang(se) /usr/share/locale/se/LC_MESSAGES/*
%lang(tr) /usr/share/locale/tr/LC_MESSAGES/*

%files devel
%attr(644,root,root) /usr/X11R6/include/*.h
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%changelog
* Thu Sep  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.19.3-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- removed "rm -r %%{builddir}" - it's automatically removed if rpm is runed
  on building with --clean,
- removed COPYING and INSTALL from %doc (copyright statment is in Copyright
  field),
- WindowMaker is now builded from bz2 source tar,
- removed Packager field (this must be placed in persolan ~/.rpmrc),
- nls stuff moved to /usr/share/locale,
- added --disable-debug for configure,
- adde %lang macros for /usr/share/locale/*/LC_MESSAGES/* files,
- added WindowMaker-fix_po.patch wit fixing .po files,
- simplification in %files and added using %defattr macro also.

* Tue Jul 21 1998 W. Reilly Cooley <wcooley@nakedape.ml.org>
- updated from 16.1 to 17.2; made it use RPM_OPT_FLAGS
