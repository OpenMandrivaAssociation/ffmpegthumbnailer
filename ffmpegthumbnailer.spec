%define major 4
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Lightweight video thumbnailer
Name:		ffmpegthumbnailer
Version:	2.1.0
Release:	1
License:	GPLv2+
Group:		Video
Url:		https://github.com/dirkvdb/ffmpegthumbnailer
Source0:	https://github.com/dirkvdb/ffmpegthumbnailer/releases/download/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	jpeg-devel
BuildRequires:	cmake >= 2.8
Requires:	%{libname} = %{EVRD}

%description
This video thumbnailer can be used by file managers to create thumbnails for
your video files. The thumbnailer uses ffmpeg to decode frames from the video
files, so supported videoformats depend on the configuration flags of ffmpeg.

This thumbnailer was designed to be as fast and lightweight as possible.

%files
%{_bindir}/%{name}
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

%prep
%setup -q
chmod 644 AUTHORS ChangeLog README TODO

%build
%cmake \
     -DENABLE_STATIC:BOOL=OFF \
     -DENABLE_GIO:BOOL=ON \
     -DENABLE_THUMBNAILER:BOOL=ON

%make

%install
%makeinstall_std -C build

