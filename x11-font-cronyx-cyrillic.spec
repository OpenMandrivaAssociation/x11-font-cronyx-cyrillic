Name: x11-font-cronyx-cyrillic
Version: 1.0.4
Release: 2
Summary: Xorg X11 font cronyx-cyrillic
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-cronyx-cyrillic-%{version}.tar.xz
License: MIT-like
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font cronyx-cyrillic.

%prep
%autosetup -p1 -n font-cronyx-cyrillic-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/cyrillic

%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/cyrillic/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/cyrillic/fonts.scale

%post
mkfontscale %{_datadir}/fonts/cyrillic
mkfontdir %{_datadir}/fonts/cyrillic

%postun
mkfontscale %{_datadir}/fonts/cyrillic
mkfontdir %{_datadir}/fonts/cyrillic

%files
%doc COPYING
%{_datadir}/fonts/cyrillic/crox*.pcf.gz
%{_datadir}/fonts/cyrillic/koi*.pcf.gz
