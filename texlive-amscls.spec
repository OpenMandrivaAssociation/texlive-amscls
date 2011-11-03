# revision 23392
# category Package
# catalog-ctan /macros/latex/required/amslatex/amscls
# catalog-date 2011-07-19 12:21:10 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-amscls
Version:	20110719
Release:	1
Summary:	AMS document classes for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/amslatex/amscls
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amscls.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This bundle contains three AMS classes, amsart (for writing
articles for the AMS), amsbook (for books) and amsproc (for
proceedings), together with some supporting material. The
material is made available as part of the AMS-LaTeX
distribution.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/amscls/amsalpha.bst
%{_texmfdistdir}/bibtex/bst/amscls/amsplain.bst
%{_texmfdistdir}/tex/latex/amscls/amsart.cls
%{_texmfdistdir}/tex/latex/amscls/amsbook.cls
%{_texmfdistdir}/tex/latex/amscls/amsbooka.sty
%{_texmfdistdir}/tex/latex/amscls/amsdtx.cls
%{_texmfdistdir}/tex/latex/amscls/amsldoc.cls
%{_texmfdistdir}/tex/latex/amscls/amsmidx.sty
%{_texmfdistdir}/tex/latex/amscls/amsproc.cls
%{_texmfdistdir}/tex/latex/amscls/amsthm.sty
%{_texmfdistdir}/tex/latex/amscls/upref.sty
%doc %{_texmfdistdir}/doc/latex/amscls/00LICENSE.txt
%doc %{_texmfdistdir}/doc/latex/amscls/amsart.template
%doc %{_texmfdistdir}/doc/latex/amscls/amsbook.template
%doc %{_texmfdistdir}/doc/latex/amscls/amsclass.pdf
%doc %{_texmfdistdir}/doc/latex/amscls/amsdtx.pdf
%doc %{_texmfdistdir}/doc/latex/amscls/amsmidx.pdf
%doc %{_texmfdistdir}/doc/latex/amscls/amsproc.template
%doc %{_texmfdistdir}/doc/latex/amscls/amsthdoc.pdf
%doc %{_texmfdistdir}/doc/latex/amscls/diffs-c.txt
%doc %{_texmfdistdir}/doc/latex/amscls/instr-l.pdf
%doc %{_texmfdistdir}/doc/latex/amscls/thmtest.pdf
%doc %{_texmfdistdir}/doc/latex/amscls/upref.pdf
#- source
%doc %{_texmfdistdir}/source/latex/amscls/00LICENSE.txt
%doc %{_texmfdistdir}/source/latex/amscls/00readme.txt
%doc %{_texmfdistdir}/source/latex/amscls/ams-c1.ins
%doc %{_texmfdistdir}/source/latex/amscls/amsclass.dtx
%doc %{_texmfdistdir}/source/latex/amscls/amsdtx.dtx
%doc %{_texmfdistdir}/source/latex/amscls/amsdtx.ins
%doc %{_texmfdistdir}/source/latex/amscls/amsmidx.dtx
%doc %{_texmfdistdir}/source/latex/amscls/amsthdoc.tex
%doc %{_texmfdistdir}/source/latex/amscls/install.txt
%doc %{_texmfdistdir}/source/latex/amscls/instr-l.tex
%doc %{_texmfdistdir}/source/latex/amscls/manifest.txt
%doc %{_texmfdistdir}/source/latex/amscls/thmtest.tex
%doc %{_texmfdistdir}/source/latex/amscls/upref.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}