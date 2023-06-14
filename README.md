# Openutau Manifests
resampler manifests for OpenUtau

## How to use
### import
* [download this repo](https://github.com/oxygen-dioxide/openutau-templates/archive/refs/heads/main.zip)
* Place all the .yaml files in the "Resamplers" folder of your OpenUtau installation.

### usage
* Open a project and select a resampler
* You can add all the flags at once in `Expressions -> Add all expressions suggested by renderers`.

<img width="453" alt="image" src="https://user-images.githubusercontent.com/54425948/227085816-4cced732-98dd-4c76-bc40-9a94f971a066.png">

## Note
* Corrupted flags between different resamplers aren't included currently. For example, the `A` flag changes volume of notes depending on pitch in moresampler and tn_fnds, but emphasizes high frequencies in f2resamp. So `A` isn't included in f2resamp.yaml

## Links
* [UTAU Flag guide](https://www.tumblr.com/utau-bowl/647016314853097472/utau-flag-guide?source=share) by Just UTAU Things
* [OpenUtau documentation for resampler manifests](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#resampler-manifest)
