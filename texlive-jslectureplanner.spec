%global tl_name jslectureplanner
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.15
Release:	%{tl_revision}.1
Summary:	Creation and management of university course material
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jslectureplanner
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jslectureplanner.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jslectureplanner.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The jslectureplanner package facilitates the generation and management
of university course material. It provides an interface to set up and
access centralized course data that can be reused in all course
documents. Furthermore, the package is able to calculate the session
dates of a whole semester and generate course programs, if the course is
held weekly and the date of the first lecture is specified. Moreover,
the package can be used to generate a sectioned course bibliography via
BibLaTeX. The bundle also includes a package jsmembertable.sty that
helps in generating course member and presence lists.

