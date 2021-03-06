Name:		texlive-amscls
Version:	2.20.4
Release:	2
Summary:	AMS document classes for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/amslatex/amscls
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle contains three AMS classes, amsart (for writing
articles for the AMS), amsbook (for books) and amsproc (for
proceedings), together with some supporting material. The
material is made available as part of the AMS-LaTeX
distribution.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/amscls
%{_texmfdistdir}/tex/latex/amscls
%doc %{_texmfdistdir}/doc/latex/amscls
#- source
%doc %{_texmfdistdir}/source/latex/amscls

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
