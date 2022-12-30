FROM python:3.9.13

WORKDIR /usr/src/app

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build

# hadolint ignore=DL3013

RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip uninstall pycurl && \
    python -m pip install pycurl --compile --global-option="--with-openssl" --no-cache-dir && \
    apt update && install -y sudo && apt install -y systemd && apt install -y vim


EXPOSE 8000

#RUN cp generic_celeryd /etc/init.d/celeryd && \
#    sudo chmod 755 /etc/init.d/celeryd && \
#    sudo chown root:root /etc/init.d/celeryd

CMD ["/bin/bash"]
