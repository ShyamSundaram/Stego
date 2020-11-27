![Markdown Logo](pics/logo.ico)
# STEGO
### *A steganography tool*
---
*Steganography* is hiding secret data in non-secret data. Yeah, it's exactly what it sounds like. To be brief, you can do things like hiding an image inside another image file or hiding text in an audio file etc.

In cryptography you obscure data so that no one else other than the person who is allowed access to that data can read it. But, the fact that a message or "secret" is sent or communicated is known to all. 

In steganography, there is no such paper trail. The fact that there is a message itself is hidden. Combining this with cryptography is pretty cool.
<br><br>
## TECHNIQUES

The ones currently in the application use the Least Significant Bit method. But the project will support other methods slowly (in the long run. Pull requests are welcome).

* [x] LSB
* [ ] Phase Encoding
* [ ] Spread Spectrum

<br><br>
## TERMS
**Payload** - It is the secret data you want to hide.

**Carrier** - It is the non-secret data in which you hide the payload.
<br><br>

## FILE TYPES SUPPORTED
The table shows what files can be merged and extracted as of now.



<table>
<tr>
    <th>Payload</th>
    <th>Carrier</th>
    <th>Merge Output</th>
    <th>Extraction Output</th>
</tr>
<tr>
    <td rowspan=2>Text file (.txt)</td>
    <td>Image files (PNG, JPEG, WEBP)</td>
    <td>Image file of PNG format</td>
    <td>Text file (.txt)</td>
</tr>
<tr>
    <td>Audio files (WAV, MP3)</td>
    <td>Audio file of WAV</td>
    <td>Text file (.txt)</td>
</tr>
<tr>
    <td>Image (PNG, JPEG, WEBP)</td>
    <td>Image files (PNG, JPEG, WEBP)</td>
    <td>Image file of PNG format</td>
    <td>Image files (PNG, JPEG, WEBP)</td>
</tr>
</table>
<br><br>

## ENCRYPTION
Encryption technique/standard used is mentioned and those available are marked in tasks.

* [x] Text In Audio (AES Encryption)
* [ ] Text In Image