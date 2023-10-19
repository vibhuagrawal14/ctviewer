import copy
import numpy as np
import ipywidgets as ipyw
import matplotlib.pyplot as plt

class CTViewer:
    """
    View a volumetric CT image using widgets in ipython notebooks. This class builds
    upon ImageSliceViewer3D (https://github.com/mohakpatel/ImageSliceViewer3D).
    
    The orientation, slice numbers, and CT windows can be changed interactively.
    
    Arguments
    volume: A volumetric CT image converted to Hounsfield units (HU)
    figsize: Size of the figure to be plotted. Defaults to (8, 8)
    """
    
    def __init__(self, volume, mask=None, figsize=(8,8), continuous_update=True):
        self.volume = volume
        self.mask = mask
        self.figsize = figsize
        self.continuous_update = continuous_update
        self.v = [np.min(volume), np.max(volume)]
        self.last_known_slice = 0
        
        self.orientations = {"y-z":[1,2,0],
                             "z-x":[2,0,1],
                             "x-y": [0,1,2]}
        
        self.windows = {"None": [None, None], 
                        "Bone" : [500, 2000],
                        "Lung": [-600, 1600],
                        "Abdomen": [40, 400],
                        "Brain": [30, 70],
                        "Soft Tissue": [50, 350],
                        "Liver": [60, 160],
                        "Mediastinum": [50, 500],
                        "Stroke": [30, 30],
                        "CTA": [170, 600]}
        
        self.segments = {}
        if self.mask is not None:
            self.segments = {
                f'{k}': ipyw.ToggleButton(
                    value=True,
                    description=f'Mask - {k}',
                    disabled=False,
                    button_style='', # 'success', 'info', 'warning', 'danger' or ''
                    tooltip=f'Click to toggle mask {k}',
                    icon='check' # (FontAwesome names without the `fa-` prefix)
                )
                for k in np.unique(self.mask[self.mask != 0])
            }
                

        ipyw.interact(self.check_if_custom_window,
                      view=ipyw.RadioButtons(
                          options=list(self.orientations),
                          value='x-y', 
                          description='Slice plane selection:',
                          disabled=False,
                          style={'description_width': 'initial'}), 
                      window=ipyw.Dropdown(
                          options=list(self.windows)  + ['Custom'],
                          value='None', 
                          description='CT Window:',
                          disabled=False,
                          style={'description_width': 'initial'}),
                      window_level=ipyw.fixed(None),
                      window_width=ipyw.fixed(None))
        
    def check_if_custom_window(self, view, window):
        """
        Function to handle the "Custom" option in the window selection dropdown.
        """
        ipyw.interact(self.view_selection,
                      view=ipyw.fixed(view), 
                      window=ipyw.fixed(window),
                      window_level=ipyw.IntText(
                          value=2000,
                          description='Window_level:',
                          disabled=False) if window == "Custom" else ipyw.fixed(None),
                      window_width=ipyw.IntText(
                          value=4000,
                          description='Window_width:',
                          disabled=False) if window == "Custom" else ipyw.fixed(None))

    def view_selection(self, view, window, window_level=None, window_width=None):
        """
        Process the volume according to the selected values for view and window.
        """
        
        # Transpose the volume according to selected view
        self.vol = np.transpose(self.volume, self.orientations[view])
        if self.mask is not None:
            self.m = np.transpose(self.mask, self.orientations[view])
        maxZ = self.vol.shape[2] - 1
        
        # CT Windowing
        if window != "None":
            if window != "Custom":
                window_level, window_width = self.windows[window]
            upper, lower = window_level + window_width//2, window_level - window_width//2
            self.vol = np.clip(self.vol, lower, upper)            
        self.v = [np.min(self.vol), np.max(self.vol)]

        ipyw.interact(self.plot_slice, 
                      z=ipyw.IntSlider(min=0,
                                       max=maxZ,
                                       value=self.last_known_slice,
                                       step=1,
                                       continuous_update=self.continuous_update, 
                                       description='Image Slice:'),
                                       **self.segments)
        
    def plot_slice(self, z, **kwargs):
        """
        Plot the selected slice.
        """
        self.last_known_slice = z
        self.fig = plt.figure(figsize=self.figsize)

        plt.imshow(self.vol[:,:,z], cmap='gray', vmin=self.v[0], vmax=self.v[1])
        if self.mask is not None:
            ignored_masks = [0]
            for k, v in kwargs.items():
                if not v:
                    ignored_masks.append(int(k))
            mask_ = np.logical_or.reduce([self.m[:,:,z] == i for i in ignored_masks])
            masked = np.ma.masked_where(mask_, self.m[:,:,z])
            plt.imshow(masked, 
                       cmap='jet',
                       alpha=0.2,
                       vmin=0,
                       vmax=len(self.segments))
