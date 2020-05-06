%define		package	HttpKernel
%define		php_min_version 5.3.9
Summary:	Symfony2 HttpKernel Component
Name:		php-symfony2-HttpKernel
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	c10b900ef39d415dec96069555a67a13
URL:		https://symfony.com/doc/2.8/components/http_kernel.htmlintroduction.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(session)
Requires:	php(spl)
Requires:	php(tokenizer)
Requires:	php-dirs >= 1.6
Requires:	php-psr-Log >= 1.0
Requires:	php-symfony2-Debug >= 2.6.2
Requires:	php-symfony2-EventDispatcher >= 2.6.7
Requires:	php-symfony2-HttpFoundation >= 2.5.4
Suggests:	php-symfony2-BrowserKit
Suggests:	php-symfony2-ClassLoader
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-Console
Suggests:	php-symfony2-DependencyInjection
Suggests:	php-symfony2-Finder
#Suggests:	php-symfony2-VarDumper
Conflicts:	php-symfony2-Config < 2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HttpKernel Component provides a structured process for converting
a Request into a Response by making use of the event dispatcher. It's
flexible enough to create a full-stack framework (Symfony), a
micro-framework (Silex) or an advanced CMS system (Drupal).

%prep
%setup -q -n http-kernel-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/HttpKernel
%{php_data_dir}/Symfony/Component/HttpKernel/*.php
%{php_data_dir}/Symfony/Component/HttpKernel/Bundle
%{php_data_dir}/Symfony/Component/HttpKernel/CacheClearer
%{php_data_dir}/Symfony/Component/HttpKernel/CacheWarmer
%{php_data_dir}/Symfony/Component/HttpKernel/Config
%{php_data_dir}/Symfony/Component/HttpKernel/Controller
%{php_data_dir}/Symfony/Component/HttpKernel/DataCollector
%{php_data_dir}/Symfony/Component/HttpKernel/Debug
%{php_data_dir}/Symfony/Component/HttpKernel/DependencyInjection
%{php_data_dir}/Symfony/Component/HttpKernel/Event
%{php_data_dir}/Symfony/Component/HttpKernel/EventListener
%{php_data_dir}/Symfony/Component/HttpKernel/Exception
%{php_data_dir}/Symfony/Component/HttpKernel/Fragment
%{php_data_dir}/Symfony/Component/HttpKernel/HttpCache
%{php_data_dir}/Symfony/Component/HttpKernel/Log
%{php_data_dir}/Symfony/Component/HttpKernel/Profiler
