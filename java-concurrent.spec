%include	/usr/lib/rpm/macros.java
Summary:	Utility classes for concurrent Java programming
Summary(pl.UTF-8):	Klasy narzędziowe do programowania współbieżnego w Javie
Name:		concurrent
Version:	1.3.2
Release:	1
Epoch:		0
License:	Public Domain
Group:		Development/Languages/Java
Source0:	http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/current/%{name}.tar.gz
# Source0-md5:	6a7898a403c3c400f271c6e9285ce9a2
Source1:	%{name}-ant.xml
URL:		http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/util/concurrent/
BuildRequires:	ant
BuildRequires:	jpackage-utils >= 0:1.5
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides standardized, efficient versions of utility
classes commonly encountered in concurrent Java programming. This code
consists of implementations of ideas that have been around for ages,
and is merely intended to save you the trouble of coding them.
Discussions of the rationale and applications of several of these
classes can be found in the second edition of Concurrent Programming
in Java.

%description -l pl.UTF-8
Ten pakiet udostępnia ustandaryzowaną, wydajną wersję klas
narzędziowych zwykle spotykanych w programowaniu współbieżnym w Javie.
Ten kod składa się z implementacji idei, które istniały od wieków i ma
jedynie uchronić przed kodowaniem ich. Dyskusje o zasadności
stosowania niektórych z nich można znaleźć w drugim wydaniu pozycji
"Concurrent Programming in Java" (Programowanie współbieżne w Javie).

%package javadoc
Summary:	Javadoc for %{name}
Summary(pl.UTF-8):	Dokumentacja Javadoc dla pakietu %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Javadoc for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja Javadoc dla pakietu %{name}.

%prep
%setup -c -q
mkdir -p src/EDU/oswego/cs/dl/util
mv concurrent src/EDU/oswego/cs/dl/util
cp %{SOURCE1} build.xml

%build
%ant \
	-Dversion=%{version} \
	-Dj2se.apiurl=%{_javadocdir}/java \
	jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

cp -a docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/concurrent*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
