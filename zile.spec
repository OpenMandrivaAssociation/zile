%define name    zile
%define version 2.4.8
%define release 1
%define Summary Zile Is Lossy Emacs

Summary:        %Summary
Name:           %name
Epoch:		1
Version:        %version
Release:        %release
License:        GPLv3+
Group:          Editors
URL:            http://www.gnu.org/software/zile/
Source0:	http://ftp.gnu.org/gnu/zile/%name-%version.tar.gz
Patch0:         zile-2.4.6-mdv-ncursesw.patch
BuildRequires:  ncursesw-devel
BuildRequires:	texinfo
BuildRequires:	tetex-latex
BuildRequires:	termcap-devel
BuildRequires:	help2man
BuildRequires:	pkgconfig(bdw-gc)


%description
Zile is another Emacs-clone. Zile is a customizable, self-documenting
real-time open-source display editor.

Zile was written to be as similar as possible to Emacs; every Emacs user
should feel at home with Zile. Zile features

    * Small but fast and powerful. It is very useful for small footprint
      installations (like on floppy disk) or quick editing sessions.
    * 8-bit clean. Zile can operate with binary files.
    * Looks like Emacs. Most Zile key sequences and function names are
      identical to Emacs ones.
    * Multi buffer editing w/multi level undo. Zile can open an infinite
      number of files and can record an infinite sequence of undo
      operations.
    * Multi window. Zile can display multiple windows on the screen.
    * Killing, yanking and registers. The typical killing, yanking and
      register features of Emacs are available under Zile.
    * Minibuffer completion. Zile can complete the user written text.
      This is very useful for M-x commands and for selecting files.
    * Colors. Zile makes use of the color capatibilities of the terminal
      if available.
    * Source highlighting (``C'', ``C++'', and shell scripts). Zile can
      highlight ``C'', ``C++'' source files and shell scripts for
      better reading.
    * Auto fill (word wrap). Zile automatically breaks the lines when
      they become too wide (if the Auto Fill Mode is enabled).


%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%post
%_install_info        %name.info

%preun
%_remove_install_info %name.info

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING NEWS README
#%_datadir/%name
%_mandir/man1/%name.1.*


%changelog
* Mon Jul 16 2012 Alexander Khrukin <akhrukin@mandriva.org> 1:2.4.8-1
+ Revision: 809773
- version update 2.4.8

* Thu Mar 22 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:2.4.7-1
+ Revision: 786054
- update to 2.4.7

* Sun Feb 19 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:2.4.6-1
+ Revision: 777420
- new version 2.4.6
- link to ncursesw instead ncurses
- don't package INSTALL file

  + Alexander Khrukin <akhrukin@mandriva.org>
    - version update 2.4.5

  + Funda Wang <fwang@mandriva.org>
    - update to new version 2.3.22
    - update to new version 2.3.21

* Sat Aug 14 2010 Funda Wang <fwang@mandriva.org> 1:2.3.19-1mdv2011.0
+ Revision: 569547
- update to new version 2.3.19

* Wed Mar 03 2010 Sandro Cazzaniga <kharec@mandriva.org> 1:2.3.15-1mdv2010.1
+ Revision: 513762
- fix licence
- update to 2.3.15

* Wed Nov 11 2009 Frederik Himpe <fhimpe@mandriva.org> 1:2.3.13-1mdv2010.1
+ Revision: 464903
- update to new version 2.3.13

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 1:2.3.12-1mdv2010.0
+ Revision: 444859
- update to new version 2.3.12

* Tue Sep 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1:2.3.11-1mdv2010.0
+ Revision: 423671
- update to new version 2.3.11

* Mon Jul 27 2009 Emmanuel Andry <eandry@mandriva.org> 1:2.3.9-1mdv2010.0
+ Revision: 400746
- New version 2.3.9

* Fri Mar 20 2009 Nicolas Vigier <nvigier@mandriva.com> 1:2.3.4-1mdv2009.1
+ Revision: 359081
- version 2.3.4

* Sat Dec 13 2008 Funda Wang <fwang@mandriva.org> 1:2.3.0-1mdv2009.1
+ Revision: 313902
- New version 2.3.0

* Mon Aug 04 2008 Funda Wang <fwang@mandriva.org> 1:2.2.61-1mdv2009.0
+ Revision: 263137
- update to new version 2.2.61

* Sun Jul 27 2008 Funda Wang <fwang@mandriva.org> 1:2.2.60-1mdv2009.0
+ Revision: 250482
- update to new version 2.2.60

* Wed May 14 2008 Funda Wang <fwang@mandriva.org> 1:2.2.59-1mdv2009.0
+ Revision: 207225
- update to new version 2.2.59

* Wed May 07 2008 Funda Wang <fwang@mandriva.org> 1:2.2.58-1mdv2009.0
+ Revision: 202698
- New version 2.2.58

* Wed Apr 16 2008 Funda Wang <fwang@mandriva.org> 1:2.2.57-1mdv2009.0
+ Revision: 194513
- update to new version 2.2.57

* Wed Mar 05 2008 Nicolas Vigier <nvigier@mandriva.com> 1:2.2.56-1mdv2008.1
+ Revision: 180172
- new version

* Mon Feb 11 2008 Funda Wang <fwang@mandriva.org> 1:2.2.54-1mdv2008.1
+ Revision: 165018
- update to new version 2.2.54

* Tue Feb 05 2008 Funda Wang <fwang@mandriva.org> 1:2.2.53-1mdv2008.1
+ Revision: 162742
- update to new version 2.2.53

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 20 2007 Funda Wang <fwang@mandriva.org> 1:2.2.52-1mdv2008.1
+ Revision: 110734
- New version 2.2.52

* Mon Nov 12 2007 Funda Wang <fwang@mandriva.org> 1:2.2.50-1mdv2008.1
+ Revision: 108147
- New version 2.2.50

* Tue Oct 16 2007 Funda Wang <fwang@mandriva.org> 1:2.2.48-1mdv2008.1
+ Revision: 99000
- New version 2.2.48

* Sun Oct 14 2007 Funda Wang <fwang@mandriva.org> 1:2.2.47-1mdv2008.1
+ Revision: 98313
- New version 2.2.47

* Sun Oct 14 2007 Funda Wang <fwang@mandriva.org> 1:2.2.46-1mdv2008.1
+ Revision: 98140
- New version 2.2.46

* Thu Oct 11 2007 Funda Wang <fwang@mandriva.org> 1:2.2.43-1mdv2008.1
+ Revision: 97025
- New version 2.2.43

* Sun Aug 19 2007 Funda Wang <fwang@mandriva.org> 1:2.2.41-1mdv2008.0
+ Revision: 66538
- New version 2.2.41

* Fri Aug 10 2007 Funda Wang <fwang@mandriva.org> 1:2.2.40-1mdv2008.0
+ Revision: 61031
- New version 2.2.40

* Tue Jul 17 2007 Funda Wang <fwang@mandriva.org> 1:2.2.39-1mdv2008.0
+ Revision: 52975
- New version

* Thu Jul 12 2007 Funda Wang <fwang@mandriva.org> 1:2.2.38-1mdv2008.0
+ Revision: 51566
- New version

* Sun Jul 08 2007 Nicolas Vigier <nvigier@mandriva.com> 1:2.2.37-1mdv2008.0
+ Revision: 49619
- new version

