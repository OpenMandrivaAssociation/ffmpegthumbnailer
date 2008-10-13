%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Lightweight video thumbnailer
Name:		ffmpegthumbnailer
Version:	1.3.0
Release:	%mkrel 2
License:	GPLv2+
Group:		Video
URL:		http://code.google.com/p/ffmpegthumbnailer/
Source0:	http://ffmpegthumbnailer.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires:	ffmpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This video thumbnailer can be used by file managers to 
create thumbnails for your video files. The thumbnailer 
uses ffmpeg to decode frames from the video files, so 
supported videoformats depend on the configuration 
flags of ffmpeg.

This thumbnailer was designed to be as fast and 
lightweight as possible.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		Video

%description -n %{libname}
Main library for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}

%makeinstall_std

rm -rf %{buildroot}%{_libdir}/libffmpegthumbnailer.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_bindir}/ffmpegthumbnailer
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
