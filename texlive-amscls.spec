%global tl_name amscls
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.20.6
Release:	%{tl_revision}.1
Summary:	AMS document classes for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/required/amscls
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle contains three AMS classes, amsart (for writing articles for
the AMS), amsbook (for books) and amsproc (for proceedings), together
with some supporting material. This material forms one branch of what
was originally the AMS-LaTeX distribution. The other branch, amsmath, is
now maintained and distributed separately. The user documentation can be
found in the package amscls-doc.

