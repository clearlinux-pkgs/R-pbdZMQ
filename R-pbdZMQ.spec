#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pbdZMQ
Version  : 0.3.3
Release  : 29
URL      : https://cran.r-project.org/src/contrib/pbdZMQ_0.3-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pbdZMQ_0.3-3.tar.gz
Summary  : Programming with Big Data -- Interface to 'ZeroMQ'
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: R-pbdZMQ-lib
BuildRequires : clr-R-helpers
BuildRequires : libzmq-dev
BuildRequires : pkgconfig(libunwind)
BuildRequires : sed

%description
asynchronous messaging in scalable, distributed applications.  This
    package provides high level R wrapper functions to easily utilize
    'ZeroMQ'. We mainly focus on interactive client/server programming
    frameworks. For convenience, a minimal 'ZeroMQ' library (4.2.2)
    is shipped with 'pbdZMQ', which can be used if no system installation
    of 'ZeroMQ' is available.  A few wrapper functions compatible with
    'rzmq' are also provided.

%package lib
Summary: lib components for the R-pbdZMQ package.
Group: Libraries

%description lib
lib components for the R-pbdZMQ package.


%prep
%setup -q -c -n pbdZMQ

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526838400

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1526838400
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbdZMQ
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbdZMQ
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbdZMQ
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pbdZMQ|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pbdZMQ/CITATION
/usr/lib64/R/library/pbdZMQ/DESCRIPTION
/usr/lib64/R/library/pbdZMQ/INDEX
/usr/lib64/R/library/pbdZMQ/Meta/Rd.rds
/usr/lib64/R/library/pbdZMQ/Meta/demo.rds
/usr/lib64/R/library/pbdZMQ/Meta/features.rds
/usr/lib64/R/library/pbdZMQ/Meta/hsearch.rds
/usr/lib64/R/library/pbdZMQ/Meta/links.rds
/usr/lib64/R/library/pbdZMQ/Meta/nsInfo.rds
/usr/lib64/R/library/pbdZMQ/Meta/package.rds
/usr/lib64/R/library/pbdZMQ/Meta/vignette.rds
/usr/lib64/R/library/pbdZMQ/NAMESPACE
/usr/lib64/R/library/pbdZMQ/R/pbdZMQ
/usr/lib64/R/library/pbdZMQ/R/pbdZMQ.rdb
/usr/lib64/R/library/pbdZMQ/R/pbdZMQ.rdx
/usr/lib64/R/library/pbdZMQ/demo/check_eintr.r
/usr/lib64/R/library/pbdZMQ/demo/hwclient.r
/usr/lib64/R/library/pbdZMQ/demo/hwserver.r
/usr/lib64/R/library/pbdZMQ/demo/iter_next.r
/usr/lib64/R/library/pbdZMQ/demo/iter_try.r
/usr/lib64/R/library/pbdZMQ/demo/mpclient.r
/usr/lib64/R/library/pbdZMQ/demo/mpserver.r
/usr/lib64/R/library/pbdZMQ/demo/mspoller.r
/usr/lib64/R/library/pbdZMQ/demo/msreader.r
/usr/lib64/R/library/pbdZMQ/demo/tasksink.r
/usr/lib64/R/library/pbdZMQ/demo/taskvent.r
/usr/lib64/R/library/pbdZMQ/demo/taskwork.r
/usr/lib64/R/library/pbdZMQ/demo/wuclient.r
/usr/lib64/R/library/pbdZMQ/demo/wuserver.r
/usr/lib64/R/library/pbdZMQ/doc/index.html
/usr/lib64/R/library/pbdZMQ/doc/pbdZMQ-guide.Rnw
/usr/lib64/R/library/pbdZMQ/doc/pbdZMQ-guide.pdf
/usr/lib64/R/library/pbdZMQ/etc/Makeconf
/usr/lib64/R/library/pbdZMQ/examples/README
/usr/lib64/R/library/pbdZMQ/examples/reqrep/client.r
/usr/lib64/R/library/pbdZMQ/examples/reqrep/rzmq_client.r
/usr/lib64/R/library/pbdZMQ/examples/reqrep/rzmq_server.r
/usr/lib64/R/library/pbdZMQ/examples/reqrep/server.r
/usr/lib64/R/library/pbdZMQ/help/AnIndex
/usr/lib64/R/library/pbdZMQ/help/aliases.rds
/usr/lib64/R/library/pbdZMQ/help/paths.rds
/usr/lib64/R/library/pbdZMQ/help/pbdZMQ.rdb
/usr/lib64/R/library/pbdZMQ/help/pbdZMQ.rdx
/usr/lib64/R/library/pbdZMQ/html/00Index.html
/usr/lib64/R/library/pbdZMQ/html/R.css
/usr/lib64/R/library/pbdZMQ/libs/symbols.rds
/usr/lib64/R/library/pbdZMQ/zmq_copyright/AUTHORS
/usr/lib64/R/library/pbdZMQ/zmq_copyright/COPYING
/usr/lib64/R/library/pbdZMQ/zmq_copyright/COPYING.LESSER

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pbdZMQ/libs/pbdZMQ.so
/usr/lib64/R/library/pbdZMQ/libs/pbdZMQ.so.avx2
/usr/lib64/R/library/pbdZMQ/libs/pbdZMQ.so.avx512
