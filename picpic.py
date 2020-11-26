from PIL import Image

def tobin( rgb):
        #r, g, b = rgb
        b=bin(rgb[1])[2::]
        a=bin(rgb[0])[2::]
        c=bin(rgb[2])[2::]
        return (a,b,c)

def toint(rgb):
        #r, g, b = rgb
        r=rgb[0]
        g=rgb[1]
        b=rgb[2]
        return (int(r, 2),int(g, 2),int(b, 2))

def rgbmerge( rgb1, rgb2):
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        r1=r1[:4]
        r2=r2[:4]
        g1=g1[:4]
        g2=g2[:4]
        b1=b1[:4]
        b2=b2[:4]
        rgb = (r1+r2,g1+g2,b1+b2)
        return rgb

def merge(i1, i2,output): #merge second into first
        i1=Image.open(i1)
        i2=Image.open(i2)
        l,w=i1.size[0],i1.size[1]
        l2,w2=i2.size[0],i2.size[1]

        if l2 > l or w2 > w:
            raise ValueError('Carrier needs to be bigger than Payload!')

        immap1 = i1.load()
        immap2 = i2.load()
        img = Image.new(i1.mode, i1.size)
        npix =  img.load()
        
        for i in range(l):
            for j in range(w):
                rgb1 = tobin(immap1[i, j])
                rgb2 = tobin((0, 0, 0))
                if i < l2 and j < w2:
                    rgb2 = tobin(immap2[i, j])
                rgb =  rgbmerge(rgb1, rgb2)   #merge happens here
                npix[i, j] =  toint(rgb)
        img.save(output)

def unmerge(i1,output):
        img=Image.open(i1)
        immap = img.load()
        img2 = Image.new(img.mode, img.size)
        npix =  img2.load()

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b =  tobin(immap[i, j])
                r=r[4:] + '0000'
                g=g[4:] + '0000'
                b=b[4:] + '0000'
                rgb = (r,g,b)
                npix[i, j] =  toint(rgb)
        
        img2.save(output)