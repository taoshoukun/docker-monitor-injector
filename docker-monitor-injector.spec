Name: docker-monitor-injector
Version: 0.1.0
Release: 1
Summary: docker-monitor-injector
URL: http://www.weidian.com
Group: vdian/common
License: weidian
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define inject_so inject.so
%define injector_sh injector.sh

%description 
docker monitor injector

%build 
cd %{name}-%{version}
make

%install
rm -rf %{buildroot}
#mkdir -p %{buildroot}/etc/profile.d/
mkdir -p %{buildroot}/usr/lib/

#install -p -D -m 0755  %{name}-%{version}/%{injector_sh} %{buildroot}/etc/profile.d/%{injector_sh}
install -p -D  %{name}-%{version}/%{inject_so} %{buildroot}/usr/lib/%{inject_so}


%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}


%post
echo "/usr/lib/inject.so" >>/etc/ld.so.preload
%preun
sed -i '/inject.so/d' /etc/ld.so.preload

%files
#%attr(755,root,root) %dir /etc/profile.d/%{injector_sh}
%attr(755,root,root) %dir /usr/lib/%{inject_so}



%changelog
* Mon Sep 19 2016 Chentairan <taoshoukun@weidian.com>
- first commit
