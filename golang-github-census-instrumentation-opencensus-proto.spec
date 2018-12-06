# Run tests in check section
%bcond_without check

# https://github.com/census-instrumentation/opencensus-proto
%global goipath         github.com/census-instrumentation/opencensus-proto
Version:                0.1.0

%global common_description %{expand:
Census provides a framework to define and collect stats against metrics and 
to break those stats down across user-defined dimensions.

The Census framework is natively available in many languages (e.g. C++, Go, 
and Java). The API interface types are defined using protos to ensure 
consistency and interoperability for the different implementations.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Language Independent Interface Types For OpenCensus
# Detected licences
# - *No copyright* Apache License (v2.0) at 'LICENSE'
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/grpc)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc AUTHORS README.md CONTRIBUTING.md RELEASING.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- First package for Fedora

