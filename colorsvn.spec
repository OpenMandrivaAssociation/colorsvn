Summary:	Colorizer for subversion, based on colorgcc and colorcvs
Name:		colorsvn
Version:	0.3.3
Release:	2
Group:		Development/Other
License:	GPLv2
Url:		http://colorsvn.tigris.org/
Source0:	http://colorsvn.tigris.org/files/documents/4414/49311/colorsvn-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	subversion
Requires:	subversion 

%description
Subversion output colorizer.

%prep
%autosetup -p1

%build
%configure

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

