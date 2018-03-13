Summary:	Helper for enabling better Steam integration
Name:		linux-steam-integration
Version:	0.7.2
Release:	1
License:	LGPL-2.1
Group:		Games/Other
Url:		https://github.com/solus-project/linux-steam-integration
Source:		%{name}-%{version}.tar.xz
BuildRequires:	meson
BuildRequires:	pkgconfig(gtk+-3.0)

%description
Linux Steam* Integration is a helper system to make
the Steam Client and Steam games run better on Linux. 
In a nutshell, LSI automatically applies various workarounds
to get games working, and fixes long standing bugs in both 
games and the client.

%files -f %{name}.lang
%{_bindir}/lsi-exec
%{_bindir}/lsi-settings
%{_libdir}/liblsi-intercept.so
%{_libdir}/liblsi-redirect.so
%{_datadir}/applications/lsi-settings.desktop

%prep
%setup -q

%build
%meson \
	-Dwith-frontend=true
%meson_build

%install
%meson_install

rm -rf %{buildroot}/%{_bindir}/steam

%find_lang %{name}


