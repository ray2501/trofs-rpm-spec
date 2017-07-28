Name:           trofs
BuildRequires:  tcl-devel >= 8.5
Summary:        Tcl Read-only Filesystem
License:        NIST
Group:          Development/Libraries/Tcl
Version:        0.4.9
Release:        0
Url:            http://math.nist.gov/~DPorter/tcltk/trofs/
Source0:        %name%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
trofs is a Tcl package that provides commands to create, mount,
and unmount archives containing read-only filesystems.

%prep
%setup -q -n %name%version

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--libdir=%_libdir \
	--prefix=/usr \
	--with-tcl=%_libdir
make

%install
make install \
	DESTDIR=%buildroot \
	PKG_HEADERS= \
	libdir=%_libdir/tcl

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc ChangeLog README license.terms
%_libdir/tcl
/usr/share/man/mann

%changelog
