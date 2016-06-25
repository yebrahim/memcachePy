from memcache import Memcache

cache = Memcache()
cache.set('a', 10)
cache.set('b', 10)
assert cache.count(10) == 2
assert cache.count(20) == 0
cache.delete('a')
assert cache.count(10) == 1
cache.set('b', 30)
assert cache.count(10) == 0

cache = Memcache()
cache.begin()
cache.set('a',10)
assert cache.get('a') == 10
cache.begin()
cache.set('a',20)
assert cache.get('a') == 20
cache.rollback()
assert cache.get('a') == 10
cache.rollback()
assert cache.get('a') == 'NULL'

cache = Memcache()
cache.begin()
cache.set('a',30)
cache.begin()
cache.set('a',40)
cache.commit()
assert cache.get('a') == 40
assert cache.rollback() == 'NO TRANSACTION'

cache = Memcache()
cache.set('a',50)
cache.begin()
assert cache.get('a') == 50
cache.set('a',60)
cache.begin()
cache.delete('a')
assert cache.get('a') == 'NULL'
cache.rollback()
assert cache.get('a') == 60
cache.commit()
assert cache.get('a') == 60

cache = Memcache()
cache.set('a',10)
cache.begin()
assert cache.count(10) == 1
cache.begin()
cache.delete('a')
assert cache.count(10) == 0
cache.rollback()
assert cache.count(10) == 1
