Name:		texlive-expkv-cs
Version:	62003
Release:	2
Summary:	Define expandable key=val macros using expkv
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/expkv-cs
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv-cs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv-cs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv-cs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is a frontend to define expandable macros with
key=val arguments. It provides four syntaxes, each of which
will define <cs> to take a single key=val argument:
ekvcSplit<cs>{<key>=<initial>, ...}{<definition>}
ekvcSplitAndForward<cs><cs2>{<key>=<initial>, ...}
ekvcHash<cs>{<key>=<initial>, ...}{<definition>}
ekvcHashAndForward<cs><cs2>{<key>=<initial>, ...} Additional
keys for each <cs> might be defined using
ekvcSecondaryKeys<cs>{<prefix> <key>=<definition>, ...}
expkv-cs is generic code and only requires expkv for its
parsing. A LaTeX package expkv-cs.sty is included to play
nicely on LaTeX's package loading system, but that package is
not needed and does not provide more functionality than the
generic code in expkv-cs.tex. Note: In this context, "cs"
stands for "control sequence" (i.e.: macro).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/expkv-cs
%{_texmfdistdir}/tex/latex/expkv-cs
%{_texmfdistdir}/tex/generic/expkv-cs
%{_texmfdistdir}/tex/context/third/expkv-cs
%doc %{_texmfdistdir}/doc/latex/expkv-cs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
