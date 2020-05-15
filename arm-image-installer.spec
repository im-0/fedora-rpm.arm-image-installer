# Tarfile created using git
# git clone https://pagure.io/arm-image-installer.git
# git archive --format=tar --prefix=%{name}-%{version}/ %{version} | xz > ~/%{name}-%{version}.tar.xz

Name:		arm-image-installer
Version:	2.17
Release:	1%{?dist}
Summary:	Writes binary image files to any specified block device
License:	GPLv2+
Url:		https://pagure.io/arm-image-installer

BuildArch:	noarch
Source0:	%{name}-%{version}.tar.xz

Obsoletes:	fedora-arm-installer < 2.5
Provides:	fedora-arm-installer < 2.5
Requires:	e2fsprogs
Requires:	parted
Requires:	sudo
Requires:	util-linux


%description
Allows one to first select a source image (local or remote). The image must be
a binary file containing: [MBR + Partitions + File Systems + Data]. A
destination block device should then be selected for final installation.


%prep
%autosetup

%build
echo "skipping..."

%install
install -d %{buildroot}%{_datadir}/arm-image-installer
install -d %{buildroot}%{_datadir}/arm-image-installer/socs.d
install -pm 644 socs.d/* %{buildroot}%{_datadir}/arm-image-installer/socs.d/
install -d %{buildroot}%{_datadir}/arm-image-installer/boards.d
install -pm 644 boards.d/* %{buildroot}%{_datadir}/arm-image-installer/boards.d/

install -d %{buildroot}%{_bindir}
install -pm 0755 update-uboot %{buildroot}%{_bindir}/
install -pm 0755 arm-image-installer %{buildroot}%{_bindir}/
install -pm 0755 rpi-uboot-update %{buildroot}%{_bindir}/
ln -s /usr/bin/arm-image-installer %{buildroot}%{_bindir}/fedora-arm-image-installer

%files
%license COPYING
%doc AUTHORS README TODO SUPPORTED-BOARDS
%{_bindir}/arm-image-installer
%{_bindir}/fedora-arm-image-installer
%{_bindir}/update-uboot
%{_bindir}/rpi-uboot-update
%{_datadir}/arm-image-installer/

%changelog
* Fri May 15 2020 Paul Whalen <pwhalen@fedoraproject.org> - 2.17-1
- Update to 2.17
- readd rpi-uboot-update

* Tue Apr 07 2020 Paul Whalen <pwhalen@fedoraproject.org> - 2.16-1
- Update to 2.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Paul Whalen <pwhalen@fedoraproject.org> - 2.15-1
- Update to 2.15

* Thu Dec 19 2019 Paul Whalen <pwhalen@fedoraproject.org> - 2.14-1
- Update to 2.14

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Paul Whalen <pwhalen@fedoraproject.org> - 2.13-1
- Update to 2.13
- Fix BZ#1655329, BZ#1692903

* Tue Apr 09 2019 Paul Whalen <pwhalen@fedoraproject.org> - 2.11-1
- Update to 2.11

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Paul Whalen <pwhalen@fedoraproject.org> - 2.10-1
- Update to 2.10

* Sat Dec 01 2018 Paul Whalen <pwhalen@fedoraproject.org> - 2.9-1
- Update to 2.9

* Tue Oct 09 2018 Paul Whalen <pwhalen@redhat.com> - 2.8-1
- Update to 2.8

* Tue Aug 28 2018 Paul Whalen <pwhalen@redhat.com> - 2.7-1
- Update to 2.7

* Tue Aug 28 2018 Paul Whalen <pwhalen@redhat.com> - 2.6-1
- Update to 2.6

* Tue Jul 10 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.5-1
- Update to 2.5
- Package rename with obsolete/provides

* Fri Jun 01 2018 Paul Whalen <pwhalen@redhat.com> - 2.4-1
- Update to 2.4
- Add initial IoT disk image support
- Add lvm support

* Mon May 28 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.3-1
- Update to 2.3

* Thu Apr 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.2-1
- Update to 2.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 2.1-1
- Update to 2.1

* Thu Nov 23 2017 Peter Robinson <pbrobinson@fedoraproject.org> 2.0-1
- Update to 2.0
- Initial support for aarch64 images and associated SBCs

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.16-1
- Update to 1.99.16

* Wed May  3 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.15-1
- Update to 1.99.15

* Fri Apr 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.14-1
- Update to 1.99.14

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.13-1
- Update to 1.99.13
- Add basic Raspberry Pi firmware upgrade script

* Wed Sep 21 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.12-1
- Update to 1.99.12

* Mon Aug 22 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.11-1
- Update to 1.99.11

* Wed Aug 17 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.10-1
- Update to 1.99.10
- Added numerous boards

* Tue Jun 21 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.9-2
- Require sudo

* Wed May 18 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.9-1
- Update to 1.99.9
- Support for ClearFog

* Mon Mar  7 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.8-1
- Update to 1.99.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.7-1
- Minor updates

* Mon Jan 18 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.6-2
- Fix directory of data location

* Mon Jan 18 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.6-1
- Update to 1.99.6
- Rename binary to arm-image-installer, add compat symlink

* Sun Aug  2 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.5-1
- Update to 1.99.5

* Fri Jul 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.4-1
- Update to 1.99.4

* Fri Jul  3 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.3-1
- Update to 1.99.3 for u-boot 2015.07 support

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.2-1
- Update to 1.99.2

* Wed Mar 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.99.1-0.1
- Update to new upstream
