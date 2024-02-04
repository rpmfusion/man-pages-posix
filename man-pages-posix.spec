%global posix_version 2017
%global posix_release a
%global posix_name man-pages-posix-%{posix_version}
%global posix_name_rel %{posix_name}-%{posix_release}

Summary: POSIX interface documentation
Name: man-pages-posix
Version: %{posix_version}%{posix_release}
Release: 3%{?dist}
License: LicenseRef-IEEE-2017
URL: https://www.kernel.org/doc/man-pages/
Source: https://www.kernel.org/pub/linux/docs/man-pages/man-pages-posix/%{posix_name_rel}.tar.xz

BuildRequires: make

# POSIX man pages used to be part of the regular `man-pages` package before the
# version below
Conflicts: man-pages < 5.12-3

BuildArch: noarch

%description
A collection of POSIX manual pages from the Linux Documentation Project (LDP).

%prep
%autosetup -n %{posix_name}

## Remove man pages we are not going to use ##

# we do not have sccs (rhbz#203302)
rm man1p/{admin,delta,get,prs,rmdel,sact,sccs,unget,val,what}.1p

%build
# nothing to build

%install
make install DESTDIR="$RPM_BUILD_ROOT"

%files
%doc README %{posix_name_rel}.Announce
%license POSIX-COPYRIGHT
%{_mandir}/man*/*

%changelog
* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2017a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2017a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Nov 25 2022 Christoph Erhardt <fedora@sicherha.de> - 2017a-1
- Initial package
