
# norootforbuild

# Find version of boo
%define boo_version %(rpm -q boo --queryformat '%{VERSION}')

Name:           monodevelop
BuildRequires:  boo bytefx-data-mysql gconf-sharp2 gtk-sharp2-gapi gtkhtml-sharp2 gtksourceview-sharp2 ikvm intltool mono-basic mono-data-oracle mono-data-postgresql mono-data-sqlite mono-data-sybase mono-devel mono-nunit monodoc-core gecko-sharp2 perl-XML-Parser vte-sharp2 xsp shared-mime-info
URL:            http://www.go-mono.com/
License:        GNU General Public License (GPL)
Group:          Development/Languages/Other
Autoreqprov:    on
Version:        0.14
Release:        1
Summary:        A Full-Featured IDE for Mono and Gtk#
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
# Boo's assemblies are always version at 1.0.0.0.  Force built against or newer.
Requires:       boo >= %boo_version
Requires:       ikvm xsp
Requires:       mono-data-postgresql bytefx-data-mysql
Requires:       mono-basic
PreReq:         shared-mime-info



%if 0%{?suse_version}
BuildRequires: update-desktop-files desktop-file-utils

%if %suse_version <= 1000
# Doesn't work on 9.3 and 10.0...
# Syntax must have changed... skip for now
%define suse_update_desktop_file true
%endif


%endif

# TODO: Add build requirements for xulrunner/mozilla, etc... md does some checks at build time for aspnetedit
#  (not currently enabled, but we'll need those checks when it is)


%if 0%{?fedora_version}
%define env_options export MONO_SHARED_DIR=/tmp

# TODO: what to do here on fedora?
%define suse_update_desktop_file true

%endif


%description
MonoDevelop is intended to be a full-featured integrated development
environment (IDE) for mono and Gtk#. It was originally a port of
SharpDevelop 0.98. See http://monodevelop.com/ for more information.


%debug_package
%prep
%setup -q

%build
%{?env_options}
./configure --prefix=%{_prefix} \
	    --enable-java \
	    --enable-boo \
	    --enable-subversion \
	    --enable-aspnet \
	    --disable-update-mimedb \
	    --disable-update-desktopdb
#            --enable-debugger=yes
make

%install
%{?env_options}
make install DESTDIR=$RPM_BUILD_ROOT GACUTIL_FLAGS="/package monodevelop /root ${RPM_BUILD_ROOT}/usr/%_lib"
#
mkdir -p $RPM_BUILD_ROOT/usr/share/pkgconfig
mv $RPM_BUILD_ROOT/usr/lib/pkgconfig/* $RPM_BUILD_ROOT/usr/share/pkgconfig

%suse_update_desktop_file -N "Mono Development Environment" -G "Integrated Development Environment" -C "Develop software using Mono tools" %name "Application Development IDE"
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_prefix}/bin/*
%{_prefix}/share/applications/monodevelop.desktop
%{_prefix}/share/mime/packages/monodevelop.xml
%{_prefix}/share/pixmaps/monodevelop.png
%{_prefix}/lib/monodevelop
%{_prefix}/share/pkgconfig/monodevelop.pc

%post
update-mime-database /usr/share/mime >/dev/null || :

%postun
update-mime-database /usr/share/mime >/dev/null || :

# auto dep/req generation for older distros (it will take a while for the .config scanning to get upstream)
%if 0%{?suse_version} <= 1040 || 0%{?fedora_version} <= 7
%if 0%{?fedora_version}
# Allows overrides of __find_provides in fedora distros... (already set to zero on newer suse distros)
%define _use_internal_dependency_generator 0
%endif
%define __find_provides env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/find-provides && printf "%s\\n" "${filelist[@]}" | /usr/bin/mono-find-provides ; } | sort | uniq'
%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%s\\n" "${filelist[@]}" | /usr/lib/rpm/find-requires && printf "%s\\n" "${filelist[@]}" | /usr/bin/mono-find-requires ; } | sort | uniq'
%endif

%changelog