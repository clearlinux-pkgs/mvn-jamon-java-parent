#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jamon-java-parent
Version  : 2.4.1
Release  : 1
URL      : https://sourceforge.net/code-snapshots/svn/j/ja/jamon/code/jamon-code-r3129-releases-jamon-java-parent-jamon-java-parent-2.4.1.zip
Source0  : https://sourceforge.net/code-snapshots/svn/j/ja/jamon/code/jamon-code-r3129-releases-jamon-java-parent-jamon-java-parent-2.4.1.zip
Source1  : https://repo1.maven.org/maven2/org/jamon/jamon-java-parent/2.4.1/jamon-java-parent-2.4.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MPL-2.0
Requires: mvn-jamon-java-parent-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jamon-java-parent package.
Group: Data

%description data
data components for the mvn-jamon-java-parent package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jamon/jamon-java-parent/2.4.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/jamon/jamon-java-parent/2.4.1/jamon-java-parent-2.4.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/jamon/jamon-java-parent/2.4.1/jamon-java-parent-2.4.1.pom
