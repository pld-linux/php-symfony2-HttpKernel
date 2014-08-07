%define		pearname	HttpKernel
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 HttpKernel Component
Name:		php-symfony2-HttpKernel
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	d808e3c915adace99d6dcbc9cd2f1eae
URL:		http://symfony.com/doc/2.4/components/http_kernel/introduction.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(session)
Requires:	php(spl)
Requires:	php(tokenizer)
Requires:	php-pear >= 4:1.3.10
Requires:	php-psr-Log >= 1.0
Requires:	php-symfony2-Debug >= 2.3
Requires:	php-symfony2-EventDispatcher >= 2.1
Requires:	php-symfony2-HttpFoundation >= 2.2
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
%setup -q -n %{pearname}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
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
