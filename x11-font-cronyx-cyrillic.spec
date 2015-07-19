Name: x11-font-cronyx-cyrillic
Version: 1.0.3
Release: 13
Summary: Xorg X11 font cronyx-cyrillic
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/font/font-cronyx-cyrillic-%{version}.tar.bz2
License: MIT-like
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-cyrillic-fonts <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font cronyx-cyrillic

%prep
%setup -q -n font-cronyx-cyrillic-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/cyrillic

%make

%install
%makeinstall_std
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


