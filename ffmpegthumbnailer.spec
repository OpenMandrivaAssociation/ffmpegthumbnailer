Summary:	Lightweight video thumbnailer
Name:		ffmpegthumbnailer
Version:	1.1.4
Release:	%mkrel 2
License:	GPLv2+
Group:		Video
URL:		http://code.google.com/p/ffmpegthumbnailer/
Source0:	http://ffmpegthumbnailer.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires:	ffmpeg-devel
BuildRequires:	libpng-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This video thumbnailer can be used by file managers to 
create thumbnails for your video files. The thumbnailer 
uses ffmpeg to decode frames from the video files, so 
supported videoformats depend on the configuration 
flags of ffmpeg.

This thumbnailer was designed to be as fast and 
lightweight as possible.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_bindir}/ffmpegthumbnailer
