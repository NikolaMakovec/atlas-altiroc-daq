##############################################################################
## This file is part of 'ATLAS ALTIROC DEV'.
## It is subject to the license terms in the LICENSE.txt file found in the 
## top-level directory of this distribution and at: 
##    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
## No part of 'ATLAS ALTIROC DEV', including this file, 
## may be copied, modified, propagated, or distributed except according to 
## the terms contained in the LICENSE.txt file.
##############################################################################

## Activate Rogue conda Environment
export alias fpga_aa=192.168.1.192
export alias fpga_ab=192.168.1.193
export alias fpga_ad=192.168.1.195
source /home/hgtd-lal/Documents/anaconda3/etc/profile.d/conda.sh
conda activate rogue_V3

# Python Package directories
export SURF_DIR=${PWD}/../firmware/submodules/surf/python

# Setup python path
export PYTHONPATH=${PWD}/python:${SURF_DIR}:${PYTHONPATH}
#export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.7/site-packages/

alias go="cd "$PWD