#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libplacebo
Version  : 1.18.0
Release  : 4
URL      : https://github.com/haasn/libplacebo/archive/v1.18.0.tar.gz
Source0  : https://github.com/haasn/libplacebo/archive/v1.18.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: libplacebo-lib = %{version}-%{release}
Requires: libplacebo-license = %{version}-%{release}
BuildRequires : SPIRV-Headers-dev
BuildRequires : SPIRV-Tools-dev
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : buildreq-meson
BuildRequires : glslang-dev
BuildRequires : glslang-staticdev
BuildRequires : lcms2-dev

%description
TA ("Tree Allocator") is a wrapper around malloc() and related functions,
adding features like automatically freeing sub-trees of memory allocations if
a parent allocation is freed.

%package dev
Summary: dev components for the libplacebo package.
Group: Development
Requires: libplacebo-lib = %{version}-%{release}
Provides: libplacebo-devel = %{version}-%{release}
Requires: libplacebo = %{version}-%{release}

%description dev
dev components for the libplacebo package.


%package lib
Summary: lib components for the libplacebo package.
Group: Libraries
Requires: libplacebo-license = %{version}-%{release}

%description lib
lib components for the libplacebo package.


%package license
Summary: license components for the libplacebo package.
Group: Default

%description license
license components for the libplacebo package.


%prep
%setup -q -n libplacebo-1.18.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567785898
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dvulkan=enabled \
-Dglslang=enabled \
-Dshaderc=disabled  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libplacebo
cp LICENSE %{buildroot}/usr/share/package-licenses/libplacebo/LICENSE
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libplacebo/colorspace.h
/usr/include/libplacebo/common.h
/usr/include/libplacebo/config.h
/usr/include/libplacebo/context.h
/usr/include/libplacebo/dispatch.h
/usr/include/libplacebo/dither.h
/usr/include/libplacebo/dummy.h
/usr/include/libplacebo/filters.h
/usr/include/libplacebo/gpu.h
/usr/include/libplacebo/renderer.h
/usr/include/libplacebo/shaders.h
/usr/include/libplacebo/shaders/av1.h
/usr/include/libplacebo/shaders/colorspace.h
/usr/include/libplacebo/shaders/sampling.h
/usr/include/libplacebo/swapchain.h
/usr/include/libplacebo/utils/upload.h
/usr/include/libplacebo/vulkan.h
/usr/lib64/libplacebo.so
/usr/lib64/pkgconfig/libplacebo.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libplacebo.so.18

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libplacebo/LICENSE
