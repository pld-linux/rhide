Summary:	IDE for developing like the old known Borland 3.1 IDE
Summary:	IDE dla programistów podobne do starego IDE z Borland 3.1
Name:		rhide
Version:	1.5
Release:	0.1
License:	GPL
Group:		Development/Debuggers
Source0:	http://dl.sourceforge.net/rhide/%{name}-%{version}.tar.gz
Patch0:		%{name}-libs.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	librhtv-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RHIDE allows you to develop your programs in an text-based environment
like known from old Borlands`s IDE but improved and adapted for
GNU/Linux. RHIDE supports nearly every compiler, which gcc supports,
and additionally also the Pascal compilers gpc and fpc. The Pascal
support is somewhat untested but should work after some runtime
configuration on RHIDE.

%description -l pl
RHIDE pozwala na tworzenie programów w ¶rodowisku tekstowym podobnym
do znanego z starego Borlandowskiego IDE, ale ulepszonym i
zaadoptowanym dla systemu GNU/Linux. RHIDE obs³uguje prawie ka¿dy
kompilator obs³ugiwany przez gcc i dodatkowo kompilatory Pascala gpc i
fpc. Obs³uga Pascala jest gdzieniegdzie nieprzetestowana ale powinna
dzia³aæ po ustawieniu w konfiguracji.

%prep
%setup -q
%patch0

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	RHIDESRC=`pwd`

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	RHIDESRC=`pwd` \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post
tic /usr/share/rhide/eterm-rhide

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/gpr2mak
#%attr(755,root,root) %{_bindir}/gprexp
#%attr(755,root,root) %{_bindir}/rhgdb
#%attr(755,root,root) %{_bindir}/rhide
#%attr(755,root,root) %{_bindir}/rhidex
#%attr(755,root,root) %{_bindir}/rhgdbx
#%doc %{_datadir}/doc/rhide/COPYING
#%doc %{_datadir}/doc/rhide/COPYING.RH
#%doc %{_datadir}/doc/rhide/LINUX.TXT
#%doc %{_datadir}/doc/rhide/README.IDE
#%doc %{_datadir}/doc/rhide/RHIDE.BIN
#%doc %{_datadir}/doc/rhide/VCSA.SH
#%doc %{_datadir}/doc/rhide/readme.key
#%doc %{_datadir}/doc/rhide/rhide.txt
#%{_datadir}/info/infview.inf
#%{_datadir}/info/rhide.inf
#%{_datadir}/info/setedit.inf
#%{_datadir}/locale/cs/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/da/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/de/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/es/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/fi/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/fr/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/it/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/nl/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/no/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/pl/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/pt/LC_MESSAGES/rhide.mo
#%{_datadir}/locale/sv/LC_MESSAGES/rhide.mo
#%config %{_datadir}/rhide/rhide_.env
#%config %{_datadir}/rhide/SET/clippmac.pmc
#%config %{_datadir}/rhide/SET/cpmacros.pmc
#%config %{_datadir}/rhide/SET/htmlmac.pmc
#%config %{_datadir}/rhide/SET/macros.slp
#%config %{_datadir}/rhide/SET/perlmac.pmc
#%config %{_datadir}/rhide/SET/pmacros.pmc
#%config %{_datadir}/rhide/SET/syntaxhl.shl
#%config %{_datadir}/rhide/eterm-rhide
