%define		extraver	0.1

Summary:	NeXT-alike window manager
Summary(fr):	Gestionnaire de fenêtres avec le look NeXT
Summary(pl):	Mened¿er okien w stylu NeXT
Name:		WindowMaker
Version:	0.64.0
Release:	3
Group:		X11/Window Managers
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
License:	GPL
Source0:	ftp://ftp.windowmaker.org/pub/beta/srcs/%{name}-%{version}.tar.bz2
Source1:	ftp://windowmaker.org/pub/%{name}-data.tar.gz
Source2:	ftp://ftp.windowmaker.org/pub/beta/srcs/%{name}-extra-%{extraver}.tar.gz
Source3:	%{name}.desktop
Source4:	%{name}.RunWM
Source5:	%{name}.wm_style
Patch0:		%{name}-CFLAGS.patch
Patch1:		%{name}-wmconfig.patch
Patch2:		%{name}-a_macro.patch
Patch3:		%{name}-pixmaps.patch
Patch4:		%{name}-shared.patch
Patch5:		%{name}-areas.patch
Patch6:		%{name}-runinst.patch
Patch7:		%{name}-IconPosition.patch
Patch8:		%{name}-singleclick.patch
Patch9:		%{name}-plmenu.patch
Patch10:	%{name}-dockit.patch
URL:		http://www.windowmaker.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libPropList-devel >= 0.10.1
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
Requires:	wmconfig >= 0.9.9-5
Requires:	cpp
Requires:	%{name}-libs = %{version}
Requires:	tk
Requires:	xinitrc >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11
%define		_wmpropsdir	%{_datadir}/wm-properties

%description
Window Maker is an X11 window manager which emulates the look and feel
of the NeXTSTEP (TM) graphical user interface. It is relatively fast,
feature rich and easy to configure and use. Window Maker is part of
the official GNU project, which means that Window Maker can
interoperate with other GNU projects, such as GNOME.

Window Maker allows users to switch themes 'on the fly,' to place
favorite applications on either an application dock, similar to
AfterStep's Wharf or on a workspace dock, a 'clip' which extends the
application dock's usefulness.

You should install the WindowMaker package if you use Window Maker as
your window manager or if you'd like to try using it. If you do
install the WindowMaker package, you may also want to install the
AfterStep-APPS package, which includes applets that will work with
both AfterStep and Window Maker window managers.

%description -l fr
Window Maker est un gestionnaire de fenêtres pour X11 qui cherche à
reproduire l'allure et l'ergonomie ("look & feel") de l'interface
graphique NeXTSTEP(tm) (aka OpenStep). Il est relativement rapide,
évolué, et facile à configurer et à utiliser. Window Maker fait
officiellement partie du projet GNU, ce qui signifie que Window Maker
peut coopérer avec d'autres projets GNU, comme par exemple GNOME.

Window Maker permet de changer de thèmes facilement, de placer ses
applications favorites soit sur un "dock" similaire au programme Wharf
de AfterStep, soit sur un dock intégré à l'espace de travail, appelé
"clip" (trombone), et qui permet d'étendre les possibilités du dock
principal.

Vous devriez installer ce package si votre gestionnaire de fenêtres
est Window Maker, ou si vous voulez l'essayer. Si vous installez le
package Window Maker, vous voudrez peut-être installer aussi le
package AfterStep-APPS, qui contient des "applets" (petites
applications) qui fonctionnent à la fois dans les gestionnaires de
fenêtres AfterStep et Window Maker.

%description -l pl
WindowMaker jest mened¿erem okien przypominaj±cym wygl±dem i wygod±
obs³ugi interfejs systemu NeXTSTEP(tm). Jest szybki, stosunkowo ma³y,
o du¿ych mo¿liwo¶ciach i ³atwy w konfiguracji. Konfiguruje siê go
myszk±, za pomoc± programu WPrefs wchodz±cego w sk³ad tego pakietu.

%package libs
Summary:	WindowMaker shared libraries
Summary(pl):	Biblioteki wspó³dzielone WindowMakera
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki

%description libs
This package contains shared libraries for run WindowMaker.

%description libs -l pl
Ten pakiet zawiera biblioteki wspó³dzielone niezbêdne do pracy
mened¿era okien WindowMaker.

%package devel
Summary:	WindowMaker libraries - development part
Summary(fr):	Librairies de WindowMaker
Summary(pl):	Biblioteki WindowMakera - czê¶æ dla programistów
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-libs = %{version}

%description devel
This package contains libraries for building WindowMaker-enhanced
applications.

%description devel -l fr
Ce paquet contient des librairies pour faire des applications mise en
valeur par WindowMaker.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i biblioteki niezbêdne do
tworzenia aplikacji wykorzystuj±cych mo¿liwo¶ci mened¿era okien
WindowMaker.

%package static
Summary:	WindowMaker static libraries
Summary(pl):	Biblioteki statyczne WindowMakera
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries for building
WindowMaker-enhanced applications.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki niezbêdne do tworzenia
aplikacji wykorzystuj±cych mo¿liwo¶ci menad¿era okien WindowMaker.

%prep
%setup -q -a 1 -a 2
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
aclocal
autoconf
automake -a -c
LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru  \
	 se sk tr zh_CN zh_TW.Big5" ; export LINGUAS
CPP_PATH="/lib/cpp" ; export CPP_PATH

%configure \
	--with-nlsdir=%{_datadir}/locale \
	--enable-sound \
	--enable-gnome \
	--disable-debug \
	--enable-kde \
	--enable-shared \
	--enable-static \
	--enable-usermenu

touch WindowMaker/Defaults/W*.in

%{__make} \
	LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru  \
	 	se sk tr zh_CN zh_TW.Big5" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

autoconf
cd %{name}-extra-%{extraver}
%configure \
	--with-nlsdir=%{_datadir}/locale \
	--with-iconsdir=%{_datadir}/pixmaps

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/pixmaps,%{_wmpropsdir}} \
	$RPM_BUILD_ROOT/etc/sysconfig/wmstyle

%{__make} install \
	LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru  \
	 	se sk tr zh_CN zh_TW.Big5" \
	DESTDIR=$RPM_BUILD_ROOT 

install util/bughint $RPM_BUILD_ROOT%{_bindir}

install contrib/dockit   $RPM_BUILD_ROOT%{_bindir}
install contrib/dockit.1 $RPM_BUILD_ROOT%{_mandir}/man1

install WindowMaker-data/pixmaps/* $RPM_BUILD_ROOT%{_datadir}/pixmaps
install %{SOURCE3} $RPM_BUILD_ROOT%{_wmpropsdir}

install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.sh
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.names

(cd %{name}-extra-%{extraver};
%{__make} DESTDIR=$RPM_BUILD_ROOT install )

gzip -9nf AUTHORS BUGFORM BUGS ChangeLog FAQ NEWS README

%find_lang %{name} --all-name

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz

%dir %{_sysconfdir}/WindowMaker
%config %verify(not size mtime md5) %{_sysconfdir}/WindowMaker/*

%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names

%{_mandir}/man1/*

%{_pixmapsdir}/*
%{_wmpropsdir}/WindowMaker.desktop

%attr(755,root,root) %{_bindir}/bughint
%attr(755,root,root) %{_bindir}/geticonset
%attr(755,root,root) %{_bindir}/getstyle
%attr(755,root,root) %{_bindir}/seticons
%attr(755,root,root) %{_bindir}/setstyle
%attr(755,root,root) %{_bindir}/wdwrite
%attr(755,root,root) %{_bindir}/wdread
%attr(755,root,root) %{_bindir}/wkdemenu.pl
%attr(755,root,root) %{_bindir}/wm-oldmenu2new
%attr(755,root,root) %{_bindir}/wmagnify
%attr(755,root,root) %{_bindir}/wmaker
%attr(755,root,root) %{_bindir}/wmaker.inst
%attr(755,root,root) %{_bindir}/wmsetbg
%attr(755,root,root) %{_bindir}/wmchlocale
%attr(755,root,root) %{_bindir}/wsetfont
%attr(755,root,root) %{_bindir}/wxcopy
%attr(755,root,root) %{_bindir}/wxpaste
%attr(755,root,root) %{_bindir}/dockit

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
%attr(755,root,root) %{_bindir}/get-wings-flags
%attr(755,root,root) %{_bindir}/get-wraster-flags
%attr(755,root,root) %{_bindir}/get-wutil-flags
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/WINGs

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/get-wraster-flags
%{_includedir}/*
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
