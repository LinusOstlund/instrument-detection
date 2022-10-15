# VGGish

VGGish are features from a pretrained CNN by Google ([research paper](https://arxiv.org/pdf/1609.09430.pdf)). Apple has a nice [comprehensible explanation](https://apple.github.io/turicreate/docs/userguide/sound_classifier/how-it-works.html). 

They benchmark their approach against [*Audio Set*](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45857.pdf) (obs innehåller även djurljud!). It seems to be just tags to YouTube videos?

* **AED**: Acoustic Event Detection
* **VGGish**: Seem to be feature from a pretrained CNN? Not sure, but [link to repo here](https://github.com/tensorflow/models/tree/master/research/audioset/vggish)

# Where do I find the code?
Currently working on data preprocessing in [data.ipynb](/src/data.ipynb).

# How to run

1. Download the [OpenMIC-2018 dataset](https://zenodo.org/record/1432913#.Y0rtuOxBw-Q) and add as a subfolder to `data` (`data/openmic-2018/all/goes/here`)
2. Make sure you have Docker up and running, and open the project in Visual Studio Code.
3. VSC *should* prompt for `Open project in .devcontainer?`
4. Accept.