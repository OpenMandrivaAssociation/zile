Summary:	Lossy Emacs
Name:		zile
Epoch:		1
Version:	2.4.9
Release:	3
License:	GPLv3+
Group:		Editors
URL:		http://www.gnu.org/software/zile/
Source0:	http://ftp.gnu.org/gnu/zile/%{name}-%version.tar.gz
Source1:	http://ftp.gnu.org/gnu/zile/%{name}-%version.tar.gz.sig
Patch0:		zile-2.4.6-mdv-ncursesw.patch

BuildRequires:	help2man
BuildRequires:	texinfo
BuildRequires:	tetex-latex
BuildRequires:	termcap-devel
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	pkgconfig(ncursesw)

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
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_mandir}/man1/%{name}.1*

