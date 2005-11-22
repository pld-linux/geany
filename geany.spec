Summary:	GTK+2 Programmer's Editor
Name:		geany
Version:	0.3
Release:	2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://geany.uvena.de/files/%{name}-%{version}.tar.bz2
# Source0-md5:	64bc92e6d0582bc3594537da5fa7cf91
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-doc_dir.patch
URL:		http://geany.uvena.de/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geany is a small and lightweight integrated development environment.
It was developed to provide a small and fast IDE, which has only a few
dependencies from other packages. Another goal was to be as
independent as possible from a special Desktop Environment like KDE or
GNOME. So it uses only the GTK+2 toolkit and therefore you need only
the GTK+2 runtime libraries to run Geany.

Basic features of Geany
- syntax highlighting
- code completion
- auto completion of often used constructs like if, for and while
- auto completion of XML and HTML tags
- call tips
- many supported filetypes like C, Java, PHP, HTML, Python, Perl,
  Pascal
- symbol lists

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
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
