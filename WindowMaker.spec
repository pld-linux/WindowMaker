Summary:	NeXT-alike window manager
Summary(fr):	Gestionnaire de fenêtres avec le look NeXT
Summary(pl):	Mened¿er okien w stylu NeXT
Name:		WindowMaker
Version:	0.51.0
Release:	1d
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Copyright:	GPL
Source:		ftp://ftp.windowmaker.org/pub/beta/srcs/%{name}-%{version}.tar.bz2
Source1:	ftp://windowmaker.org/pub/WindowMaker-data.tar.gz
Patch:		WindowMaker-pl.po.patch
Patch1:		WindowMaker-po.install.patch
Patch2:		WindowMaker-CFLAGS.patch
Patch3:		WindowMaker-wmconfig.patch
URL:		http://www.windowmaker.org/
Requires:	wmconfig
Requires:	libjpeg
Requires:	libpng
Requires:	libtiff
Requires:	libungif
Requires:	xpm
Requires:	XFree86-libs
Requires:	libPropList
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

%package devel
Summary:	WindowMaker libraries
Summary(fr):	Librairies de WindowMaker
Summary(pl):	Biblioteki WindowMakera
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

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
Requires:	%{name} = %{version}

%description static
This package contains static libraries for building WindowMaker-enhanced
applications.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki niezbêdne do tworzenia
aplikacji wykorzystuj±cych mo¿liwo¶ci mened¿era okien WindowMaker.

%prep
#%setup -q 
%setup -q -a 1
#(cd $RPM_BUILD_DIR/%{name}-%{version}; tar xzf %{SOURCE1})

%patch  -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
echo "b" | LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru se tr" \
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--with-nlsdir=/usr/X11R6/share/locale \
	--enable-kanji \
	--enable-sound \
	--without-gnome \
	--disable-shm \
	--disable-debug \
	--enable-superfluous \
        --enable-newstyle \
	--enable-kde
make \
	LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru se tr" \
	CFLAGS="$RPM_OPT_FLAGS" \
	LDFLAGS="-s" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps

make install \
	LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru se tr" \
	DESTDIR=$RPM_BUILD_ROOT 

install util/bughint $RPM_BUILD_ROOT/usr/X11R6/bin

install WindowMaker-data/pixmaps/* $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/*
bzip2 -9 AUTHORS BUGFORM BUGS ChangeLog FAQ NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.bz2 BUGFORM.bz2 BUGS.bz2 
%doc ChangeLog.bz2 FAQ.bz2 NEWS.bz2 README.bz2

%attr(644,root, man) /usr/X11R6/man/man1/*

/usr/X11R6/share/pixmaps/*

%attr(755,root,root) /usr/X11R6/bin/*

%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

%dir /usr/X11R6/share/WINGs
%dir /usr/X11R6/share/WindowMaker

/usr/X11R6/share/WINGs/*
/usr/X11R6/share/WindowMaker/*

%dir /usr/X11R6/GNUstep
%dir /usr/X11R6/GNUstep/Apps
%dir /usr/X11R6/GNUstep/Apps/WPrefs.app

%attr(755,root,root) /usr/X11R6/GNUstep/Apps/WPrefs.app/WPrefs

/usr/X11R6/GNUstep/Apps/WPrefs.app/tiff
/usr/X11R6/GNUstep/Apps/WPrefs.app/xpm
/usr/X11R6/GNUstep/Apps/WPrefs.app/WPrefs.tiff
/usr/X11R6/GNUstep/Apps/WPrefs.app/WPrefs.xpm

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
%lang(tr) /usr/X11R6/share/locale/tr/LC_MESSAGES/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so

/usr/X11R6/lib/lib*.a
/usr/X11R6/lib/lib*.la
/usr/X11R6/include/*.h

%changelog
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
