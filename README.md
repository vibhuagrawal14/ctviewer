
<p align="center">
  
  <img width="600" src="https://i.imgur.com/6R6WsaM.png"/>
  <br>
  <strong>View volumetric (3D) medical images in Jupyter notebooks</strong>
  <br>
  <a href="https://badge.fury.io/py/ctviewer"><img src="https://badge.fury.io/py/ctviewer.svg" alt="PyPI version" height="18"></a>
  
</p>

# CTViewer

This tiny, but very useful utility enables interactive slice-by-slice viewing of 3D images in ipython notebooks. It builds upon [ImageSliceViewer3D](https://github.com/mohakpatel/ImageSliceViewer3D/) and is specifically designed for viewing CT images. Key features:
- Change orientation of 3D images to view them along any of the three possible axes
- Window CT images. All major presets for window level and window width provided. See the table below for the complete list of presets
- Window CT images using custom values for window level and window width


## Installation 

CTViewer can be installed from PyPI with the following command:

```bash 
  pip install ctviewer
```

## Usage

CTViewer takes as input a 3-dimensional numpy array. For windowing to work as intended, the voxel values should be in [Hounsfield Units (HU)](https://en.wikipedia.org/wiki/Hounsfield_scale). Typical usage:

```python
  from ctviewer import CTViewer
  # assuming that volumetric_image is the 3-dimensional numpy array
  CTViewer(volumetric_image)
```

For a more detailed example of loading a stack of dicom images from disk, converting to HU, and then viewing using CTViewer, check the `sample_run.ipynb` inside the `examples` folder

## Windowing

The following windows are available as presets, along with custom inputs for window level and window width:

| Window Name | Window Level | Window Width |
|-------------|--------------|--------------|
| Bone        | 500          | 2000         |
| Lung        | -600         | 1600         |
| Abdomen     | 40           | 400          |
| Brain       | 30           | 70           |
| Soft Tissue | 50           | 350          |
| Liver       | 60           | 160          |
| Mediastinum | 50           | 500          |
| Stroke      | 30           | 30           |
| CTA         | 170          | 600          |  

## Example

<img src="https://i.imgur.com/PoUEToj.gif" width="500"/>

## Support

Reach out to me at one of the following places!

Twitter: @vibhuagrawal  
Email: vibhu[dot]agrawal14[at]gmail


