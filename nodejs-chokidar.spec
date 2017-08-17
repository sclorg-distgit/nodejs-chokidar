%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name chokidar

Summary:       A neat wrapper around node.js fs.watch / fs.watchFile / fsevents
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.6.1
Release:       2%{?dist}
License:       MIT
URL:           https://github.com/paulmillr/chokidar
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}runtime
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
A neat wrapper around node.js fs.watch / fs.watchFile / fsevents.

%prep
%setup -q -n package

%nodejs_fixdep inherits
%nodejs_fixdep async-each

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%doc CHANGELOG.md README.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.6.1-2
- rh-nodejs8 rebuild

* Mon Oct 31 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.6.1-1
- Updated with script

* Wed Apr 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.1-10
- Changed inherits fixdep

* Thu Mar 17 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.1-9
- Add nodejs-devel dependency

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.1-8
- Use proper macro in -runtime dependency

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.1-6
- Use proper macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.1-5
- rebuilt

* Fri Jan 29 2016 Tomas Hrcka <thrcka@redhat.com> - 1.4.1-4
- Enable scl macros

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 1.4.1-2
- Fix dependencies

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 1.4.1-1
- Initial package
