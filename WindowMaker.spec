
# TODO
# - either package or remove pkgconf .pc files

%define		extraver	0.1
%define		_snap		20050409

Summary:	NeXT-alike window manager
Summary(es.UTF-8):   Administrador de Ventanas parecido con el NeXT
Summary(fr.UTF-8):   Gestionnaire de fenêtres avec le look NeXT
Summary(pl.UTF-8):   Zarządca okien w stylu NeXT
Summary(pt_BR.UTF-8):   Gerente de Janelas parecido com o NeXT
Summary(ru.UTF-8):   WindowMaker - оконный менеджер для X11
Summary(uk.UTF-8):   WindowMaker - віконний менеджер для X11
Name:		WindowMaker
Version:	0.92.0
Release:	0.%{_snap}.2
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.windowmaker.org/pub/source/snapshots/%{name}-CVS-%{_snap}.tar.gz
# Source0-md5:	362e05b20d50ad0ecde59a333b7e76da
Source1:	ftp://windowmaker.org/pub/%{name}-data.tar.gz
# Source1-md5:	6ea0c37314ea9e9ab27e8bdf45a31a82
Source2:	ftp://ftp.windowmaker.org/pub/source/release/%{name}-extra-%{extraver}.tar.gz
# Source2-md5:	07c7700daaaf232bc490f5abaabef085
Source3:	%{name}.desktop
Source4:	%{name}.RunWM
Source5:	%{name}.wm_style
Source6:	%{name}-xsession.desktop
Patch0:		%{name}-CFLAGS.patch
Patch1:		%{name}-wmconfig.patch
Patch2:		%{name}-pixmaps.patch
Patch3:		%{name}-shared.patch
Patch4:		%{name}-areas.patch
Patch5:		%{name}-IconPosition.patch
Patch6:		%{name}-singleclick.patch
Patch7:		%{name}-plmenu.patch
Patch8:		%{name}-dockit.patch
Patch9:		%{name}-po.patch
Patch10:	%{name}-rxvt.patch
Patch11:	%{name}-pl.po-update.patch
Patch12:	%{name}-wmchlocale-fixes.patch
Patch13:	http://www.heily.com/mark/code_samples/appicon_captions_maxprotect.diff
Patch14:	%{name}-localenames.patch
Patch15:	%{name}-CVS-before-xft2.patch
Patch16:	%{name}-configure.patch
URL:		http://www.windowmaker.org/
BuildRequires:	Hermes-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
Requires:	%{name}-libs = %{version}
Requires:	cpp
Requires:	tk
Requires:	wmconfig >= 0.9.9-5
Requires:	xinitrc >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11
%define		_wmpropsdir	/usr/share/wm-properties

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

%description -l es.UTF-8
WindowMaker es un administrador de ventanas proyectado para emular la
apariencia de parte de la interface de usuario del NEXTSTEP(tm). Se
hizo para ser rápido, relativamente pequeño, rico en características y
de configuración fácil, con una apariencia sencilla y elegante
prestada del NEXTSTEP(tm).

%description -l fr.UTF-8
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

%description -l pl.UTF-8
WindowMaker jest zarządcą okien przypominającym wyglądem i wygodą
obsługi interfejs systemu NeXTSTEP(tm). Jest szybki, stosunkowo mały,
o dużych możliwościach i łatwy w konfiguracji. Konfiguruje się go
myszką, za pomocą programu WPrefs wchodzącego w skład tego pakietu.

%description -l pt_BR.UTF-8
WindowMaker é um gerente de janelas projetado para emular a aparência
de parte da interface de usuário do NEXTSTEP(tm). Feito para ser
rápido, relativamente pequeno, rico em características e de
configuração fácil, com uma aparência simples e elegante emprestada do
NEXTSTEP(tm).

%description -l ru.UTF-8
WindowMaker - это оконный менеджер, эмулирующий часть экранной среды
NEXTSTEP(tm). Подразумевается что он относительно невелик, быстр,
богат возможностями, легко настраивается и имеет простую и элегантную
внешность, позаимствованную у NEXTSTEP(tm).

%description -l uk.UTF-8
WindowMaker - це віконний менеджер, що емулює інтерфейс екранного
середовища NEXTSTEP(tm). Його вважають відносно невеликим, швидким,
багатим можливостями, легким для налагодження; він має просту та
елегантну зовнішність, запозичену в NEXTSTEP(tm).

%package libs
Summary:	WindowMaker shared libraries
Summary(pl.UTF-8):   Biblioteki współdzielone WindowMakera
Group:		Libraries
Obsoletes:	libwraster2

%description libs
This package contains shared libraries for run WindowMaker.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki współdzielone niezbędne do pracy
zarządcy okien WindowMaker.

%package devel
Summary:	WindowMaker libraries - development part
Summary(es.UTF-8):   Bibliotecas, archivos de inclusión, e etc. para desarrollar aplicaciones WindowMaker
Summary(fr.UTF-8):   Librairies de WindowMaker
Summary(pl.UTF-8):   Biblioteki WindowMakera - część dla programistów
Summary(pt_BR.UTF-8):   Arquivos de inclusão e bibliotecas para o WindowMaker
Summary(ru.UTF-8):   Библиотеки поддержки и .h файлы для WindowMaker
Summary(uk.UTF-8):   Бібліотеки підтримки та .h файли для WindowMaker
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}
Obsoletes:	libwraster2-devel

%description devel
This package contains libraries for building WindowMaker-enhanced
applications.

%description devel -l es.UTF-8
Bibliotecas, archivos de inclusión, e etc. para desarrollar
aplicaciones WindowMaker

%description devel -l fr.UTF-8
Ce paquet contient des librairies pour faire des applications mise en
valeur par WindowMaker.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i biblioteki niezbędne do
tworzenia aplikacji wykorzystujących możliwości zarządcy okien
WindowMaker.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão e bibliotecas para o desenvolvimento de programas
baseados no WindowMaker

%description devel -l ru.UTF-8
Этот пакет содержит библиотеки и .h файлы, предназначенные для сборки
приложений, использующих возможности WindowMaker.

%description devel -l uk.UTF-8
Цей пакет містить бібліотеки та .h файли, призначені для прикладних
програм, що використовують можливості WindowMaker.

%package static
Summary:	WindowMaker static libraries
Summary(pl.UTF-8):   Biblioteki statyczne WindowMakera
Summary(ru.UTF-8):   Статические библиотеки поддержки для WindowMaker
Summary(uk.UTF-8):   Статичні бібліотеки підтримки для WindowMaker
Group:		Development/Libraries
Summary(pt_BR.UTF-8):   Componentes estáticos de desenvolvimento para o WindowMaker
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries for building
WindowMaker-enhanced applications.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki do tworzenia aplikacji
wykorzystujących możliwości zarządcy okien WindowMaker.

%description static -l pt_BR.UTF-8
Instale este pacote se você deseja desenvolver para o WindowMaker,
utilizando componentes estáticos (raramente necessário).

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки предназначенные для сборки
приложений, использующих возможности WindowMaker.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки, призначені для прикладних
програм, що використовують можливості WindowMaker.

%prep
%setup -q -a 1 -a 2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
#%patch9 -p1	ISO-8859-2 or UTF-8? that's the question... 
%patch10 -p1
#%patch11 -p1	Temporarily disabled because of no pl.po file in tarball
%patch13 -p1
#%patch15 -p1 ???
%patch16 -p1

for f in WindowMaker/*menu*; do
	sed s,/usr/local/GNUstep/,%{_libdir}/GNUstep/, $f >$f.new
	mv -f $f.new $f
done

mv -f po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd %{name}-extra-%{extraver}
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	%{__automake}
cd ..

perl -pi -e 's/defaultAppIcon.#extension#;SharedAppIcon = Yes;/defaultAppIcon.#extension#;/' \
	WindowMaker/Defaults/WMWindowAttributes.in

%configure \
	CPP_PATH="/lib/cpp" \
	LINGUAS="bg cs da de el es et fi fr gl hr hu it ja ko ms nb nl pl pt ro ru \
		 sk sv tr zh_CN zh_TW" \
	--disable-rpath \
	--with-nlsdir=%{_datadir}/locale \
	--with-gnustepdir=%{_libdir}/GNUstep \
	--enable-sound \
	--enable-gnome \
	--disable-debug \
	--enable-kde \
	--enable-shared \
	--enable-static \
	--enable-usermenu

touch WindowMaker/Defaults/W*.in

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{__autoconf}
cd %{name}-extra-%{extraver}
%configure \
	--with-nlsdir=%{_datadir}/locale \
	--with-iconsdir=%{_datadir}/pixmaps

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_pixmapsdir},%{_wmpropsdir}} \
	$RPM_BUILD_ROOT/etc/sysconfig/wmstyle

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install util/bughint $RPM_BUILD_ROOT%{_bindir}

install contrib/dockit   $RPM_BUILD_ROOT%{_bindir}
install contrib/dockit.1 $RPM_BUILD_ROOT%{_mandir}/man1

install WindowMaker-data/pixmaps/* $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_wmpropsdir}

install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/wmaker.sh
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/wmaker.names
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/xsessions/WindowMaker.desktop

cd %{name}-extra-%{extraver}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGFORM BUGS ChangeLog FAQ NEWS README

%dir %{_sysconfdir}/WindowMaker
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/WindowMaker/*

%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names

%{_mandir}/man1/*
%lang(sk) %{_mandir}/sk/man1/*

%{_pixmapsdir}/*
%{_wmpropsdir}/WindowMaker.desktop

%attr(755,root,root) %{_bindir}/bughint
%attr(755,root,root) %{_bindir}/convertfonts
%attr(755,root,root) %{_bindir}/geticonset
%attr(755,root,root) %{_bindir}/getstyle
%attr(755,root,root) %{_bindir}/seticons
%attr(755,root,root) %{_bindir}/setstyle
#%attr(755,root,root) %{_bindir}/wcopy
%attr(755,root,root) %{_bindir}/wdwrite
%attr(755,root,root) %{_bindir}/wdread
%attr(755,root,root) %{_bindir}/wkdemenu.pl
%attr(755,root,root) %{_bindir}/wm-oldmenu2new
%attr(755,root,root) %{_bindir}/wmagnify
%attr(755,root,root) %{_bindir}/wmaker
%attr(755,root,root) %{_bindir}/wmaker.inst
%attr(755,root,root) %{_bindir}/wmsetbg
%attr(755,root,root) %{_bindir}/wmsetup
#%attr(755,root,root) %{_bindir}/wmchlocale
#%attr(755,root,root) %{_bindir}/wpaste
#%attr(755,root,root) %{_bindir}/wsetfont
%attr(755,root,root) %{_bindir}/wxcopy
%attr(755,root,root) %{_bindir}/wxpaste
%attr(755,root,root) %{_bindir}/dockit

%{_datadir}/WindowMaker
%{_datadir}/xsessions/WindowMaker.desktop

# the first one is shared with gnustep-make...
%dir %{_libdir}/GNUstep
%dir %{_libdir}/GNUstep/Apps
%dir %{_libdir}/GNUstep/Apps/WPrefs.app

%attr(755,root,root) %{_libdir}/GNUstep/Apps/WPrefs.app/WPrefs

%{_libdir}/GNUstep/Apps/WPrefs.app/tiff
%{_libdir}/GNUstep/Apps/WPrefs.app/xpm
%{_libdir}/GNUstep/Apps/WPrefs.app/WPrefs.tiff
%{_libdir}/GNUstep/Apps/WPrefs.app/WPrefs.xpm

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/WINGs

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_bindir}/get-wings-flags
%attr(755,root,root) %{_bindir}/get-wraster-flags
%attr(755,root,root) %{_bindir}/get-wutil-flags
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
