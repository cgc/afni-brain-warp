FROM miykael/nipype_advanced
MAINTAINER Carlos Correa <cgc@stanford.edu>

# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}
WORKDIR ${FLYWHEEL}

COPY run manifest.json align.csh run ${FLYWHEEL}/
ADD https://raw.githubusercontent.com/scitran/utilities/11b8fca/metadata_from_gear_output.py ${FLYWHEEL}/
RUN chmod +x ${FLYWHEEL}/metadata_from_gear_output.py

ENTRYPOINT ["/flywheel/v0/run"]
