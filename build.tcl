#!/usr/bin/tclsh

package require http

set arch "x86_64"
set base "0.4.9"

if {[file exists trofs$base.tar.gz]==0} {
    puts "Dowonload file..."
    set f [open trofs$base.tar.gz {WRONLY CREAT EXCL}]
    set token [http::geturl http://math.nist.gov/~DPorter/tcltk/trofs/trofs$base.tar.gz -channel $f]
    http::cleanup $token
    close $f
    puts "Done."
}

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force trofs$base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb trofs.spec]
exec >@stdout 2>@stderr {*}$buildit

file delete trofs$base.tar.gz

