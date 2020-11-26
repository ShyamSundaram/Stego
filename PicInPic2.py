#import click
from PIL import Image



def tobin( rgb):
    #r, g, b = rgb
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    #b=int(b,2)
    #a=int(a,2)
    #c=int(c,2)
    return ('{0:08b}'.format(r),'{0:08b}'.format(g),'{0:08b}'.format(b))

def toint(rgb):
    #r, g, b = rgb
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    return (int(r, 2),int(g, 2),int(b, 2))

def rgbmerge( rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    rgb = (r1[:4] + r2[:4],g1[:4] + g2[:4],b1[:4] + b2[:4])
    return rgb

def merge1(carrier, payload): #merge second into first
    if payload.size[0] > carrier.size[0] or payload.size[1] > carrier.size[1]:
        raise ValueError('Image 2 should not be larger than Image 1!')

    carr = carrier.load()
    pay = payload.load()
    out = Image.new(carrier.mode, carrier.size)
    pic = out.load()
    
    for i in range(carrier.size[0]):
        for j in range(carrier.size[1]):
            rgb1 = tobin(carr[i, j])
            rgb2 = tobin((0, 0, 0))
            if i < payload.size[0] and j < payload.size[1]:
                rgb2 = tobin(pay[i, j])
            rgb = rgbmerge(rgb1, rgb2)   #merge happens here
            pic[i, j] = toint(rgb)

    return out

def unmerge1(img):
    pic = img.load()      
    payload = Image.new(img.mode, img.size)
    pay = payload.load()
    size = img.size

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = tobin(pic[i, j])
            rgb = (r[4:] + '0000',g[4:] + '0000',b[4:] + '0000')
            pay[i, j] = toint(rgb)
            if pay[i, j] != (0, 0, 0):
                size = (i + 1, j + 1)
    payload = payload.crop((0, 0, size[0], size[1]))
    return payload



def merge(img1, img2, output):
    merged_image = merge1(Image.open(img1), Image.open(img2))
    merged_image.save(output)


def unmerge(img, output):
    unmerged_image = unmerge1(Image.open(img))
    if(output.split('.')[1]!='png'):
        unmerged_image=unmerged_image.convert('RGB')
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