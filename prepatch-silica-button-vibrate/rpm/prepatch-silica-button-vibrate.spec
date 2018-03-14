Name:       prepatch-silica-button-vibrate

BuildArch: noarch

Summary:    A prepatch patch which makes silica-buttons and icon-buttons vibrate when touched or released.
Version:    0.1.1
Release:    1
Group:      Qt/Qt
License:    Other
Source0:    %{name}-%{version}.tar.bz2
Requires:   patch prepatch

%description
A prepatch patch which makes silica-buttons and icon-buttons vibrate when touched or released.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/prepatch
cp -r 050-prepatch-silica-button-vibrate %{buildroot}/usr/share/prepatch

%pre

%preun

%files
%defattr(-,root,root,-)
%{_datadir}/prepatch/050-prepatch-silica-button-vibrate
