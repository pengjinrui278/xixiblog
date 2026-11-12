"""Small, dependency-free SVG drawing tools for the physics study notes."""
from pathlib import Path
from html import escape
import math

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'public' / 'images' / 'physics'
INK = '#302e2a'
GRAY = '#77736c'
BLUE = '#2569a3'
RED = '#bc493d'
GREEN = '#287b64'
PURPLE = '#7652a4'
ORANGE = '#b87620'
LIGHT = '#eee8dc'
BG = '#fffdf7'

class Diagram:
    def __init__(self, name, title, width=640, height=440, desc=''):
        self.name, self.width, self.height = name, width, height
        self.parts = [f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>',
            f'<rect width="{width}" height="{height}" rx="14" fill="{BG}"/>']
        self.markers = set()
        self.text(24, 36, title, size=23, weight='bold', anchor='start')
    def text(self,x,y,text,size=22,anchor='middle',color=INK,weight='normal',italic=False):
        style = ' font-style="italic"' if italic else ''
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}" font-weight="{weight}"{style}>{escape(str(text))}</text>')
    def _marker(self, color):
        key = 'a'+color.replace('#','').replace(' ','')
        if key not in self.markers:
            self.parts.append(f'<defs><marker id="{key}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse" markerUnits="userSpaceOnUse"><path d="M 0 0 L 10 5 L 0 10 Z" fill="{color}"/></marker></defs>')
            self.markers.add(key)
        return key
    def line(self,x1,y1,x2,y2,color=INK,width=2,dash=None,arrow=False):
        self.path(f'M {x1} {y1} L {x2} {y2}',color,width,dash=dash,arrow=arrow)
    def arrow(self,x1,y1,x2,y2,color=BLUE,width=3):
        self.line(x1,y1,x2,y2,color,width,arrow=True)
    def path(self,d,color=INK,width=2,fill='none',dash=None,arrow=False):
        extra = f' stroke-dasharray="{dash}"' if dash else ''
        if arrow: extra += f' marker-end="url(#{self._marker(color)})"'
        self.parts.append(f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{extra}/>')
    def rect(self,x,y,w,h,fill='none',stroke=INK,radius=0,width=2):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')
    def circle(self,x,y,r,fill='none',stroke=INK,width=2):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')
    def ellipse(self,x,y,rx,ry,fill='none',stroke=INK,width=2):
        self.parts.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')
    def polyline(self,points,color=INK,width=2,fill='none',dash=None,arrow=False):
        self.path('M '+' L '.join(f'{x} {y}' for x,y in points),color,width,fill,dash,arrow)
    def charge(self,x,y,sign='+',r=17):
        c=RED if sign=='+' else BLUE
        self.circle(x,y,r,fill=BG,stroke=c,width=2)
        self.text(x,y+7,sign,size=24,color=c,weight='bold')
    def symbol(self,x,y,kind='out',color=PURPLE,r=11):
        self.circle(x,y,r,fill=BG,stroke=color,width=2)
        if kind in ('out','dot'):
            self.circle(x,y,2.7,fill=color,stroke=color,width=1)
        else:
            t=r*0.55
            self.line(x-t,y-t,x+t,y+t,color,2)
            self.line(x-t,y+t,x+t,y-t,color,2)
    def resistor(self,x1,y1,x2,y2,color=INK):
        dx,dy=x2-x1,y2-y1
        length=math.hypot(dx,dy); ux,uy=dx/length,dy/length
        points=[(x1,y1),(x1+0.2*dx,y1+0.2*dy)]
        for i in range(1,8):
            t=0.2+0.6*i/8; s=8 if i%2 else -8
            points.append((x1+t*dx-uy*s,y1+t*dy+ux*s))
        points.extend([(x1+0.8*dx,y1+0.8*dy),(x2,y2)])
        self.polyline(points,color,2.5)
    def footer(self,text):
        self.text(24,self.height-20,text,size=18,anchor='start',color=GRAY)
    def save(self):
        OUT.mkdir(parents=True,exist_ok=True)
        p=OUT/(self.name+'.svg')
        body='\n'.join(self.parts)
        p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" width="{self.width}" height="{self.height}" role="img" aria-labelledby="title desc" font-family="Microsoft YaHei, PingFang SC, Noto Sans CJK SC, sans-serif">\n{body}\n</svg>\n',encoding='utf-8')
        return p

def figure(name,caption,alt,height):
    src='/images/physics/'+name+'.svg'
    return f'\n<figure class="physics-figure">\n  <a href="{src}" target="_blank" rel="noopener" title="打开大图"><img src="{src}" alt="{escape(alt,quote=True)}" width="640" height="{height}" loading="lazy" decoding="async" /></a>\n  <figcaption>{escape(caption)}</figcaption>\n</figure>\n'
