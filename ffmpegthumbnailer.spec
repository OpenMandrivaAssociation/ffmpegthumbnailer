%define major 4
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Lightweight video thumbnailer
Name:		ffmpegthumbnailer
Version:	2.2.3
Release:	4
License:	GPLv2+
Group:		Video
Url:		https://github.com/dirkvdb/ffmpegthumbnailer
Source0:	https://github.com/dirkvdb/ffmpegthumbnailer/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         newest-ffmpeg.patch

BuildSystem:    cmake
BuildOption:    -DENABLE_STATIC:BOOL=OFF
BuildOption:    -DENABLE_GIO:BOOL=ON
BuildOption:    -DENABLE_THUMBNAILER:BOOL=ON

BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	jpeg-devel
Requires:	%{libname} = %{EVRD}

%description
This video thumbnailer can be used by file managers to create thumbnails for
your video files. The thumbnailer uses ffmpeg to decode frames from the video
files, so supported videoformats depend on the configuration flags of ffmpeg.

This thumbnailer was designed to be as fast and lightweight as possible.

%files
%{_bindir}/%{name}
%{_datadir}/thumbnailers/ffmpegthumbnailer.thumbnailer
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		Video

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%{_libdir}/libffmpegthumbnailer.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%doc AUTHORS ChangeLog README TODO
%{_libdir}/libffmpegthumbnailer.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

