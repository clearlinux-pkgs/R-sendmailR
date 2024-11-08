#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sendmailR
Version  : 1.4.0
Release  : 48
URL      : https://cran.r-project.org/src/contrib/sendmailR_1.4-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sendmailR_1.4-0.tar.gz
Summary  : Send Email Using R
Group    : Development/Tools
License  : GPL-2.0
Requires: R-base64enc
BuildRequires : R-base64enc
BuildRequires : buildreq-R

%description
provides a portable solution for sending email, including file attachments and inline html reports, 
        from within R. SMTP Authentication and SSL/STARTTLS is implemented using curl.

%prep
%setup -q -n sendmailR
cd %{_builddir}/sendmailR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678833260

%install
export SOURCE_DATE_EPOCH=1678833260
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/sendmailR/Meta/vignette.rds
/usr/lib64/R/library/sendmailR/NAMESPACE
/usr/lib64/R/library/sendmailR/R/sendmailR
/usr/lib64/R/library/sendmailR/R/sendmailR.rdb
/usr/lib64/R/library/sendmailR/R/sendmailR.rdx
/usr/lib64/R/library/sendmailR/doc/index.html
/usr/lib64/R/library/sendmailR/doc/sending-html-reports.R
/usr/lib64/R/library/sendmailR/doc/sending-html-reports.Rmd
/usr/lib64/R/library/sendmailR/doc/sending-html-reports.html
/usr/lib64/R/library/sendmailR/help/AnIndex
/usr/lib64/R/library/sendmailR/help/aliases.rds
/usr/lib64/R/library/sendmailR/help/paths.rds
/usr/lib64/R/library/sendmailR/help/sendmailR.rdb
/usr/lib64/R/library/sendmailR/help/sendmailR.rdx
/usr/lib64/R/library/sendmailR/html/00Index.html
/usr/lib64/R/library/sendmailR/html/R.css
/usr/lib64/R/library/sendmailR/tests/multiple_recipients.R
