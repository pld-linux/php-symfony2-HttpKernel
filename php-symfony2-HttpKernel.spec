%define		pearname	HttpKernel
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 HttpKernel Component
Name:		php-symfony2-HttpKernel
Version:	2.3.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	b3b1442b35d201cf9061f2f01e71dd29
URL:		http://symfony.com/doc/current/components/http_kernel/introduction.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-EventDispatcher
Requires:	php-symfony2-HttpFoundation
Suggests:	php-symfony2-BrowserKit
Suggests:	php-symfony2-ClassLoader
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-Console
Suggests:	php-symfony2-DependencyInjection
Suggests:	php-symfony2-Finder
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HttpKernel Component provides a structured process for converting
a Request into a Response by making use of the event dispatcher. It's
flexible enough to create a full-stack framework (Symfony), a
micro-framework (Silex) or an advanced CMS system (Drupal).

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/HttpKernel
%{php_pear_dir}/Symfony/Component/HttpKernel/*.php
%{php_pear_dir}/Symfony/Component/HttpKernel/Bundle
%{php_pear_dir}/Symfony/Component/HttpKernel/CacheClearer
%{php_pear_dir}/Symfony/Component/HttpKernel/CacheWarmer
%{php_pear_dir}/Symfony/Component/HttpKernel/Config
%{php_pear_dir}/Symfony/Component/HttpKernel/Controller
%{php_pear_dir}/Symfony/Component/HttpKernel/DataCollector
%{php_pear_dir}/Symfony/Component/HttpKernel/Debug
%{php_pear_dir}/Symfony/Component/HttpKernel/DependencyInjection
%{php_pear_dir}/Symfony/Component/HttpKernel/Event
%{php_pear_dir}/Symfony/Component/HttpKernel/EventListener
%{php_pear_dir}/Symfony/Component/HttpKernel/Exception
%{php_pear_dir}/Symfony/Component/HttpKernel/Fragment
%{php_pear_dir}/Symfony/Component/HttpKernel/HttpCache
%{php_pear_dir}/Symfony/Component/HttpKernel/Log
%{php_pear_dir}/Symfony/Component/HttpKernel/Profiler
