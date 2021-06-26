import pandas as pd
from sqlalchemy import create_engine


ks_leg = pd.read_csv('../../resources/getlegislators_ks.csv')
mo_leg = pd.read_csv('../../resources/getlegislators_mo.csv')
wagner = pd.read_csv('../../resources/zzAnn L Wagner (R).csv')
long = pd.read_csv('../../resources/zzBilly Long (R).csv')
luetkemeyer = pd.read_csv('../../resources/zzBlaine Luetkemeyer (R).csv')
cleaver = pd.read_csv('../../resources/zzEmanuel Cleaver (D).csv')
smith = pd.read_csv('../../resources/zzJason Smith (R).csv')
moran = pd.read_csv('../../resources/zzJerry Moran (R).csv')
hawley = pd.read_csv('../../resources/zzJosh Hawley (R).csv')
roberts = pd.read_csv('../../resources/zzPat Roberts (R).csv')
marshall = pd.read_csv('../../resources/zzRoger Marshall (R).csv')
estes = pd.read_csv('../../resources/zzRon Estes (R).csv')
blunt = pd.read_csv('../../resources/zzRoy Blunt (R).csv')
graves = pd.read_csv('../../resources/zzSam Graves (R).csv')
davids = pd.read_csv('../../resources/zzSharice Davids (D).csv')
watkins = pd.read_csv('../../resources/zzSteve Watkins (R).csv')
hartzler = pd.read_csv('../../resources/zzVicky Hartzler (R).csv')
clay = pd.read_csv('../../resources/zzWilliam L Clay Jr. (D).csv')

engine = create_engine(
    'postgresql://postgres:postgres@localhost:5432/followthemoney')
connection = engine.connect()

ks_leg.to_sql("ks_legislators", connection)
mo_leg.to_sql("mo_legislators", connection)
wagner.to_sql("ann_wagner", connection)
long.to_sql("billy_long", connection)
luetkemeyer.to_sql("blaine_luetkemeyer", connection)
cleaver.to_sql("emanuel_cleaver", connection)
smith.to_sql("jason_smith", connection)
moran.to_sql("jerry_moran", connection)
hawley.to_sql("josh_hawley", connection)
roberts.to_sql("pat_roberts", connection)
marshall.to_sql("roger_marshall", connection)
estes.to_sql("ron_estes", connection)
blunt.to_sql("roy_blunt", connection)
graves.to_sql("sam_graves", connection)
davids.to_sql("sharice_davids", connection)
watkins.to_sql("steve_watkins", connection)
hartzler.to_sql("vicky_hartzler", connection)
clay.to_sql("william_clay", connection)