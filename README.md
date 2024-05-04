<h1>BMP to PBM Image Converter</h1>
This Python script converts BMP images to PBM format using ImageMagick.

<h3>Situation</h3>
<p>Working with displaying images from rasberry pico onto your <a href="https://esphome.io/components/display/ssd1306.html">ssd1306 oled</a> screens. here is an easy way to convert your images from any format into bpm </p>

<h3>Reason</h3>
<p>I was finding that videos could not be played using such a restrictive display</p>
<p>So i worked out a system where i would save the video into multiple images using <a href="https://www.blackmagicdesign.com/products/davinciresolve/?gad_source=1&gclid=Cj0KCQjwltKxBhDMARIsAG8KnqVhnjNkxVSnKG_3CkTPRG3tfB5WcNx2tyGtQNUmTOsl0KYXpnt_pkkaAlgoEALw_wcB">divinci resolve</a>.</p>
<p>Convert the images using magik into bpm which drasticly decreases the image file size even more.</p>


<h3>Requirements</h3>
Python 3.5 or later
<p>https://www.python.org/downloads/release/python-350/</p>



ImageMagick
<pre>
npm install imagemagick
npm install imagemagick-convert
</pre>


<h3>How it works</h3>
<p>-Install ImageMagick if you haven't already.</p>
<p>-Place the BMP images you want to convert in the specified input_folder.</p>
<pre>input_folder = "/users/documents/input_folder"</pre>
<p>-Run the script to convert the images to PBM format in the output_folder.</p>
<pre>input_folder = "/users/documents/output_folder"</pre>

<h3>How to Run</h3>
Clone the repository or copy script into your code.
Modify the input_folder and output_folder variables in the script to match your desired input and output locations.
Run the script in your code.

<pre>python imagetobpm.py</pre>


