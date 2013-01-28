%define major 4
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Lightweight video thumbnailer
Name:		ffmpegthumbnailer
Version:	2.0.8
Release:	3
License:	GPLv2+
Group:		Video
URL:		http://code.google.com/p/ffmpegthumbnailer/
Source0:		http://ffmpegthumbnailer.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	libjpeg-devel
Requires:	%{libname} = %{version}-%{release}

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
Obsoletes:	%{mklibname %{name} 2}

%description -n %{libname}
Main library for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for %{name}.

%prep
%setup -q
%__chmod 644 AUTHORS ChangeLog README TODO

%build
%configure2_5x \
	--disable-static 
	
%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_libdir}/libffmpegthumbnailer.la


%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/ffmpegthumbnailer
%{_mandir}/man1/*

%files -n %{libname}
%doc AUTHORS ChangeLog README TODO
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog README TODO
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc



