Summary:	HomeBank - free easy personal accounting for all
Name:		homebank
Version:	4.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://homebank.free.fr/public/%{name}-%{version}.tar.gz
# Source0-md5:	b6f3c01d27cf476e4ae74eb56e06bc00
URL:		http://homebank.free.fr
BuildRequires:	atk-devel
BuildRequires:	cairo-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gtk+2-devel
BuildRequires:	libofx-devel
BuildRequires:	perl(XML::Parser)
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HomeBank is the free software you have always wanted to manage your
personal accounts at home. The main concept is to be light, simple and
very easy to use. It brings you many features that allows you to
analyze your finances in a detailed way instantly and dynamically with
powerful report tools based on filtering and graphical charts.

%prep
%setup -q

%build
%{__intltoolize} --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

#desktop-file-install                                    \
#        --delete-original                               \
#        --dir $RPM_BUILD_ROOT%{_desktopdir}   \
#        --mode 0644                                     \
#        $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help
%{_datadir}/%{name}/images
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}.svg
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml
