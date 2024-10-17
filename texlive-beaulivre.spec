Name:		texlive-beaulivre
Version:	70050
Release:	1
Summary:	Write your books in a colorful way
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beaulivre
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beaulivre.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beaulivre.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class for typesetting books with
a colorful design. Currently, it has native support for Chinese
(both simplified and traditional), English, French, German,
Italian, Japanese, Portuguese (European and Brazilian), Russian
and Spanish typesetting. It compiles with either XeLaTeX or
LuaLaTeX. This is part of the colorist class series and depends
on colorist.sty from the colorist package. The package name
"beaulivre" is taken from the French words "beau" (=
"beautiful") and "livre" (= "book").

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beaulivre
%doc %{_texmfdistdir}/doc/latex/beaulivre

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
