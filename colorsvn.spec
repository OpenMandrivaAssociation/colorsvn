Summary:	Colorizer for subversion, based on colorgcc and colorcvs
Name:		colorsvn
Version:	0.3.2
Release:	12
Group:		Development/Other
License:	GPLv2
Url:		http://www.console-colors.de/
Source0:	http://www.console-colors.de/downloads/colorsvn/colorsvn-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	subversion
Requires:	subversion 

%description
Subversion output colorizer.

%prep
%setup -q

%build
%configure2_5x

%install
%makeinstall_std
perl -p -e 's|/bin/sh|/bin/csh|;' \
	-e 's|=| |g;' \
	%{buildroot}%{_sysconfdir}/profile.d/colorsvn-env.sh \
	> %{buildroot}%{_sysconfdir}/profile.d/colorsvn-env.csh

%files
%doc ChangeLog COPYING CREDITS INSTALL
%{_bindir}/colorsvn
%{_mandir}/man1/colorsvn.1*
%config(noreplace) %{_sysconfdir}/colorsvnrc
%attr(0755,root,root) %{_sysconfdir}/profile.d/colorsvn-env.sh
%attr(0755,root,root) %{_sysconfdir}/profile.d/colorsvn-env.csh

