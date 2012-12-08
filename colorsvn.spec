Name:           colorsvn
Version:        0.3.2
Release:        %mkrel 10
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




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0:0.3.2-8mdv2011.0
+ Revision: 663390
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.3.2-7mdv2011.0
+ Revision: 603841
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.3.2-6mdv2010.1
+ Revision: 522388
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0:0.3.2-5mdv2010.0
+ Revision: 413257
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0:0.3.2-4mdv2009.1
+ Revision: 350726
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0:0.3.2-3mdv2009.0
+ Revision: 243617
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0:0.3.2-1mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Apr 04 2007 David Walluck <walluck@mandriva.org> 0:0.3.2-1mdv2007.1
+ Revision: 150462
- 0.3.2

* Mon Oct 16 2006 David Walluck <walluck@mandriva.org> 0:0.3.1-1mdv2007.1
+ Revision: 65287
- BuildRequires: subversion
- Import colorsvn

* Thu Sep 21 2006 David Walluck <walluck@mandriva.org> 0:0.3.1-1mdv2007.0
- release

