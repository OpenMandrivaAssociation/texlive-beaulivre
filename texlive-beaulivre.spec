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
BuildSystem:	texlive
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

