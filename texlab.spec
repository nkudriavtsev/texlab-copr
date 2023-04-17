Name: texlab
Version: 5.5.0
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
