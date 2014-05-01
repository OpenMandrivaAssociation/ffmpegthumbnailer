%define major 4
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Lightweight video thumbnailer
Name:		ffmpegthumbnailer
Version:	2.0.8
Release:	5
License:	GPLv2+
Group:		Video
Url:		http://code.google.com/p/ffmpegthumbnailer/
Source0:	http://ffmpegthumbnailer.googlecode.com/files/%{name}-%{version}.tar.gz
Patch1:		ffmpegthumbnailer-2.0.8-libpng-1.6.patch
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	jpeg-devel

%description
This video thumbnailer can be used by file managers to create thumbnails for
your video files. The thumbnailer uses ffmpeg to decode frames from the video
files, so supported videoformats depend on the configuration flags of ffmpeg.

This thumbnailer was designed to be as fast and lightweight as possible.

%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/ffmpegthumbnailer
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		Video

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%doc AUTHORS ChangeLog README TODO
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
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

