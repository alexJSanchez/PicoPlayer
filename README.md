<h1>Video to Image Conversion for Raspberry Pi Pico SSD1306 OLED Display</h1>
<h2>Overview</h2>
This project aims to provide a solution for displaying videos on the SSD1306 OLED display connected to a Raspberry Pi Pico. Since the display has limitations in playing videos directly, we use DaVinci Resolve to convert the video into a sequence of images. These images are then converted to PBM format using ImageMagick and displayed on the <a href="https://esphome.io/components/display/ssd1306.html">SSD1306 OLED screen</a>  using Python and the framebuf module.

<h3>Steps</h3>
<li>
  <ol>Download Required tools</ol>
  <ol>Use DaVinci Resolve to save the video as multiple images
  <ol></ol></ol>
</li>

<h3>Reason</h3>
<p>I was finding that videos could not be played using such a restrictive display</p>
<p>So i worked out a system where i would save the video into multiple images using <a href="https://www.blackmagicdesign.com/products/davinciresolve/?gad_source=1&gclid=Cj0KCQjwltKxBhDMARIsAG8KnqVhnjNkxVSnKG_3CkTPRG3tfB5WcNx2tyGtQNUmTOsl0KYXpnt_pkkaAlgoEALw_wcB">divinci resolve</a>.</p>
<p>Convert the images using magik into bpm, i found working with bpm is much easier when using raspberry pi pico framebuf.MONO_HLSB when creating a framebuffer</p>
<p>framebuf.MONO_HLSB: Monochrome (black and white) format with 1 bit per pixel, stored horizontally, using least significant bits first. This is often used for OLED displays.</p>
<pre>
fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
</pre>

<h3>Requirements</h3>
Python 3.5 or later
<p>https://www.python.org/downloads/release/python-350/</p>

ImageMagick

<pre>
npm install imagemagick
npm install imagemagick-convert
</pre>

Divinci resolve

<p><a href="https://www.blackmagicdesign.com/products/davinciresolve/?gad_source=1&gclid=Cj0KCQjwltKxBhDMARIsAG8KnqVhnjNkxVSnKG_3CkTPRG3tfB5WcNx2tyGtQNUmTOsl0KYXpnt_pkkaAlgoEALw_wcB">Link to main page</a>.</p>

<h2>How it works</h2>

<h3>Save video as image files</h3>
<ol>
<li>upload your video file you want to divinci resolve and click the render tab at the bottom right of the screen(circled in red on the image)</li>
<img src="./readmeimages/screen_one.png" alt="Screen One">
<li>Navigate on the left to the individual clip option and remember what export format you chose. You will need it for you Magick image Convert</li>
<img src="./readmeimages/screen_two.png" alt="Screen Two">
<li>choose your export folder and click render at the bottom</li>
<img src="./readmeimages/screen_three.png" alt="Screen Three">
</ol>

<h3>-Convert Images with Magick</h3>

<ol>
  <li>Open the imagetobpm.py file.</li>
  <li>replace destination of input_folder to where you saved the files from divinci.</li>
  <pre>input_folder = "/users/documents/input_folder"</pre>
  <li>replace destination of output_folder to where you want converted images to be saved.</li>
  <pre>input_folder = "/users/documents/output_folder"</pre>
  <li>Run the script in temrinal to convert the images to PBM format in the output_folder.</li>
  <pre>python imagetobpm.py</pre>
</ol>

<h2>Loading images to raspberry pico w with thonny</h2>
<p>-Ive stored my images on a SD drive ive connected to my raspberry pico, i suggest research expanding stoarage space for larger video lengths</p>
<p>-copy the main.py files to your thonny ide </p>
<ol>
  <li>Change the path to your folder with your bpm images, my images are located in my sd folder</li>
  <pre>file_path = '/sd/pbm_converted'</pre>
  <li>Run Thoony program</li>
</ol>

<h2>Errors and road blocks</h2>
<ul>
  <li>Remmeber to keep image size of 128 x 64 as its the native resolution of the screen</li>
  <li>You can adjust the color invert to better display your image if needed</li>
  <pre> oled.invert(1)</pre>
  or
  <pre>oled.invert(0)</pre>
  <li>file memory on pico is minimal. expanding to sd would give ability for larger files</li>
</ul>






