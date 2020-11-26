import click
from PIL import Image


class PicInPic(object):

    @staticmethod
    def tobin( rgb):
        #r, g, b = rgb
        r=rgb[0]
        g=rgb[1]
        b=rgb[2]
        #b=int(b,2)
        #a=int(a,2)
        #c=int(c,2)
        return ('{0:08b}'.format(r),'{0:08b}'.format(g),'{0:08b}'.format(b))

    @staticmethod
    def toint(rgb):
        #r, g, b = rgb
        r=rgb[0]
        g=rgb[1]
        b=rgb[2]
        return (int(r, 2),int(g, 2),int(b, 2))

    @staticmethod
    def rgbmerge( rgb1, rgb2):
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        rgb = (r1[:4] + r2[:4],g1[:4] + g2[:4],b1[:4] + b2[:4])
        return rgb

    @staticmethod
    def merge(img1, img2): #merge second into first
        if img2.size[0] > img1.size[0] or img2.size[1] > img1.size[1]:
            raise ValueError('Image 2 should not be larger than Image 1!')

        pixel_map1 = img1.load()
        pixel_map2 = img2.load()
        new_image = Image.new(img1.mode, img1.size)
        pixels_new = new_image.load()

        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                rgb1 = PicInPic.tobin(pixel_map1[i, j])
                rgb2 = PicInPic.tobin((0, 0, 0))
                if i < img2.size[0] and j < img2.size[1]:
                    rgb2 = PicInPic.tobin(pixel_map2[i, j])
                rgb = PicInPic.rgbmerge(rgb1, rgb2)   #merge happens here
                pixels_new[i, j] = PicInPic.toint(rgb)

        return new_image

    @staticmethod
    def unmerge(img):
        pixel_map = img.load()      
        new_image = Image.new(img.mode, img.size)
        pixels_new = new_image.load()
        original_size = img.size

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = PicInPic.tobin(pixel_map[i, j])
                rgb = (r[4:] + '0000',g[4:] + '0000',b[4:] + '0000')
                pixels_new[i, j] = PicInPic.toint(rgb)
                if pixels_new[i, j] != (0, 0, 0):
                    original_size = (i + 1, j + 1)
        new_image = new_image.crop((0, 0, original_size[0], original_size[1]))
        return new_image



def merge(img1, img2, output):
    merged_image = PicInPic.merge(Image.open(img1), Image.open(img2))
    merged_image.save(output)


def unmerge(img, output):
    unmerged_image = PicInPic.unmerge(Image.open(img))
    unmerged_image.save(output)


if __name__ == '__main__':
    ch=int(input("1. Merge\n2. Unmerge\nChoice: "))
    if(ch==1):
        img1=input("img1(carrier) name: ")
        img2=input("img2 name(payload): ")
        output=input("Output name: ")
        merge(img1,img2,output)
    if(ch==2):
        img=input("img name: ")
        output=input("output name: ")
        unmerge(img,output)
