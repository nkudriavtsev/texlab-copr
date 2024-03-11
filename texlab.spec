Name: texlab
Version: 5.13.0
Release: 1%{?dist}
Summary: texlab language server
License: GPL-3.0
URL: https://texlab.netlify.app/
Source0: https://github.com/latex-lsp/texlab/archive/v%{version}.tar.gz
BuildRequires: cargo
%if 0%{?fedora} >= 24
ExclusiveArch: x86_64 i686 armv7hl
%else
ExclusiveArch: x86_64 aarch64
%endif


%description
A cross-platform implementation of the Language Server Protocol
providing rich cross-editing support for the LaTeX typesetting system

# Disable debug info; texlab doesn't include debug info in release profile
%define debug_package %{nil}
%prep
%autosetup -v -n %{name}-%{version}


%build
cargo build --release


%install
install -D -p -s -m 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}


%check
cargo test


%files
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/%{name}

%changelog
* Mon Mar 11 2024 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.13.0-1
- Release 5.13.0
* Tue Feb 27 2024 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.12.4-1
- Release 5.12.4
* Mon Jan 29 2024 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.12.3-1
- Release 5.12.3
* Mon Jan 22 2024 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.12.2-1
- Release 5.12.2
* Mon Jan 08 2024 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.12.1-1
- Release 5.12.1
* Mon Dec 04 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.12.0-1
- Release 5.12.0
* Mon Nov 06 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.11.0-1
- Release 5.11.0
* Wed Oct 18 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.10.1-1
- Release 5.10.1
* Tue Oct 03 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.10.0-1
- Release 5.10.0
* Mon Aug 21 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.9.2-1
- Release 5.9.2
* Tue Aug 15 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.9.1-1
- Release 5.9.1
* Mon Aug 7 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.9.0-1
- Release 5.9.0
* Sun Aug 6 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.8.0-1
- Release 5.8.0
* Mon Jun 12 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.7.0-1
- Release 5.7.0
* Mon May 22 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.6.0-1
- Release 5.6.0
* Mon May 08 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.5.1-1
- Release 5.5.1
* Mon Apr 17 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.5.0-1
- Release 5.5.0
* Mon Mar 27 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.4.1-1
- Release 5.4.1
* Mon Mar 13 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.4.0-1
- Release 5.4.0
* Mon Feb 27 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.3.0-1
- Release 5.3.0
* Mon Jan 30 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.2.0-1
- Release 5.2.0
* Mon Jan 23 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.1.0-1
- Release 5.1.0
* Mon Jan 02 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 5.0.0-1
- Release 5.0.0
* Mon Nov 21 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 4.3.2-1
- Release 4.3.2
* Mon Oct 24 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 4.3.1-1
- Release 4.3.1
* Tue Sep 27 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 4.3.0-1
- Release 4.3.0
* Mon Aug 29 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 4.2.2-1
- Release 4.2.2
* Mon Aug 08 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 4.2.1-1
- Release 4.2.1
- Removed texlab.pdf and texlab.1
* Tue Jul 06 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 4.2.0-1
- Release 4.2.0
* Mon Jan 18 2021 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 2.2.2-1
- Release 2.2.2
- Initial spec file
