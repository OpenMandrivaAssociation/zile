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
