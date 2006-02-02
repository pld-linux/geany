Summary:	Fast and lightweight IDE using GTK+2
Summary(pl):	Szybkie i lekkie IDE u¿ywaj±ce GTK+2
Name:		geany
Version:	0.5
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/geany/%{name}-%{version}.tar.bz2
# Source0-md5:	526b7a47c269ffaa7bf13e939e09b73f
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

%description -l pl
Geany jest ma³ym i lekkim zintegrowanym ¶rodowiskiem programistycznym.
Zosta³ napisany z my¶l± o byciu ma³ym i szybkim IDE, z ma³± liczb±
zale¿no¶ci od innych pakietów. Kolejnym, przy¶wiecaj±cym tworzeniu go
celem by³o maksymalne uniezale¿nienie od konkretnego ¶rodowiska
graficznego jak KDE czy GNOME.

Podstawowe cechy Geany to:
- pod¶wietlanie sk³adni
- uzupe³nianie kodu
- automatyczne uzupe³nianie czêsto u¿ywanych konstrukcji jak if, for
  i while
- automatyczne uzupe³nianie znaczników XML i HTML
- wy¶wietlanie podpowiedzi
- wiele wspieranych typów plików jak C, Java, PHP, Python, Perl,
  Pascal
- wykazy symboli

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/geany
%{_desktopdir}/geany.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/geany.png
