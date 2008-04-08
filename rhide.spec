# NOTE:
# - this is:
#   - bad
#   - ugly
#   - stupid
#   - non-right-way
#   - doesn't support other archs than ix86(probably)
# but: IT WORKS! And please don't do any "cleanup" without test if it will
# working after cleanup.
# "TODO":
# - compile with newer rhtvision and setedit
# - use shared libs
# - big, big, big... cleanup
# - sleep() (ups.. it's for me, not spec...)
Summary:	IDE for developing like the old known Borland C++ 3.1 IDE
Summary(pl.UTF-8):	IDE dla programistów podobne do starego IDE z Borland C++ 3.1
Name:		rhide
Version:	1.5
Release:	0.1
License:	GPL
Group:		Development/Debuggers
Source0:	http://dl.sourceforge.net/rhide/%{name}-%{version}.tar.gz
# Source0-md5:	e9a197c729ea80a429bd9aa8107db666
Source1:	http://dl.sourceforge.net/tvision/rhtvision-2.0.1.src.tar.gz
# Source1-md5:	409c52e8ec111a10f40b41a7fd198766
Source2:	http://dl.sourceforge.net/setedit/setedit-0.5.0.tar.gz
# Source2-md5:	81e89ab19c9b25015fb2078512e32f03
Source3:	http://ftp.gnu.org/gnu/gdb/gdb-5.3.tar.gz
# Source3-md5:	1e8566325f222edfbdd93e40c6ae921b
Patch0:		%{name}-libs.patch
Patch1:		%{name}-gdblib.patch
Patch2:		%{name}-tvision2.patch
Patch4:		%{name}-misc.patch
BuildRequires:	autoconf
BuildRequires:	automake
# BuildRequires:	librhtv-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RHIDE allows you to develop your programs in an text-based environment
like known from old Borlands's IDE but improved and adapted for
GNU/Linux. RHIDE supports nearly every compiler, which gcc supports,
and additionally also the Pascal compilers gpc and fpc. The Pascal
support is somewhat untested but should work after some runtime
configuration on RHIDE.

%description -l pl.UTF-8
RHIDE pozwala na tworzenie programów w środowisku tekstowym podobnym
do znanego ze starego borlandowskiego IDE, ale ulepszonym i
zaadoptowanym dla systemu GNU/Linux. RHIDE obsługuje prawie każdy
kompilator obsługiwany przez gcc i dodatkowo kompilatory Pascala gpc i
fpc. Obsługa Pascala jest gdzieniegdzie nieprzetestowana ale powinna
działać po ustawieniu w konfiguracji.

%prep
%setup -q -a 1 -a 2 -a 3
%patch0
%patch1
%patch2 -p1
%patch4

sed -i -e 's:--add-location $(po_list_l):--add-location --from-code=iso-8859-1 $(po_list_l):' \
	setedit/internac/gnumake.in

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
export CFLAGS
cd tvision
./configure \
	--prefix=%{_prefix} \
	--fhs
sed -i -e 's/all: static-lib dynamic-lib/all: static-lib/' Makefile
%{__make}

cd -
cd setedit
./configure \
	--prefix=%{_prefix} \
	--fhs \
	--libset \
	--without-mp3
sed -i -e 's/needed: internac doc-basic/needed: internac/' Makefile
%{__make}
cd -

SETSRC=`pwd`/setedit
SETOBJ=$SETSRC/makes
GDB_SRC=`pwd`/gdb-5.3
TVSRC=`pwd`/tvision
TVOBJ=$TVSRC/linux
TV_INC=`pwd`/tvision/include

export SETSRC SETOBJ GDB_SRC TVSRC TVOBJ TV_INC
#cp -f /usr/share/automake/config.sub .
#%{__aclocal}
#%{__autoconf}
%configure

for x in configure `find . -name '*.mak' -o -name 'makefile.src'`; do
	%{__perl} -pi -e "s|-O2|%{rpmcflags} -I/usr/include/ncurses|g" $x
done

%{__make} -C po

%{__make} \
	RHIDESRC=`pwd` \
	C_OPT_FLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	C_EXTRA_FLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	C_WARN_FLAGS="" \
	SET_SPECIAL_LDFLAGS="%{rpmldflags} -L%{_prefix}/X11R6/%{_lib} -lXmu"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	RHIDESRC=`pwd` \
	prefix=$RPM_BUILD_ROOT%{_prefix}

tic eterm-rhide -o .
install -D x/xterm-eterm-tv $RPM_BUILD_ROOT%{_datadir}/terminfo/x/xterm-eterm-tv

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpr2mak
%attr(755,root,root) %{_bindir}/gprexp
%attr(755,root,root) %{_bindir}/rhgdb
%attr(755,root,root) %{_bindir}/rhide
%attr(755,root,root) %{_bindir}/rhidex
%attr(755,root,root) %{_bindir}/rhgdbx
%dir %{_docdir}/rhide
%{_docdir}/rhide/COPYING
%{_docdir}/rhide/COPYING.RH
%{_docdir}/rhide/LINUX.TXT
%{_docdir}/rhide/README.IDE
%{_docdir}/rhide/RHIDE.BIN
%{_docdir}/rhide/VCSA.SH
%{_docdir}/rhide/readme.key
%{_docdir}/rhide/rhide.txt
%{_infodir}/rhide.*
%dir %{_datadir}/rhide
%config %{_datadir}/rhide/rhide_.env
%dir %{_datadir}/rhide/SET
%config %{_datadir}/rhide/SET/clippmac.pmc
%config %{_datadir}/rhide/SET/cpmacros.pmc
%config %{_datadir}/rhide/SET/htmlmac.pmc
%config %{_datadir}/rhide/SET/macros.slp
%config %{_datadir}/rhide/SET/perlmac.pmc
%config %{_datadir}/rhide/SET/pmacros.pmc
%config %{_datadir}/rhide/SET/syntaxhl.shl
%config %{_datadir}/rhide/eterm-rhide
%{_datadir}/terminfo/x/xterm-eterm-tv
