%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name chokidar

Summary:       A neat wrapper around node.js fs.watch / fs.watchFile / fsevents
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.4.1
Release:       7%{?dist}
License:       MIT
URL:           https://github.com/paulmillr/chokidar
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
A neat wrapper around node.js fs.watch / fs.watchFile / fsevents.

%prep
%setup -q -n package

%nodejs_fixdep inherits '2.0.0'
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
* Thu Feb 11 2016 Tomas Hrcka <thrcka@redhat.com> - 1.4.1-7
- Rebuilt 

* Fri Jan 29 2016 Tomas Hrcka <thrcka@redhat.com> - 1.4.1-4
- Enable scl macros

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 1.4.1-2
- Fix dependencies

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 1.4.1-1
- Initial package
