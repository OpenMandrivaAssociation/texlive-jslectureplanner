Name:		texlive-jslectureplanner
Version:	57095
Release:	2
Summary:	Creation and management of university course material
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jslectureplanner
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jslectureplanner.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jslectureplanner.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The jslectureplanner package facilitates the generation and
management of university course material. It provides an
interface to set up and access centralized course data that can
be reused in all course documents. Furthermore, the package is
able to calculate the session dates of a whole semester and
generate course programs, if the course is held weekly and the
date of the first lecture is specified. Moreover, the package
can be used to generate a sectioned course bibliography via
BibLaTeX. The bundle also includes a package jsmembertable.sty
that helps in generating course member and presence lists.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jslectureplanner
%doc %{_texmfdistdir}/doc/latex/jslectureplanner

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
