Name:           ooparse
Version:        0.1.0
Release:        1%{?dist}
Summary:        General purpose parser generating AST graphs from custom grammar expressions.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooparse
Source0:        ooparse-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooparse is a sovereign, capability-bounded LEXER & PARSER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooparse
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooparse-uninstall

%files
/usr/bin/ooparse
/usr/bin/ooparse-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
