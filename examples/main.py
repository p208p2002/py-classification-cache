from ..chcache import chcache
chcache = chcache.chcache()
chcache.save('菲力普',{'age':20,'money':5000,'en_name':'Philip'})
Philip = chcache.get('菲力普')
print(Philip)