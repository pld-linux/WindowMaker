%define		extraver	0.1

Summary:	NeXT-alike window manager
Summary(fr):	Gestionnaire de fenêtres avec le look NeXT
Summary(pl):	Mened¿er okien w stylu NeXT
Name:		WindowMaker
Version:	0.53.0
Release:	3
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Copyright:	GPL
Source0:	ftp://ftp.windowmaker.org/pub/beta/srcs/%{name}-%{version}.tar.bz2
Source1:	ftp://windowmaker.org/pub/WindowMaker-data.tar.gz
Source2:	ftp://ftp.windowmaker.org/pub/beta/srcs/%{name}-extra-%{extraver}.tar.gz
Patch0:		WindowMaker-CFLAGS.patch
Patch1:		WindowMaker-wmconfig.patch
Patch2:		WindowMaker-a_macro.patch
Patch3:		WindowMaker-pixmaps.patch
Patch4:		WindowMaker-shared.patch
Patch5:		WindowMaker-areas.patch
Patch6:		WindowMaker-runinst.patch
Patch7:		WindowMaker-configure.patch
URL:		http://www.windowmaker.org/
BuildPrereq:	libPropList-devel >= 0.8.3
BuildPrereq:	xpm-devel
BuildPrereq:	libpng-devel
BuildPrereq:	libjpeg-devel >= 6b
BuildPrereq:	libtiff-devel
BuildPrereq:	gettext
Requires:	wmconfig
Requires:	/lib/cpp
Requires:	%{name}-libs = %{version}
BuildRoot:	/tmp/%{name}-%{version}-root

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

%description -l pl
WindowMaker jest mened¿erem okien przypominaj±cy wygl±dem i wygod± obs³ugi
interfejs systemu NeXTSTEP(tm). Jest szybki, stosunkowo ma³y, o du¿ych
mo¿liwo¶ciach i ³atwy w konfiguracji. Konfiguruje siê go myszk±, za pomoc±
programu WPrefs wchodz±cego w sk³ad tego pakietu.

%package libs
Summary:	WindowMaker shared libraries
Summary(pl):	Biblioteki wspó³dzielone WindowMakera
Group:		Libraries
Group(pl):	Biblioteki

%description libs
This package contains shared libraries for run WindowMaker.

%description libs -l pl
Ten pakiet zawiera biblioteki wspó³dzielone niezbêdne do pracy
mened¿era okien WindowMaker.

%package devel
Summary:	WindowMaker libraries
Summary(fr):	Librairies de WindowMaker
Summary(pl):	Biblioteki WindowMakera
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-libs = %{version}

%description devel
This package contains libraries for building WindowMaker-enhanced
applications.

%description devel -l fr
Ce paquet contient des librairies pour faire des applications mise en valeur
par WindowMaker.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i biblioteki niezbêdne do tworzenia
aplikacji wykorzystuj±cych mo¿liwo¶ci mened¿era okien WindowMaker.

%package static
Summary:	WindowMaker static libraries
Summary(pl):	Biblioteki statyczne WindowMakera
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries for building WindowMaker-enhanced
applications.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki niezbêdne do tworzenia
aplikacji wykorzystuj±cych mo¿liwo¶ci mened¿era okien WindowMaker.

%prep
%setup -q -a 1 -a 2

%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
#patch7 -p1

%build
libtoolize --copy --force
aclocal
autoconf
(cd wrlib;
libtoolize --copy --force
aclocal
autoconf)

LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru  \
	 se sk tr zh_CN zh_TW.Big5" ; export LINGUAS
CPP_PATH="/lib/cpp" ; export CPP_PATH

%configure --prefix=/usr/X11R6 \
	--with-nlsdir=/usr/X11R6/share/locale \
	--sysconfdir=/etc/X11 \
	--enable-kanji \
	--enable-sound \
	--enable-gnome \
	--disable-shm \
	--disable-debug \
	--enable-superfluous \
        --enable-newstyle \
	--enable-kde \
	--enable-shared \
	--enable-static
make \
	LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru  \
	 	se sk tr zh_CN zh_TW.Big5" \
	CFLAGS="$RPM_OPT_FLAGS" \
	LDFLAGS="-s" 

cd %{name}-extra-%{extraver}
./configure \
	--prefix=/usr/X11R6 \
	--with-iconsdir=/usr/X11R6/share/pixmaps

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps

make install \
	LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru  \
	 	se sk tr zh_CN zh_TW.Big5" \
	DESTDIR=$RPM_BUILD_ROOT 

install util/bughint $RPM_BUILD_ROOT/usr/X11R6/bin

install WindowMaker-data/pixmaps/* $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps

(cd %{name}-extra-%{extraver};
make DESTDIR=$RPM_BUILD_ROOT install )

strip --strip-unneeded $RPM_BUILD_ROOT/usr/X11R6/lib/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/* \
	AUTHORS BUGFORM BUGS ChangeLog FAQ NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.gz BUGFORM.gz BUGS.gz 
%doc ChangeLog.gz FAQ.gz NEWS.gz README.gz

%dir /etc/X11/WindowMaker
%config %verify(not size mtime md5) /etc/X11/WindowMaker/*

/usr/X11R6/man/man1/*

/usr/X11R6/share/pixmaps/*

%attr(755,root,root) /usr/X11R6/bin/geticonset
%attr(755,root,root) /usr/X11R6/bin/getstyle
%attr(755,root,root) /usr/X11R6/bin/seticons
%attr(755,root,root) /usr/X11R6/bin/setstyle
%attr(755,root,root) /usr/X11R6/bin/wdwrite
%attr(755,root,root) /usr/X11R6/bin/wkdemenu.pl
%attr(755,root,root) /usr/X11R6/bin/wm-oldmenu2new
%attr(755,root,root) /usr/X11R6/bin/wmaker
%attr(755,root,root) /usr/X11R6/bin/wmaker.inst
%attr(755,root,root) /usr/X11R6/bin/wmsetbg
%attr(755,root,root) /usr/X11R6/bin/wsetfont
%attr(755,root,root) /usr/X11R6/bin/wxcopy
%attr(755,root,root) /usr/X11R6/bin/wxpaste

/usr/X11R6/share/WindowMaker

%dir /usr/X11R6/GNUstep
%dir /usr/X11R6/GNUstep/Apps
%dir /usr/X11R6/GNUstep/Apps/WPrefs.app

%attr(755,root,root) /usr/X11R6/GNUstep/Apps/WPrefs.app/WPrefs

%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/*
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/*
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/*
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/*
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/*
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/*
%lang(gl) /usr/X11R6/share/locale/gl/LC_MESSAGES/*
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/*
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/*
%lang(ja) /usr/X11R6/share/locale/ja/LC_MESSAGES/*
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/*
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/*
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/*
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/*
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/*
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/*
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/*
%lang(se) /usr/X11R6/share/locale/se/LC_MESSAGES/*
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/*
%lang(tr) /usr/X11R6/share/locale/tr/LC_MESSAGES/*
%lang(zh_CN) /usr/X11R6/share/locale/zh_CN/LC_MESSAGES/*
%lang(zh_TW.Big5) /usr/X11R6/share/locale/zh_TW.Big5/LC_MESSAGES/*

/usr/X11R6/GNUstep/Apps/WPrefs.app/tiff
/usr/X11R6/GNUstep/Apps/WPrefs.app/xpm
/usr/X11R6/GNUstep/Apps/WPrefs.app/WPrefs.tiff
/usr/X11R6/GNUstep/Apps/WPrefs.app/WPrefs.xpm

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*
/usr/X11R6/share/WINGs

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so
%attr(755,root,root) /usr/X11R6/bin/get-wraster-flags
/usr/X11R6/include/*.h
/usr/X11R6/lib/lib*.la

%files static
%defattr(644,root,root,755)
/usr/X11R6/lib/lib*.a

%changelog
* Fri Apr 30 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.53.0-3]
- build with grep 2.3 and new libtool

* Wed Apr 28 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.53.0-2]
- added WindowMaker-extra (more themes)
- added areas and runinst patches from RH 6.0

* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.52.0-1]
- recompiles on new rpm,
- more BuildPrereq (libjpg-deve, xpm-devel, libpng-devel, libtiff-devel).

* Fri Mar 12 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.51.2-1]
- added more locale (dk and zh_TW.Big5)
- removed WindowMaker-po.install.patch
- upgraded WindowMaker-pl.po.patch (sync with i18n CVS)
- added WindowMaker-pixmaps.patch (add /usr/X11/share/pixmaps to default 
  icons/pixmaps path)
- added --sysconfdir=/etc/X11 to ./configure
- added /etc/X11/WindowMaker to %%files section

* Wed Mar  3 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.51.0-2]
- removed man group from man pages.

* Tue Feb  9 1999 Micha³ Kuratczyk <kurkens@polbox.com>
- gzipping instead bzipping
- simplification in %files
- cosmetic changes

* Wed Feb  3 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.50.2-1d]
- added stripping shared libraries,
- removed SONAME symlinks from main package.

* Fri Jan 15 1999 Artur Frysiak <wiget@usa.net>
- upgraded to 0.50.2
- rewrite %{name}-po.patch
- added icons (WindowMaker-data.tar.gz) 
  by Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- added --enable-superfluous and --enable-newstyle configure options 
  by Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- added --enable-kde configure options
- added more Requires
- added wmconfig support

* Sat Sep 26 1998 Pawe³ Gajda <pagaj@shadow.eu.org>
  [0.20.0-1d]
- added --disable-shm option to configure script
- added patches to fix I18N stuff
- moved bughint script to /usr/X11R6/bin
- WPrefs is now back in /usr/X11R6/GNUstep
- built against Tornado,
- build from non root's account.

* Mon Sep 21 1998 Pawe³ Gajda <pagaj@shadow.eu.org>
  [0.19.3-2]
- fixed problems with paths to icons, styles and WPrefs
- removed all patches
- moved WPrefs stuff to /usr/X11R6/share/GNUstep
- fixed I18N
- added Polish summary and description

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
