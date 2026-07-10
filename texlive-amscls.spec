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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle contains three AMS classes, amsart (for writing articles for
the AMS), amsbook (for books) and amsproc (for proceedings), together
with some supporting material. This material forms one branch of what
was originally the AMS-LaTeX distribution. The other branch, amsmath, is
now maintained and distributed separately. The user documentation can be
found in the package amscls-doc.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/amscls
%dir %{_datadir}/texmf-dist/doc/latex/amscls
%dir %{_datadir}/texmf-dist/source/latex/amscls
%dir %{_datadir}/texmf-dist/tex/latex/amscls
%{_datadir}/texmf-dist/bibtex/bst/amscls/amsalpha.bst
%{_datadir}/texmf-dist/bibtex/bst/amscls/amsplain.bst
%doc %{_datadir}/texmf-dist/doc/latex/amscls/00LICENSE.txt
%doc %{_datadir}/texmf-dist/doc/latex/amscls/README
%doc %{_datadir}/texmf-dist/doc/latex/amscls/amsart-template.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls/amsbook-template.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls/amsbooka.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls/amsclass.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls/amsdtx.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls/amsmidx.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls/amsproc-template.tex
%doc %{_datadir}/texmf-dist/doc/latex/amscls/amsthdoc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls/diffs-c.txt
%doc %{_datadir}/texmf-dist/doc/latex/amscls/manifest.txt
%doc %{_datadir}/texmf-dist/doc/latex/amscls/thmtest.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amscls/upref.pdf
%doc %{_datadir}/texmf-dist/source/latex/amscls/amsbooka.dtx
%doc %{_datadir}/texmf-dist/source/latex/amscls/amsbooka.ins
%doc %{_datadir}/texmf-dist/source/latex/amscls/amsclass.dtx
%doc %{_datadir}/texmf-dist/source/latex/amscls/amsclass.ins
%doc %{_datadir}/texmf-dist/source/latex/amscls/amsclass.pdf
%doc %{_datadir}/texmf-dist/source/latex/amscls/amsdtx.dtx
%doc %{_datadir}/texmf-dist/source/latex/amscls/amsdtx.ins
%doc %{_datadir}/texmf-dist/source/latex/amscls/amsmidx.dtx
%doc %{_datadir}/texmf-dist/source/latex/amscls/amsmidx.ins
%doc %{_datadir}/texmf-dist/source/latex/amscls/amsthdoc.tex
%doc %{_datadir}/texmf-dist/source/latex/amscls/install.txt
%doc %{_datadir}/texmf-dist/source/latex/amscls/thmtest.tex
%doc %{_datadir}/texmf-dist/source/latex/amscls/upref.dtx
%doc %{_datadir}/texmf-dist/source/latex/amscls/upref.ins
%{_datadir}/texmf-dist/tex/latex/amscls/amsart.cls
%{_datadir}/texmf-dist/tex/latex/amscls/amsbook.cls
%{_datadir}/texmf-dist/tex/latex/amscls/amsbooka.sty
%{_datadir}/texmf-dist/tex/latex/amscls/amsdtx.cls
%{_datadir}/texmf-dist/tex/latex/amscls/amsldoc.cls
%{_datadir}/texmf-dist/tex/latex/amscls/amsmidx.sty
%{_datadir}/texmf-dist/tex/latex/amscls/amsproc.cls
%{_datadir}/texmf-dist/tex/latex/amscls/amsthm.sty
%{_datadir}/texmf-dist/tex/latex/amscls/upref.sty
