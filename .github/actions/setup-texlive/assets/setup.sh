#!/usr/bin/env bash

export PATH="/usr/local/texlive/2021/bin/$(uname -m)-linux:$PATH"
export TEXLIVE_MIRROR="http://ctan.math.utah.edu/ctan/tex-archive/systems/texlive/tlnet"

# Install necessary system dependencies
apt-get update
apt-get -y install --no-install-recommends \
    build-essential \
    ca-certificates \
    tzdata          \
    gnupg           \
    cpanminus       \
    libc6-dev
apt-get autoremove -y
apt-get clean autoclean -y

# Install Texlive
mkdir /tmp/texlive
cd /tmp/texlive
wget -qO- "${TEXLIVE_MIRROR}/install-tl-unx.tar.gz" | tar -xz --strip-components=1
perl install-tl -profile texlive.profile --location $TEXLIVE_MIRROR
cpanm -n -q Log::Log4perl
cpanm -n -q XString
cpanm -n -q Log::Dispatch::File
cpanm -n -q YAML::Tiny
cpanm -n -q File::HomeDir
cpanm -n -q Unicode::GCString

# Install LaTeX packages
tlmgr update --self --all --reinstall-forcibly-removed
tlmgr install   \
    chktex      \
    comment     \
    enumitem    \
    latexindent \
    latexmk     \
    lastpage    \
    revtex      \
    textcase    \
    ulem        \
    xcolor
texhash 

# Clean up
rm -r /tmp/texlive

