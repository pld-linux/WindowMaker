%define		extraver	0.1

Summary:	NeXT-alike window manager
Summary(es):	Administrador de Ventanas parecido con el NeXT
Summary(fr):	Gestionnaire de fenЙtres avec le look NeXT
Summary(pl):	Zarz╠dca okien w stylu NeXT
Summary(pt_BR):	Gerente de Janelas parecido com o NeXT
Summary(ru):	WindowMaker - оконный менеджер для X11
Summary(uk):	WindowMaker - в╕конний менеджер для X11
Name:		WindowMaker
Version:	0.92.0
Release:	0.3
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.windowmaker.org/pub/source/release/%{name}-%{version}.tar.gz
# Source0-md5:	678cb4a9b22a557cfb524dc3cb457c08
Source1:	%{name}-data.tar.gz
# Source1-md5:	6ea0c37314ea9e9ab27e8bdf45a31a82
Source2:	ftp://ftp.windowmaker.org/pub/source/release/%{name}-extra-%{extraver}.tar.gz
# Source2-md5:	07c7700daaaf232bc490f5abaabef085
Source3:	%{name}.desktop
Source6:	%{name}-xsession.desktop
Patch0:		%{name}-cvs.patch
Patch1:		%{name}-pl.po-update.patch
Patch2:		%{name}-CFLAGS.patch
Patch3:		%{name}-vfmg.patch
Patch4:		%{name}-shared.patch
Patch5:		%{name}-IconPosition.patch
Patch6:		%{name}-singleclick.patch
Patch7:		%{name}-plmenu.patch
Patch8:		%{name}-dockit.patch
Patch9:		http://www.heily.com/mark/code_samples/appicon_captions_maxprotect.diff
Patch10:	%{name}-localenames.patch
Patch11:	%{name}-0.91.0-translucency-1.patch
Patch12:	%{name}-gnustep.patch
URL:		http://www.windowmaker.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libungif-devel
BuildRequires:	perl-base
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cpp
Requires:	gnustep-dirs
Requires:	tk
Requires:	vfmg
Requires:	xinitrc-ng
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

%description -l es
WindowMaker es un administrador de ventanas proyectado para emular la
apariencia de parte de la interface de usuario del NEXTSTEP(tm). Se
hizo para ser rАpido, relativamente pequeЯo, rico en caracterМsticas y
de configuraciСn fАcil, con una apariencia sencilla y elegante
prestada del NEXTSTEP(tm).

%description -l fr
Window Maker est un gestionnaire de fenЙtres pour X11 qui cherche Ю
reproduire l'allure et l'ergonomie ("look & feel") de l'interface
graphique NeXTSTEP(tm) (aka OpenStep). Il est relativement rapide,
ИvoluИ, et facile Ю configurer et Ю utiliser. Window Maker fait
officiellement partie du projet GNU, ce qui signifie que Window Maker
peut coopИrer avec d'autres projets GNU, comme par exemple GNOME.

Window Maker permet de changer de thХmes facilement, de placer ses
applications favorites soit sur un "dock" similaire au programme Wharf
de AfterStep, soit sur un dock intИgrИ Ю l'espace de travail, appelИ
"clip" (trombone), et qui permet d'Иtendre les possibilitИs du dock
principal.

Vous devriez installer ce package si votre gestionnaire de fenЙtres
est Window Maker, ou si vous voulez l'essayer. Si vous installez le
package Window Maker, vous voudrez peut-Йtre installer aussi le
package AfterStep-APPS, qui contient des "applets" (petites
applications) qui fonctionnent Ю la fois dans les gestionnaires de
fenЙtres AfterStep et Window Maker.

%description -l pl
WindowMaker jest zarz╠dc╠ okien przypominaj╠cym wygl╠dem i wygod╠
obsЁugi interfejs systemu NeXTSTEP(tm). Jest szybki, stosunkowo maЁy,
o du©ych mo©liwo╤ciach i Ёatwy w konfiguracji. Konfiguruje siЙ go
myszk╠, za pomoc╠ programu WPrefs wchodz╠cego w skЁad tego pakietu.

%description -l pt_BR
WindowMaker И um gerente de janelas projetado para emular a aparЙncia
de parte da interface de usuАrio do NEXTSTEP(tm). Feito para ser
rАpido, relativamente pequeno, rico em caracterМsticas e de
configuraГЦo fАcil, com uma aparЙncia simples e elegante emprestada do
NEXTSTEP(tm).

%description -l ru
WindowMaker - это оконный менеджер, эмулирующий часть экранной среды
NEXTSTEP(tm). Подразумевается что он относительно невелик, быстр,
богат возможностями, легко настраивается и имеет простую и элегантную
внешность, позаимствованную у NEXTSTEP(tm).

%description -l uk
WindowMaker - це в╕конний менеджер, що емулю╓ ╕нтерфейс екранного
середовища NEXTSTEP(tm). Його вважають в╕дносно невеликим, швидким,
багатим можливостями, легким для налагодження; в╕н ма╓ просту та
елегантну зовн╕шн╕сть, запозичену в NEXTSTEP(tm).

%package libs
Summary:	WindowMaker shared libraries
Summary(pl):	Biblioteki wspСЁdzielone WindowMakera
Group:		Libraries
Obsoletes:	libwraster2

%description libs
This package contains shared libraries for run WindowMaker.

%description libs -l pl
Ten pakiet zawiera biblioteki wspСЁdzielone niezbЙdne do pracy
zarz╠dcy okien WindowMaker.

%package devel
Summary:	WindowMaker libraries - development part
Summary(es):	Bibliotecas y archivos de inclusiСn para WindowMaker
Summary(fr):	Librairies de WindowMaker
Summary(pl):	Biblioteki WindowMakera - czЙ╤Ф dla programistСw
Summary(pt_BR):	Arquivos de inclusЦo e bibliotecas para o WindowMaker
Summary(ru):	Библиотеки поддержки и .h файлы для WindowMaker
Summary(uk):	Б╕бл╕отеки п╕дтримки та .h файли для WindowMaker
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	xorg-lib-libXft-devel
Requires:	xorg-lib-libXpm-devel
Obsoletes:	libwraster2-devel

%description devel
This package contains libraries for building WindowMaker-enhanced
applications.

%description devel -l es
Bibliotecas, archivos de inclusiСn, e etc. para desarrollar
aplicaciones WindowMaker

%description devel -l fr
Ce paquet contient des librairies pour faire des applications mise en
valeur par WindowMaker.

%description devel -l pl
Ten pakiet zawiera pliki nagЁСwkowe i biblioteki niezbЙdne do
tworzenia aplikacji wykorzystuj╠cych mo©liwo╤ci zarz╠dcy okien
WindowMaker.

%description devel -l pt_BR
Arquivos de inclusЦo e bibliotecas para o desenvolvimento de programas
baseados no WindowMaker

%description devel -l ru
Этот пакет содержит библиотеки и .h файлы, предназначенные для сборки
приложений, использующих возможности WindowMaker.

%description devel -l uk
Цей пакет м╕стить б╕бл╕отеки та .h файли, призначен╕ для прикладних
програм, що використовують можливост╕ WindowMaker.

%package static
Summary:	WindowMaker static libraries
Summary(pl):	Biblioteki statyczne WindowMakera
Summary(ru):	Статические библиотеки поддержки для WindowMaker
Summary(uk):	Статичн╕ б╕бл╕отеки п╕дтримки для WindowMaker
Group:		Development/Libraries
Summary(pt_BR):	Componentes estАticos de desenvolvimento para o WindowMaker
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libraries for building
WindowMaker-enhanced applications.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki do tworzenia aplikacji
wykorzystuj╠cych mo©liwo╤ci zarz╠dcy okien WindowMaker.

%description static -l pt_BR
Instale este pacote se vocЙ deseja desenvolver para o WindowMaker,
utilizando componentes estАticos (raramente necessАrio).

%description static -l ru
Этот пакет содержит статические библиотеки предназначенные для сборки
приложений, использующих возможности WindowMaker.

%description static -l uk
Цей пакет м╕стить статичн╕ б╕бл╕отеки, призначен╕ для прикладних
програм, що використовують можливост╕ WindowMaker.

%prep
%setup -q -a 1 -a 2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p0

for f in WindowMaker/*menu*; do
	sed -i s,/usr/lib/GNUstep/,%{_libdir}/GNUstep/, $f
	sed -i s,/usr/local/GNUstep/,%{_libdir}/GNUstep/, $f
done

mv -f po/{no,nb}.po

%build
#%ifarch %{x8664}
# hack, should be obsolete - needs check
#export ac_cv_c_inline_asm=no
#%endif
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
cd %{name}-extra-%{extraver}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..

%{__perl} -pi -e 's/defaultAppIcon.#extension#;SharedAppIcon = Yes;/defaultAppIcon.#extension#;/' \
	WindowMaker/Defaults/WMWindowAttributes.in

%configure \
	CPP_PATH="/lib/cpp" \
	LINGUAS="bg cs da de el es et fi fr gl hr hu it ja ko ms nb nl pl pt ro ru \
		 sk sv tr zh_CN zh_TW" \
	--disable-debug \
	--disable-rpath \
	--enable-shared \
	--enable-static \
	--enable-usermenu \
	--with-appspath=%{_libdir}/GNUstep/Apps \
	--with-nlsdir=%{_datadir}/locale \
	--with-gnustepdir=%{_libdir}/GNUstep \
	--enable-sound \
	--enable-gnome \
	--enable-kde

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
	$RPM_BUILD_ROOT/etc/sysconfig/wmstyle \
	$RPM_BUILD_ROOT%{_datadir}/WindowMaker/{Sounds,SoundSets}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install util/bughint $RPM_BUILD_ROOT%{_bindir}

install contrib/dockit   $RPM_BUILD_ROOT%{_bindir}
install contrib/dockit.1 $RPM_BUILD_ROOT%{_mandir}/man1

install WindowMaker-data/pixmaps/* $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_wmpropsdir}

install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/xsessions/WindowMaker.desktop

%{__make} -C %{name}-extra-%{extraver} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGFORM BUGS ChangeLog FAQ NEWS README

%dir %{_sysconfdir}/WindowMaker
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/WindowMaker/*

%{_mandir}/man1/*
%lang(sk) %{_mandir}/sk/man1/*

%{_pixmapsdir}/*
%{_wmpropsdir}/WindowMaker.desktop

%attr(755,root,root) %{_bindir}/convertfonts
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
%attr(755,root,root) %{_bindir}/wmsetup
%attr(755,root,root) %{_bindir}/wxcopy
%attr(755,root,root) %{_bindir}/wxpaste
%attr(755,root,root) %{_bindir}/dockit

%{_datadir}/WindowMaker
%{_datadir}/xsessions/WindowMaker.desktop

# the first one is shared with gnustep-make...
%dir %{_libdir}/GNUstep/Applications
%dir %{_libdir}/GNUstep/Applications/WPrefs.app

%attr(755,root,root) %{_libdir}/GNUstep/Applications/WPrefs.app/WPrefs

%{_libdir}/GNUstep/Applications/WPrefs.app/tiff
%{_libdir}/GNUstep/Applications/WPrefs.app/xpm
%{_libdir}/GNUstep/Applications/WPrefs.app/WPrefs.tiff
%{_libdir}/GNUstep/Applications/WPrefs.app/WPrefs.xpm

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/WINGs

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/get-wings-flags
%attr(755,root,root) %{_bindir}/get-wraster-flags
%attr(755,root,root) %{_bindir}/get-wutil-flags
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
