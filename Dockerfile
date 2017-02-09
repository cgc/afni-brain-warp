FROM miykael/nipype_advanced
MAINTAINER Carlos Correa <cgc@stanford.edu>

# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}
WORKDIR ${FLYWHEEL}

RUN env -u HOSTNAME -u PWD > environment.sh

COPY run manifest.json align.csh ${FLYWHEEL}/

CMD ["/flywheel/v0/run"]
