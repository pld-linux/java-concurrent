%include	/usr/lib/rpm/macros.java
Summary:	Utility classes for concurrent Java programming
Name:		concurrent
Version:	1.3.2
Release:	0.1
Epoch:		0
License:	Public domain
Source0:	http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/current/%{name}.tar.gz
# Source0-md5:	6a7898a403c3c400f271c6e9285ce9a2
Source1:	%{name}-ant.xml
Group:		Development/Languages/Java
URL:		http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/util/concurrent/
BuildRequires:	ant
BuildRequires:	jpackage-utils >= 0:1.5
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
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

%package javadoc
Summary:	Javadoc for %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Javadoc for %{name}.

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
install %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}
