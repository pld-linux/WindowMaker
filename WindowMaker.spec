%define		extraver	0.1

Summary:	NeXT-alike window manager
Summary(es):	Administrador de Ventanas parecido con el NeXT
Summary(fr):	Gestionnaire de fen�tres avec le look NeXT
Summary(pl):	Zarz�dca okien w stylu NeXT
Summary(pt_BR):	Gerente de Janelas parecido com o NeXT
Summary(ru):	WindowMaker - ������� �������� ��� X11
Summary(uk):	WindowMaker - צ������ �������� ��� X11
Name:		WindowMaker
Version:	0.80.2
Release:	4
License:	GPL
Group:		X11/Window Managers
Source0:	ftp://ftp.windowmaker.org/pub/source/release/%{name}-%{version}.tar.bz2
# Source0-md5:	9f4fabc8831af6c58edf8708ee90126f
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

%description -l es
WindowMaker es un administrador de ventanas proyectado para emular la
apariencia de parte de la interface de usuario del NEXTSTEP(tm). Se
hizo para ser r�pido, relativamente peque�o, rico en caracter�sticas y
de configuraci�n f�cil, con una apariencia sencilla y elegante
prestada del NEXTSTEP(tm).

%description -l fr
Window Maker est un gestionnaire de fen�tres pour X11 qui cherche �
reproduire l'allure et l'ergonomie ("look & feel") de l'interface
graphique NeXTSTEP(tm) (aka OpenStep). Il est relativement rapide,
�volu�, et facile � configurer et � utiliser. Window Maker fait
officiellement partie du projet GNU, ce qui signifie que Window Maker
peut coop�rer avec d'autres projets GNU, comme par exemple GNOME.

Window Maker permet de changer de th�mes facilement, de placer ses
applications favorites soit sur un "dock" similaire au programme Wharf
de AfterStep, soit sur un dock int�gr� � l'espace de travail, appel�
"clip" (trombone), et qui permet d'�tendre les possibilit�s du dock
principal.

Vous devriez installer ce package si votre gestionnaire de fen�tres
est Window Maker, ou si vous voulez l'essayer. Si vous installez le
package Window Maker, vous voudrez peut-�tre installer aussi le
package AfterStep-APPS, qui contient des "applets" (petites
applications) qui fonctionnent � la fois dans les gestionnaires de
fen�tres AfterStep et Window Maker.

%description -l pl
WindowMaker jest zarz�dc� okien przypominaj�cym wygl�dem i wygod�
obs�ugi interfejs systemu NeXTSTEP(tm). Jest szybki, stosunkowo ma�y,
o du�ych mo�liwo�ciach i �atwy w konfiguracji. Konfiguruje si� go
myszk�, za pomoc� programu WPrefs wchodz�cego w sk�ad tego pakietu.

%description -l pt_BR
WindowMaker � um gerente de janelas projetado para emular a apar�ncia
de parte da interface de usu�rio do NEXTSTEP(tm). Feito para ser
r�pido, relativamente pequeno, rico em caracter�sticas e de
configura��o f�cil, com uma apar�ncia simples e elegante emprestada do
NEXTSTEP(tm).

%description -l ru
WindowMaker - ��� ������� ��������, ����������� ����� �������� �����
NEXTSTEP(tm). ��������������� ��� �� ������������ �������, �����,
����� �������������, ����� ������������� � ����� ������� � ����������
���������, ���������������� � NEXTSTEP(tm).

%description -l uk
WindowMaker - �� צ������ ��������, �� ������ ��������� ���������
���������� NEXTSTEP(tm). ���� �������� צ������ ���������, �������,
������� ������������, ������ ��� ������������; צ� ��� ������ ��
��������� ���Φ�Φ���, ���������� � NEXTSTEP(tm).

%package libs
Summary:	WindowMaker shared libraries
Summary(pl):	Biblioteki wsp�dzielone WindowMakera
Group:		Libraries
Obsoletes:	libwraster2

%description libs
This package contains shared libraries for run WindowMaker.

%description libs -l pl
Ten pakiet zawiera biblioteki wsp�dzielone niezb�dne do pracy
zarz�dcy okien WindowMaker.

%package devel
Summary:	WindowMaker libraries - development part
Summary(es):	Bibliotecas, archivos de inclusi�n, e etc. para desarrollar aplicaciones WindowMaker
Summary(fr):	Librairies de WindowMaker
Summary(pl):	Biblioteki WindowMakera - cz�� dla programist�w
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para o WindowMaker
Summary(ru):	���������� ��������� � .h ����� ��� WindowMaker
Summary(uk):	��̦����� Ц������� �� .h ����� ��� WindowMaker
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}
Obsoletes:	libwraster2-devel

%description devel
This package contains libraries for building WindowMaker-enhanced
applications.

%description devel -l es
Bibliotecas, archivos de inclusi�n, e etc. para desarrollar
aplicaciones WindowMaker

%description devel -l fr
Ce paquet contient des librairies pour faire des applications mise en
valeur par WindowMaker.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe i biblioteki niezb�dne do
tworzenia aplikacji wykorzystuj�cych mo�liwo�ci zarz�dcy okien
WindowMaker.

%description devel -l pt_BR
Arquivos de inclus�o e bibliotecas para o desenvolvimento de programas
baseados no WindowMaker

%description devel -l ru
���� ����� �������� ���������� � .h �����, ��������������� ��� ������
����������, ������������ ����������� WindowMaker.

%description devel -l uk
��� ����� ͦ����� ¦�̦����� �� .h �����, ��������Φ ��� ����������
�������, �� �������������� ��������Ԧ WindowMaker.

%package static
Summary:	WindowMaker static libraries
Summary(pl):	Biblioteki statyczne WindowMakera
Summary(ru):	����������� ���������� ��������� ��� WindowMaker
Summary(uk):	������Φ ¦�̦����� Ц������� ��� WindowMaker
Group:		Development/Libraries
Summary(pt_BR):	Componentes est�ticos de desenvolvimento para o WindowMaker
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries for building
WindowMaker-enhanced applications.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki do tworzenia aplikacji
wykorzystuj�cych mo�liwo�ci zarz�dcy okien WindowMaker.

%description static -l pt_BR
Instale este pacote se voc� deseja desenvolver para o WindowMaker,
utilizando componentes est�ticos (raramente necess�rio).

%description static -l ru
���� ����� �������� ����������� ���������� ��������������� ��� ������
����������, ������������ ����������� WindowMaker.

%description static -l uk
��� ����� ͦ����� ������Φ ¦�̦�����, ��������Φ ��� ����������
�������, �� �������������� ��������Ԧ WindowMaker.

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
%patch12 -p1
%patch13 -p1

for f in WindowMaker/*menu*; do
	sed s,/usr/local/GNUstep/,%{_libdir}/GNUstep/, $f >$f.new
	mv -f $f.new $f
done

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

LINGUAS="bg cs da de el es et fi fr gl hr hu it ja ko ms nl no pl pt ro ru \
	 sk sv tr zh_CN zh_TW.Big5" ; export LINGUAS
CPP_PATH="/lib/cpp" ; export CPP_PATH
%configure \
	--disable-rpath \
	--with-nlsdir=%{_datadir}/locale \
	--with-appspath=%{_libdir}/GNUstep/Apps \
	--enable-sound \
	--enable-gnome \
	--disable-debug \
	--enable-kde \
	--enable-shared \
	--enable-static \
	--enable-usermenu

touch WindowMaker/Defaults/W*.in

%{__make} \
	LINGUAS="bg cs da de el es et fi fr gl hr hu it ja ko ms nl no pl pt ro ru \
	 	sk sv tr zh_CN zh_TW.Big5" \
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
	LINGUAS="cs de el es fi fr gl hr it ja ko nl no pl pt ro ru  \
	 	se sk tr zh_CN zh_TW.Big5" \
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
%attr(755,root,root) %{_bindir}/geticonset
%attr(755,root,root) %{_bindir}/getstyle
%attr(755,root,root) %{_bindir}/seticons
%attr(755,root,root) %{_bindir}/setstyle
%attr(755,root,root) %{_bindir}/wcopy
%attr(755,root,root) %{_bindir}/wdwrite
%attr(755,root,root) %{_bindir}/wdread
%attr(755,root,root) %{_bindir}/wkdemenu.pl
%attr(755,root,root) %{_bindir}/wm-oldmenu2new
%attr(755,root,root) %{_bindir}/wmagnify
%attr(755,root,root) %{_bindir}/wmaker
%attr(755,root,root) %{_bindir}/wmaker.inst
%attr(755,root,root) %{_bindir}/wmsetbg
%attr(755,root,root) %{_bindir}/wmsetup
%attr(755,root,root) %{_bindir}/wmchlocale
%attr(755,root,root) %{_bindir}/wpaste
%attr(755,root,root) %{_bindir}/wsetfont
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
