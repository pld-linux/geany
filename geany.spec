Summary:	Fast and lightweight IDE using GTK+2
Summary(pl.UTF-8):	Szybkie i lekkie IDE używające GTK+2
Name:		geany
Version:	0.14
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/geany/%{name}-%{version}.tar.bz2
# Source0-md5:	c6c22c7f9feff81a15f5c8ece03b87c1
Patch0:		%{name}-desktop.patch
URL:		http://geany.uvena.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	vte-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geany is a small and lightweight integrated development environment.
It was developed to provide a small and fast IDE, which has only a few
dependencies from other packages. Another goal was to be as
independent as possible from a special Desktop Environment like KDE or
GNOME.

Basic features of Geany
- syntax highlighting
- code completion
- auto completion of often used constructs like if, for and while
- auto completion of XML and HTML tags
- call tips
- many supported filetypes like C, Java, PHP, HTML, Python, Perl,
  Pascal
- symbol lists

%description -l pl.UTF-8
Geany jest małym i lekkim zintegrowanym środowiskiem programistycznym.
Został napisany z myślą o byciu małym i szybkim IDE, z małą liczbą
zależności od innych pakietów. Kolejnym, przyświecającym tworzeniu go
celem było maksymalne uniezależnienie od konkretnego środowiska
graficznego jak KDE czy GNOME.

Podstawowe cechy Geany to:
- podświetlanie składni
- uzupełnianie kodu
- automatyczne uzupełnianie często używanych konstrukcji jak if, for
  i while
- automatyczne uzupełnianie znaczników XML i HTML
- wyświetlanie podpowiedzi
- wiele wspieranych typów plików jak C, Java, PHP, Python, Perl,
  Pascal
- wykazy symboli

%package plugin-classbuilder
Summary:	Plugin for class maintenance in geany
Summary(pl.UTF-8):	Wtyczka do zarządzenia klasami w geany
Group:		Libraries

%description plugin-classbuilder
Plugin that allows maintenance of classes within geany.

%description plugin-classbuilder -l pl.UTF-8 
Wtyczka pozwalająca na zarządzanie klasami w geany.

%package plugin-export
Summary:	Plugin for exporting projects from geany
Summary(pl.UTF-8):	Wtyczka do eksportowania projektów z geany
Group:		Libraries

%description plugin-export
Plugin that allows exporting projects from geany into various formats
(HTML and LaTeX by now).

%description plugin-export -l pl.UTF-8
Wtyczka służąca do eksportowania projektów z geany do różnych formatów
(aktualnie HTML i LaTeX).

%package plugin-htmlchars
Summary:	Plugin for enhanced HTML editing in geany
Summary(pl.UTF-8):	Wtyczka z rozszerzeniami do edycji HTML w geany
Group:		Libraries

%description plugin-htmlchars
Plugin containing a library of special HTML tags.

%description plugin-htmlchars -l pl.UTF-8
Wtyczka zawierająca bibliotekę znaczników specjalnych HTML.

%package plugin-filebrowser
Summary:	Sidebar File Browser plugin
Summary(pl.UTF-8):	Panel boczny do przeglądania systemu plików
Group:		Libraries

%description plugin-filebrowser
Sidebar File Browser.

%description plugin-filebrowser -l pl.UTF-8
Przeglądarka plików w panelu bocznym.

%package plugin-autosave
Summary:	Auto Save plugin
Summary(pl.UTF-8):	Wtyczka do auto zapisu
Group:		Libraries

%description plugin-autosave
Plugin for automatically saving changes.

%description plugin-autosave -l pl.UTF-8
Wtyczka do automatycznego zapisywania zmian.

%package plugin-vcdiff
Summary:	Version Control Diff plugin
Summary(pl.UTF-8):	Wtyczka Version Control Diff	
Group:		Libraries

%description plugin-vcdiff
Plugin form getting diffs over Version Control system, supports:
- svn
- cvs
- git

%description plugin-vcdiff -l pl.UTF-8
Wtyczka do porównywania zmian względem systemu kontroli wersji.
Aktualnie wspierane są:
- svn
- cvs
- git

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--docdir=%{_defaultdocdir}/%{name}-%{version}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_pixmapsdir}/%{name}.ico

%find_lang %{name}
%{!?_noautocompressdoc:find $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version} -not -name '*.html' -not -name '*.png' -exec gzip '{}' ';'}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/%{name}.1*
%dir %{_libdir}/%{name}
%doc %{_defaultdocdir}/%{name}-%{version}

%files plugin-classbuilder
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/classbuilder.so
%{_iconsdir}/hicolor/16x16/apps/classviewer-class.png
%{_iconsdir}/hicolor/16x16/apps/classviewer-macro.png
%{_iconsdir}/hicolor/16x16/apps/classviewer-member.png
%{_iconsdir}/hicolor/16x16/apps/classviewer-method.png
%{_iconsdir}/hicolor/16x16/apps/classviewer-namespace.png
%{_iconsdir}/hicolor/16x16/apps/classviewer-other.png
%{_iconsdir}/hicolor/16x16/apps/classviewer-struct.png
%{_iconsdir}/hicolor/16x16/apps/classviewer-var.png

%files plugin-export
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/export.so

%files plugin-htmlchars
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/htmlchars.so

%files plugin-autosave
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/autosave.so

%files plugin-vcdiff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/vcdiff.so

%files plugin-filebrowser
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/filebrowser.so
