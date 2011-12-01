%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           pywebkitgtk
Version:        1.1.6
Release:        3%{?dist}
Summary:        Python Bindings for WebKit-gtk

Group:          Development/Languages
License:        LGPLv2+
URL:            http://code.google.com/p/pywebkitgtk/
Source0:        http://pywebkitgtk.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildArch:      
BuildRequires:  pygtk2-devel WebKit-gtk-devel >= 1.0.0-0.8 libxslt-devel
Requires:       pygtk2

%description
The purpose of pywebkitgtk is to bring an alternative web engine to
Python/GTK+ application developers who might need a web browser engine for
their next application or developers wishing to have a better browser engine
that they can access to using the Python programming language.

%prep
%setup -q
chmod -x demos/*

%build
%configure
make %{?_smp_mflags} PYGTK_CODEGEN=pygobject-codegen-2.0

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT \( -name \*.la -o -name \*.a \) -exec rm {} \;
cat > $RPM_BUILD_ROOT%{python_sitearch}/webkit-1.0.pth << EOF
webkit-1.0
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING MAINTAINERS NEWS README demos
%{_datadir}/pywebkitgtk/defs/webkit-*.defs
%{python_sitearch}/webkit-1.0
%{python_sitearch}/webkit-1.0.pth

%changelog
* Thu Jul  1 2010 Colin Walters <walters@redhat.com> - 1.1.6-3
- Fix license; it's really LGPL
- Resolves: #610238

* Fri Aug 28 2009 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.1.6-2
- Added .pth for webkit-1.0

* Wed Aug 26 2009 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.1.6-1
- Updated to 1.1.6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 08 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org>
- Rebuilt for soname bump for webkitgtk+

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec  5 2008 Jeremy Katz <katzj@redhat.com> - 1.0.1-4
- Fix build for python 2.6.  Patch matches what went upstream to 
  fix the same problem

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.1-3
- Rebuild for Python 2.6

* Thu Aug 28 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.0.1-2
- Switch to pygobject code generator

* Wed Aug 27 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 1.0.1-1
- Upstream update

* Fri May 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 0.3-0.2.git9824a495
- Fixed release scheme
- Fixed license tag
- Fixed ownership
- Removed .la files

* Wed Apr 23 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> 0.3-0.1.git9824a495
- Initial RPM release
