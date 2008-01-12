Summary:	Fast and lightweight IDE using GTK+2
Summary(pl.UTF-8):	Szybkie i lekkie IDE używające GTK+2
Name:		geany
Version:	0.12
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/geany/%{name}-%{version}.tar.bz2
# Source0-md5:	bfb6dd5e833f2852935f93218a09de93
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-doc_dir.patch
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__glib_gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_pixmapsdir}/%{name}.ico

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO scintilla/License.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/%{name}.1*
%dir %{_libdir}/%{name}

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
