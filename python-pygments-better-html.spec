Name:           python-pygments-better-html
Version:        0.1.4
Release:        1%{?dist}
Summary:        Better line numbers for Pygments HTML

License:        BSD
URL:            https://github.com/Kwpolska/pygments_better_html
Source0:        %{pypi_source pygments_better_html}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This library provides improved line numbers for the Pygments HTML formatter.
}

%description %_description

%package -n python3-pygments-better-html
Summary: %{summary}

%description -n python3-pygments-better-html %_description

%prep
%autosetup -p1 -n pygments_better_html-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pygments_better_html

%check
%pyproject_check_import

%files -n python3-pygments-better-html -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Mon Feb 21 2022 supakeen <cmdr@supakeen.com> - 0.1.4-1
- Initial version of the package.
