# v8: build a small self-hosted vector basemap (Natural Earth, public domain) → build/geo_out/base.json
# Run manually when the source data changes: python3 geo.py /workspace/ne   (output is committed; the normal build only copies it)
import json,sys,os
from shapely.geometry import shape,box,mapping,LineString
NE=sys.argv[1] if len(sys.argv)>1 else '/workspace/ne'
OUT=os.path.join(os.path.dirname(__file__),'geo_out','base.json')
BB=box(-13,20,52,62)   # Europe + Mediterranean + Near East (Ur, Egypt, Sinai, Asia Minor, Rome)
def rd(g,n=3):
    def r(c):
        if isinstance(c[0],(int,float)): return [round(c[0],n),round(c[1],n)]
        return [r(x) for x in c]
    m=mapping(g); return {'type':m['type'],'coordinates':r(m['coordinates'])}
F=[]
def load(f): return json.load(open(os.path.join(NE,f+'.geojson')))['features']
for f in load('ne_110m_land'):
    g=shape(f['geometry']).simplify(0.15,preserve_topology=True)
    F.append({'type':'Feature','properties':{'k':'w'},'geometry':rd(g,2)})
for f in load('ne_50m_land'):
    g=shape(f['geometry']).intersection(BB)
    if g.is_empty: continue
    g=g.simplify(0.02,preserve_topology=True)
    if g.area<0.004: continue
    F.append({'type':'Feature','properties':{'k':'l'},'geometry':rd(g)})
for f in load('ne_50m_lakes'):
    g=shape(f['geometry']).intersection(BB)
    if g.is_empty or g.area<0.01: continue
    F.append({'type':'Feature','properties':{'k':'a','n':f['properties'].get('name')},'geometry':rd(g.simplify(0.02))})
KEEP={'Rhein','Rhine','Rhin','Elbe','Jordan','Rhône','Rhne','Danube','Nile','Euphrates','Tigris','Main','Maas','Seine','Loire','Thames','Oder','Odra','Weser','Moselle','Mosel','Po','Tiber','Tevere','Vistula','Wisła','Schelde','Escaut','Ems','Garonne','Ebro','Tagus','Tejo','Halys','Kızılırmak','Orontes','Dnieper','Dniester'}
for f in load('ne_10m_rivers_lake_centerlines'):
    p=f['properties']; nm=p.get('name') or ''
    if nm not in KEEP and (p.get('scalerank') or 99)>5: continue
    g=shape(f['geometry']).intersection(BB)
    if g.is_empty: continue
    F.append({'type':'Feature','properties':{'k':'r','n':nm},'geometry':rd(g.simplify(0.015))})
# Neckar (not in NE 10m): hand-traced, approximate — Villingen → Tübingen → Stuttgart → Heilbronn → Heidelberg → Mannheim
nk=[(8.52,48.06),(8.75,48.45),(9.05,48.52),(9.25,48.70),(9.21,48.80),(9.22,49.14),(9.10,49.30),(8.99,49.38),(8.80,49.40),(8.69,49.41),(8.57,49.44),(8.46,49.50)]
F.append({'type':'Feature','properties':{'k':'r','n':'Neckar'},'geometry':{'type':'LineString','coordinates':[list(x) for x in nk]}})
for f in load('ne_50m_admin_0_boundary_lines_land'):
    g=shape(f['geometry']).intersection(BB)
    if g.is_empty: continue
    F.append({'type':'Feature','properties':{'k':'b'},'geometry':rd(g.simplify(0.03))})
os.makedirs(os.path.dirname(OUT),exist_ok=True)
json.dump({'type':'FeatureCollection','attribution':'Natural Earth (public domain) · Neckar hand-traced','features':F},open(OUT,'w'),separators=(',',':'))
print(len(F),'features',os.path.getsize(OUT)//1024,'KB')
