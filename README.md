# 8Bit Upsizer

This scripe will increase the size of files in the input folder using nearest neighbor upsampling. 

## How to use

Clone this repo. Make sure you have Pillow installed. Can be installed with `pip install --upgrade Pillow`

Then run this commmand

```bash
python main.py
```

You can set the scale to whatever number you choose. It defaults to 10x. For 20x run

```bash
python main.py --scale=20
```