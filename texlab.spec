Name: texlab
Version: 4.2.2
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
