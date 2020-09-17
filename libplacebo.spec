#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libplacebo
Version  : 2.72
Release  : 13
URL      : file:///insilications/build/clearlinux/packages/libplacebo/libplacebo-v2.72.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/libplacebo/libplacebo-v2.72.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1+
BuildRequires : Mako
BuildRequires : Mako-python3
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : asciidoctor
BuildRequires : buildreq-meson
BuildRequires : findutils
BuildRequires : gcc-dev
BuildRequires : gcc-libs-math
BuildRequires : lcms2-dev
BuildRequires : lcms2-staticdev
BuildRequires : libepoxy-dev
BuildRequires : libepoxy-staticdev
BuildRequires : pkgconfig(SPIRV-Tools)
BuildRequires : pkgconfig(SPIRV-Tools-shared)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(shaderc)
BuildRequires : pkgconfig(shaderc_combined)
BuildRequires : pkgconfig(shaderc_static)
BuildRequires : pkgconfig(vulkan)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : shaderc
BuildRequires : shaderc-dev
BuildRequires : shaderc-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-revision.h-requirement.patch
Patch2: 0002-Build-for-shaderc_combined.patch

%description
TA ("Tree Allocator") is a wrapper around malloc() and related functions,
adding features like automatically freeing sub-trees of memory allocations if
a parent allocation is freed.

%package dev
Summary: dev components for the libplacebo package.
Group: Development
Provides: libplacebo-devel = %{version}-%{release}
Requires: libplacebo = %{version}-%{release}

%description dev
dev components for the libplacebo package.


%package staticdev
Summary: staticdev components for the libplacebo package.
Group: Default
Requires: libplacebo-dev = %{version}-%{release}

%description staticdev
staticdev components for the libplacebo package.


%prep
%setup -q -n libplacebo
cd %{_builddir}/libplacebo
%patch1 -p1
%patch2 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600372366
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects -fPIC -ffat-lto-objects $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects -fPIC -ffat-lto-objects $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects -fPIC -ffat-lto-objects $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -fPIC -ffat-lto-objects -fPIC -ffat-lto-objects $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC -ffat-lto-objects -fPIC -ffat-lto-objects -Wl,-Bdynamic -L/usr/lib64 -pthread -lpthread -lrt -lc -ldl -lgcc -lgcc_s -lstdc++ -lmvec -lm $PGO_GEN"
## pgo use
## -ffat-lto-objectsts -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects -fPIC -ffat-lto-objects $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects -fPIC -ffat-lto-objects $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects -fPIC -ffat-lto-objects $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC -ffat-lto-objects -fPIC -ffat-lto-objects $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -ffat-lto-objects -fPIC -ffat-lto-objects -Wl,-Bdynamic -L/usr/lib64 -pthread -lpthread -lrt -lc -ldl -lgcc -lgcc_s -lstdc++ -lmvec -lm $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
# -Dcpp_args=-I/usr/include/glslang
## altflags_pgo end
##
%define _lto_cflags 1
##
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dvulkan=enabled -Dopengl=enabled -Dglslang=disabled -Dshaderc=enabled -Ddefault_library=static -Db_lto=true -Dlcms=enabled -Dtests=true  builddir
ninja -v -C builddir

meson test -C builddir
find builddir/ -type f,l -not -name '*.gcno' -delete -print
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dvulkan=enabled -Dopengl=enabled -Dglslang=disabled -Dshaderc=enabled -Ddefault_library=static -Db_lto=true -Dlcms=enabled -Dtests=true  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
meson test -C builddir

%install
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
/usr/include/libplacebo/opengl.h
/usr/include/libplacebo/renderer.h
/usr/include/libplacebo/shaders.h
/usr/include/libplacebo/shaders/av1.h
/usr/include/libplacebo/shaders/colorspace.h
/usr/include/libplacebo/shaders/custom.h
/usr/include/libplacebo/shaders/sampling.h
/usr/include/libplacebo/swapchain.h
/usr/include/libplacebo/utils/upload.h
/usr/include/libplacebo/vulkan.h
/usr/lib64/pkgconfig/libplacebo.pc

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libplacebo.a
