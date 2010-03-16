Name:           colorsvn
Version:        0.3.2
Release:        %mkrel 6
Epoch:          0
Summary:        Colorizer for subversion, based on colorgcc and colorcvs
Group:          Development/Other
License:        GPL
URL:            http://www.console-colors.de/
Source0:        http://www.console-colors.de/downloads/colorsvn/colorsvn-%{version}.tar.gz
Requires:       subversion 
BuildRequires:  subversion
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Subversion output colorizer.

%prep
%setup -q

%build
%{configure2_5x}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__perl} -p -e 's|/bin/sh|/bin/csh|;' \
             -e 's|=| |g;' \
  %{buildroot}%{_sysconfdir}/profile.d/colorsvn-env.sh \
  > %{buildroot}%{_sysconfdir}/profile.d/colorsvn-env.csh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog COPYING CREDITS INSTALL
%attr(0755,root,root) %{_bindir}/colorsvn
%{_mandir}/man1/colorsvn.1*
%config(noreplace) %{_sysconfdir}/colorsvnrc
%attr(0755,root,root) %{_sysconfdir}/profile.d/colorsvn-env.sh
%attr(0755,root,root) %{_sysconfdir}/profile.d/colorsvn-env.csh


