FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-21.04

ENV DEBIAN_FRONTEND="noninteractive"
ENV TEXLIVE_DOCFILES=0
ENV TEXLIVE_INSTALL_NO_CONTEXT_CACHE=1
ENV TEXLIVE_INSTALL_NO_WELCOME=1
ENV TEXLIVE_MIRROR=http://ctan.math.utah.edu/ctan/tex-archive/systems/texlive/tlnet
ENV TEXLIVE_SRCFILES=0
ENV TEXLIVE_SCHEME=scheme-basic
ENV TEXLIVE_VERSION=2021

RUN apt-get update \
    && apt-get -y install --no-install-recommends \
        build-essential ca-certificates tzdata wget curl fish gnupg cpanminus libc6-dev python3-pip \
    && apt-get autoremove -y \
    && apt-get clean autoclean -y \
    && rm -r /var/cache/* /var/lib/apt/lists/*

WORKDIR /tmp/texlive

RUN wget -qO- "${TEXLIVE_MIRROR}/install-tl-unx.tar.gz" | tar -xz --strip-components=1 \
    && touch profile.txt \
    && echo "selected_scheme ${TEXLIVE_SCHEME}" >> profile.txt \
    && echo "instopt_letter 0" >> profile.txt \
    && echo "tlpdbopt_autobackup 0" >> profile.txt \
    && echo "tlpdbopt_desktop_integration 0" >> profile.txt \
    && echo "tlpdbopt_file_assocs 0" >> profile.txt \
    && echo "tlpdbopt_install_docfiles ${TEXLIVE_DOCFILES}" >> profile.txt \
    && echo "tlpdbopt_install_srcfiles ${TEXLIVE_SRCFILES}" >> profile.txt \
    && perl install-tl -profile profile.txt --location "${TEXLIVE_MIRROR}" \
    && chown -R vscode:vscode /usr/local/texlive \
    && cd / \
    && rm -r /tmp/texlive 

RUN cpanm -n -q Log::Log4perl \
    && cpanm -n -q XString \
    && cpanm -n -q Log::Dispatch::File \
    && cpanm -n -q YAML::Tiny \
    && cpanm -n -q File::HomeDir \
    && cpanm -n -q Unicode::GCString

USER vscode

ENV HOME="/home/vscode"
ENV PATH="$HOME/.local/bin:$PATH"

WORKDIR $HOME

RUN export PATH="/usr/local/texlive/${TEXLIVE_VERSION}/bin/$(uname -m)-linux:$PATH" \
    && tlmgr update --self --all --reinstall-forcibly-removed \
    && tlmgr install \
        chktex comment enumitem latexindent latexmk lastpage revtex textcase ulem xcolor \
    && texhash

RUN pip3 install invoke==1.6.0

RUN echo "export PATH=\"/usr/local/texlive/${TEXLIVE_VERSION}/bin/$(uname -m)-linux:\$PATH\"" >> $HOME/.profile
