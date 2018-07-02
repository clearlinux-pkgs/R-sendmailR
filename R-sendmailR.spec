#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sendmailR
Version  : 1.2.1
Release  : 4
URL      : https://cran.r-project.org/src/contrib/sendmailR_1.2-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sendmailR_1.2-1.tar.gz
Summary  : send email using R
Group    : Development/Tools
License  : GPL-2.0
Requires: R-base64enc
BuildRequires : R-base64enc
BuildRequires : clr-R-helpers

%description
portable solution for sending email, including attachment, from
        within R.

%prep
%setup -q -c -n sendmailR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530440722

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530440722
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sendmailR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sendmailR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sendmailR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library sendmailR|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sendmailR/DESCRIPTION
/usr/lib64/R/library/sendmailR/INDEX
/usr/lib64/R/library/sendmailR/Meta/Rd.rds
/usr/lib64/R/library/sendmailR/Meta/features.rds
/usr/lib64/R/library/sendmailR/Meta/hsearch.rds
/usr/lib64/R/library/sendmailR/Meta/links.rds
/usr/lib64/R/library/sendmailR/Meta/nsInfo.rds
/usr/lib64/R/library/sendmailR/Meta/package.rds
/usr/lib64/R/library/sendmailR/NAMESPACE
/usr/lib64/R/library/sendmailR/R/sendmailR
/usr/lib64/R/library/sendmailR/R/sendmailR.rdb
/usr/lib64/R/library/sendmailR/R/sendmailR.rdx
/usr/lib64/R/library/sendmailR/help/AnIndex
/usr/lib64/R/library/sendmailR/help/aliases.rds
/usr/lib64/R/library/sendmailR/help/paths.rds
/usr/lib64/R/library/sendmailR/help/sendmailR.rdb
/usr/lib64/R/library/sendmailR/help/sendmailR.rdx
/usr/lib64/R/library/sendmailR/html/00Index.html
/usr/lib64/R/library/sendmailR/html/R.css
