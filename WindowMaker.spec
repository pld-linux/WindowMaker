%define		extraver	0.1

Summary:	NeXT-alike window manager
Summary(fr):	Gestionnaire de fen�tres avec le look NeXT
Summary(pl):	Mened�er okien w stylu NeXT
Name:		WindowMaker
Version:	0.60.0
Release:	2
Group:		X11/Window Managers
Group(pl):	X11/Zarz�dcy Okien
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
Patch7:		WindowMaker-ru.po.patch
Patch8:		Windowmaker-WINGs.h.patch
URL:		http://www.windowmaker.org/
BuildPrereq:	libPropList-devel >= 0.8.3
BuildPrereq:	xpm-devel
BuildPrereq:	libpng-devel
BuildPrereq:	libjpeg-devel >= 6b
BuildPrereq:	libtiff-devel
BuildPrereq:	libungif-devel
BuildPrereq:	gettext
Requires:	wmconfig
Requires:	/lib/cpp
Requires:	%{name}-libs = %{version}
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11

%description
WindowMaker is a window manager designed to emulate the look and feel of
part of the NEXTSTEP(tm) GUI. It's supposed to be fast, relatively small,
feature rich and easy to configure, with a simple and elegant appearance
borrowed from NEXTSTEP(tm).

%description -l fr
WindowMaker est un "Window Manager" con�u pour �muler l'apparence et la
sensation de l'interface graphique NeXTSTEP(tm). Il est supos� �tre rapide,
relativement petit, facile a configurer, extremement complet et avec
l'apparence simple et �l�gante emprunt�e a NeXTSTEP(tm).

%description -l pl
WindowMaker jest mened�erem okien przypominaj�cy wygl�dem i wygod� obs�ugi
interfejs systemu NeXTSTEP(tm). Jest szybki, stosunkowo ma�y, o du�ych
mo�liwo�ciach i �atwy w konfiguracji. Konfiguruje si� go myszk�, za pomoc�
programu WPrefs wchodz�cego w sk�ad tego pakietu.

%package libs
Summary:	WindowMaker shared libraries
Summary(pl):	Biblioteki wsp�dzielone WindowMakera
Group:		Libraries
Group(pl):	Biblioteki

%description libs
This package contains shared libraries for run WindowMaker.

%description libs -l pl
Ten pakiet zawiera biblioteki wsp�dzielone niezb�dne do pracy
mened�era okien WindowMaker.

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
Ten pakiet zawiera pliki nag��wkowe i biblioteki niezb�dne do tworzenia
aplikacji wykorzystuj�cych mo�liwo�ci mened�era okien WindowMaker.

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
Ten pakiet zawiera statyczne biblioteki niezb�dne do tworzenia
aplikacji wykorzystuj�cych mo�liwo�ci mened�era okien WindowMaker.

%prep
%setup -q -a 1 -a 2

%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p1

%build
autoconf
LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru  \
	 se sk tr zh_CN zh_TW.Big5" ; export LINGUAS
CPP_PATH="/lib/cpp" ; export CPP_PATH

%configure \
	--sysconfdir=%{_sysconfdir} \
	--with-nlsdir=%{_datadir}/locale \
	--enable-kanji \
	--enable-sound \
	--enable-gnome \
	--disable-debug \
	--enable-superfluous \
        --enable-newstyle \
	--enable-kde \
	--enable-shared \
	--enable-static \
	--enable-usermenu

touch WindowMaker/Defaults/W*.in

make \
	LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru  \
	 	se sk tr zh_CN zh_TW.Big5" \
	CFLAGS="$RPM_OPT_FLAGS" \
	LDFLAGS="-s" 

autoconf
cd %{name}-extra-%{extraver}
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--with-nlsdir=%{_datadir}/locale \
	--with-iconsdir=%{_datadir}/pixmaps

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps

make install \
	LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru  \
	 	se sk tr zh_CN zh_TW.Big5" \
	DESTDIR=$RPM_BUILD_ROOT 

install util/bughint $RPM_BUILD_ROOT%{_bindir}

install WindowMaker-data/pixmaps/* $RPM_BUILD_ROOT%{_datadir}/pixmaps

(cd %{name}-extra-%{extraver};
make DESTDIR=$RPM_BUILD_ROOT install )

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS BUGFORM BUGS ChangeLog FAQ NEWS README

%find_lang %{name}
%find_lang WPrefs
cat WPrefs.lang >> %{name}.lang

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -r $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.gz BUGFORM.gz BUGS.gz 
%doc ChangeLog.gz FAQ.gz NEWS.gz README.gz

%dir /etc/X11/WindowMaker
%config %verify(not size mtime md5) %{_sysconfdir}/WindowMaker/*

%{_mandir}/man1/*

%{_datadir}/pixmaps/*

%attr(755,root,root) %{_bindir}/geticonset
%attr(755,root,root) %{_bindir}/getstyle
%attr(755,root,root) %{_bindir}/seticons
%attr(755,root,root) %{_bindir}/setstyle
%attr(755,root,root) %{_bindir}/wdwrite
%attr(755,root,root) %{_bindir}/wkdemenu.pl
%attr(755,root,root) %{_bindir}/wm-oldmenu2new
%attr(755,root,root) %{_bindir}/wmaker
%attr(755,root,root) %{_bindir}/wmaker.inst
%attr(755,root,root) %{_bindir}/wmsetbg
%attr(755,root,root) %{_bindir}/wsetfont
%attr(755,root,root) %{_bindir}/wxcopy
%attr(755,root,root) %{_bindir}/wxpaste

%{_datadir}/WindowMaker

%dir %{_prefix}/GNUstep
%dir %{_prefix}/GNUstep/Apps
%dir %{_prefix}/GNUstep/Apps/WPrefs.app

%attr(755,root,root) %{_prefix}/GNUstep/Apps/WPrefs.app/WPrefs

%{_prefix}/GNUstep/Apps/WPrefs.app/tiff
%{_prefix}/GNUstep/Apps/WPrefs.app/xpm
%{_prefix}/GNUstep/Apps/WPrefs.app/WPrefs.tiff
%{_prefix}/GNUstep/Apps/WPrefs.app/WPrefs.xpm

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/WINGs

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/get-wraster-flags
%{_includedir}/*.h
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Sat Jul 10 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.60.0-2]
- aadde Windowmaker-WINGs.h.patch which fix probems compiling WM on system
  without installed WindowMaker-devel,
- fix: include WPrefs .mo files.

* Fri Jun 25 1999 Piotr Czerwi�ski <pius@pld.org.pl> 
  [0.60.0-1]
- updated to 0.60.0,
- added using more rpm macros,
- added %{name}-ru.po.patch,
- added --enable-usermenu to ./configure options.

* Mon Jun 07 1999 Jan R�korajski <baggins@pld.org.pl>
  [0.53.0-4]
- fixed --prefix
- added find_lang macro

* Sun May  9 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.53.0-3]
- now package is FHS 2.0 compliant.

* Wed Apr 28 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.53.0-2]
- added WindowMaker-extra (more themes)
- added areas and runinst patches from RH 6.0

* Mon Apr 19 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
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

* Wed Mar  3 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.51.0-2]
- removed man group from man pages.

* Tue Feb  9 1999 Micha� Kuratczyk <kurkens@polbox.com>
- gzipping instead bzipping
- simplification in %files
- cosmetic changes

* Wed Feb  3 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.50.2-1d]
- added stripping shared libraries,
- removed SONAME symlinks from main package.

* Fri Jan 15 1999 Artur Frysiak <wiget@usa.net>
- upgraded to 0.50.2
- rewrite %{name}-po.patch
- added icons (WindowMaker-data.tar.gz) 
  by Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- added --enable-superfluous and --enable-newstyle configure options 
  by Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- added --enable-kde configure options
- added more Requires
- added wmconfig support

* Sat Sep 26 1998 Pawe� Gajda <pagaj@shadow.eu.org>
  [0.20.0-1d]
- added --disable-shm option to configure script
- added patches to fix I18N stuff
- moved bughint script to /usr/X11R6/bin
- WPrefs is now back in /usr/X11R6/GNUstep
- built against Tornado,
- build from non root's account.

* Mon Sep 21 1998 Pawe� Gajda <pagaj@shadow.eu.org>
  [0.19.3-2]
- fixed problems with paths to icons, styles and WPrefs
- removed all patches
- moved WPrefs stuff to /usr/X11R6/share/GNUstep
- fixed I18N
- added Polish summary and description

* Thu Sep  8 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
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
- nls stuff moved to %{_datadir}/locale,
- added --disable-debug for configure,
- adde %lang macros for %{_datadir}/locale/*/LC_MESSAGES/* files,
- added WindowMaker-fix_po.patch wit fixing .po files,
- simplification in %files and added using %defattr macro also.

* Tue Jul 21 1998 W. Reilly Cooley <wcooley@nakedape.ml.org>
- updated from 16.1 to 17.2; made it use RPM_OPT_FLAGS
