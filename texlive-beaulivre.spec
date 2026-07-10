%global tl_name beaulivre
%global tl_revision 78004

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Write your books in a colorful way
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/beaulivre
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beaulivre.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beaulivre.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(colorist)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX class for typesetting books with a
colorful design. Currently, it has native support for Chinese (both
simplified and traditional), English, French, German, Italian, Japanese,
Portuguese (European and Brazilian), Russian and Spanish typesetting. It
compiles with either XeLaTeX or LuaLaTeX. This is part of the colorist
class series and depends on colorist.sty from the colorist package. The
package name "beaulivre" is taken from the French words "beau" (=
"beautiful") and "livre" (= "book").

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beaulivre
%dir %{_datadir}/texmf-dist/tex/latex/beaulivre
%doc %{_datadir}/texmf-dist/doc/latex/beaulivre/DEPENDS.txt
%doc %{_datadir}/texmf-dist/doc/latex/beaulivre/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/beaulivre/README.md
%{_datadir}/texmf-dist/tex/latex/beaulivre/beaulivre.cls
