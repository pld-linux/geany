Summary:	Fast and lightweight IDE using GTK+2
Summary(pl.UTF-8):	Szybkie i lekkie IDE używające GTK+2
Name:		geany
Version:	1.38
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://download.geany.org/%{name}-%{version}.tar.bz2
# Source0-md5:	47b7b89d58ed5bbef6ff8d517ed01efd
URL:		http://www.geany.org/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	which
Obsoletes:	geany-plugin-vcdiff
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
- automatyczne uzupełnianie często używanych konstrukcji jak if, fi
  while
- automatyczne uzupełnianie znaczników XML i HTML
- wyświetlanie podpowiedzi
- wiele wspieranych typów plików jak C, Java, PHP, Python, Perl,
  Pascal
- wykazy symboli

%package devel
Summary:	Header files for geany
Summary(pl.UTF-8):	Pliki nagłówkowe dla geany
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for geany.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla geany.

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

%package plugin-saveactions
Summary:	Provides different actions related to saving files
Summary(pl.UTF-8):	Wtyczka do automatycznego zapisu plików
Group:		Libraries
Provides:	geany-plugin-autosave
Obsoletes:	geany-plugin-autosave

%description plugin-saveactions
Provides different actions related to saving files (autosave,
instantsave, backupcopy).

%description plugin-saveactions -l pl.UTF-8
Wtyczka umożliwiająca wybór rodzaju zapisu pliku (autozapis, zapis
ciągły, kopia zapasowa).

%package plugin-splitwindow
Summary:	Splits the editor view into two windows
Summary(pl.UTF-8):	Wtyczka dzieląca okno na dwie części
Group:		Libraries

%description plugin-splitwindow
Splits the editor view into two windows.

%description plugin-splitwindow -l pl.UTF-8
Wtyczka dzieląca okno na dwie części.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-gtkdoc-header \
	--docdir=%{_docdir}/%{name}-%{version}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/Tango

# fix locales
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,lb}

%{__rm} $RPM_BUILD_ROOT%{_libdir}{/%{name},}/*.la

%find_lang %{name}
%{!?_noautocompressdoc:find $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} -not -name '*.html' -not -name '*.png' -exec gzip '{}' ';'}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%attr(755,root,root) %{_libdir}/libgeany.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libgeany.so.0
%{_iconsdir}/hicolor/*x*/apps/geany.png
%{_iconsdir}/hicolor/*x*/actions/geany*.png
%{_iconsdir}/hicolor/scalable/apps/geany.svg
%{_iconsdir}/hicolor/scalable/actions/geany*.svg

%{_mandir}/man1/%{name}.1*
%dir %{_libdir}/%{name}
%doc %{_docdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%attr(755,root,root) %{_libdir}/libgeany.so
%{_pkgconfigdir}/*.pc

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

%files plugin-saveactions
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/saveactions.so

%files plugin-splitwindow
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/splitwindow.so

%files plugin-filebrowser
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/filebrowser.so
