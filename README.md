#Video editing with foundational stabel diffusion model

Stable diffusion model can generate images based on given input prompts, making a pretrianed diffusion model viable tool to eidit images with conditions.

This pipeline is adapted from the work of Tune-A-Video ([github](https://github.com/zhuowenzhao/Tune-A-Video), [paper](https://arxiv.org/abs/2212.11565))that is based on open-source [ Huggigface Diffusers](https://huggingface.co/docs/diffusers/index) and its [pretrained checkpoints](https://huggingface.co/CompVis/stable-diffusion-v1-4).

## Results
<table class="center">
<tr>
  <td style="text-align:center;"><b>Input Video</b></td>
  <td style="text-align:center;" colspan="3"><b>Output Video</b></td>
</tr>
<tr>
  <td><img src="data/gifs/input_demo.gif" loop=infinite></td>
  <td><img src="data/gifs/superwoman.gif"></td>
  <td><img src="data/gifs/batwoman.gif"></td>              
  <td><img src="data/gifs/wonderwoman.gif"></td>
</tr>
<tr>
  <td width=25% style="text-align:center;color:gray;">"A woman is talking"</td>
  <td width=25% style="text-align:center;">"A woman, wearing Superman clothes, is talking”</td>
  <td width=25% style="text-align:center;">"A woman, wearing Batman's mask, is talking"</td>
  <td width=25% style="text-align:center;">"A Wonder Woman is talking, cartoon style"</td>
</tr>
</table>


##The pipeline
### Set-ups
In my tests, it works with conda enviroment and Python==3.11

```
pip install -r requirements.txt
```

### Training:   
The input video will be decomposed to frame images.
The prompt and the images (in batch) will be embedded into latent vectors. During training, the model will semantically match hese latent vectors going through cross-attention Unet architecture. 

1. Download stable diffusion mdoel and the pretrined weights.  
  ```
  ./download_models.sh
  ```
  
2. Stongly suggest lanching in terminal. First, configurate `Accelerate` for non/distributed training.

	```
	accelerate config
	```
2. Launch the training job

	```
	accelerate launch train_tuneavideo.py --config='./configs/woman-talking.yaml'
	```

Notes
I have tried different aspect ratios and resolutions, I think the best is 512x512, which is the default image sizes of the pretrained model.
During the training, GPU memory is a bottelneck (even with A100 40GBs) since the model itself is quite huge. I was only able to train videos with a total frames up to 16. 

###Inferencing:  
Once the training is done (modify `inference.py` if needed)

```
python inference.py
```
In this process:

1. New prompts will be embeded. The new latent vectors are initialized through DDIM inversion, providing structure guidance for sampling.
2. The new latent vectors will be used to reconstruct frames (the same dimension as input videos) through a VAE decoder.

###Postporcessing:  
It contains a few functionalites using module `moviepy`:

1. An audio is extracted from the original video.
2. A new video is made by combining the audio and new video of the same duration.

See `postprocess.ipynb`


